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
    
    def set_head(self, data: Any) -> None:
        node = self.Node(data)
        node.next = self.head
        self.head = node

    def get_head(self) -> Node:
        return self.head

    def set_tail(self, data: Any) -> None:
        if self.head:
            *_, last = self
            last.next = self.Node(data)
        else:
            self.head = self.Node(data)

    def get_tail(self) -> Node:
        if self.head.next:
            *_, last = self
            return last
        return self.head

    def __repr__(self) -> str:
        if self.head:
            result = [x for x in self]
            return str(result)
        return 'None'

    def __iter__(self) -> Any:
        current = self.head
        while current:
            yield current
            current = current.next
