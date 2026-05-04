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

class Molecul:

    def __init__(self, atoms: list[Atom]):
        self.atoms = atoms

    def mass_mol(self):
        total = 0
        for atom in self.atoms:
            total += atom.masse_atom()
        return total

class Molecul2:

    def __init__(self, atoms: list[tuple[Atom, int]]):
        self.atoms = atoms

    def mass_mol(self):
        total = 0
        for couple in self.atoms:
            total += couple[0].masse_atom() * couple[1]
        return total

if __name__ == '__main__':
    fer = Atom(26,26,26,4,"Fe")
    assert fer.masse_atom() == 52
    assert fer.nb_electron == 26
    fer.ox(2)
    assert fer.nb_electron == 24
    fer.red(2)
    assert fer.nb_electron == 26
    h = Atom(1,1,0,1,"H")
    o = Atom(8,8,8,2,"O")
    h2o = Molecul([h,h,o])
    print(h2o.mass_mol())
    h2o = Molecul2([(h,2), (o,1)])
    print(h2o.mass_mol())