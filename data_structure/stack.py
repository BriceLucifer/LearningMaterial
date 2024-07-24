# stack implmentation
class Stack:
    def __init__(self):
        self.items = [ ]
        self.head = 0
    
    def push(self, item):
        self.items.append(item)
        self.head += 1
    
    def pop_top(self):
        self.head -= 1
        return self.items.pop()
        
    def peek(self):
        return self.items[self.head-1]
    
    def print_stack(self):
        for i in range(self.head-1, -1, -1):
            print(self.items[i])
            
        
if __name__ == "__main__":
    test:Stack = Stack();
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    
    peek = test.peek()
    print(peek)
    print("------------")
    
    test.pop_top()
    peek = test.peek()
    print(peek)
    print("------------")
    
    test.push(10)
    test.print_stack()