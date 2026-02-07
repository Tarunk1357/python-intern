class BankAccount:
    def __init__(self, account_holder):
        self.account_holder=account_holder
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount


    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.display_balance()
        else:
            print("You have insufficient amount in your Account.")


    def display_balance(self):
        print("The balance is",self.balance)




class SavingsAccount(BankAccount):
    def __init__(self,interest_rate,name):
        temp_interest=interest_rate/100
        self.interest_rate=temp_interest
        super().__init__(name)
    def add_interest(self):
        self.balance*=(1+self.interest_rate)
        super().display_balance()




class CurrentAccount(BankAccount):
    def __init__(self,overdraft_limit, name):
        self.overdraft_limit=overdraft_limit
        super().__init__(name)
    def withdraw_with_overdraft(self,amount):
        if amount<self.balance+self.overdraft_limit:  
            self.balance-=amount
            super().display_balance()
        else:
            print("Overdraft limit is exceeded")


SA=SavingsAccount(10,"Raja")
CA=CurrentAccount(100,"Raja")




CA.deposit(500)
CA.withdraw_with_overdraft(590)