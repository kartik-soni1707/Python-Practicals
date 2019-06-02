import sys
sys.setrecursionlimit(3296)#Incraesing recursion limit

def fib(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)

x=int(input('Enter no.:'))
fib(x)