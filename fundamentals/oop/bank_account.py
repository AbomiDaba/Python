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
        print(f"Balalnce:${round(self.balance, 2)}")
        return self

    def yield_int(self):
        if self.balance > 0:
            self.balance += round((self.balance*self.int_rate), 2)
        return self
    

acc1 = BankAccount()
acc2 = BankAccount()

acc1.deposit(8000).deposit(1737).deposit(4918).with_draw(880).yield_int().display_account_info()

acc1.deposit(8000).deposit(9000).with_draw(150).with_draw(1000).with_draw(100).with_draw(450).yield_int().display_account_info()





