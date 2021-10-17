from typing import Any


class LinkedList:
    ''' Linked list class implementation '''

    class Node:
        ''' Inner class «Node» implementation '''

        def __init__(self, data) -> None:
            self.data = data
            self.next = None
        
        def __repr__(self) -> str:
            return str(self.data)

    def __init__(self) -> None:
        self.head: Node = None
    
    def set_head(self, data) -> None:
        node = self.Node(data)
        node.next = self.head
        self.head = node

    def get_head(self) -> Node:
        return self.head

    def set_tail(self, data) -> None:
        if not self.head:
            self.head = self.Node(data)
        else:
            *_, last = self
            last.next = self.Node(data)

    def get_tail(self) -> Node:
        if not self.head.next:
            return self.head
        else:
            *_, last = self
            return last

    def __repr__(self) -> str:
        if not self.head:
            return 'None'
        result = []
        for node in self:
            result.append(node)
        return str(result)
        
    def __iter__(self) -> Any:
        current = self.head
        while current:
            yield current
            current = current.next
