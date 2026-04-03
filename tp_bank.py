import datetime

class Owner:
    pass

class Transaction:
    pass

    # montant
    # date
    # datetime.datetime.now()
    # Quand on crédite BankAccount on créé une transaction +montant
    # Auand on débite                               ``     -montant
    # Un BankAccount possède une liste de transaction à la création = []

class BankAccount:

    def __init__(self, id, owner: Owner):
        self.id = id
        self.solde = 0
        self.owner = owner

    def crediter(self, montant):
        self.solde += montant

    def debiter(self, montant):
        if montant > self.solde:
            raise ValueError("Montant > Solde")
        self.solde -= montant

if __name__ == '__main__':
    c1 = BankAccount("123", "Cyril")
    print(c1.solde)
    c1.crediter(100)
    c1.debiter(20)
    print(c1.solde)