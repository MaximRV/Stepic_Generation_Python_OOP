class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
        else:
            raise ValueError("На счете недостаточно средств")

    def transfer(self, account, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
            account.deposit(amount)
        else:
            raise ValueError("На счете недостаточно средств")

account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)