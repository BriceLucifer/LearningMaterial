# 使用之前创建好的数据结构
from stack import Stack

def divideBy2(decNumber: int)-> str:
    
    binary:Stack = Stack()
    while decNumber > 0:
        rem:int = decNumber % 2
        binary.push(rem)
        decNumber //= 2
        
    bin_str:str = ""
    while not binary.isEmpty():
        bin_str += str(binary.pop())
        
    return bin_str

if __name__ == "__main__":
    test = divideBy2(13)
    print(test)