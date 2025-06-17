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
        print(f"Current Balance: ${self.account_balance:.2f}")
        
    
    


    
# Example usage:
if __name__ == "__main__":
    my_account = BankAccount(100)
    my_account.display_balance()


        