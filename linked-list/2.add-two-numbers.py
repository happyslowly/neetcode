# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        carry = 0
        dummy = ListNode()  # type: ignore
        tail = dummy
        while carry > 0 or l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            carry, z = divmod(x + y + carry, 10)
            tail.next = ListNode(z)  # type: ignore
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


# @leet end

