'''We can create a class decorator by adding __call__ method inside which will act as a wrapper function'''
'''function decorator'''
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @log
# def add(a, b):
#     return a+b
# print(add(1, 2))
#
# @log
# def sub(a, b):
#     return a-b
# print(sub(4, 2))


'''class decorator'''

# class Log:
#     def __init__(self, func):
#         self.func = func
#
# # very similar to the wrapper function
#     def __call__(self, *args, **kwargs):
#         print(f"__call__ calling {self.func.__name__}")
#         return self.func(*args, **kwargs)
#
#
# @Log
# def add(a, b):
#     return a+b
#
#
# @Log
# def sub(a, b):
#     return a-b
#
# print(add(1, 2))
# print(sub(4, 2))

'''another examples'''

# class Record:
#     def __init__(self,func):
#         self.func = func
#         self._count = 0
#
#     def __call__(self, *args, **kwargs):
#         self._count += 1
#         return self.func(*args, **kwargs)
#
# @Record
# def add(a, b):
#     return a+b
# print(add(1,2))
# print(add(1,2))
#
# @Record
# def sub(a, b):
#     return a-b
# print(add(1,2))



#####################################################################################
'''custom sorting using callable example'''
#####################################################################################
# items = ['at','bu', 'cz', 'dw']
#
# #key arguments takes a cllable argument
# # lambda expressions are callable
# # functions are callable
# # any class which defined with __call__method is callable
#
# #callable function
# def get_last_char(item):
#     return item[-1]
#
# #callable class
# class GetLastChar:
#     def __call__(self, item):
#         return item[-1]
#
# #callable lambda expression
# lambda_get_last_char = lambda item: item[-1]
#
# g = GetLastChar()
# # by_last = sorted(items, key = g)
# # by_last = sorted(items, key = lambda_get_last_char)
# by_last = sorted(items, key = get_last_char)
# print(by_last)

'''attaching an instance method to the class using class decorator'''

# def attach_init(cls):
#     def wrapper(self, a, b):
#         print("wrapper as init")
#         self.a = a
#         self.b = b
#     cls.__init__ = wrapper
#     return cls
#
#
# @attach_init   #Arithmatic = attach_init(Arithmetic)
# class Arithmetic:
#     # def __init__(self, a, b):
#     #     self.a = a
#     #     self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a -self.b
#
#     def mul(self):
#         return self.a * self.b
#
# a = Arithmetic(1, 2)
# print(a.add())

'''decorating whole class'''

# def use_(func):
#     def wrapper(*args, **kwargs):
#         print("calling only callable")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def sort_(cls):
#     for key, value in cls.__dict__.items():
#         if callable(value):
#             setattr(cls, key, use_(value))
#     return cls
#
#
# @sort_
# class Arithmetic:
#     value = 10
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a -self.b
#
#     def mul(self):
#         return self.a * self.b
#
# a = Arithmetic(4,2)
# print(a.add())

''' assessment '''
'''1)'''

'''2)Create a class which delays the functionality of the other class'''

from time import sleep

class Delay:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    def _delay(func):
        def wrapper(*args, **kwargs):
            print("delaying the function")
            sleep(2)
            return func(*args, **kwargs)
        return wrapper

class Arithmetic(Delay):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def _delay(func):
    #     def wrapper(*args, **kwargs):
    #         print("delaying the function")
    #         sleep(2)
    #         return func(*args, **kwargs)
    #     return wrapper

    @_delay     # add = _delay(add)
    def add(self):
        return self.a + self.b

    @_delay
    def sub(self):
        return self.a - self.b

a = Arithmetic(4,2)
print(a.add())


# class First_:
#     def greet(self):
#         print("hello")
#
# class Second_(First_):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#
#     def sub(self):
#         return self.a - self.b
#
# a = Second_(4,2)
# a.greet()