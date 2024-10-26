class User:
    id = 0

    def __init__(self, name):
        self.id = User.id + 1
        User.id += 1
        self.name = name

class Account:

    def __init__(self, user: User):
        self.user = user
        self.deposit = 0

    def make_deposit(self, deposit):
        self.deposit += deposit

    def withdraw(self, amount):
        if(amount > self.deposit):
            print("You want to withdraw more than you have.")
            self.deposit = 0
            print("Withdrawing only ",self.deposit)
        else:
            self.deposit -= amount
            print("Withdrawing: ", amount, ". Your balance is: ",self.deposit,".")

    def __str__(self):
        print("Your deposit is: ", self.deposit, "")