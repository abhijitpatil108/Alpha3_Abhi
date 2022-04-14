from collections import defaultdict

''' class '''















#
# dd = defaultdict(int)
#
# def count_(func):
#     func.count = 0
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         func.count += 1
#         dd[func.__name__] = func.count
#         return res
#     return wrapper
#
# use_ = count_
# @use_
# def add(a, b):
#     return a+b
# print(add(1, 2))
# print(add(1, 2))
# print(add(1, 2))
#
# @use_
# def sub(a, b):
#     return a-b
# print(sub(4, 2))
#
# @use_
# def mult(a, b):
#     return a*b
# print(mult(2, 2))
# print(mult(2, 2))
#
# print(dict(dd))
