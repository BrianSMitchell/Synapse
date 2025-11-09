import numpy as np

class Distribution:
    def __init__(self, seed=None):
        self.rng = np.random.default_rng(seed)

    def sample(self):
        raise NotImplementedError

class Normal(Distribution):
    def __init__(self, mean, std, seed=None):
        super().__init__(seed)
        self.mean = mean
        self.std = std

    def sample(self):
        return self.rng.normal(self.mean, self.std)

class Bernoulli(Distribution):
    def __init__(self, p, seed=None):
        super().__init__(seed)
        self.p = p

    def sample(self):
        return self.rng.binomial(1, self.p)

class Uniform(Distribution):
    def __init__(self, low, high, seed=None):
        super().__init__(seed)
        self.low = low
        self.high = high

    def sample(self):
        return self.rng.uniform(self.low, self.high)

# Factory
def normal(mean, std, seed=None):
    return Normal(mean, std, seed)

def bernoulli(p, seed=None):
    return Bernoulli(p, seed)

def uniform(low, high, seed=None):
    return Uniform(low, high, seed)
