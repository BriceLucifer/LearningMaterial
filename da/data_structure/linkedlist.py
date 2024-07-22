from typing import Optional

class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None
        
    def insert(self, val:int):
        # 头部插入
        if not self.next:
            self.next = Node(val)
        else:
            # 当前节点的下一个节点不为空时，递归插入
            self.next.insert(val)
    
    def delete(self):
        if not self.next:
            print("链表为空")
            return
        else:
            self.next = self.next.next

    def print_linked(self):
        if not self.next:
            print(self.val)
            return
        else:
            print(self.val)
            self.next.print_linked()  # 使用正确的递归调用方式
            
if "__main__" == __name__:
    head = Node(0)
    head.insert(1)
    head.insert(2)
    head.insert(3)
    head.insert(4)
    head.print_linked()
    print("--------------")
    head.delete()
    head.print_linked()