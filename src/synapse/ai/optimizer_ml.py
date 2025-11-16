"""
Synapse AI Optimizer ML Model for Phase 16.4
Loads dataset/*.json, trains RF to predict best OptimizationLevel for max speedup.
Features: code metrics (lines, defs, loops, etc.)
Target: speedup_rules
"""

import os
import glob
import json
import pickle
import re
from typing import Dict, Any, List, Tuple
from pathlib import Path
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

DATASET_DIR = "dataset"
MODEL_PATH = f"{DATASET_DIR}/optimizer_model.pkl"

def extract_code_features(code: str) -> List[float]:
    """Extract numerical features from Synapse code"""
    features = []
    
    lines = code.strip().split('\n')
    features.append(len(lines))  # 0: num_lines
    
    # Number of defs
    def_matches = re.findall(r'def\s+\w+\s*\(', code, re.MULTILINE | re.IGNORECASE)
    features.append(len(def_matches))  # 1: num_defs
    
    # Number of loops
    loop_matches = re.findall(r'\b(for|while)\b', code, re.MULTILINE | re.IGNORECASE)
    features.append(len(loop_matches))  # 2: num_loops
    
    # Number of ifs
    if_matches = re.findall(r'\bif\b', code, re.MULTILINE | re.IGNORECASE)
    features.append(len(if_matches))  # 3: num_ifs
    
    # Number of calls
    call_matches = re.findall(r'\w+\s*\(', code)
    features.append(len(call_matches))  # 4: num_calls
    
    # Avg nesting (heuristic: indent levels)
    indent_levels = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
    avg_indent = np.mean(indent_levels) if indent_levels else 0
    features.append(avg_indent / 4)  # 5: avg_nesting (assume 4-space)
    
    # Lines with ops
    op_lines = len([l for l in lines if any(op in l for op in ['+', '-', '*', '/', '='])])
    features.append(op_lines)  # 6: op_lines
    
    return features

def load_dataset() -> List[Dict[str, Any]]:
    """Load all dataset/*.json"""
    dataset = []
    json_files = glob.glob(f"{DATASET_DIR}/*.json")
    for path in json_files:
        if path.endswith('summary.json'):
            continue
        with open(path, 'r') as f:
            data = json.load(f)
            dataset.append(data)
    return dataset

def train_model() -> RandomForestRegressor:
    """Train RF model on dataset"""
    dataset = load_dataset()
    if not dataset:
        raise ValueError("No dataset found. Run benchmark.py first.")
    
    X = []
    y = []
    for entry in dataset:
        code = entry['code']
        speedup = entry['speedup_rules']
        features = extract_code_features(code)
        X.append(features)
        y.append(speedup)
    
    X = np.array(X)
    y = np.array(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    print(f"R2 Train: {train_score:.3f}, Test: {test_score:.3f}")
    
    # Save
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    
    print(f"Model saved to {MODEL_PATH}")
    return model

def load_model() -> RandomForestRegressor:
    """Load trained model"""
    if not os.path.exists(MODEL_PATH):
        raise ValueError(f"Model not found. Train first with train_model()")
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)

def predict_best_opt(code: str) -> Tuple[int, float]:
    """Predict best OptimizationLevel and expected speedup"""
    model = load_model()
    features = np.array([extract_code_features(code)])
    predicted_speedup = model.predict(features)[0]
    
    # Map to level (simple: higher speedup -> higher level)
    level = min(int(predicted_speedup * 1), 3)  # Cap at 3
    return level, predicted_speedup

if __name__ == "__main__":
    model = train_model()
