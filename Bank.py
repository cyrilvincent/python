from typing import List

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Transaction:

    def __init__(self, amount):
        self.amount = amount

class Account:

    def __init__(self, id, owner: User, transactions: List[Transaction] = []):
        self.id = id
        self.balance = 0
        self.owner = owner
        self.transactions = transactions

    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            t = Transaction(amount)
            self.transactions.append(t)
        else:
            pass

    def debit(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(Transaction(-amount))
        else:
            pass





if __name__ == '__main__':
    u1 = User("Cyril", "Vincent")
    a1 = Account(123, u1)
    a1.credit(120)
    a1.debit(50)
    print(a1.balance)