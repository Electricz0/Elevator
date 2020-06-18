"""
define direction enumerator
"""

import enum

@enum.unique
class Direction( enum.Enum ):
    UP = enum.auto()
    DOWN = enum.auto()
