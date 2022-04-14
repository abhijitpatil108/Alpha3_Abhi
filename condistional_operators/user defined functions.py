'''user defined functions'''

'''basic example'''


# def add(a, b):
#     c = a + b
#     return c
#
#
# d = add(4, 5)
# print(d)

'''returning multiple values'''

# def ope(a, b):
#     c = a + b
#     d = a * b
#     return c, d
#
#
# d = ope(4, 5)
# print(d)
'''whenever the return function is returning multiple answers, it will return in tuple'''

'''key arguments vs positional arguments'''

'''positional arguments'''
# def greet(name, age):
#     print(f"{name} is {age} years old")
#
# greet("Ram", 25)
# greet(25, "Ram")

'''key arguments'''
# def greet(name, age):
#     print(f"{name} is {age} years old")
#
# greet(name="Ram", age=25)
# greet(age=25, name="Ram")

'''combination of key arguments vs positional arguments'''

# def comb(a, b, /, *, c, d):
#     print(a, b, c, d)
# comb(1, 2, 3, 4)
# comb(a=1, b=2, c=3, d=4)
# comb(1, 2, c=3, d=4)
# comb(a=1, b=2, 3, 4)

'''Only keywords arguments'''

# def comb(a, b, c, d,):
#     print(a, b, c, d)
# comb(1, 2, 3, 4)
# comb(a=1, b=2, c=3, d=4)
# comb(1, 2, c=3, d=4)
# comb(a=1, b=2, 3, 4)

'''write a function to add two numbers and returns the result
use positional as well as keyword arguments
Use positional only arguments
use keywords only arguments'''

'''use positional as well as keyword arguments'''


# def add1(a, *, b):
#     c = a + b
#     return c
#
#
# d = add1(4, b=5)
# print(d)
'''Use positional only arguments'''


# def add1(num1, num2, /):
#     a = num1
#     b = num2
#     c = a + b
#     return c
#
#
# d = add1(4, 5)
# print(d)

'''use keywords only arguments'''

#
# def add1(*, a, b):
#     c = a + b
#     return c
#
#
# d = add1(a=5, b=4)
# print(d)

'''Q WAF which returns list of even numbers within the range of 1-50'''


# def even(start, end):
#     # lis = []
#     # for num in range(start, end+1):
#     #     if num % 2 == 0:
#     #         lis.append(num)
#     lis = [num for num in range(start, end+1) if num % 2 == 0]
#     return lis
#
# print(even(1, 50))

# def even(start, end):
#     lis = []
#     for num in range(start, end):
#         if num % 2 == 0:
#             lis.append(num)
#     return lis
#
#
# lis1 = even(1, 51)
# print(lis1)

###########################3
'''Using Default Parameters'''

'''Here as start is a keyword argument, hence it must be written after positional argument'''
#
# def even(end, start=1):
#     lis = []
#     for num in range(start, end):
#         if num % 2 == 0:
#             lis.append(num)
#     return lis
#
#
# lis1 = even(51)
# print(lis1)

'''re-initialization of default arguments inside function not allowed'''
# x = 10
#
#
# def add_(a, b =x):
#     print(a + b)
#
#
# x = 30
# add_(10)


''' Q WAF that returns all the prime numbers in user defined range
if the user doesn't provide start index, take it as 2'''

# def prime_(end, start=2):
#     lis = []
#     for num in range(start, end+1):
#         for n in range(start, num):
#             if num % n == 0:
#                 break
#         else:
#             lis.append(num)
#     return lis


# print(prime_(50))

''' Q WAF to print fibonacci series in the user defined range'''


# def fibo(n, a=0, b=1):
#     lis = [a, b]
#     while len(lis) < n:
#         c = a+b
#         a = b
#         b = c
#         lis.append(c)
#     return lis
#
# s = fibo(10)
# print(s)

# def fibo(n, first=0, second=1):
#     lis = [first, second]
#     while len(lis) < n:
#         next = first + second
#         first = second
#         second = next
#         lis.append(next)
#     return lis
#
# s = fibo(10)
# print(s)



# def fibo(n, start=0):
#     i = 0
#     n1 = 0
#     n2 = 1
#     print(n1, end=' ')
#     print(n2, end=' ')
#     while i < n-2:
#         nn = n1 + n2
#         print(nn, end =' ')
#         n1 = n2
#         n2 = nn
#         i += 1
#
# print(fibo(10))


'''WAF that returns fibonacci series upto the number specified'''

# def fibo(last, first=0, second=1):
#     lis = [first, second]
#     while lis[-1] < last:
#         next = first + second
#         first = second
#         second = next
#         lis.append(next)
#     return lis[:]
#
# s = fibo(89)
# print(s)

'''WAF that returns nth fibonacci number'''

# def fibo(n, start=0, end=1):
#     lis = [start, end]
#     while len(lis) < n:
#         next = start + end
#         start = end
#         end = next
#         lis.append(next)
#     return lis[-1]
#
# s = fibo(8)
# print(s)

