#Function definition 
def sqr(param):
    return param*param 
List=[1,2,3,4,5,'a','b','c','d','e']#This is a list
Tuple=(1,2,3,4,5,'a','b','c','d','e')#This is a tuple
Diction={'Key 1':'Val 1','Key 2':'Val 2','Key 3':'Val 3'}#This is a diction
List[1]=9
#Note list is mutable but a tuple isn't
#For eg:Tuple[1] is illegal
k=int(input('Enter number'))
#Calling sqr function
print(sqr(k))
