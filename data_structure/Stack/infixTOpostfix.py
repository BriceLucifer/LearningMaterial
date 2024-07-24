from stack import Stack

import string

def inToPost(infixExpr: str)-> str:
    prec:dict = dict()
    prec["*"] = 3
    prec["/"] = 3
    prec["-"] = 2
    prec["+"] = 2
    prec["("] = 1
    
    opStack:Stack = Stack()
    postfixList:list = list()
    
    tokenList:list[str] = infixExpr.split()
    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
                
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
            
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
        
    return " ".join(postfixList)

if __name__ == "__main__" :
    post = inToPost("A * B + C * ( D + E )")
    print(post)