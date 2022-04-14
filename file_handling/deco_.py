
'''	ü Function should be nested function'''
'''ü Outer function must accept only one parameter'''
'''ü The parameter of outer function must be called inside nested function'''
'''ü Outer function must return inners function's address.'''
import time


# def spam(func):
#     def wrapper(*args, **kwargs):
#         print("The no of arguments :", len(args)+len(kwargs))
#         func(*args, **kwargs)
#     return wrapper
#
# @spam               # add = spam(add)
# def add(a,b):
#     print(a+b)
#
# add(1,2)


'''WAD to log a message before calling a main function'''

# def log(func):
#     def wrapper(*args, **kwargs):
#         print("In decorator function")
#         func(*args, **kwargs)
#     return wrapper
#
# @log               # add = spam(add)
# def display():
#     print("in display")
#
# display()

'''WAD to input some delay before executing any function'''

# import time
#
# def delay(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(2)                         # in python it will Second compared to java's Milisecond
#         return func(*args, **kwargs)
#     return wrapper
#
# @delay        # display = delay(display)
# def display():
#     return "in display"
#
# print(display())

'''for note'''
# def spam(func):
#     def wrapper():
#         print("in wrapper")
#         func()
#     return wrapper
#
# @spam               # add = wrapper
# def add():
#     print("in function")
#
# add()


'''WAD which takes a string and reverse it'''

# def rev(func):
#     def wrapper(*args, **kwargs):
#
#         return func(*args, **kwargs)
#     return wrapper
#
# @rev
# def st(a):
#     return a
#
# print(st("hello"))

'''WAD to execute a function for 3 times'''

# def deco(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#     return wrapper
#
# @deco
# def ab():
#     print("hello")
#
# ab()

'''WAD which executes a function for n times'''

# def outer(n):
#     def repeat_(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#
#     return repeat_
#
# @outer(3)
# def add(a, b):
#     print(a+b)
#
# add(1, 2)
#
# @outer(2)
# def sub(a, b):
#     print(a-b)
#
# sub(5, 1)

'''WAD which inputs a delay of n seconds'''

# def outer_(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#         return wrapper
#     return delay
#
# @outer_(3)
# def add(a, b):
#     print(a+b)
#
# add(1, 2)
#
# @outer_(2)
# def sub(a, b):
#     print(a-b)
#
# sub(5, 1)

'''WAD that calculates time of execution of a function'''

# def outer_(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             time.sleep(n)
#             func(*args, **kwargs)
#             end = time.time()
#             print(f"time taken for execution : {end-start}")
#         return wrapper
#     return delay
#
# @outer_(2)
# def add(a, b):
#     print(a+b)
#
# add(4, 5)

'''WADF to count the number of arguments passed to a function'''

# def arg(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
# @arg      # a = arg(a)
# def a(*args, **kwargs):
#     n = len(args)+len(kwargs)
#     print(f"total number of arguments passed are : {n}")
#
# a(1, 2, a=3, b=4)

'''WADF to return only positive values after subtraction'''

# def pos_(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
# @pos_
# def sub_(a, b):
#     c = a-b
#     print(abs(c))
# sub_(4,5)

'''WADF to print "hello world" message if the user has not given input'''

# n = "hello world"
# def inn_(*args, **kwargs):
#         def spam(func):
#             def wrapper(*args, **kwargs):
#                 if len(args) + len(kwargs) != 0:
#                     return func(*args, **kwargs)
#                 else:
#                     print(n)
#             return wrapper
#         return spam
#
#
# @inn_(n)
# def ui_(*args, **kwargs):
#     print(args, kwargs)
#
# ui_()

'''WADF to return the length of the given iterables'''

# def l(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
# @l
# def len_(a):
#     print(len(a))
#
# l = [1,2,3,4,5]
# len_(l)
