# @leet start
from typing import Optional


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache: dict[int, Node] = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._promote(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.cap:
            self._evict()
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self._insert(node)
        else:
            node = self.cache[key]
            node.value = value
            self._promote(node)

    def _evict(self) -> None:
        node = self.tail.prev
        assert node is not None
        assert node.prev is not None
        node.prev.next = self.tail
        self.tail.prev = node.prev
        node.next = None
        node.prev = None
        del self.cache[node.key]

    def _promote(self, node: Node) -> None:
        assert node.prev is not None
        assert node.next is not None
        node.prev.next = node.next
        node.next.prev = node.prev
        self._insert(node)

    def _insert(self, node: Node) -> None:
        assert self.head.next is not None
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @leet end
