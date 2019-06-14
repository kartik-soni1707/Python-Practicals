class topten:#Using iterator
    def __init__(self):
        self.val=1
    def __iter__(self):
        return self
    def __next__(self):

        if self.val<=10:
            temp = self.val
            self.val+=1
            return temp
        else:
            raise StopIteration


def generator():#using a generator
    num=0
    while num<=10:
        yield num*num*num
        num+=1
ts=generator()
for k in  ts:
    print(k)