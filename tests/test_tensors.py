import sys
sys.path.insert(0, 'src')

from synapse.core.tensors import embed, reason

def test_embed():
    emb = embed("test")
    assert emb.shape == (10,)

def test_reason():
    emb = embed("test")
    result = reason(emb, None)
    assert result is not None
