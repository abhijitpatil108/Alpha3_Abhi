class Parent:
    def __init__(self, value):
        self.value = value

    def google(self):
        print(f"Executing Parent google {self.value}")
        print("spam")

    def apple(self):
        print("Executing parent apple")
        self.google()


'''case 1'''
#Child class having an extra seperate method
class Child1(Parent):
    def demo(self):
        print("executing demo")

'''case 2'''
#Child overriding parent method
class Child2(Parent):
    def hello_World(self):
        print("hello World")

    def google(self):
        # self.value = 21
        print(f"Executing Child2 google {self.value+3}")
        super().google()

# c = Child2(21)
# c.google()



'''case 3'''
#Child adding extra functionality and re-using the original functionality of the parent class
class Child3(Parent):
    def spam(self):
        print("Executing Child3 Spam")

    def google(self):
        # self.value = 21
        print(f"Executing Child3 google {self.value+3}")
        super().google()

# c = Child3(21)
# c.google()

# print(Child3.__mro__)

'''case 4'''
#Child having its own constructor and also inheriting superclass constructor
class Child4(Parent):
    def __init__(self, value, name):
        self.name = name
        super().__init__(value)
    def hello(self):
        print(f"Executing Child4 hello {self.value}")
        print(f"Executing Child4 hello {self.name}")


# c = Child4(10, "Abhi")
# c.hello()


class Facebook:
    def spam(self):
        print("Executing Facebook Spam")

    def google(self):
        print(f"Executing Facebook google {self.value}")


'''case 5'''
#Multiple Inheritance (with only one supercalss having constructor)

# class Child5(Parent, Facebook):
class Child5(Facebook, Parent):
    pass

# c = Child5(24)
# c.spam()
# c.google()

'''case 6'''
#multiple Inheritance

#case a
class Parent1:
    def demo(self):
        print("class Parent1 demo")

class Demo(Parent1):
    def demo(self):
        print("class Demo demo")
        super().demo()

class Spam(Parent1):
    def demo(self):
        print("class Spam demo")
        super().demo()

class Child1(Spam, Demo):
    pass

# c = Child1()
# c.demo()

# case b
class Parent1:
    def demo(self):
        print("class Parent1 demo")

class Parent2:
    def demo(self):
        print("class Parent2 demo")

class Demo(Parent1):
    def demo(self):
        print("class Demo demo")
        super().demo()

class Spam(Parent2):
    def demo(self):
        print("class Spam demo")
        super().demo()

class Child1(Spam, Demo):
    pass

class Child2(Demo, Spam):
    pass

# c = Child1()
# c.demo()
#
# c1 = Child2()
# c1.demo()

# case c
class Parent1:
    def demo(self):
        print("class Parent1 demo")

class Parent2(Parent1):
    def demo(self):
        print("class Parent2 demo")
        super().demo()

class Demo(Parent2):
    def demo(self):
        print("class Demo demo")
        super().demo()

class Spam(Parent2):
    def demo(self):
        print("class Spam demo")
        super().demo()

class Child1(Spam, Demo):
    pass

class Child2(Demo, Spam):
    pass

# c1 = Child1()
# c1.demo()
#
# c2 = Child2()
# c2.demo()


'''Banking example'''

class BankAccount1:
    interest_rate = 0.04

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount should be greater than 0")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            raise ValueError("insufficient Funds")

    def roi(self):
        interest_amount = BankAccount1.interest_rate * self.balance
        self.balance += interest_amount


class SalaryAccount(BankAccount1):
    def __init__(self, name):
        self.is_first_month_salary = True
        self.max_draft_amount = 10000
        self.draft_amount_taken = 0.0
        super().__init__(name, 0.0)

    def deposit(self, amount):
        if self.is_first_month_salary:
            self.is_first_month_salary = False
            super().deposit(amount + 1000)
        else:
            super().deposit(amount)

    def overdraft(self, amount):
        if amount <= self.max_draft_amount:
            super().deposit(amount)  # handover
            self.max_draft_amount -= amount
        else:
            raise ValueError(f"Max available draft amount is {self.max_draft_amount}")

class SeniorCitizenAccount(BankAccount1):
    interest_rate = 0.06
    def withdraw(self, amount):
        if amount > 20000:
            raise ValueError("cannot withdraw more than 20k")
        super().withdraw(amount)


class SukanyaSamrudhhiAccount(BankAccount1):
    pass  #add


class PenaltyAccount:
    penalty_amount = 0
    def withdraw(self, amount):
        self.balance -= self.__class__.penalty_amount
        super().withdraw(amount)


class PensionAccount(PenaltyAccount, BankAccount1):
    penalty_amount = 200

c = PensionAccount("shyam", 50000)
c.withdraw(21800)
print(c.balance)



class MaxTransactionLimit(PenaltyAccount, BankAccount1):
    penalty_amount = 1000

