import sys
sys.path.insert(0, 'src')

from synapse.core.autodiff import compute_gradient

def test_grad():
    import torch
    x = torch.tensor(1.0, requires_grad=True)
    grads = compute_gradient(lambda: x ** 2, x)
    assert len(grads) > 0
