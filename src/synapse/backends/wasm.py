def transpile_to_wasm(synapse_code):
    """Transpile Synapse code to WebAssembly (placeholder)"""
    # Simulate: wrap in WASM-like structure
    wasm_code = f"(module (func $main {synapse_code}))"
    return wasm_code

def test_wasm():
    code = "let x = normal(0,1)"
    wasm = transpile_to_wasm(code)
    return "(module" in wasm  # Simulated execution in JS env

if __name__ == "__main__":
    print("WASM export test:", test_wasm())
