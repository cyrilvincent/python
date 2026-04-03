import datetime

class Owner:

    def __init__(self, id, prenom, nom, tel, mail):
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.tel = tel
        self.mail = mail

class Transaction:

    def __init__(self, montant):
        self.montant = montant
        self.date = datetime.datetime.now()

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
        self.transactions: list[Transaction] = []

    def crediter(self, montant):
        self.solde += montant
        transaction = Transaction(montant)
        self.transactions.append(transaction)

    def debiter(self, montant):
        if montant > self.solde:
            raise ValueError("Montant > Solde")
        self.solde -= montant
        transaction = Transaction(-montant)
        self.transactions.append(transaction)


class BankAcountRemunere(BankAccount):

    # interest_rate

    def compute_interest(self):
        pass
        # solde * interest_rate

if __name__ == '__main__':
    o1 = Owner("0", "Cyril", "Vincent", "0622538762", "contact@cyrilvincent.com")
    c1 = BankAccount("123", o1)
    print(c1.solde)
    c1.crediter(100)
    c1.debiter(20)
    print(c1.solde)
    print(c1.owner.prenom)
    for t in c1.transactions:
        print(t.montant, t.date)
