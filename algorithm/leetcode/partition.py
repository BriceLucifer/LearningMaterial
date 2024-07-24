from typing import Optional

class ListNode:
    def __init__(self,val):
        self.val = val 
        self.next = None

class Solution:
    def partition(self,head:Optional[ListNode],x:int)->Optional[ListNode]:
        # 双指针
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        
        p = head # 头指针
        while p :
            if p.val >= x:
                # 如果大于等于那么我就插入到第二个链表
                dummy2.next = p
                dummy2 = dummy2.next
            else:
                dummy1.next = p
                dummy1 = dummy1.next
            # 让移动的指针断开 如果是cpp的话 需要delete
            temp:ListNode = p.next 
            p.next = None
            p = temp
            
        dummy1.next = dummy2.next
        return dummy1.next