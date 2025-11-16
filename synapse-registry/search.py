"""
Synapse Registry - Search Engine
Full-text search and package discovery

Author: Synapse Team
License: MIT
"""

import logging
from typing import List, Tuple, Optional
import re
from models import db, Package, PackageVersion, SearchIndex

logger = logging.getLogger(__name__)


class SearchEngine:
    """Full-text search engine for package discovery"""
    
    def __init__(self):
        self.min_query_length = 2
    
    def index_package(self, package: Package, version: PackageVersion) -> None:
        """Index package for full-text search"""
        # Remove old index entries for this version
        SearchIndex.query.filter_by(version_id=version.id).delete()
        
        # Create new index entry
        entry = SearchIndex(
            package_id=package.id,
            version_id=version.id,
            name=package.name,
            description=package.description or '',
            keywords=' '.join(self._parse_keywords(version.keywords_json)) if version.keywords_json else '',
            author=package.author or '',
            popularity_score=version.download_count,
            relevance_score=self._calculate_relevance(package, version),
        )
        
        db.session.add(entry)
        db.session.commit()
        
        logger.info(f'Indexed package: {package.name}@{version.version}')
    
    def search(
        self,
        query: str,
        limit: int = 20,
        offset: int = 0
    ) -> Tuple[List[dict], int]:
        """Search packages"""
        query = query.strip().lower()
        
        if len(query) < self.min_query_length:
            return [], 0
        
        # Build query
        search_query = SearchIndex.query.filter(
            db.or_(
                SearchIndex.name.ilike(f'%{query}%'),
                SearchIndex.description.ilike(f'%{query}%'),
                SearchIndex.keywords.ilike(f'%{query}%'),
                SearchIndex.author.ilike(f'%{query}%'),
            )
        )
        
        # Count total results
        total = search_query.count()
        
        # Sort by relevance and popularity
        results = search_query.order_by(
            SearchIndex.relevance_score.desc(),
            SearchIndex.popularity_score.desc(),
        ).offset(offset).limit(limit).all()
        
        # Format results
        formatted = []
        for entry in results:
            formatted.append({
                'name': entry.package.name,
                'version': entry.version.version,
                'description': entry.package.description or '',
                'downloads': entry.version.download_count,
                'author': entry.package.author or '',
                'score': round(entry.relevance_score + (entry.popularity_score / 1000), 2),
            })
        
        return formatted, total
    
    def search_by_keyword(self, keyword: str) -> List[dict]:
        """Search packages by keyword"""
        keyword = keyword.lower()
        
        results = SearchIndex.query.filter(
            SearchIndex.keywords.ilike(f'%{keyword}%')
        ).order_by(SearchIndex.popularity_score.desc()).all()
        
        return [
            {
                'name': r.package.name,
                'version': r.version.version,
                'description': r.package.description,
                'downloads': r.version.download_count,
            }
            for r in results
        ]
    
    def search_by_author(self, author: str) -> List[dict]:
        """Search packages by author"""
        author = author.lower()
        
        results = SearchIndex.query.filter(
            SearchIndex.author.ilike(f'%{author}%')
        ).order_by(SearchIndex.popularity_score.desc()).all()
        
        return [
            {
                'name': r.package.name,
                'version': r.version.version,
                'description': r.package.description,
                'downloads': r.version.download_count,
            }
            for r in results
        ]
    
    def autocomplete(self, prefix: str) -> List[str]:
        """Autocomplete package names"""
        if len(prefix) < 2:
            return []
        
        prefix = prefix.lower()
        results = SearchIndex.query.filter(
            SearchIndex.name.ilike(f'{prefix}%')
        ).distinct(SearchIndex.name).limit(10).all()
        
        return list(set(r.package.name for r in results))
    
    def get_trending(self, limit: int = 10) -> List[dict]:
        """Get trending packages (by recent downloads)"""
        results = SearchIndex.query.order_by(
            SearchIndex.popularity_score.desc()
        ).limit(limit).all()
        
        return [
            {
                'name': r.package.name,
                'version': r.version.version,
                'downloads': r.version.download_count,
                'description': r.package.description,
            }
            for r in results
        ]
    
    def get_recent(self, limit: int = 10) -> List[dict]:
        """Get recently published packages"""
        results = SearchIndex.query.order_by(
            SearchIndex.indexed_at.desc()
        ).limit(limit).all()
        
        return [
            {
                'name': r.package.name,
                'version': r.version.version,
                'published_at': r.version.published_at.isoformat(),
                'description': r.package.description,
            }
            for r in results
        ]
    
    def _parse_keywords(self, keywords_json: str) -> List[str]:
        """Parse keywords from JSON"""
        import json
        try:
            keywords = json.loads(keywords_json or '[]')
            return keywords if isinstance(keywords, list) else []
        except:
            return []
    
    def _calculate_relevance(self, package: Package, version: PackageVersion) -> float:
        """Calculate relevance score (0-1)"""
        score = 0.0
        
        # Package name relevance
        if package.name:
            score += 0.3
        
        # Description quality
        if package.description and len(package.description) > 50:
            score += 0.2
        
        # Has metadata
        if package.author:
            score += 0.1
        if package.homepage:
            score += 0.1
        if package.repository:
            score += 0.1
        
        # Has dependencies (indicates maturity)
        import json
        try:
            deps = json.loads(version.dependencies_json or '{}')
            if deps:
                score += 0.1
        except:
            pass
        
        # Normalize to 0-1
        return min(score, 1.0)


