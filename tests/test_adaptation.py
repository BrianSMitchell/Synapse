import sys
sys.path.insert(0, 'src')

from synapse.core.adaptation import adapt_plan

def test_adapt():
    plan = adapt_plan(['explore'], {'reward': 'low'})
    assert plan == ['explore']
