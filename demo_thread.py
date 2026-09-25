import time
import threading
class HugeComputing(threading.Thread):

    def __init__(self, id: str, nb: int):
        super().__init__()
        self.id = id
        self.nb = nb
        self.result = 1

    def run(self):
        for i in range(self.nb):
            self.result *= 2
            print(self.id, self.nb)
            time.sleep(0.1)

if __name__ == '__main__':
    huge = HugeComputing("A", 100)
    huge.start()
    huge2 = HugeComputing("B", 100)
    huge2.start()
    huge.join()
    huge2.join()
    print(huge.result)


