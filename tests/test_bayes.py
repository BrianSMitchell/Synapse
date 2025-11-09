import sys
sys.path.insert(0, 'src')

from synapse.core.bayes import BayesianBernoulli

def test_bayes_update():
    bayes = BayesianBernoulli()
    bayes.update([1, 1, 0])
    assert bayes.mean() > 0.5
