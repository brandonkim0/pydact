# allow list 

from numpy import block
import pandas as pd
import re
from pydact.functions.base import DeidFunction
from typing import List

class AllowList(DeidFunction):
    """Allow list checking if value inputted is in the list.

    User inputs value and list of allowed values; if value
    is in allow list, return value. If not in allow list,
    return None.

    Typical usage example:

    >>> AllowList().transform('Name', ['Name'])
    'Name'
    """
    def __init__(self) -> None:
        super().__init__()
    
    def transform(self, value: str, allow_list: List) -> str:
        new_set = set(allow_list)
        if value in new_set:
            return value
        else:
            return None

# block list

class BlockList(DeidFunction):
    """Block list checking if value inputted is in the list.

    User inputs value and list of blocked values; if value
    is in block list, return None. If not in block list,
    return value.

    Typical usage example:

    >>> BlockList().transform('Name', ['Name'])
    None
    """
    def __init__(self) -> None:
        super().__init__()

    def transform(self, value: str, block_list: List) -> str:
        new_set = set(block_list)
        if value in new_set:
            return None
        else:
            return value

# numeric filter (str)

class NumericFilter(DeidFunction):
    """Numeric filter checking if value inputted is numeric.

    User inputs value; if value is numeric, return value.
    If value is not numeric, return None.

    Typical usage example:

    >>> NumericFilter().transform('123')
    '123'
    """
    def __init__(self) -> None:
        super().__init__()

    # given a string, return the value that contain filter_by.
    def transform(self, value: str):
        if value.isnumeric():
            return value
        else:
            return None
        
# alphanumeric filter

class AlphaNumericFilter(DeidFunction):
    """Alphanumeric filter checking if value inputted is alphanumeric.

    User inputs value; if value is alphanumeric, return value.
    If value is not alphanumeric, return None.

    Typical usage example:

    >>> AlphaNumericFilter().transform('1k34po')
    '1k34po'
    """
    def __init__(self) -> None:
        super().__init__()

    def transform(self, value: str):
        if value.isalnum():
            return value
        else:
            return None

# regex filter

class RegexFilter(DeidFunction):
    """Regex filter checking if value inputted matches inputted regex pattern.

    User inputs value and regex pattern; if value 
    matches regex pattern, return value. If value
    does not match regex pattern, return None.

    Typical usage example:

    >>> RegexFilter().transform('[0-9]', '123')
    '123'
    """
    def __init__(self) -> None:
        super().__init__()

    def transform(self, pattern: str, value: str):
        if re.fullmatch(pattern, value) is not None:
            return value
        else:
            return None