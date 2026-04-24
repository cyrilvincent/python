class Atom:

    def __init__(self, nb_electron, nb_proton, nb_neutron, period, symbol):
        self.nb_electron = nb_electron
        self.nb_proton = nb_proton
        self.nb_neutron = nb_neutron
        self.period = period
        self.symbol = symbol

    def ox(self, n: int):
        self.nb_electron -= n

    def red(self, n: int):
        self.nb_electron += n

    def masse_atom(self):
        return self.nb_proton + self.nb_neutron

    def rayon_atom(self):
        return 1.2 * self.masse_atom() ** 1/3

if __name__ == '__main__':
    fer = Atom(26,26,26,4,"Fe")
    assert fer.masse_atom() == 52
    assert fer.nb_electron == 26
    fer.ox(2)
    assert fer.nb_electron == 24
    fer.red(2)
    assert fer.nb_electron == 26