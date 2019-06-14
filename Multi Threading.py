from threading import *
from time import sleep
class A(Thread):
    def run(self):
        for a in range(300):
            for b in range(300):
                print('A')

class B(Thread):
    def run(self):
        for a in range(300):
            for b in range(300):
                print('B')


t1= A()
t2=B()
t1.start()
t2.start()
t1.join()
t2.join()
print('End of file')