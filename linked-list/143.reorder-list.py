# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:  # type: ignore
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        head2 = self._reverse(middle)
        slow.next = None

        p, q = head, head2
        tail = head
        while p and q:
            next_p = p.next
            next_q = q.next
            tail.next = q
            q.next = next_p

            p = next_p
            q = next_q
            tail = p

    def _reverse(self, node: ListNode) -> ListNode:  # type: ignore
        prev, curr = None, node
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev


# @leet end

