class BankAccount:
    bank_name = "First National DojO"

    def __init__(self, int_rate = 0.025, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self

    def with_draw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Account Balalnce: ${round(self.balance, 2)}")
        return self

    def yield_int(self):
        if self.balance > 0:
            self.balance += round((self.balance*self.int_rate), 2)
        return self

# user class

class User:
    
    bank_name = "First National Dojo"
    def __init__(self,name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.deposit(amount)
        return self
        

    def display_user_balance(self):
        print(f"User: {self.name},", end=" ")
        self.account.display_account_info()
        return self


    def transfer_money(self,user,amount):
        self.account.balance -= amount
        user.account.balance += amount
        return self


user1 = User("Bob","bob@gmail.com")
user2 = User("John","John@yahoo.com")
user3 = User("Jack","Jack@outlook.com")

user1.make_deposit(100).make_deposit(50).make_deposit(67).make_withdrawal(25).display_user_balance()


user2.make_deposit(3000).make_deposit(2493).make_withdrawal(1711).make_withdrawal(460).display_user_balance()

user3.make_deposit(18000.48).make_withdrawal(3808.39).make_withdrawal(5372.02).make_withdrawal(700).display_user_balance()

user1.transfer_money(user3,50).display_user_balance()

user3.display_user_balance()