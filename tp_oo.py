import datetime

class Personne:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Transaction:

    def __init__(self, montant: float, date: datetime.datetime=datetime.datetime.now()):
        self.montant = montant
        self.date = date


class BankAccount:

    count = 1

    def __init__(self, banque: str, titulaire: Personne, devise="EUR"):
        self.solde = 0
        self.id = BankAccount.count
        BankAccount.count += 1
        self.devise = devise
        self.banque = banque
        self.titulaire = titulaire
        self.transactions: list[Transaction] = []

    def crediter(self, montant: float):
        if montant > 0:
            self.solde += montant
            transac = Transaction(montant)
            self.transactions.append(transac)

        else:
            raise ValueError("Montant < 0")

    def debiter(self, montant: float) -> float:
        if montant <= self.solde:
            if montant > 0:
                self.solde -= montant
                transac = Transaction(-montant)
                self.transactions.append(transac)
                return montant
            else:
                raise ValueError("Montant < 0")
        else:
            raise ValueError("Découvert non autorisé")

if __name__ == '__main__':
    p1 = Personne("Cyril", "Vincent")
    c1 = BankAccount("BP", p1)
    c1.crediter(100)
    argent = c1.debiter(60)
    assert 60 == argent
    assert 40 == c1.solde
    assert 1 == c1.id
    assert "Cyril" == c1.titulaire.fname
    assert 2 == len(c1.transactions)
    try:
        c1.debiter(41)
        assert False
    except ValueError:
        assert True
    c2 = BankAccount("CM", p1)
    c2.crediter(200)
    assert c1.solde != c2.solde
    assert 2 == c2.id





