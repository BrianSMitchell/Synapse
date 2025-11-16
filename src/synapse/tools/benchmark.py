"""
Synapse Benchmark Suite for Phase 16.4
Runs std examples/, generates profiles for ML training.
Compares baseline, rule-opt.
Outputs dataset/*.json: code, baseline_time, rules_time, speedup.
"""

import os
import glob
import json
import time
from typing import Dict, Any, List
from pathlib import Path
from dataclasses import asdict

from synapse.backends.self_host import SelfHostedCompiler
from synapse.backends.optimizer import SynapseOptimizer, OptimizationLevel
from synapse.parser.parser import parse_and_execute
from synapse.tools.profiler import ExecutionProfile

BENCHMARK_DIR = "examples"
DATASET_DIR = "dataset"
os.makedirs(DATASET_DIR, exist_ok=True)

def profile_synapse(code: str, iterations: int = 10) -> ExecutionProfile:
    """Profile Synapse execution time via parse_and_execute"""
    times = []
    success = True
    for _ in range(iterations):
        start = time.time()
        try:
            result = parse_and_execute(code)
        except Exception as e:
            print(f"Parse/exec error: {e}")
            success = False
            break
        times.append(time.time() - start)
    
    if not success or not times:
        avg_time = float('inf')
    else:
        avg_time = sum(times) / len(times)
    
    profile = ExecutionProfile(
        total_time=avg_time,
        total_mem_peak_mb=0.0,  # Stub; add psutil later
        instr_count=0,  # Stub
        hotspots=[],
        root_node=None
    )
    return profile

def run_benchmarks(iterations: int = 10) -> Dict[str, Any]:
    """Run benchmarks on all .syn files"""
    compiler = SelfHostedCompiler()
    optimizer = SynapseOptimizer(OptimizationLevel.AGGRESSIVE)
    
    results = {
        'benchmarks': [],
        'summary': {'avg_speedup_rules': 0.0, 'files': 0}
    }
    
    syn_files = glob.glob(f"{BENCHMARK_DIR}/*.syn")
    
    for syn_path in syn_files:
        filename = Path(syn_path).stem
        print(f"Benchmarking {filename}...")
        
        with open(syn_path, 'r') as f:
            code = f.read()
        
        # Baseline profile
        baseline_profile = profile_synapse(code, iterations)
        
        # Rule-based opt profile
        opt_code = optimizer.optimize(code)
        rules_profile = profile_synapse(opt_code, iterations)
        
        speedup = (baseline_profile.total_time / rules_profile.total_time) if rules_profile.total_time > 0 else 1.0
        
        # Save dataset entry
        dataset_entry = {
            'file': filename,
            'code': code,
            'baseline_profile': asdict(baseline_profile),
            'rules_profile': asdict(rules_profile),
            'speedup_rules': speedup
        }
        dataset_path = f"{DATASET_DIR}/{filename}.json"
        with open(dataset_path, 'w') as f:
            json.dump(dataset_entry, f, indent=2)
        
        results['benchmarks'].append({
            'file': filename,
            'baseline_time': baseline_profile.total_time,
            'rules_time': rules_profile.total_time,
            'speedup_rules': speedup
        })
        
        results['summary']['avg_speedup_rules'] += speedup
        results['summary']['files'] += 1
    
    results['summary']['avg_speedup_rules'] /= results['summary']['files']
    
    summary_path = f"{DATASET_DIR}/summary.json"
    with open(summary_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Benchmarks complete. Dataset generated in {DATASET_DIR}/ ({len(syn_files)} files)")
    return results

if __name__ == "__main__":
    run_benchmarks()
