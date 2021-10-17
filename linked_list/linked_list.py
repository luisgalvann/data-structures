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
            for node in self:
                pass
            node.next = self.Node(data)

    def get_tail(self) -> Node:
        if not self.head.next:
            return self.head
        else:
            for node in self:
                pass
            return node

    def __repr__(self) -> str:
        result = []
        if (current:= self.head):
            while current:
                node = current
                current = node.next
                result.append(node)
            return str(result)
        return 'None'

    def __iter__(self) -> Any:
        current = self.head
        while current:
            yield current
            current = current.next
