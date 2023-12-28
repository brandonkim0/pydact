from pydact.functions.base import DeidFunction


class Replace(DeidFunction):
    """Replace value with inputted value.

    User inputs value to be replaced and replacing value;
    replacing value takes place of value to be replaced.

    Typical usage example:

    >>> old = 'Name1'
    >>> new = 'Name2'
    >>> Replace().transform(old, new)
    >>> print(old)
    'Name2'
    """
    def __init__(self) -> None:
        super().__init__()

    def transform(self, old_value: str, new_value: str) -> str:
        old_value = old_value.replace(old_value, new_value)
        return old_value