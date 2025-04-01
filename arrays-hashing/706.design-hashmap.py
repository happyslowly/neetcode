# @leet start
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next: Node | None = None


class MyHashMap:

    def __init__(self):
        self.cap = 10
        self.buckets: list[Node | None] = [None] * self.cap

    def put(self, key: int, value: int) -> None:
        i = hash(key) % self.cap
        if not self.buckets[i]:
            self.buckets[i] = Node(-1, -1)
        p = self.buckets[i]
        assert p is not None
        while p.next:
            if p.next.key == key:
                p.next.value = value
                return
            p = p.next
        p.next = Node(key, value)

    def get(self, key: int) -> int:
        i = hash(key) % self.cap
        if not self.buckets[i]:
            return -1
        p = self.buckets[i]
        assert p is not None
        while p.next:
            if p.next.key == key:
                return p.next.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        i = hash(key) % self.cap
        if not self.buckets[i]:
            return
        p = self.buckets[i]
        assert p is not None
        while p.next and p.next.key != key:
            p = p.next
        if p.next:
            p.next = p.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @leet end

