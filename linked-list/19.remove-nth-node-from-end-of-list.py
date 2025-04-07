# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  # type: ignore
        dummy = ListNode()  # type: ignore
        dummy.next = head
        first = head
        while first and n > 0:
            first = first.next
            n -= 1
        second = dummy
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


# @leet end