class QueryParser:
    """Parse complex search queries"""
    
    def __init__(self):
        self.operators = ['AND', 'OR', 'NOT', '-']
    
    def parse(self, query: str) -> dict:
        """Parse search query into structured format"""
        query = query.strip()
        
        # Simple implementation - can be enhanced with proper query parser
        terms = []
        must_have = []
        must_not = []
        
        for part in query.split():
            if part.startswith('-') or part.startswith('NOT'):
                must_not.append(part.lstrip('-NOT ').lower())
            else:
                part = part.lower()
                if part not in ['and', 'or']:
                    terms.append(part)
                    must_have.append(part)
        
        return {
            'terms': terms,
            'must_have': must_have,
            'must_not': must_not,
            'original': query,
        }


class Ranker:
    """Rank search results"""
    
    def __init__(self):
        self.weights = {
            'name_match': 0.4,
            'description_match': 0.2,
            'keyword_match': 0.15,
            'popularity': 0.15,
            'recency': 0.1,
        }
    
    def rank(self, results: List[SearchIndex], query: str) -> List[SearchIndex]:
        """Rank results by relevance"""
        scored = []
        
        for result in results:
            score = self._calculate_score(result, query)
            scored.append((result, score))
        
        # Sort by score descending
        scored.sort(key=lambda x: x[1], reverse=True)
        
        return [result for result, _ in scored]
    
    def _calculate_score(self, result: SearchIndex, query: str) -> float:
        """Calculate relevance score for single result"""
        score = 0.0
        query_lower = query.lower()
        
        # Name match (highest weight)
        if result.name.lower().startswith(query_lower):
            score += self.weights['name_match'] * 1.0
        elif query_lower in result.name.lower():
            score += self.weights['name_match'] * 0.7
        
        # Description match
        if result.description and query_lower in result.description.lower():
            score += self.weights['description_match'] * 0.5
        
        # Keywords match
        if result.keywords and query_lower in result.keywords.lower():
            score += self.weights['keyword_match']
        
        # Popularity (normalized)
        pop_score = min(result.popularity_score / 10000, 1.0)
        score += self.weights['popularity'] * pop_score
        
        # Recency
        from datetime import datetime, timedelta
        days_old = (datetime.utcnow() - result.indexed_at).days
        recency = max(1.0 - (days_old / 365), 0.0)
        score += self.weights['recency'] * recency
        
        return score
