from datetime import datetime
from typing import Any


class FifoClass(list):
    '''Implement a class FIFO (First in First Out)'''

    def __init__(self) -> None:
        '''instantiate times list'''

        self.times = list()

    def push(self, element: Any) -> None:
        '''add an element to the class'''

        self.append(element)
        self.times.append(datetime.now())

    def pop(self) -> Any:
        '''get and remove the oldest element'''

        element = super().pop(0)
        self.times.pop(0)
        return element

    def size(self) -> int:
        '''get the number of elements'''

        size = len(self)
        return size

    def addition_time(self, position: int = -1) -> datetime:
        '''get the datetime when any element present on the FIFO was added.
        If no position is specified by default return last element addition'''
        
        time = self.times[position]
        return time
