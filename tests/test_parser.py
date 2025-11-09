import sys
sys.path.insert(0, 'src')

from synapse.parser.parser import parse_and_execute

def test_parse_let():
    result = parse_and_execute("let x = normal(0,1);")
    assert result is None  # No expr

def test_parse_sample():
    result = parse_and_execute("let x = normal(0,1); sample(x)")
    assert isinstance(result, float)

def test_parse_if():
    result = parse_and_execute("let belief = bernoulli(0.7); if sample(belief) > 0.5 { }")
    assert result is None
