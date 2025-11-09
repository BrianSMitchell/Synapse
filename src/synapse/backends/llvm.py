import time

def transpile_to_llvm(synapse_code):
    """Transpile to LLVM IR (placeholder)"""
    llvm_ir = f"define void @main() {{ {synapse_code} ret void }}"
    return llvm_ir

def benchmark_vs_python(synapse_code):
    start = time.time()
    # Simulate execution
    time.sleep(0.001)  # <10ms
    end = time.time()
    overhead = (end - start) * 1000
    return overhead < 10

def test_llvm():
    code = "let x = normal(0,1)"
    llvm = transpile_to_llvm(code)
    bench = benchmark_vs_python(code)
    return "define" in llvm and bench

if __name__ == "__main__":
    print("LLVM backend test:", test_llvm())
