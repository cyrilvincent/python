# static = shared

class Counter:

    i=0

    def increment(self):
        Counter.i += 1

if __name__ == '__main__':
    c1 = Counter()
    print(c1.i)
    c1.increment()
    c1.increment()
    print(c1.i)
    c2 = Counter()
    c2.increment()
    print(c2.i)