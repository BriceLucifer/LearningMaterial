from stack import Stack

def decToany(decNumber:int,base:int)->str:
    numberBase = "0123456789ABCDEF"
    # 16进制base
    
    container:Stack = Stack()
    # 创建保存转换后数据的容器
    
    while decNumber > 0:
        rem = decNumber % base
        container.push(rem)
        decNumber = decNumber // base
        
    result:str = ""
    while not container.isEmpty():
        result += numberBase[container.pop()]
        
    return result

if __name__ == "__main__" :
    test = decToany(255,16)
    print(test)