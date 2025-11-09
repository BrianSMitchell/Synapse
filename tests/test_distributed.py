import sys
sys.path.insert(0, 'src')

def test_sync():
    from synapse.core.distributed import shared_state, update_shared, read_shared
    update_shared("agent", "key", "value")
    result = read_shared("agent", "key")
    assert "value" in result
