# method for explictly keeping data as it is
# unsure how to implement

from pydact.functions.base import DeidFunction

class Keep(DeidFunction):
    """Keep class checking if value inputted is in the list.

    User inputs value, the keep class explicitly
    returns the same value.

    Typical usage example:

    >>> Keep().transform('Name')
    'Name'
    """
    def __init__(self) -> None:
        super().__init__()

    def transform(self, value: any):
        return value