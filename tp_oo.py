class BankAccount:

    def __init__(self, banque: str, devise="EUR"):
        self.solde = 0
        self.id = 0
        self.devise = devise
        self.banque = banque

    def crediter(self, montant: float):
        if montant > 0:
            self.solde += montant
        else:
            raise ValueError("Montant < 0")

    def debiter(self, montant: float) -> float:
        if montant <= self.solde:
            if montant > 0:
                self.solde -= montant
                return montant
            else:
                raise ValueError("Montant < 0")
        else:
            raise ValueError("Découvert non autorisé")

if __name__ == '__main__':
    c1 = BankAccount("BP")
    c1.crediter(100)
    argent = c1.debiter(60)
    assert 60 == argent
    assert 40 == c1.solde
    try:
        c1.debiter(41)
        assert False
    except ValueError:
        assert True
    c2 = BankAccount("CM")
    c2.crediter(200)
    assert c1.solde != c2.solde





