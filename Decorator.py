from functools import *
lst=[1,2,3,4,5,6,7,8,9]

odd=list(filter(lambda a:a%2==1,lst))

plus_two=list(map(lambda a:a+2,odd))

sum=reduce(lambda a,b:a+b,odd)

print(sum)
