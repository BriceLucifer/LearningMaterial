from typing import Optional

# 倒退选择k个节点
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def findFromEnd(self, head:Optional[ListNode], k:int):
        # 先判断head是否为空
        if head == None:
            return None
        
        # 然后开始双指针流程
        # p1指针先走k步
        p1 = head
        for i in range(k):
            p1 = p1.next 
            
        p2 = head
        while p1 != None:
            p1 = p1.next 
            p2 = p2.next 
        
        # 现在恰好 p1 走了n-k步 p2 走了n-k步 在n-k+1的位置
        # 1 2 3 4 5 假设总共n = 5 求倒数2个位置节点的值
        # 1 2 p1 4 5
        # 这时候p2 出现
        # p2 2 p1 4 5
        # p1 和 p2 相差k步 那么我p1 走 3 4 5 也就是 5-2 = 3步 (n-k)步
        # 1 2 3 p2 5 p1(None)
        # 所以倒过来 n-k+1 就是倒数第k个节点