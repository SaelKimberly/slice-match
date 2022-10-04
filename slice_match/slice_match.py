"""
Created by SaelKimberly (https://github.com/SaelKimberly)
"""
from abc import ABCMeta
from typing import final

__all__ = ['Slice']


@final
class Slice(metaclass=ABCMeta):
    __slots__ = ('start', 'stop', 'step')
    __match_args__ = ('start', 'stop', 'step')

    def __init__(self, start, stop=None, step=None) -> None:
        """just pass here - match case instruction does not call this function anyway"""
        pass

    __subclasscheck__ = slice.__subclasscheck__
