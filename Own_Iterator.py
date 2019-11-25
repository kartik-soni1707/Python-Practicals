class pow:
    def __init__(self,pw):
        self.power=pw
    def __iter__(self):
        self.present=0
        return self
    def __next__(self):
        if self.present<=self.power:
            ans=2**self.present
            self.present+=1
            return ans

        else:
            raise StopIteration

g=pow(6)
for i in g:
    print(i)

