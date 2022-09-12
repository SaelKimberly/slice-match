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
        self.start, self.stop, self.step = start, stop, step

    @classmethod
    def __subclasscheck__(cls, __subclass: type) -> bool:
        return slice.__subclasscheck__(__subclass)
