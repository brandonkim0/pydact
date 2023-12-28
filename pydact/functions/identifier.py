# secure hash (SHA256)
# format-preserving encryption - look up table
# format-preserving encryption - algorithm (TBD)

import secrets
import hashlib
from pydact.functions.base import DeidFunction

class Identifier(DeidFunction):
    """Apply noise to integer/integer-like identifier values.

    User inputs value, the value gets noise applied
    on the identifier.

    Typical usage example:

    >>> Identifier().transform(7df7c1be5db541a059296a85a94299526b2dfa641d7d6bd2540d73de16505421)
    2092f33fa3ec46cab258d04d64ef9cca2f03741d5f7b01769adb853d4cce8
    """

    def __init__(self) -> None:
        super().__init__()
        self.random = secrets.SystemRandom()

    def get_hash(value: object) -> bytes:
        prefix = value.to_bytes(1, 'big')
        digest = hashlib.sha256((value).encode('utf-8')).digest()
        return prefix + digest[:-1]
    
    def transform(self, value: any) -> None:
        #  length = len(value)
        hash_object = hashlib.sha256(value)
        hex_dig = hash_object.hexdigest()
        
