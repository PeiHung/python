#四則運算
n1=int(input("請輸入數字一:"))
n2=int(input("請輸入數字二:"))
op=input("請輸入運算符號+,-,*,/:")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")

#求平方根
#解法1
n=int(input("輸入一個正整數:"))
a=1
while a<=n:
    sum=a*a
    if sum==n:
        break
    a+=1
if a<n:
    print(a)
else:
    print("沒有整數平方根")

#解法2
n=int(input("輸入一個正整數"))
a=n**0.5
if a%1<=0:
    print(a)
else:
    print("無整數平方根")

#九九乘法表
for X in range(1,10):
    for Y in range(1,10):
        Z=X*Y
        print(X,"*",Y,"=",Z)
    print("============================")

