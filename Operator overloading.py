class student:
    def __init__(self,grd):
        self.grade=grd
    def __gt__(self, other):
        return self.grade>other.grade


John=student(11)
Jack=student(10)
print(John>Jack)