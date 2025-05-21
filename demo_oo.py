class Rectangle:

    def __init__(self, length:float, width:float):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.length + self.width)

class BankAccount:

    counter = 1

    def __init__(self, customer: str):
        self.customer = customer
        self.iban = BankAccount.counter
        BankAccount.counter += 1
        self.balance = 0

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        # else:
        #     raise ValueError("Découvert non autorisé")



if __name__ == '__main__':
    r1 = Rectangle(3,2)
    assert r1.area() == 6
    assert r1.perimeter() == 10
    b1 = BankAccount("Cyril")
    b1.deposit(1000)
    b1.withdraw(100)
    assert b1.balance == 900
    b2 = BankAccount("John")
    try:
        b2.withdraw(100)
        assert False
    except ValueError as error:
        pass

