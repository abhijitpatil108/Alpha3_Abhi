
""" reverse a string """
# def rev(s, a = ""):
#     if len(s) == 0:
#         return a
#     return rev(s.replace(s[-1],"",1),(a+s[-1]))
#
# print(rev("hello"))

# def rev(s, i=0, a=""):
#     if i < len(s):
#         a = s[i]+a
#         return rev(s,i+1,a)
#     return a
#
# print(rev("hello"))


""" count number of digits in a number """

# def digi(n, count = 0):
#     s = str(n)
#     if len(s) == 0:
#         return count
#     count += 1
#     return digi(s.replace(s[-1],"",1), count)
#
# print(digi(987654312))

# def digi(n, count = 0):
#     n = n // 10
#     count += 1
#     if n == 0:
#         return count
#     return digi(n, count)
#
# print(digi(987654312))




'''fibo series till nth number'''

# def fibo(n, lis = [0,1]):
#     lis.append(lis[-1]+lis[-2])
#     if lis[-1] == n:
#         return lis
#     return fibo(n,lis)
#
# print(fibo(5))

""" factorial of a number """


# def facto(n):
#     if n == 1:
#         return n
#     return n*facto(n-1)
#
# print(facto(5))



""" sum of first n numbers """

# def sum_(n):
#     if n == 0:
#         return n
#     return n+sum_(n-1)
#
# print(sum_(4))


""" add digits of the number """

# def add(n):
#     r = n % 10
#     q = n // 10
#     if q == 0:
#         return r
#     return r+add(q)
#
# print(add(121))

# def add(n, sum =0):
#     if n != 0:
#         r = n % 10
#         q = n // 10
#         sum += r
#         return add(q, sum)
#     return sum
#
# print(add(124))



'''WARF to print 10 to 1'''

# def p10to1(n):
#     if n == 0:
#         return
#     print(n)
#     p10to1(n-1)
#
# p10to1(10)


'''WARF to print 1 to 10'''

# def p1to10(n):
#     if n == 11:
#         return
#     print(n)
#     p1to10(n+1)
#
# p1to10(1)

# def p1to10(n):
#     if n < 11:
#         p1to10(n+1)
#     return n
#
# print(p1to10(1))


'''WAP to create a dictionary to count the number of occurrences of each character'''
# d = {}
# def occ(a):
#     if len(a) == 0:
#         return d
#     d[a[-1]] = a.count(a[-1])
#     return occ(a.replace(a[-1],""))
#
# print(occ("hello"))


#
# a = "hello".replace("hello"[-1],"")
# print(len(a))
# def occ(a):
#     count = a.count(a[-1])
#     if len(a) == 0:
#         return count
#     return occ(a.replace(a[-1],""))
#
# print(occ("hello"))

# def occ(a):
#     d = {}
#     s = set(a)
#     ele = s.pop()
#     d[ele] = a.count(ele)
#     if len(s) == 0:
#         return d
#     return occ(a.replace(ele,""))
#
# print(occ("hello"))




# s = "heelllol
# s1 = set(s)
# # s = set(s)
# # print(s)
# d = {char: s.count(char) for char in s1}
# # d = {}
# # i = 1
# # # # d = {char: s.count(char) for char in s}
# # d = {char: i if char not in d else (i+1) for char in s}
# print(d)

# i = 1
# for char in s:
#     if char not in d:
#         d[char] = i
#     else:
#         d[char] += i
# print(d)

# def count_(n):
#     if n <= 10:
#         print(n, end=" ")
#         n += 1
#         count_(n)
#     else:
#         return
# count_(1)

# def count_1(n):
#     if n > 10:
#         return
#     print(n, end=" ")
#     count_1(n+1)
# count_1(1)

'''WRP to print the numbers from 10 to 1'''
# lis = []
# def num_(n):
#     if n == 0:
#         return lis
#     lis.append(n)
#     return num_(n-1)
#
# print(num_(10))




# def num_(start, end):
#     if start < end:
#         return
#     else:
#         print(start, end =" ")
#         num_(start-1, end)
# num_(10, 1)


'''WRP to add the digits of a number'''

# def add(n):
#     a = n // 10
#     b = n % 10
#     if a == 0:
#         return b
#     return b + add(a)
#
# print(add(12115))

# def add(n):
#     a = n // 10   # 12 1 0
#     b = n % 10    # 1  2 1
#     if a > 0:
#         return b + add(a)
#     return b
#
# print(add(121))


# def add(d, sum=0):
#     if d > 0:
#         a = d % 10
#         d = d // 10
#         sum = sum + a
#         return add(d, sum)
#
#
#     else:
#         return sum

# print(add(123))