############## 3rd Feb 2022 ############
###########################################################
'''Variable positional argument'''
##########################################################

# def spam(*args):   # packing of data
#     print(args)
#
#
# spam(1, 2, 3)


'''WAF that takes integers and float datatype as input or arguments and returns its sum'''


# def sum_(*args):
#     print(args)
#     # print(sum(args))
#     total = 0
#     for i in args:
#         if isinstance(i, (int, float)):
#             total += i
#     print(total)
#
#
# sum_(1, 2, 3.5)


'''WAF that returns the number of positional arguments that are given to the function'''

# #
# def num_(*args):
# #     # print(args)
#       count = 0
#       for _ in args:
#           count += 1
#       print(f"number of positional arguments given are : {len(args)}")
#       print(f"number of positional arguments given are : {count}")
# #
# num_(1, 2, 3, 1.5, "hi", {"hi: 2"})

'''WAF that takes variable number of positional arguments and return all the integer values'''

# def int_v(*args):
#
#     for item in args:
#         # lis = []
#         if isinstance(item, int):
#             # lis.append(item)
#             print(item)
#
#         # return lis
#
# d = int_v(1, 2, 3.6, 4.5, "hi", 9)


'''WAF that takes multiple arguments and returns the string in reverse order'''

# def rev(*args):
#     for item in args:
#         if isinstance(item, str):
#             print(item[::-1])
#
# rev(1, 2, 3.6, 4.5, "hi", 9, "hello")
#
# def rev(*args):
#     lis = []
#     for item in args:
#         if isinstance(item, str):
#             lis.append(item[::-1])
#     return lis
#
# r = rev(1, 2, 3.6, 4.5, "hi", 9, "hello")
# print(r)

# print(list(input()))

#####################################################################
'''Variable keyword argument'''
#######################################################################

# def keyword_args(**kwargs):
#     return kwargs
#
# print(keyword_args(a=1, b=2, c=3, d=4))

'''WAF that returns the number of positional arguments and number of keyword arguments.'''
#
# def count(*args, **kwargs):
#     print(f"number of positional arguments given are : {len(args)}")
#     print(f"number of keyword arguments given are : {len(kwargs)}")
#     print(args)
#     print(kwargs)
#     print(*args)
#     print(*kwargs)
#
# count(1,2,3,4,5,6,a=2, b=3,c=4)


'''packing and unpacking in in-built function'''

# l = [1, 2, 3]
#
# print(*l) # 1 2 3
#
# d = dict(a=1, b=2, c=3)
# print(*d) # a b c
# print(**d)   # TypeError


''''unpacking in user defined function'''

# l = [1, 2, 3]
#
# def unpacking_args(a,b,c):
#     return a,b,c
#
# print(unpacking_args(*l))

'''WAF that checks if the given number of arguments is greater than 5 or not'''

# def check(*args, **kwargs):
#     if (len(args)+len(kwargs)) > 5:
#         print("The given arguments are greater than 5")
#     else:
#         print("The given arguments are not greater than 5")

# check(1,2,3, a=4, b=5, c=5)

'''WAF to print the number of arguments if the given number of arguments is greater than 5 or not'''

#
# def check(*args, **kwargs):
#     a = (len(args)+len(kwargs))
#     if a > 5:
#         return f"The total number of given arguments are {a}"
#
#     return "The given arguments are not greater than 5"
#
#
# print(check(1, 2, 3, a=4, b=5, c=5))

###################################
'''activity'''

'''1) WAF to count the number of positional and keyword arguments passed to it'''

# def count_(*args, **kwargs):
#     print(f"Number positional arguments are {len(args)} and keyword arguments are {len(kwargs)}")
#
# count_(1,2,3, a=2, b=3)

'''2) WAF to print a message "Hai Everyone" if the user input is not present and
if the user input is present print the user input'''

# def message(msg = "Hai Everyone"):
#     print(msg)
#
# message("hello")


'''3) a function takes variable number of positional arguments as input . How to check if the argument
that are passed are more than 5'''




'''WAF to check whether the number is prime or not'''

# def prime_(num):
#     for n in range(2, num):
#         if num > 2 and num % n == 0:
#             return "not prime"
#
#     return "prime"
# print(prime_(9))
#



# def prime_(a):
#     if a > 1:
#         for num in range(2,a):
#             if a % num == 0:
#                 print(f"{a} is not a prime number")
#                 break
#         else:
#             print(f"{a} is a prime number")
#     else:
#         print("enter number greater than 1")
#
#
# prime_(10)

# def prime_(a):
#     for num in range(2,a):
#         if a % num == 0:
#             return f"{a} is not a prime number"
#     return f"{a} is a prime number"
#
# print(prime_(3))


''''WAF to return last digit of a number'''

