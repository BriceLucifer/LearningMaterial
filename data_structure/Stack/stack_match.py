# 读取一个字符串 判断括号是否匹配

# 直接使用python自带的数据结构 Stack

from stack import Stack

def parChecker(symbolString:str)->bool:
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        
        index += 1
        
    if balanced and s.isEmpty():
        return True
    else:
        return False        
    
if __name__ == "__main__":
    temp:str = "((((())))"
    if parChecker(temp):
        print("parCheck success")
    else:
        print("parCheck failed")