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

    def __repr__(self) -> str:
        return str([*self]) if self.head else ''

    def size(self) -> int:
        return len([*self])

    def get_head(self) -> Node:
        return self.head

    def set_head(self, data: Any) -> None:
        node = self.Node(data)
        node.next = self.head
        self.head = node

    def pop_head(self) -> Node:
        if self.head:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        else:
            raise IndexError('pop from empty list')

    def get_tail(self) -> Node:
        if self.head:
            *_, tail = self
            return tail
        return None

    def set_tail(self, data: Any) -> None:
        if self.head:
            *_, tail = self
            tail.next = self.Node(data)
        else:
            self.head = self.Node(data)

    def pop_tail(self) -> Node:
        if self.head:
            if self.head.next:
                *_, previous, tail = self
                previous.next = None
            else:
                self.head = None
        else:
            raise IndexError('pop from empty list')

    def get_node(self, pos: int) -> Any:
        if (pos < 0) or (pos+1 > self.size()):
            raise IndexError('index out of range')

        for i, current in enumerate(self):
            if i == pos:
                return current
                
    def set_node(self, pos: int, data: Any) -> None:
        node = self.Node(data)
        if not self.size():
            self.head = node
            return
        if (pos < 0) or (pos+1 > self.size()):
            raise IndexError('index out of range')

        previous = None
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
        if not self.size():
            raise IndexError('pop from empty list')
        elif (pos < 0) or (pos+1 > self.size()):
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
