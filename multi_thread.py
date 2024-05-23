import threading
import time
from typing import Callable


class Huge(threading.Thread):

    def __init__(self, num: int, nb_loop: int, pause: float, end_cb: Callable, progress_cb: Callable):
        super().__init__()
        self.num = num
        self.pause = pause
        self.nb_loop = nb_loop
        self.result = 1
        self.end_cb = end_cb
        self.progress_cb = progress_cb

    def run(self):
        for i in range(self.nb_loop):
            if i%2 == 0:
                self.progress_cb(i / self.nb_loop, self.num)
            # print(f"Hello from thread {self.num}")
            self.result *= 2
            time.sleep(self.pause)
        self.end_cb(self.result, self.num)

def main_end(result: int, num: int):
    print(result, num)

def main_progress(progress: float, num: int):
    print(f"Progress from thread {num}: {progress*100}%")




if __name__ == '__main__':
    t1 = Huge(1, 80, 0.2, main_end, main_progress)
    t2 = Huge(2, 100, 0.1, main_end, main_progress)

    t1.start()
    t2.start()



