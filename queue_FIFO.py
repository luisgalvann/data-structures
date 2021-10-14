from datetime import datetime
from typing import Any


class QueueFIFO(list):
    ''' Implement a Queue-FIFO class (First in First Out) '''

    def __init__(self) -> None:
        ''' Instantiate times list '''

        self.times = list()

    def push(self, element: Any) -> None:
        ''' Add an element to the class '''

        self.append(element)
        self.times.append(datetime.now())

    def pop(self) -> Any:
        ''' Get and remove the oldest element '''

        element = super().pop(0)
        self.times.pop(0)
        return element

    def size(self) -> int:
        ''' Get the number of elements '''

        size = len(self)
        return size

    def addition_time(self, position: int = 0) -> datetime:
        ''' Get the datetime when any element present on the FIFO was added.
        If no position is specified by default return first element addition '''
        
        time = self.times[position]
        return time
