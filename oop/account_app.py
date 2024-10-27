from account import User, Account
from oop.account import MinimumBalanceAccount

michal = User("Michal Go!")
maciej = User("Maciej Bu!")
michal_acount = Account(michal)
michal_min_balance_account = MinimumBalanceAccount(michal, min_balance=22000)
michal_acount.make_deposit(22400)
michal_min_balance_account.make_deposit(22400)
print(michal_acount.withdraw(2000).message)
print(michal_min_balance_account.withdraw(200).message)
print(User.id)
print(michal.id)


