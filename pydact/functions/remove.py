# how do you remove?
# options: replace it with a fixed user-input text (e.g. 3 underscores)
# ?remove it entirely (returns None)
# !replace value with 3 underscores
    # given a dict, Or DataFrame

from pydact.functions.base import DeidFunction

class Remove(DeidFunction):
    """Remove value with replacement class.

    User inputs value, value is replaced with
    three underscores; '___' to indicate removed value.

    Typical usage example:

    >>> Remove().transform('Name')
    '___'
    """
    def __init__(self, replacement='___') -> None:
        self.replacement = replacement
        super().__init__()

    def transform(self, value):
        return self.replacement

