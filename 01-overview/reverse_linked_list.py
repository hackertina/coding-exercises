
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        ans = None
        while curr is not None:
            next_ = curr.next
            curr.next = ans
            ans = curr
            curr = next_
        return ans

