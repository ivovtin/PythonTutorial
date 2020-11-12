from threading import Thread
from time import sleep

def func1():
    for i in range(5):
        #print(f"from thread1: {i}")
        print "from thread1:", i
        sleep(0.5)

def func2():
    for i in range(5):
        #print(f"from thread2: {i}")
        print "from thread2:", i
        sleep(0.5)
        
th1 = Thread(target=func1)
th2 = Thread(target=func2)

th1.start()
th2.start()

th1.join()
th2.join()

print("--> stop")

