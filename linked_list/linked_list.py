from typing import Any, Tuple, Optional


class LinkedList:
    ''' Linked list class implementation '''

    class Node:
        ''' Inner class «Node» implementation '''

        def __init__(self, data) -> None:
            self.data: Any = data
            self.next: Any = None
        
        def __repr__(self) -> str:
            return str(self.data)

    def __init__(self) -> None:
        self.head: Any = None

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
        if not self.head:
            raise IndexError('pop from empty list')
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None

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
        if not self.head:
            raise IndexError('pop from empty list')
        if self.head.next:
            *_, previous, _ = self
            previous.next = None
        else:
            self.head = None

    def get_node(self, pos: int) -> Any:
        for i, current in enumerate(self):
            if i == pos:
                return current.data
        raise IndexError('index out of range')

    def get_nodes(self, pos: int) -> Tuple[Any, Optional[Any]]:
        previous = None
        for i, current in enumerate(self):
            if i == pos:
                break
            previous = current
        else:
            raise IndexError('index out of range')
        return current, previous

    def set_node(self, pos: int, data: Any) -> None:
        if pos == self.size:
            return self.set_tail(data)
        node = self.Node(data)
        if all(nodes:= self.get_nodes(pos)):
            node.next = nodes[0]
            nodes[-1].next = node
        else:
            node.next = self.head
            self.head = node

    def pop_node(self, pos: int) -> None:
        if not self.head:
            raise IndexError('pop from empty list')
        if all(nodes:= self.get_nodes(pos)):
            nodes[-1].next = nodes[0].next
        else:
            self.head = nodes[0].next
