import time
import tp3
import threading

class MyThread(threading.Thread):

    def __init__(self, num):
        super().__init__()
        self.num = num
        self.rangemin = 100000
        self.rangemax = 1000000
        self.progressCb = None

    def run(self):
        for i in range(self.rangemin, self.rangemax):
            if tp3.isPrime(i):
                #print(f"Thread{self.num}:{i}")
                pass
            if i % 100 == 0:
                self.progressCb((i - self.rangemin) / (self.rangemax - self.rangemin), self.num)
            time.sleep(0.1)


def myProgressFn(progress, num):
    print(f"Thread {num} progress: {progress * 100}%")



t1 = MyThread(1)
t1.progressCb = myProgressFn
t1.start()
t2 = MyThread(2)
t2.progressCb = myProgressFn
t2.rangemin = 1000000
t2.rangemax = 2000000
t2.start()
for i in range(1000000):
    if tp3.isPrime(i):
        print(f"Main:{i}")
    time.sleep(0.1)
