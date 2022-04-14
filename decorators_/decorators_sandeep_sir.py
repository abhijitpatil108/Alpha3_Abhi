'''Sandeep sir'''
import time
from time import sleep, time


def delay(func):
    def wrapper(*args, **kwargs):
        sleep(1)
        return func(*args, **kwargs)
    return wrapper
#
def log(func):
    def wrapper(*args, **kwargs):
        print(f"You are calling {func.__name__} function")
        sleep(1)
        res = func(*args, **kwargs)
        print(res)
        return (f"{func.__name__} function got executed")
    return wrapper


def rev(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return res[::-1]
        return res
    return wrapper

def pos(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, (int,float, complex)):
            return abs(res)
        return res
    return wrapper

def _time(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"execution time of the {func.__name__} function is {end-start}")
        return res
    return wrapper


'''how to check which function is called how many times.'''

from collections import defaultdict

_func_count = defaultdict(int)  # to check the count of function w.r.t function name

def _count(func, d = {}):
    func
    def wrapper(*args, **kwargs):
        _func_count[func.__name__] += 1
        res = func(*args, **kwargs)
        return res
    return wrapper

def _count_f(func):
    func.count = 0
    def wrapper(*args, **kwargs):
        func.count += 1
        res = func(*args, **kwargs)
        print(f"{func.__name__} was invoked {func.count} times")
        return res
    return wrapper

def _max(func):
    func.count = 0
    def wrapper(*args, **kwargs):
        func.count += 1
        if func.count > 5:
            print(f"{func.__name__} calling limit exceeded")
        res = func(*args, **kwargs)
        return res
    return wrapper


def _repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(2):
            res = func(*args, **kwargs)
        return res
    return wrapper



#
# # @delay
# @log
# @rev
# deco_ = _repeat
# deco_= {'delay':'delay', 'log':'log', 'rev':'rev', '_time':'_time'

# # @deco_
# @cache
# def add(a,b):
#     print("adding")
#     return a+b
# print(add(1,2))
# # print(add(2,3)) #added more add function to check the count of it updating or not inside the created default dict
# # print(add(2,3))
# # print(add(2,3))
# # print(add(2,3))
# # print(add(2,3))
#
# # @delay
# # @log
# # @rev
# # @deco_
# def sub(a,b):
#     return a-b
# print(sub(1,2))
# # print(sub(1,2))
#
# # @delay
# # @log
# # @rev
# # @deco_
# def greet():
#     return "hello world"
# print(greet())
# # print(greet())
# # print(greet())
#
#
# # @delay
# # @log
# # @rev
# # @deco_
# def greeting(name):
#     return f"hello {name}"
# print(greeting("Abhi"))
#
# # @delay
# # @log
# # @rev
# # @deco_
# def mul(a,b):
#     return a*b
# print(mul(-4,6))
# print(mul(-4,6))
# print(mul(-4,6))
# print(mul(-4,6))

# print(_fun_count)


#cache decorator
# def cache(func):
#     func._cache = {}    # aatching an empty dict
#     def wrapper(*args, **kwargs):
#         if args in func._cache:
#             return func._cache[args]
#         res = func(*args, **kwargs)
#         func._cache[args] = res
#         return res
#     return wrapper()
#
#
#
# @cache
# def add(a,b):
#     print("adding")
#     return a+b
# print(add(1,2))
# print(add(1,2))
#
# def sub(a,b):
#     return a-b
# print(sub(1,2))
#
#
# def greet():
#     return "hello world"
# print(greet())
#
#
# def greeting(name):
#     return f"hello {name}"
# print(greeting("Abhi"))
#
#
# def mul(a,b):
#     return a*b
# print(mul(-4,6))

'''IMP decorator program, asked in previous interviews '''
###############################################################################
# numbers = [1234512345, 1234554321, 919876598765, 111234512345]

# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) == 10:
#         str_number = "+91-" + str_number
#         return str_number
#     elif len(str_number) == 12 and str_number.startswith("91"):
#         str_number = "+" + str_number[:2] + "-" + str_number[2:]
#         return str_number
#     else:
#         return str_number
#
# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         temp = args[0]
#         processed_numbers = [ add_prefix(number) for number in temp]
#         return func(processed_numbers)
#     return wrapper
#
# @prefix_country_code
# def print_numbers(phone_numbers):
#     for item in phone_numbers:
#         print(item)
#
# print_numbers(numbers)

##################################################################################
'''parameterized decorators'''
##################################################################################

# def _delay(seconds=2):
#     def delay_(func):
#         def wrapper(*args, **kwargs):
#             sleep(seconds)
#             return func(*args, **kwargs)
#         return wrapper
#     return delay_
#
# @_delay()               # () must be included if the decorator is parameterized
# def add(a, b):
#     return a + b
# print(add(1, 2))
#
# @_delay(1)
# def sub(a, b):
#     return a - b
# print(sub(1, 2))
#
#
# @_delay(1)
# def greet():
#     return "hello world"
# print(greet())
#
#
# @_delay()
# def greeting(name):
#     return f"hello {name}"
# print(greeting("Abhi"))
#
#
# @_delay(5)
# def mul(a, b):
#     return a * b
# print(mul(-4, 6))


'''Validation of input arguments types'''

# def validates_types(expected_types, actual_values):
#     for expected_type, actual_value in zip(expected_types, actual_values):
#         if not isinstance(actual_value, expected_type):
#             raise TypeError()
#
#
# def validate_(*expected_types):
#     def _validate(func):
#         def wrapper(*args, **kwargs):
#             validates_types(expected_types, args)
#             return func(*args, **kwargs)
#         return wrapper
#     return _validate

def validate_type(expected_types, actual_types):
    for expected_type, actual_type in zip(expected_types, actual_types):
        if not isinstance(actual_type, expected_type):
            raise TypeError


def validate_(*expected_types):
    def validate(func):
        def wrapper(*args, **kwargs):
            validate_type(expected_types, args)
            res = func(*args, **kwargs)
            return res
        return wrapper
    return validate

@validate_(int, int)               # () must be included if the decorator is parameterized
def add(a, b):
    return a + b
print(add(1, 2))

@validate_(int, float)
def sub(a, b):
    return a - b
print(sub(2, 1.1))


@validate_()
def greet():
    return "hello world"
print(greet())


@validate_(str)
def greeting(name):
    return f"hello {name}"
print(greeting("Abhi"))


@validate_(int, int)
def mul(a, b):
    return a * b
print(mul(4, 6))


# def delay(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(2)
#         return func(*args, **kwargs)
#     return wrapper
#
# def add(a,b):
#     return a+b
#
# add = delay(add)
# print(add(1,2))

###############################################################################################
'''calling list of decorators '''
###############################################################################################

# import time
# from time import sleep, time
#
#
# def delay(func):
#     def wrapper(*args, **kwargs):
#         sleep(1)
#         return func(*args, **kwargs)
#     return wrapper
# #
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"You are calling {func.__name__} function")
#         sleep(1)
#         res = func(*args, **kwargs)
#         print(res)
#         return (f"{func.__name__} function got executed")
#     return wrapper
#
#
# def rev(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, str):
#             return res[::-1]
#         return res
#     return wrapper
#
# def pos(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, (int,float, complex)):
#             return abs(res)
#         return res
#     return wrapper
#
# def _time(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         res = func(*args, **kwargs)
#         end = time()
#         print(f"execution time of the {func.__name__} function is {end-start}")
#         return res
#     return wrapper



# deco_ = [delay,log, rev, pos, _time]
#
# for item in deco_:
#     @item
#     def add(a, b):
#         # sleep(3)
#         return a + b
#     print(add(1, 2))
#
#     @item
#     def sub(a, b):
#         # sleep(4)
#         return a - b
#     print(sub(1, 2))
#
#
#     @item
#     def greet():
#         # sleep(1)
#         return "hello world"
#     print(greet())
#
#
#     @item
#     def greeting(name):
#         # sleep(2)
#         return f"hello {name}"
#     print(greeting("Abhi"))
#
#
#     @item
#     def mul(a, b):
#         # sleep(5)
#         return a * b
#     print(mul(-4, 6))

############################################################################################


