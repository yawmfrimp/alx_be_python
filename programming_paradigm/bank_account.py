class BankAccount:
    def __init__(self,account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self,amount):
        return amount + self.account_balance


    def withdraw(self,amount):
        if self.account_balance >= amount:
            return self.account_balance >= amount
        else:
            return self.account_balance >= amount


    def display_balance(self):
        print("Current Balance: $",self.account_balance)


        