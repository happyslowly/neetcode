# @leet start
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.dummy = Node(-1)
        self.tail = self.dummy
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        assert self.tail is not None
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        assert self.dummy.next is not None
        self.dummy.next = self.dummy.next.next
        self.size -= 1
        if self.size == 0:
            self.tail = self.dummy
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        assert self.dummy.next is not None
        return self.dummy.next.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        assert self.tail is not None
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @leet end

