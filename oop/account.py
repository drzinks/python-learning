class User:
    id = 0

    def __init__(self, name):
        self.id = User.id + 1
        User.id += 1
        self.name = name


class Account:

    def __init__(self, user: User, balance=0):
        self.user = user
        self.balance = balance

    def make_deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, amount):
        if (amount > self.balance):
            return Result(False, "Not enough money.", self.balance)
        else:
            self.balance -= amount
            return Result(True, "You withdrawed " + str(amount), self.balance)

    def __str__(self):
        print("Your deposit is: ", self.deposit, "")


class Result:
    def __init__(self, is_success, message, balance):
        self.is_success = is_success
        self.message = message
        self.balance = balance


class MinimumBalanceAccount(Account):
    def __init__(self, user: User, balance=0, min_balance=1000):
        super().__init__(user, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if (amount > self.balance - self.min_balance):
            return Result(False, "Not enough money.", self.balance)
        else:
            return super().withdraw(amount)
