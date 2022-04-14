'''Exception handling'''
# names = ['john', 'eve', 'bob', 'emma', 'ana']
# # d = {}
# # for name in names:
# #     if name[0] in d:
# #         d[name[0]] += [name]
# #     else:
# #         d[name[0]] = [name]
# # print(d)
# # '''using exception handling'''
# d = {}
# for name in names:
#     try:
#         d[name[0]] += [name]
#     except:
#         d[name[0]] = [name]
# print(d)
'''Generic exception and specific exception'''
#generic exception

# a = 10
# b = 0
#
# try:
#     print(a/b)  # zerodivision error
#     print(l.append(10))
# except:
#     print("in Except block")
#
# print("hello")

# Specific Exception

# a = 10
# b = 0
#
# try:
#     print(a/b)  # zerodivision error
#     print(l.append(10))  #NameError
# except ZeroDivisionError:
#     print("ZeroDivisionError handled")
# except NameError:
#     print("Name Error handled ")
#
# print("hello")

# a = 10
# b = "a"
#
# try:
#     if b > a:
#         print(f"b-a :{b-a}")
#     else:
#         print(f"a-b :{a-b}")
#
# except BaseException as error:
#     print("in Exception block")
#     print(error)
#
# else:
#     print("case was ok")
# finally:
#     print("finally executed")





# you can have single except block for multiple exception

# a = 10
# b = 0
#
# try:
#     print(a/b)  # zerodivision error
#     print(l.append(10))
# except (ZeroDivisionError, NameError) as error_msg:
#     print("in except block")
#     print(error_msg)
# print("hello")

'''global local namespace example'''
# #
# def outer_function():
#     global a
#     a = 20
#
#     def inner_function():
#         global a
#         a = 30
#         print('inside inner a =', a)
#
#     inner_function()
#     print('inside outer a =', a)
#
#
# a = 10
# outer_function()
# print('a =', a)

from file_handling.jason_pickle import jason_file_handling

from abc import ABC