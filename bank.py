class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: £{}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}'s Current Account : Balance £{}".format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Savings Account : Balance £{}".format(self.name, self.balance)


if __name__ == '__main__':
    D = Current("Dk", 500)
    print(D)
    D.withdraw(1500)
    D.statement()
    D.withdraw(1)

    T = Savings("T", 300)
    print(T)
    T.withdraw(300)
    T.statement()
    T.withdraw(1)