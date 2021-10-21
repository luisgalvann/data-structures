from datetime import datetime
from typing import Any, Optional


class Stack(list):
    ''' Implement a Stack-LIFO class (Last in First Out) '''

    def __init__(self) -> None:
        ''' Instantiate times list '''

        self.times = list()

    def push(self, element: Any) -> None:
        ''' Add an element to the class '''

        self.append(element)
        self.times.append(datetime.now())

    def pop(self) -> Any:
        ''' Get and remove the newest element '''

        element = super().pop()
        self.times.pop()
        return element

    def size(self) -> int:
        ''' Get the total number of elements '''

        size = len(self)
        return size

    def addition_time(self, position: Optional[int] = -1) -> datetime:
        ''' Get the datetime when any element present on the FIFO was added.
        If no position is specified by default return last element addition '''
        
        time = self.times[position]
        return time
