from account import User, Account

michal = User("Michal Go!")
maciej = User("Maciej Bu!")
michal_acount = Account(michal)
michal_acount.make_deposit(22400)
michal_acount.withdraw(2000)
print(User.id)
print(michal.id)


