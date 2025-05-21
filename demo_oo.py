import datetime


class Point:

    def __init__(self,x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def move_relative(self, x: float, y: float):
        self.x += x
        self.y += y


class Rectangle:

    def __init__(self, length:float, width:float, origin: Point):
        self.length = length
        self.width = width
        self.origin = origin

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):

    def __init__(self, side: float, origin: Point):
        Rectangle.__init__(self, side, side, origin)

class Transaction:

    def __init__(self, amount: float):
        self.datetime = datetime.datetime.now()
        self.amount = amount

class BankAccount:

    counter = 1

    def __init__(self, customer: str, transactions: list[Transaction] = []):
        self.customer = customer
        self.iban = BankAccount.counter
        BankAccount.counter += 1
        self.balance = 0
        self.transactions = transactions

    def deposit(self, amount: float):
        self.balance += amount
        transaction = Transaction(amount)
        self.transactions.append(transaction)

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            transaction = Transaction(-amount)
            self.transactions.append(transaction)
        else:
            raise ValueError("Découvert non autorisé")


class LivretA(BankAccount):

    def __init__(self, customer: str, transactions: list[Transaction] = [], rate: float = 0):
        BankAccount.__init__(self, customer, transactions)
        self.rate = rate

    def interest(self):
        return self.balance * self.rate

    def credit_interest(self):
        interest = self.interest()
        self.deposit(interest)


if __name__ == '__main__':
    r1 = Rectangle(3,2, Point(1,-1))
    assert r1.area() == 6
    assert r1.perimeter() == 10
    assert r1.origin.x == 1
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
    s1 = Square(3, Point(1,-1))
    assert s1.area() == 9
    s1.origin.move(3,4)
    assert s1.origin.x == 3

