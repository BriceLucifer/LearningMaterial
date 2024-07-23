from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 分而知礼
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val <= list2.val :
            list1.next = Solution().mergeTwoLists(list1.next,list2)
            return list1
        
        list2.next = Solution().mergeTwoLists(list1,list2.next)
        return list2
