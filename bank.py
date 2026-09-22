# class Account
# Environ 5 attributs QUOI
# Comment deposit, withdraw
# Robustesse
# Tests
import datetime

# class Owner (first_name, last_name, address, phone, ...)
# Account à un seul Owner
# Transaction : amount, datetime, owner
# Account possède plusieurs transactions, au départ transactions = []
# datetime.datetime.now() : datetime.datetime


class Account:

    nb = 0

    def __init__(self, id: str, owner: str, bank: str, devise = "EUR"):
        self.id = id
        self.balance = 0
        self.owner = owner
        self.bank = bank
        self.devise = devise
        Account.nb += 1

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

    def __del__(self):
        Account.nb -= 1

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
    a2 = Account("002", "toto", "titi")
    assert Account.nb == 2
    del a2
    assert Account.nb == 1
    a1 = None
    assert Account.nb == 0