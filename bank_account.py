class BankAccount:
    def __init__(self, account_holder:str, initial_balance:float):
        self.holder = account_holder
        self.balance = initial_balance
    def transfer_funds(self, other_account, amount):
        if self.balance >=amount:
            self.balance -= amount
            other_account.balance += amount
            print("the transfer succeed")
        else:
            print("Error:we can not make the transfer")
    def __str__(self):
        return f"account status: holder:{self.holder} balance:{self.balance}"