# def digit(a):
#     print(str(a)[-1])
#
# digit(1234)

'''WAF named tail that takes a sequence as input and a number n and 
returns the last n elements from the sequence'''

# def tail(*, a, n):
#     return(a[-n:])
#
# print(tail(a = "Hello", n=3))
# print(tail(a = [1,2,3,4,5], n=3))

'''WAF named is perfect square that accepts a number and returns true if its a perfect square 
and returns false if its not'''

# def perfect_square(a):
#     i = [0 if a % 2 == 0 else 1]
#     print(i)
#     for b in range(i[0], a, 2):
#         if a == b*b:
#             return "perfect square number"
#     return "not a perfect square number"
#
# print(perfect_square(5))



# def is_perfect_square(a):
#     sq = a ** 0.5   # this will not work for 27, because this will show 27 is prime
#     sq = int(a ** 0.5)   #to avoid above issue, convert the result in int type
#     if a == sq * sq:
#         return f"{a} is perfect square number"
#     return f"{a} is not perfect square number"
#
# print(is_perfect_square(27))


# def is_perfect_square(a):
# #    for num in range(a):   # the loop will do unnecessary iteration even after knowing the result
#     for num in range(a//2):  # to avoid it use floor division
#         if a == num*num:
#             return f"{a} is perfect square number"
#     return f"{a} is not perfect square number"
#
# print(is_perfect_square(49))

'''WAF to get the below output
func("TRACXN", 0) should print RCN
func("TRACXN", 1)  should print TAX'''
#
# def rc(a,b=0):
#         if b == 0:
#             return a[1:len(a):2]
#         elif b == 1:
#             return a[::2]
#         else:
#             return f"{b} is invalid"
#
# print(rc("TRACXN", 1))

'''WAF that checks if the given number is a fibonacci number'''
'''0112358 13 21 '''

# def fibo(n, first=0, second=1):
#     lis = [first, second]
#     while lis[-1] < n:
#         next = first+second
#         first = second
#         second = next
#         lis.append(next)
#         if lis[-1] == n:
#             return f"{n} is a fibonacci number"
#     return f"{n} is not a fibonacci number"
# print(fibo(24))


########## try again below ################
# def fibo_n(a):
#     n=0
#     # for num in range(a):
#     while n < a:
#         b = 0+1+n
#         if b != a:
#             n += b
#         else:
#             return f"{a} is a fibonacci number"
#     return f"{a} is not a fibonacci number"
#
# print(fibo_n(21))

        # if num-1 + (num-2) == a - num-1:
            # n += 1
    #         return f"{a} is a fibonacci number"
    #
    # return f"{a} is not a fibonacci number"

# print(fibo_n(5))


# def fibo_n(num):
#     a = 0
#     b = 1
#     while a <= num:
#         if a == num:
#             return f"{num} is a fibonacci number"
#         c = a+b
#         a=b
#         b=c
#     return f"{num} is not a fibonacci number"
#
# print(fibo_n(21))

'''WAF that takes variable number of inputs and returns length of all the iterables given'''
#
# def len_(*args):
#     for item in args:
#         if not isinstance(item, (int, float, complex)):
#             print(f"length of iterable {item} is {len(args)}")
#
# len_(3,"hi",(1,2,3))
#
# print(list(range(10,0,-1)))

'''WAF to print n numbers in fibonacci series'''
# def fibo_n(n):
#
#     lis = [0, 1]
#     while len(lis) <= n:
#         lis.append((lis[-1]+lis[-2]))
#     return lis[:-1]
#try_
# print(fibo_n(10))

'''WAF which can take "code" as input and gives below output'''
#o/p=> ccocodcode

# def try_(a):
#     i = len(a)
#     b = a
#     while i > 0:
#         b = a[0:(i-1)]+b
#         i = i-1
#     return b
#
# print(try_("code"))


# def code_(a):
#     sa = str()
#     for i in range(len(a)):
#         sa += a[0:i+1]
#         return sa
#
# print(code_("code"))

# def prime_(num):
#     for n in range(2, num):
#         if num % n == 0:
#             num += 1
#     else:
#         return (num)
# n = 2
# print(prime_(90))

# def prime_(num):
#     while num > 0:
#         for n in range(2, num):
#              if num % n == 0:
#                 break
#
#         else:
#             return(num)
#         num += 1
# print(prime_(90))

'''Convert all the for loop string programs in functions'''
# l =['he', 'ne']
# l1 = dict(l)
# print(l1)
# # def spam(**kwargs):
# #     print(kwargs)
# #     # print(*kwargs)
# #
# #
# # spam(l1)


'''1) '''

# sentence = "it is a very good book and reading book i a good habit"
# lis = sentence.split()
#
# def word(*args):
#     d = {}
#     for word in args:
#         if word not in d:
#             d[word] = 1
#         else:
#             d[word] += 1
#     print(d)
#
# word(*lis)




