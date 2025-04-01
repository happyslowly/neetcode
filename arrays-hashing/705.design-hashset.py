# @leet start
class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node | None = None


class MyHashSet:

    def __init__(self):
        self.cap = 10
        self.buckets: list[Node | None] = [None] * self.cap

    def add(self, key: int) -> None:
        i = hash(key) % self.cap
        if not self.buckets[i]:
            self.buckets[i] = Node(-1)
        p = self.buckets[i]
        assert p is not None
        while p.next:
            if p.next.val == key:
                return
            p = p.next
        p.next = Node(key)

    def remove(self, key: int) -> None:
        i = hash(key) % self.cap
        if not self.buckets[i]:
            return
        p = self.buckets[i]
        assert p is not None
        while p.next and p.next.val != key:
            p = p.next
        if p.next:
            p.next = p.next.next

    def contains(self, key: int) -> bool:
        i = hash(key) % self.cap
        if not self.buckets[i]:
            return False
        p = self.buckets[i]
        assert p is not None
        while p.next and p.next.val != key:
            p = p.next
        return p.next is not None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @leet end

