import torch

def embed(text):
    """Placeholder text embedding"""
    # Simple: hash to vector
    import hashlib
    h = hashlib.md5(text.encode()).digest()
    vec = torch.tensor([b / 255.0 for b in h[:10]], dtype=torch.float32, requires_grad=True)
    return vec

def reason(embedding, graph):
    """Symbolic reasoning with tensors (placeholder)"""
    # Simulate: matmul embedding with graph (assume graph is tensor)
    if graph is None or isinstance(graph, str):
        graph = torch.eye(10)  # Placeholder graph
    result = torch.matmul(embedding, graph)
    return result

def test_tensors():
    emb = embed("hello")
    graph = torch.randn(10, 10)
    result = reason(emb, graph)
    return result.requires_grad  # Check differentiable

if __name__ == "__main__":
    print("Differentiable trace:", test_tensors())
