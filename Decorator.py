def sub(a,b):
    print(a-b)

def decorator(func):
    def smartsub(a,b):
        if b>a:
            a,b=b,a
        sub(a,b)
    return smartsub
d=decorator(sub)
print(d(1,2))