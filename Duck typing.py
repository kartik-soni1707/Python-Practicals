class A:
    def swim(self,duck):
        duck.quack()

class not_a_duck:
    def quack(self):
        print('Quackkk')

x=A()
nd=not_a_duck()

x.swim(nd)