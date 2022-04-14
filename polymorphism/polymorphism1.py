from functools import singledispatch, singledispatchmethod
#
# # from multipledispatch import dispatch
# '''using single dispatch we can achieve polymorphism at some extent'''
# '''it will only consider the datatype of first arguments'''

# @singledispatch
# def add(a, b):
#     print("Base function add")
#
# @add.register(int)
# # @singledispatch(int)
# def _(a, b):
#     print("calling int")
#     return a+b
#
# @add.register(float)
# # @singledispatch(float)
# def _(a, b):
#     print("calling float")
#     return a+b
#
# @add.register(list)
# # @singledispatch(list)
# def _(a, b):
#     print("calling list")
#     return sum(a)+b
#
# print(add(1.0, 1))

# class Arithmetic:
#     # def __init__(self, a, b):
#     #     self.a = a
#     #     self.b = b
#     @singledispatchmethod
#     def add(self, a, b):
#         print("calling base function")
#         return a + b
#     @add.register(int)
#     def _(self, a, b):
#         print("calling int")
#         return a + b
#     @add.register(float)
#     def _(self, a, b):
#         print("calling float")
#         return a + b
#     @add.register(list)
#     def _(self, a, b):
#         print("calling list")
#         return sum(a) + b
#
# a = Arithmetic()
# print(a.add(2, 2))

'''we can go with multipledispatch (check its example)'''

'''Run-time polymorphism  employee and their salary example'''

# class Employee:
#     def __init__(self, _id, name):
#         self._id = _id
#         self.name = name
#
#     def calculate_pay(self):
#         return "Salary cannot be disclosed"
#
# class WeeklyEmployee(Employee):
#     def __init__(self, _id, name, weekly_salary, weeks_worked):
#         self.weekly_salary = weekly_salary
#         self.weeks_worked = weeks_worked
#         super().__init__(_id, name)
#
#     def calculate_pay(self):
#         employee_salary = self.weekly_salary * self.weeks_worked
#         return employee_salary
#
# class HourlyEmployee(Employee):
#     def __init__(self, _id, name, hourly_salary, hours_worked):
#         self.hourly_salary = hourly_salary
#         self.hours_worked = hours_worked
#         super().__init__(_id, name)
#
#     def calculate_pay(self):
#         employee_salary = self.hourly_salary * self.hours_worked
#         return employee_salary
#
# class CommissionedEmployee(WeeklyEmployee):
#     def __init__(self, _id, name, weekly_salary, weeks_worked, commission_pay):
#         self.commission_pay = commission_pay
#         super().__init__(_id, name, weekly_salary, weeks_worked)
#
#     def calculate_pay(self):
#         employee_salary =  super().calculate_pay() + self.commission_pay
#         return employee_salary
#
#
# e = Employee(21, "emp")
# e1 = WeeklyEmployee(22, "emp1", 1000, 4)
# e2 = HourlyEmployee(23, "emp2", 25, 40)
# e3 = CommissionedEmployee(23, "emp3", 1000, 4, 250)
#
# # print(e3.calculate_pay())
#
# def emp_sal(e_list):
#     for employee in e_list:
#         yield f"Salary of {employee.name} is {employee.calculate_pay()}"
#         # return f"Salary of {employee.name} is {employee.calculate_pay()}"
# print(list(emp_sal([e1,e2,e3])))
# # print(emp_sal([e1,e2,e3]))
