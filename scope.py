class father:
    def fun(self):
        print('this is first print ')
class mother(father):
    def fun(self):
        print('this is second print ')
        def fun1(self):
            super().fun(self)
            print('this is three print')
maj=mother()
maj.fun()           

                

