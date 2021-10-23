from typing import Any, Tuple


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
        self.head = self.head.next

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

    def get_prev(self, pos: int) -> Tuple[Any, Any]:
        previous = None
        for i, current in enumerate(self):
            if i == pos:
                return previous, current
            previous = current
        raise IndexError('index out of range')

    def set_node(self, pos: int, data: Any) -> None:
        if pos == 0:
            self.set_head(data)
        elif pos == self.size:
            self.set_tail(data)
        else:
            node = self.Node(data)
            previous, current = self.get_prev(pos)
            node.next = current
            previous.next = node

    def pop_node(self, pos: int) -> None:
        if not self.head:
            raise IndexError('pop from empty list')
        if pos == 0:
            self.head = self.head.next
        else:
            previous, current = self.get_prev(pos)
            previous.next = current.next
