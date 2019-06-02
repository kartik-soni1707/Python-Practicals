import sys
sys.setrecursionlimit(3296)#Incraesing recursion limit
k=0


def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)

x=int(input('Enter no.:'))
print(fact(x))



