# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:  # type: ignore
        dummy = ListNode()  # type: ignore
        dummy.next = head
        p = dummy
        rev_head, rev_tail = None, None
        rev_before, rev_next = None, None
        prev = None
        i = 0
        while p:
            next_ = p.next
            if i == left:
                rev_before = prev
                rev_tail = p
            if i == right:
                rev_head = p
                rev_next = next_
            if left <= i <= right:
                p.next = prev
            prev = p
            p = next_
            i += 1

        assert rev_before is not None
        assert rev_tail is not None
        rev_before.next = rev_head
        rev_tail.next = rev_next
        return dummy.next


# @leet end

