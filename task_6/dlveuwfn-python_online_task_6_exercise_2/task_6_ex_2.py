from typing import Any


class Item:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class CustomList:
    def __init__(self, *data) -> None:
        if data:
            self.head = Item(data)
        else:
            self.head = None

    def append(self, value) -> None:
        node = Item(value)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def add_start(self, value) -> None:
        node = Item(value)
        node.next = self.head
        self.head = node

    def remove(self, value) -> None:
        if self.head is not None:
            if self.head.value == value:
                self.head = self.head.next
            else:
                previous_node = self.head
                for node in self:
                    if node.value == value:
                        previous_node.next = node.next
                        return None
                    else:
                        previous_node = node

        raise Exception(f"Node with value = {value} not found")

    def __getitem__(self, index) -> Any:
        if index < 0:
            index = len(self) + index

        for i, node in enumerate(self):
            if i == index:
                return node.value
        raise Exception("Index out of range")

    def __setitem__(self, index, data) -> None:
        if index < 0:
            index = len(self) + index

        for i, node in enumerate(self):
            if i == index:
                node.value = data
                return
        raise Exception("Index out of range")

    def __delitem__(self, index) -> None:
        if index < 0:
            index = len(self) + index

        if index == 0:
            self.head = self.head.next
            return
        for i, node in enumerate(self):
            if i + 1 == index:
                if node.next.next is None:
                    raise Exception("Index out of range")
                node.next = node.next.next
                return
        raise Exception("Index out of range")

    def find(self, value) -> Any:
        index = 0

        if self.head is not None:
            for node in self:
                if node.value == value:
                    return index
                index += 1

        raise Exception(f"Node with value = {value} not found")

    def clear(self) -> None:
        self.head = None

    def __len__(self) -> int:
        result = 0
        for node in self:
            result += 1
        return result

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
