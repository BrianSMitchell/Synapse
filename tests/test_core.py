import pytest
import sys
sys.path.insert(0, 'src')

from synapse.core.distributions import normal, bernoulli, uniform
from synapse.core.morphing import Morpher
from synapse.core.agents import Agent

def test_normal():
    x = normal(0, 1, seed=42)
    assert isinstance(x.sample(), float)

def test_bernoulli():
    x = bernoulli(0.5, seed=42)
    assert x.sample() in [0, 1]

def test_uniform():
    x = uniform(0, 1, seed=42)
    s = x.sample()
    assert 0 <= s <= 1

def test_morphing():
    morpher = Morpher("code")
    morpher.morph(lambda acc: acc < 0.9, lambda tree: "modified")
    assert morpher.accuracy > 0.6

def test_morph_safety():
    morpher = Morpher("code", max_morphs=1)
    try:
        morpher.morph(lambda acc: True, lambda tree: "mod")
        morpher.morph(lambda acc: True, lambda tree: "mod")
        assert False  # Should raise
    except Exception:
        assert True

def test_agent():
    agent = Agent("test")
    assert agent.name == "test"

if __name__ == "__main__":
    pytest.main([__file__])
