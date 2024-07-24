# 多符号匹配
from stack import Stack

    

def parChecker_multi(symbolString:str)->bool:
    
    # 使用lambda 直接封装一个函数
    opens:str = "({["
    closers:str = ")}]"
    match = lambda top,close : opens.index(top) == closers.index(close)
    
    s = Stack() # 创建栈数据结构
    balanced = True # 平衡标志
    index = 0   # index为了后续的索引
    
    # 循环 如果index小于字符串长度 并且不失衡
    while index < len(symbolString) and balanced:
        
        # 从第一个0位索引字符串开始
        symbol = symbolString[index]
        # 如果这个字符在opens里面 那么进行入栈
        if symbol in opens:
            s.push(symbol)
        # 如果不在 那就是在closers里面 那就进行判断
            # 如果是空的 那么说明多余了一个 直接退出
            # 不是空的 那么弹出栈顶 和现有的匹配 
                # 如果括号的index相同 那么说明匹配了 然后继续执行循环 如果不匹配 直接退出了循环 
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balanced = False
        index += 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    test = "([[([])]])"
    if parChecker_multi(test):
        print("parChecker success")
    else:
        print("parChecker fail")