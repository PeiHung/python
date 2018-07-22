def multi(n1,n2):
    for X in range(1,n1+1):
        for Y in range(1,n2+1):
            Z=X*Y
            print(X,"*",Y,"=",Z)

def caculation(x,y,op):
    x=int(x)
    y=int(y)
    if op=="+":
        print(x+y)
    elif op=="-":
        print(x-y)
    elif op=="*":
        print(x*y)
    elif op=="/":
        print(x/y)
    else:
        print("不支援的運算")
