from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reserveList(self,head:Optional[ListNode])->Optional[ListNode] :
        if not head or not head.next:
            return None

        newhead = self.reserveList(head.next)
        head.next.next = head
        head.next = None
        return newhead
        
