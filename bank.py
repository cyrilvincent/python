# class Account
# Environ 5 attributs QUOI
# Comment deposit, withdraw
# Robustesse
# Tests

class Account:

    def __init__(self, id: str, owner: str, bank: str, devise = "EUR"):
        self.id = id
        self.balance = 0
        self.owner = owner
        self.bank = bank
        self.devise = devise

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("The amount must be strictly positive")

    def withdraw(self, amount: float):
        if amount <= self.balance:
            if amount > 0:
                self.balance -= amount
            else:
                raise ValueError("The amount must be strictly positive")
        else:
            raise ValueError("Amount must be <= balance")

if __name__ == '__main__':
    a1 = Account("001", "Cyril", "CEA")
    assert a1.balance == 0
    a1.deposit(100)
    assert a1.balance == 100
    a1.withdraw(20)
    assert a1.balance == 80
    try:
        a1.withdraw(1000)
    except ValueError:
        pass