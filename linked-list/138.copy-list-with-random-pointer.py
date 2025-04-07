# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":  # type: ignore
        p = head
        while p:
            node = Node(p.val, next=p.next, random=p.random)  # type: ignore
            p.next = node
            p = node.next

        # update random pointers
        p = head
        while p:
            node = p.next
            if node.random:
                node.random = node.random.next
            p = node.next

        # split
        p = head
        dummy = Node(0)  # type: ignore
        tail = dummy
        while p:
            node = p.next
            p.next = p.next.next
            p = p.next
            tail.next = node
            tail = node

        return dummy.next


# @leet end
