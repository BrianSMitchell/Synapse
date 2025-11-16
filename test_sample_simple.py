import sys
sys.path.insert(0, 'src')
from synapse.parser.parser import parse_and_execute

# Test simple case
result = parse_and_execute("let belief = bernoulli(0.7); sample(belief)")
print(f"Result: {result}")
print(f"Type: {type(result)}")
print(f"Is float: {isinstance(result, float)}")
