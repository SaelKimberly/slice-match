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

    __init__ = slice.__init__  # type: ignore

    __subclasscheck__ = slice.__subclasscheck__
    __getattribute__ = slice.__getattribute__  # type: ignore
