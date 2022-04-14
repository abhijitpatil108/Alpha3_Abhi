class BankAccount:
    interest_rate = 0.04  # class variable (will be common for all the instances)
    # all the customer will share same interest_rate
    count = 0
    def __init__(self, name, balance=0):
        # instance variable
        self.name = name
        self.balance = balance
        self.transaction = []
        self.transaction.append(f"******* Initial Amount deposited {balance} *******")
        BankAccount.count += 1

    def deposit(self, amount):
        self.balance = self.balance+amount
        self.transaction.append(f"Amount Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Funds")
        self.balance = self.balance-amount
        self.transaction.append(f"Amount Withdrawn {amount}")
        # return f"Please collect the cash {amount}"

    def transfer(self, to_account, amount):
        if self.balance < amount:
            raise ValueError("Insufficient Funds")
        to_account.deposit(amount)
        self.balance -= amount
        self.transaction.append(f"Amount transferred {amount} from {self.name} to {to_account.name}")

    def statement(self):
        for transaction in self.transaction:
            print(transaction)
        print(f"Available Balance is {self.balance}")
        print("*" * 50)

    def roi(self):
        interest_amount = self.balance * BankAccount.interest_rate
        self.balance = self.balance + interest_amount
        self.transaction.append(f"Interest Amount credited {interest_amount}")


c1 = BankAccount("Sandeep", 1000)
c2 = BankAccount("Steve", 2000)
c3 = BankAccount("Bill")


c1.deposit(5000)
c1.transfer(c2, 3000)
print(c1.__dict__)
print(c2.__dict__)
# c3.withdraw(1000)

c1.roi()
c2.roi()
c3.roi()

c1.statement()
c2.statement()
c3.statement()

print(BankAccount.count)
