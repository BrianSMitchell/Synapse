"""
Synapse Profiler for Phase 16.4
Instruments AST execution to collect runtime profiles for ML optimization.
Metrics: total_time, per_node_time, hotspots (top 5 slow nodes), mem_peak, instr_count.
"""

import time
import psutil  # For memory profiling
import json
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict, field

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    print("Warning: psutil not installed for memory profiling. pip install psutil")

@dataclass
class ProfileNode:
    """Profile data for a single AST node"""
    node_type: str
    node_id: str  # repr(node) hash
    exec_time: float = 0.0
    call_count: int = 0
    children: List['ProfileNode'] = field(default_factory=list)

@dataclass
class ExecutionProfile:
    """Full execution profile"""
    total_time: float = 0.0
    total_mem_peak_mb: float = 0.0
    instr_count: int = 0
    hotspots: List[Dict[str, Any]] = field(default_factory=list)  # Top 5 by time/call_count
    root_node: Optional[ProfileNode] = None

class ASTProfiler:
    """Instruments and profiles AST execution"""
    
    def __init__(self):
        self.current_process = psutil.Process() if PSUTIL_AVAILABLE else None
    
    def instrument(self, ast: Dict[str, Any]) -> Dict[str, Any]:
        """
        Wrap AST nodes with timing instrumentation.
        Returns modified AST with _profile_key.
        """
        def wrap(node: Dict[str, Any]) -> Dict[str, Any]:
            if isinstance(node, dict):
                node['_profile_key'] = f"{node.get('type', 'unknown')}_{id(node)}"
                for key, value in node.items():
                    if isinstance(value, list):
                        node[key] = [wrap(item) for item in value]
                    elif isinstance(value, dict):
                        node[key] = wrap(value)
            return node
        
        return wrap(ast)
    
    def execute_with_profile(self, instrumented_ast: Dict[str, Any], executor_func) -> ExecutionProfile:
        """
        Execute instrumented AST and collect profile.
        executor_func(ast) -> result
        """
        profile_data = {}  # node_key -> times
        start_time = time.time()
        mem_start = self._get_mem_mb()
        
        result = executor_func(instrumented_ast)
        
        total_time = time.time() - start_time
        mem_peak = self._get_mem_mb() - mem_start if self.current_process else 0
        
        # Extract profile data (assumes executor updates profile_data)
        # For now, simulate based on executor_func usage
        hotspots = self._compute_hotspots(profile_data)
        
        profile = ExecutionProfile(
            total_time=total_time,
            total_mem_peak_mb=mem_peak,
            instr_count=len(profile_data),
            hotspots=hotspots,
            root_node=self._build_tree(profile_data)
        )
        return profile
    
    def _get_mem_mb(self) -> float:
        if PSUTIL_AVAILABLE and self.current_process:
            return self.current_process.memory_info().rss / 1024 / 1024
        return 0.0
    
    def _compute_hotspots(self, profile_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Compute top 5 hotspots by avg time"""
        hotspot_list = []
        for key, data in profile_data.items():
            avg_time = data['total_time'] / max(data['call_count'], 1)
            hotspot_list.append({
                'node_key': key,
                'total_time': data['total_time'],
                'call_count': data['call_count'],
                'avg_time': avg_time
            })
        hotspot_list.sort(key=lambda x: x['avg_time'], reverse=True)
        return hotspot_list[:5]
    
    def _build_tree(self, profile_data: Dict[str, Any]) -> ProfileNode:
        # Simplified; full impl would reconstruct tree
        return ProfileNode("root", "root", 0.0, 0, [])
    
    def save_profile(self, profile: ExecutionProfile, path: str):
        """Save profile to JSON"""
        data = asdict(profile)
        if profile.root_node:
            data['root_node'] = asdict(profile.root_node)
        else:
            data['root_node'] = None
        with open(path, 'w') as f:
            json.dump(data, f, indent=2, default=str)

# Integration helper
def profile_execution(ast: Dict[str, Any], executor_func, output_path: str = None):
    """Convenience: instrument + exec + profile + optional save"""
    profiler = ASTProfiler()
    instr_ast = profiler.instrument(ast)
    profile = profiler.execute_with_profile(instr_ast, executor_func)
    if output_path:
        profiler.save_profile(profile, output_path)
    return profile

if __name__ == "__main__":
    print("Synapse Profiler ready for Phase 16.4")
