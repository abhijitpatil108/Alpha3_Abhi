from collections import defaultdict

'''1)WAF print the output for given input depending on number of occurrences of the characters'''
# import time
from time import sleep, time
# input_ = "AABBBCCDAADDBBCDDDDD"
#o/p = "2A3B2C1D2A2D2B1C1D
#
# def count_(string):
#     im = string+" "
#     count = 1
#     res = ""
#     for i in range(len(im)-1):
#         if im[i] == im[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + im[i]
#             count = 1
#     return res
# print(count_(input_))

# # another method
# s = "AABBBCCDAADDBBCDDDDD"
# #o/p = "2A3B2C1D2A2D2B1C1D
# def count_(s):
#     count = 0
#     res = ""
#     i = 0
#     while i < len(s):
#         if s[i] == s[i+1:i+2]:
#             count += 1
#             i += 1
#         else:
#             count += 1
#             res += str(count) + s[i]
#             count = count-count
#             i += 1
#     return res
# print(count_(s))


# a = "hhi"
# print(a[3])
# print(a[4])
# print(a[4:5])

'''Decorator class examples'''

#log
#delay
#time
#reverse
#positive
#count

def log_(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        res = func(*args, **kwargs)
        return res
    return wrapper

def delay_(func):
    def wrapper(*args, **kwargs):
        sleep(2)
        res = func(*args, **kwargs)
        return res
    return wrapper

def time_(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        return f"time taken to execute {func.__name__} is {end-start}"
    return wrapper

def reverse_(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if not isinstance(res, str):
            return res
        return res[::-1]
    return wrapper

def positive_(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return abs(res)
    return wrapper

from collections import defaultdict
d = defaultdict(int)
def count_(func):
    # func.count = 0
    # d = defaultdict(int)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        # func.count += 1
        d[func.__name__] += 1
        # print(f"{func.__name__} called {func.count} times")
        # return func.count
        return res
    return wrapper

d = {}
def cache_(func):
    def wrapper(*args, **kwargs):
        key = (func.__name__, args)
        if key in d:
            print("getting from cache_dict")
            return f"{key} is {d[key]}"
        else:
            res = func(*args, **kwargs)
            d[key] = res
            return res
    return wrapper

# def times_(n):
#     def repeat_(func):
#         def wrapper(*args, **kwargs):
#             a = n
#             lis = []
#             while a > 0:
#                 res = func(*args, **kwargs)
#                 lis.append(res)
#                 a -= 1
#             return lis
#         return wrapper
#     return repeat_

def times_(n):
    def repeat_(func):
        def wrapper(*args, **kwargs):
            lis = []
            for _ in range(n):
                res = func(*args, **kwargs)
                lis.append(res)
            return lis
        return wrapper
    return repeat_

# def max_calls_(n):
#     def call_(func):
#         def wrapper(*args, **kwargs):
#             count = 0
#             while count < n:
#                 res = func(*args, **kwargs)
#                 count += 1
#                 print(res)
#             print("Function calling limit exceeded")
#         return wrapper
#     return call_

# def max_calls_(n):
#     def call_(func):
#         func.count = 0
#         def wrapper(*args, **kwargs):
#             func.count += 1
#             if func.count > n:
#                 raise ValueError(f"{func.__name__} calling limit exceeded")
#             else:
#                 res = func(*args, **kwargs)
#                 print(res)
#         return wrapper
#     return call_


# a = "he"#[1,2,3] #10
# def spam():
#     global a
#     a += "llo"
#
#     print(a)
#
# spam()
# print(a)

# log_ delay_ positive_ reverse_ time_ count_ cache_ times_ max_calls_
# call_ = max_calls_
# @call_(5)
# def add(a,b):
#     # sleep(1)
#     return a+b
# add(1,2)

# print(add(1,2))

# @call_
# def sub(a,b):
#     # sleep(1)
#     return a-b
# print(sub(1,2))
# print(sub(1,2))
#
# @call_
# def mul(a,b):
#     # sleep(1)
#     return a*b
# print(mul(-4,6))
#
# @call_
# def greet():
#     # sleep(2)
#     return "hello world"
# print(greet())
# print(greet())
#
# @call_
# def greeting(name):
#     # sleep(2.4)
#     return f"hello {name}"
# print(greeting("Abhi"))
# print(greeting("Abhi"))
#
# print(d)
# #


# d = {}
# def cache_(func):
#     def wrapper(*args, **kwargs):
#         if args in d:
#             print("getting from cache_dict")
#             return d[args]
#         else:
#             res = func(*args, **kwargs)
#             d[args] = res
#             return res
#     return wrapper
#
# @cache_
# def add(a, b):
#     sleep(1)
#     return a + b
#
# print(add(2,3))
# print(add(2,3))

'''encapsulation'''

# class String_:
#     def __init__(self, text):
#         self.text = text
#
#     def len(self):
#         return len(self.text)
#         # count = 0
#         # for item in self.text:
#         #     count += 1
#         # print(count)
#
#     def _clean_up(self):  # methods with _ are non-public and should be called inside class only
#         return self.text.strip()
#
#
#     def split_(self):
#         temp = self._clean_up()
#         return temp.split()
#
# a = String_(" hello Hi")
# print(a.len())
# print(a.split_())
# print(a._clean_up())
# from math import pi
# class Circle:
#     def __init__(self, rad):
#         self.rad = rad
#
#     @property
#     def rad(self):
#         return self._rad
#
#     @rad.setter
#     def rad(self, value):
#         if not isinstance(value, int):
#             raise TypeError
#         self._rad = value
#
#     def circumferential(self):
#         return (2 * pi * self._rad)
#
#
# a = Circle(5)
# print(a.rad)
# print(a.circumferential())

'''making class callable'''
#
# portfolio = [
# {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
#
# # class By:
# #     def __init__(self, key):
# #         self.key = key
# #
# #     def __call__(self, item):
# #         if self.key == 'name':
# #             return item['name']
# #         elif self.key == 'shares':
# #             return item['shares']
# #         else:
# #             return item['price']
# #
# # res1 = sorted(portfolio, key=By('name'))
# # res2 = sorted(portfolio, key=By('shares'))
# # res3 = sorted(portfolio, key=By('price'))
# # print(sorted(portfolio,key = lambda item : item["price"]))
# # print(res3)
# #
#
# # class Square_:
# #     def __init__(self, a):
# #         self.a = a
# #     def __call__(self):
# #         print(self.a*2)
# #
# # a = Square_(2)
# # a()
# # Square_(2)()
#
# class Log:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args, **kwargs):
#         print(f"calling {self.func.__name__} function")
#         return self.func(*args, **kwargs)
#
# @Log  # add = Log(add)
# def add(a, b):
#     return a+b
# print(add(2,2))

'''decorators to prefix 91 to numbers'''

# numbers = [1234567890, 911234567899, 991122334455, 9988776655]
#
# def validate_(num):
#     if len(num) == 10:
#         return "91-"+num
#     elif len(num) == 12 and num.startswith("91"):
#         return "91-"+num[2:]
#     else:
#         return num
#
# def num_(func):
#     def wrapper(*args, **kwargs):
#         prefixed_numbers = [validate_(str(number)) for number in args[0]]
#         return func(prefixed_numbers)
#     return wrapper
#
# @num_
# def dial_(nums):
#     for number in nums:
#         # print(number)
#         if number.startswith("91-"):
#             print(f"dialing {number}")
#         else:
#             print(f"{number} is invalid number")
# dial_(numbers)

'''validation of inputs with its datatypes'''

def validate_type(expecteds, actuals):
    for expected_type, actual_value in zip(expecteds, actuals):
        if not isinstance(actual_value, expected_type):
            raise TypeError(f"provided datatypes doesn't match with required ones")



def validate_(*expected_types): # (int, int)
    def _validate(fucn):
        def wrapper(*args, **kwargs):  #(2,2)
            validate_type(expected_types, args)
            return fucn(*args, **kwargs)
        return wrapper
    return _validate

@validate_(int, int)
def add(a, b):
    return a + b
print(add(2,2))

@validate_(int, float)
def sub(a, b):
    return a -b
print(sub(4, 1.6))

@validate_(str, int)
def multi(a, b):
    return a * b
print(multi("hi",2))
