class Account:

    def __init__(self, id, owner):
        self.id = id
        self.owner = owner
        self._balance = 0 #private

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self._balance -= amount
            return amount
        else:
            raise ValueError("Amount > Balance")

    def __repr__(self):
        return f"Account {self.id}: {self.balance}"

class LivretA(Account):

    def __init__(self, id, owner, rate):
        super().__init__(id, owner)
        self.rate = rate

    def interest(self):
        return self.balance * self.rate

    def add_interest(self):
        self.deposit(self.interest())

if __name__ == '__main__':

    a1 = Account("001", "Cyril")
    a1.deposit(100)
    a1.withdraw(30)
    print(a1._balance)
    la1 = LivretA("002", "Cyril", 0.005)
    la1.deposit(1000)
    print(la1.interest())
    la1.add_interest()
    print(la1.balance)
    print(la1)

