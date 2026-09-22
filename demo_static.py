class Counter:

    count = 0

    # def __init__(self):
    #     # self.count = 0
    #     pass

    def increment(self):
        # self.count += 1
        Counter.count += 1


if __name__ == '__main__':
    c1 = Counter()
    c1.increment()
    c1.increment()
    print(c1.count)
    c2 = Counter()
    c2.increment()
    print(c2.count)
