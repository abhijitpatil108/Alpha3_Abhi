'''accessing global variable'''

# a = 10
#
# def spam():
#     print(a)
#
# spam()

'''modifying the global variable'''

# a = 10
#
# def spam():
#     global a
#     a = a+5
#     print(a)
#
#
# spam()

'''accessing local variable outside a function'''
#
# def spam():
#     global a
#     a = 10
#     print(a)
#
#
# spam()
# print(a)

'''modifying local variable inside nested function'''

# def f1():
#     x = 10
#
#     def f2():
#
#         def f3():
#             nonlocal x
#             x += 2
#             print(x)
#         f3()
#     f2()
#     print(x)
# f1()

