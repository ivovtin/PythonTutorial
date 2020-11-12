import threading

from threading import Thread

class f1:

    def __init__(self):
        pass

    def func1(self):
        for i in range(10):
            print('Working111')
class f2:

    def __init__(self):
        pass

    def func2(self):
        for i in range(10):
            print('Working222')


ff1 = f1()

ff2 = f2()

if __name__ == '__main__':

    Thread(target = ff1.func1).start()
    Thread(target = ff2.func2).start()
    
