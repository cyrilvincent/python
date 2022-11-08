class Account:

    def __init__(self, id, owner):
        self.id = id
        self.balance = 0
        self.owner = owner

    def credit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            pass

    def debit(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
            pass

if __name__ == '__main__':
    a1 = Account(123, "Cyril")
    a1.credit(120)
    a1.debit(50)
    print(a1.balance)