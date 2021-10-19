from typing import Any


class LinkedList:
    ''' Linked list class implementation '''

    class Node:
        ''' Inner class «Node» implementation '''

        def __init__(self, data) -> None:
            self.data: Any = data
            self.next: Node = None
        
        def __repr__(self) -> str:
            return str(self.data)

    def __init__(self) -> None:
        self.head: Node = None

    def __iter__(self) -> Any:
        current = self.head
        while current:
            yield current
            current = current.next

    def __contains__(self, data: Any) -> bool:
        for node in self:
            if node.data == data:
                return True
        return False

    def __repr__(self) -> str:
        return str([*self])

    @property
    def size(self) -> int:
        return len([*self])

    def get_head(self) -> Any:
        return self.head.data

    def set_head(self, data: Any) -> None:
        node = self.Node(data)
        node.next = self.head
        self.head = node

    def pop_head(self) -> None:
        if self.head:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        else:
            raise IndexError('pop from empty list')

    def get_tail(self) -> Any:
        if self.head:
            *_, tail = self
            return tail.data
        return None

    def set_tail(self, data: Any) -> None:
        if self.head:
            *_, tail = self
            tail.next = self.Node(data)
        else:
            self.head = self.Node(data)

    def pop_tail(self) -> None:
        if self.head:
            if self.head.next:
                *_, previous, tail = self
                previous.next = None
            else:
                self.head = None
        else:
            raise IndexError('pop from empty list')

    def get_node(self, pos: int) -> Any:
        if (pos < 0) or (pos+1 > self.size):
            raise IndexError('index out of range')

        for i, current in enumerate(self):
            if i == pos:
                return current.data

    def set_node(self, pos: int, data: Any) -> None:
        if pos == self.size:
            self.set_tail(data)
            return
        elif (pos < 0) or (pos > self.size):
            raise IndexError('index out of range')

        previous = None
        node = self.Node(data)
        for i, current in enumerate(self):
            if i == pos:
                break
            previous = current
        if previous:
            node.next = current
            previous.next = node
        else:
            node.next = self.head
            self.head = node

    def pop_node(self, pos: int) -> None:
        if not self.head:
            raise IndexError('pop from empty list')
        elif (pos < 0) or (pos+1 > self.size):
            raise IndexError('index out of range')

        previous = None
        for i, current in enumerate(self):
            if i == pos:
                break
            previous = current
        if previous:
            previous.next = current.next
        else:
            self.head = current.next
