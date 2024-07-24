# stack implmentation
class Stack:
    def __init__(self):
        self.items = [ ]
        self.head = 0
    
    def push(self, item):
        self.items.append(item)
        self.head += 1
    
    def pop(self)->int:
        self.head -= 1
        return self.items.pop()
        
    def peek(self)->int:
        return self.items[self.head-1]
    
    def size(self)->int:
        return self.head
    
    def isEmpty(self)->bool:
        return self.head == 0
    
    def print_stack(self):
        for i in range(self.head-1, -1, -1):
            print(self.items[i])
            
        
if __name__ == "__main__":
    test:Stack = Stack()
    if test.isEmpty():
        print("is empty")
        
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    
    peek = test.peek()
    print(peek)
    print("------------")
    
    test.pop()
    peek = test.peek()
    print(peek)
    print("------------")
    
    test.push(10)
    test.print_stack()
