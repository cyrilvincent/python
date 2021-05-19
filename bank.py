class Account:

    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self._balance = 0 #private

    @property
    def balance(self):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self._balance -= amount
            return amount
        else:
            raise ValueError("Amount > Balance")

if __name__ == '__main__':

    a1 = Account("001", "Cyril")
    a1.deposit(100)
    a1.withdraw(30)
    print(a1._balance)