# def add_(a,b,c):
#     return a+b+c
#
# print(add_(1,2,3))

# def add_(*args):
#     n = args
#     n = args % 10
#
# print(add_(121))



# a = 121
# # print(121 % 10)
# print(121 // 10)
# d = 0
# m = a
# while m > 0:
#     n = a % 10
#     m = a // 10
#
#     a = m
#     d += n
# print(d)

# def add_(a):
#     m = a
#     d = 0
#     n = 0
#     while m > 0:
#         m %= 10
#         m //= 10
#         #
#         a = m //= 10
#         d += (m %= 10)
#     return d
# print(add_(123))
'''IMP program...decode and again try==> check with python.tutor'''
# def add_(num, sum=0):
#     if num > 0:
#         last = num % 10
#         sum += last
#         num = num // 10
#         return add_(num, sum)
#     else:
#         return sum
#
# print(add_(12))


'''WRP to find the sum of first n numbers'''

# def add(n):
#     if n == 1:
#         return n
#     return n + add(n-1)
# print(add(5))
#


# def sum_(n, sum=0):
#     if n > 0:
#         sum += n
#         # n = n-1
#         return sum_(n-1, sum)
#     return sum
# print(sum_(5))

# def facto(n):
#
#     if n == 1:
#         return n
#     return n * facto(n-1)
#
# print(facto(5))
#

# def sum(n, add=0):
#     if n > 0:
#         add += n
#         return sum(n-1, add)
#     return add
# print(sum(5))


'''WRP to find factorial of a number'''

# def sum_(n, fact=1):
#     if n > 0:
#         fact *= n
#         # n = n-1
#         return sum_(n-1, fact)
#     return fact
# print(sum_(5))

####### in reverse way###########
# def sum_(n):
#     if n == 1:
#         return 1
#     return n+sum_(n-1)
# print(sum_(3))

# def sum_(n):
#     if n == 1:
#         return 1
#     return n+sum_(n-1)
# print(sum_(3))


'''WRP to count the number of digits in a number'''







# def num_d(n, count=0):
#     if n > 0:
#         n = n // 10
#         count += 1
#         return num_d(n, count)
#     elif n < 0:
#         return num_d(-n)
#     return count
#
# print(num_d(1234))

# def count_(n):
#     if n // 10 == 0:
#         return 1
#     return 1+count_(n // 10)
# print(count_(-300))

'''WRP to reverse a string'''

# def rev_s(string, i=0, res=""):
#     if i < len(string):
#         res = string[i] + res
#         return rev_s(string, i+1, res)
#     return res
# print(rev_s("hello"))

# def rev(a, s:str):
#     if len(a) > 0:
#         s +=
#         return rev()
#
# print(rev("hi"))

'''assignment : WRP to print fibonacci series upto n'''

# def rec(n):
#     lis = [0, 1]
#     if len(lis) == n:
#         return lis[n-1]
#     else:
#         lis.pop()
#         return rec(n-1)

# rec(7)
# print(rec(7))

# def facto(n):
#     if n == 1:
#         return 1
#     return n + facto(n-1)
# print(facto(5))

# def add(n):  # 12
#     a = n // 10  # 1
#     b = n % 10  # 2
#     if a < 10:
#         return a
#     return b + add(a)
# print(add(12))
#
# def sum_(a):
#
#     if a % 10 == 0:
#         return a
#     return a % 10 + sum_(a // 10)
#
# print(sum_(121))

# def sum_(a):
#     n = a % 10  # 1
#     m = a // 10  # 12
#
#     if n == 0:
#         return n
#     return n + sum_(m)
#
# print(sum_(121))


# def count(d): # 1234
#     n = d // 10
#     if n == 0:
#         return 1
#     return 1 + count(n)
#
# print(count(1234))

# def rev(s): #hello
#     a = ""
#     a = s[-1]+a
#     if len(a) == len(s):
#         return a
#     return a + rev(s[:len(s)-1])
#
# print(rev("hello"))

'''number of occurrences of each character'''

# def ocrn(s):  # helloooh
#     lis = list(s)
#     if len(lis) == 1:
#         return lis[0], s.count(lis[0])
#     lis.pop()
#     return ocrn(str(lis))
#
# print(ocrn("hellooh"))

# def a(s):
#     print(s)
#     return a(s[1::])
#
#
# a("hai")

# import sys
# sys.setrecursionlimit(1000)
# print(sys.getrecursionlimit())

# def i(a):
#     return i(a)
# i(2)

# string = "welcome to python python is a easy programming language"
#
# def occ_(a):
#     s = a.split()
#     lis = set(s)
#     d = {word:s.count(word) for word in lis}
#     return d
#
# print(occ_(string))