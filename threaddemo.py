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
        self.mock = 0

    def run(self):
        for i in range(self.rangemin, self.rangemax):
            if tp3.isPrime(i):
                #print(f"Thread{self.num}:{i}")
                pass
            if i % 100 == 0:
                self.progressCb((i - self.rangemin) / (self.rangemax - self.rangemin), self.num)
            time.sleep(0.1)

class MainThread(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        self.t1 = MyThread(1)
        self.t1.progressCb = self.myProgressFn
        self.t1.start()
        self.t2 = MyThread(2)
        self.t2.progressCb = self.myProgressFn
        self.t2.rangemin = 1000000
        self.t2.rangemax = 2000000
        self.t2.start()
        for i in range(1000000):
            if tp3.isPrime(i):
                print(f"Main:{i}")
            time.sleep(0.1)

    def myProgressFn(self, progress, num):
        print(f"Thread {num} progress: {progress * 100}%")
        if num == 1:
            self.t2.mock += 1


if __name__ == '__main__':
    main = MainThread()
    main.start()




