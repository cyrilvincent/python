class Counter:

    i = 0 # Shared

    @staticmethod
    def count():
        Counter.i += 1
        return Counter.i

if __name__ == '__main__':
    c1 = Counter()
    print(c1.count())
    print(c1.count())
    c2 = Counter()
    print(c2.count())

    print(Counter.count())