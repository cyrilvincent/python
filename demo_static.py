class Counter:

    _i = 0

    @staticmethod
    def inc():
        Counter._i += 1

    @staticmethod
    def get_i():
        return Counter._i

    def __del__(self):
        pass


class Singleton:

    instance = None

    @staticmethod
    def factory():
        if Singleton.instance is None:
            Singleton.instance = Singleton()
        return Singleton.instance



if __name__ == '__main__':
    c1 = Counter()
    c1.inc()
    c2 = Counter()
    c2.inc()
    Counter.inc()
    print(Counter.get_i())
    # c1 = None
    # c1 = c2
    # del(c1)
    instance = Singleton.factory()
    instance2 = Singleton.factory()
    print(instance is instance2)
