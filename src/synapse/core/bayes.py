from synapse.core.distributions import Bernoulli

class BayesianBernoulli:
    def __init__(self, prior_alpha=1, prior_beta=1):
        self.alpha = prior_alpha  # successes
        self.beta = prior_beta    # failures

    def update(self, data):
        """Update with list of 0/1 data"""
        for d in data:
            if d == 1:
                self.alpha += 1
            else:
                self.beta += 1

    def sample(self, seed=None):
        """Sample from posterior"""
        dist = Bernoulli(self.alpha / (self.alpha + self.beta), seed)
        return dist.sample()

    def mean(self):
        return self.alpha / (self.alpha + self.beta)

# For convergence test
def test_convergence():
    bayes = BayesianBernoulli()
    # Prior mean ~0.5
    data = [1] * 10  # All successes
    bayes.update(data)
    mean = bayes.mean()
    return mean > 0.8  # Should converge to ~0.91

if __name__ == "__main__":
    print("Converges:", test_convergence())
