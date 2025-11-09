import torch

def compute_gradient(func, *inputs):
    """Compute gradients for a function (func takes no args, tensors in closure)"""
    for inp in inputs:
        if hasattr(inp, 'requires_grad'):
            inp.grad = None
    outputs = func()
    if isinstance(outputs, torch.Tensor) and outputs.requires_grad:
        outputs.backward(torch.ones_like(outputs))
        grads = [inp.grad for inp in inputs if inp.grad is not None]
        return grads
    return []

def test_autodiff():
    def composite_func(x):
        return x ** 2 + torch.sin(x)

    x = torch.tensor(2.0, requires_grad=True)
    grads = compute_gradient(composite_func, x)
    return len(grads) > 0 and grads[0] is not None

if __name__ == "__main__":
    print("Gradient flow:", test_autodiff())
