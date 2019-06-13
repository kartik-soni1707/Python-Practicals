class Laptop:
    def __init__(self,proc,ram,str):
        self.prc=proc
        self.ram=ram
        self.str=str
        self.st=self.storage(self.str)
    class storage:
        def __init__(self,stor):
            self.stor=stor
            self.show()
        def show(self):
            print(self.stor)

hp=Laptop('i5',8,'Hdd')