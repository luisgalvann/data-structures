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
        if self.head:
            return str([*self])
        return str()
        
    def set_head(self, data: Any) -> None:
        node = self.Node(data)
        node.next = self.head
        self.head = node

    def get_head(self) -> Node:
        return self.head

    def set_tail(self, data: Any) -> None:
        if self.head:
            *_, tail = self
            tail.next = self.Node(data)
        else:
            self.head = self.Node(data)

    def get_tail(self) -> Node:
        if self.head:
            *_, tail = self
            return tail
        return None

    def pop_node(self, pos: int) -> None:
        if not (lng:= len([*self])):
            raise IndexError('pop from empty list')
        elif (pos < 0) or (pos > lng-1):
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

    def insert_node(self, pos: int, data: Any) -> None:
        node = self.Node(data)
        if not (lng:= len([*self])):
            self.head = node
            return
        if (pos < 0) or (pos > lng-1):
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
