import sys
sys.path.insert(0, 'src')

from synapse.backends.wasm import transpile_to_wasm
from synapse.backends.llvm import transpile_to_llvm

def test_wasm():
    code = transpile_to_wasm("code")
    assert "(module" in code

def test_llvm():
    code = transpile_to_llvm("code")
    assert "define" in code
