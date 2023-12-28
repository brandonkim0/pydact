# add fixed set of noise ... maybe the arg is a numpy rng?

from pydact.functions.base import DeidFunction
import pandas as pd
import numpy as np

class Perturb(DeidFunction):
    """Noise applied to user inputted value.

    User inputs value, the value gets noise applied;
    changing the value randomly within a threshold.

    Typical usage example:

    >>> Perturb().transform(42)
    45
    """
    def __init__(self, noise=3) -> None:
        self.noise = noise
        self.random = np.random.default_rng()
        super().__init__()

    # add some noise to int
    # children age is set then is fuzzed/noised
    # remove age > 89, set it to 91

    def transform(self, value: int):
        fuzz_by = self.random.integers(self.noise, size=1)
        value += fuzz_by
        return value

class UpperLimit(DeidFunction):
    """Noise applied to user inputted upper limit value.

    User inputs upper limit value, returns a static value.

    Typical usage example:

    >>> UpperLimit().transform(89)
    91
    """
    def __init__(self) -> None:
        self.limit = 91
        super().__init__()

    def transform(self, value: int):
        # elderly
        if value >= 89:
            value = self.limit
            return value
        else:
            return value

class LowerLimit(DeidFunction):
    """Noise applied to user inputted lower limit value.

    User inputs lower limit value, returns a static value.

    Typical usage example:

    >>> LowerLimit().transform(14)
    13
    """
    def __init__(self) -> None:
        self.limit = 13
        super().__init__()

    def transform(self, value: int):
        # children
        if value <= 18:
            value = self.limit
            return value
        else:
            return value
    