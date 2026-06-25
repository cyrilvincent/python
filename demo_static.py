class Compteur:

    i = 0

    def __init__(self):
        # self.i = 0
        pass

    
    # def inc(self):
    #     # self.i += 1
    #     Compteur.i += 1

    @staticmethod
    def inc():
        Compteur.i += 1


c1 = Compteur()
# c1.inc()
# c1.inc()
Compteur.inc()
print(c1.i)
c2 = Compteur()
# c2.inc()
# print(c1.i, c2.i)