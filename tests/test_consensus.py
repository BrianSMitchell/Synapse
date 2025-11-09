import sys
sys.path.insert(0, 'src')

from synapse.core.consensus import consensus

def test_consensus():
    agreed, _ = consensus([True, True, True, False], 0.6)
    assert agreed
