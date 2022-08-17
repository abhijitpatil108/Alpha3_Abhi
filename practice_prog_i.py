'''1. Write a program to find the length of the string without using inbuilt function (len)'''
from itertools import count
from collections import Counter
# string_ = "hello"
# count = 0
# for char in string_:
#     count += 1
# print(count)
from math import prod

'''2. Write a program to reverse a string without using any inbuilt functions.'''

# def _rev(s):
#     rev = ""
#     for char in s:
#         rev = char + rev
#     return rev
# print(_rev("hello"))

# def _rev(s): #hello
# #     if len(s) == 1:
# #         return s
# #     return s+_rev(s[-1])
# #
# # print(_rev("hello"))

# def _rev(s, res=""): #hello
#     if len(s) != 0:
#         res = res+ s[-1]
#         _rev(s[:-1], res)
#     return res
#
# print(_rev("hello"))

# def _rev(s):
#     return s[::-1]
#
# print(_rev("hello"))

'''3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".'''

# s = "Hello World"
# print(s.replace("World","universe"))

'''4. How to convert a string to a list and vice-versa.'''

# s = "Hello World"
# l = list(s)
# l1 = s.split()
# s1 = "".join(l)
# s2 = " ".join(l1)
# print(l1)
# print(l)
# print(s1)
# print(s2)

'''5. Covert the string "Hello welcome to Python" to a comma separated string.'''
# s = "Hello welcome to Python"
# print(s.replace(" ", ","))

'''6. Write a program to print alternate characters in a string.'''
# word = "python"
# print(word[::2],word[1::2],sep="")

'''7. Write a Program to print ascii values of the characters present in a string.'''
# word = "build"
# print({char:ord(char) for char in word})

'''8. Write program to convert upper case to lower case and vice-versa without using inbuilt method.'''
# default_ = "Hello"
# # swapcase_ = default_.swapcase()
# # print(swapcase_)
# d = 32
# print("".join([chr(ord(char)+d) if 'A' <= char <= 'Z' else chr(ord(char)-32) for char in default_]))
#

'''9. Write program to swap two numbers without using 3rd variable.'''
# a = 10 #5
# b = 20 #30
# a, b = b, a
# # a, b = [a + (b-a), b - (b-a)]
# print(a, b)

'''10. Write program to merge two different lists.'''
# l1 = [1,2,3]
# l2 = [4,5,6]

# print(l1+l2)
# print([item for item in (*l1,*l2)])


# l = [4,5,6]
# l1 = [1,2]
# l3 = [3]
# lis = []
# for i in range((len(l)*2)-1):
#     lis.append(0)
# lis.append(l[-1])
# print(lis)

# lis = [0 for i in range((len(l3)*2)-1)]
# lis.append(l3[-1])
# print(lis)

"""11. Write program to read a random line in a file. (ex. 50, 65, 78th line)"""

# from itertools import islice
#
# path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\football.txt"
#
# lis = [50, 65, 78]
#
# def read_specific_lines(num):
#     with open(path) as f:
#         res = islice(f, num, num + 1)
#         return list(res)
#
#
# _line = map(read_specific_lines, lis)
# print(list(_line))
#

# from itertools import islice
#
# path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\football.txt"
#
# def read_specific_line(num):
#     with open(path) as f:
#         _line = islice(f, num, num+1)
#         return list(_line)
#
# print(read_specific_line(2))

# def read_line(num):
#     with open(path) as f:
#         for index, line in enumerate(f, start=1):
#             if index == num:
#                 return line
#
# res = read_line(2)
# print(res)

"""12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)"""

from itertools import islice

# def random_lines(num):
# 	with open(path) as f:
# 		_line = islice(f, num-6, num)
# 		return list(_line)
# print(random_lines(15))

# def random_lines(start, end):
#     with open(path) as f:
#         s = islice(f, start, end)
#         for line in s:
#             print(line)
#
# random_lines(9,15)

# def read_n_lines(start_line, end_line):
#     with open(path) as f:
#         s = islice(f, start_line,end_line)
#         for line in s:
#             print(line)
#
# read_n_lines(10, 15)



"""13 Program to print last "N" lines of a file."""

path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\football.txt"

# from collections import deque
#
# # def last_lines(num):
# #     with open(path) as f:
# #         lines = deque(f, num)
# #         return list(lines)
# #
# #
# # print(last_lines(3))
# num = 3
# with open(path) as f:
#     lines = deque(f, num)
#     print(list(lines))
#     # for line in lines:
#     #     print(line)


# def tail(n):
#     with open(path) as f:
#         d = deque(f, n)             # only last 'n' lines will be loaded to the deque
#         return d
#
# last_10_lines = tail(10)     # returns last 10 lines of the file
# for line in last_10_lines:
#    print(line)









# class Demo:
#
#     def add(self, a, b):
#         self.a = a
#         self.b = b
#         a += 5
#         return a + b
#
#     def add1(self):
#         return a
#
#
# a = Demo()
# print(a.add(1,2))
# print(a.add1())








#
# l = [1,2,2,2,2,2,2,4]

# l1 = [4, 2, 2, 2, 2, 2, 2, 1]
# # # # print(list(reversed(l)))
# # #
# # l = [item if l.count(item) == 1 else l.remove(item) for item in reversed(l) ]
#
# l = [item if l.count(item) == 1 else str(l.remove(item)) for item in reversed(l) ]

# print(l)
# # #
# #
# print(l)
#
# l = [1,2,3,2,4]
#
# print(str(None).replace("None",""))

"""14. Write a program to check if the given string is Palindrome or not without using reversed method."""
# word = "naman"
# if word == word[::-1]:
# 	print(f"{word} is palindrome")

# word = "naman"
# new_word =""
#
# for i in range(len(word)):
#     new_word = word[i] + new_word
#     print(new_word)
# if new_word == word:
#     print(f"{word} is palindrome")

# def is_palindrome(word):
#     new_word = word[::-1]
#     if word == new_word:
#         return True
#     return False
# print(is_palindrome("naman"))

''' 21 Write a class named Simple and it should have iteration capability.'''

# class Sample:
#     def __init__(self, items):
#         self.items = items
#
#     def __iter__(self):
#         return iter(self.items)
#
# s = Sample([1,2,3,4])
#
# for item in s:
#     print(item)

'''74'''

# for i in range(1, 6):
#     print("*"*i)
#
# for i in range(1, 6):
#     s = " "
#     print(f"{s}*("*"*i)
#
# for i in range(5):

# for i in range(1,6):
#     print(f"{'* '*i:^10}")

# for i in range(5, 0, -1):
#     print(f"{'* '*i:^10}")

# pat = ''
# for i in range(1, 6):
#     pat += str(i)
#     print(f"{pat:<5}")

# pat = ''
# for i in range(1, 6):
#     pat += str(i)
#     print(f"{pat:>5}")

# pat = ''
# for i in range(1, 6):
#     pat = pat + ' ' + str(i)
#     print(f"{pat:^10}")

# pat = ''
# for i in range(5, 0, -1):
#     pat = pat + ' ' + str(i)
#     print(f"{pat:^10}")

import re
# sentence = "Hello welcome to python programming language selenium webdriver poom pooom pyteeest"
# v = "aeiouAEIOU"
# vowels_1 = []
# vowels_3 = []
# for word in sentence.split():
#     res1 = re.findall(r"\b[^aeiouAEIOU].*[aeiouAEIOU].*[^aeiouAEIOU]\b", word)
#     res3 = re.findall(r"\b[^aeiouAEIOU].*[aeiouAEIOU]{3}.*[^aeiouAEIOU]\b", word)
#     if len(res1) != 0:
#         vowels_1.append(res1)
#     if len(res3) != 0:
#         vowels_3.append(res3)
#
# print(vowels_1)
# print(vowels_3)

# sentence = "Hello welcome to python programming language selenium webdriver poom pooom pyteeest"
# word = "po$oom" #"Webdriver" #"poom" #"language" #"Webdriver"
# res = re.findall(r"\b[^aeiouAEIOU].*[aeiouAEIOU].*[^aeiouAEIOU]\b", word)
# if res:
#     res1= re.findall(r"[aeiouAEIOU]", word)
#     print(f"no of vowels in {word}:{len(res1)}")
#     if len(res1) > 2:
#         print(f"word with more than 3 vowels: {word}")
# else:
#     print(f"{word} word is not of required condition")

sentence = "Hello welcome to python programming language selenium webdriver poom pooom pyteeest"
# word = "Webedriver" #"poom" #"language" #"Webdriver"
# res = []
# while len(word) > 2:
# # for i in range(len(word)-1):
#     res += re.findall(r"[^aeiouAEIOU][aeiouAEIOU][^aeiouAEIOU]", word[:3])
#     word = word.replace(word[0],'',1)
#     # print(word)
# print(res)
# print(len(res))

# word = "pooomoooonoommommmm"
# word = "Hello welcome to python programming language selenium webdriver poom pooom pyteeest"
# res = []
# # i = 0
# while len(word) > 0:
#     r = re.findall(r"[^aeiouAEIOU][aeiouAEIOU]+[^aeiouAEIOU]", word)
#     if len(r) != 0:
#         res += [r[0]]
#         word = word.replace(r[0][:-1],'',1)
#         # print(word)
#         # i += 1
#     else:
#         word = ''
# count_ = [len(item[1:-1]) for item in res]
# vowels_ = [item[1:-1] for item in res if len(item[1:-1]) > 2]
# print(res)
# print(count_)
# print(vowels_)
# print(sum(count_))




# print(r[1:-1])
# res = []
# res += re.findall(r"[^aeiouAEIOU][aeiouAEIOU]+[^aeiouAEIOU]", word)
# while len(word) > 2:
# for i in range(len(word)-1):
#     r = re.findall(r"[^aeiouAEIOU][aeiouAEIOU]+[^aeiouAEIOU]", word)
#     print(r[1:-1])
#     # word = word.replace(r[0][:-1], '', 1)
#     # print(word)
#     res += r
# print(res)
# print(len(res))



# if res:
#     res1= re.findall(r"[aeiouAEIOU]", word)
#     print(f"no of vowels in {word}:{len(res1)}")
#     if len(res1) > 2:
#         print(f"word with more than 3 vowels: {word}")
# else:
#     print(f"{word} word is not of required condition")

# num = 10
# for n in range (2, num):
#     if num % n == 0:
#         print(f"{num} is not prime")
#         break
#     # else:
#     #     continue
# else:
#     print(f"{num} is prime")

# def even_(start, end):
#     lis = []

# def even_(end, start=1):
#     lis = []
#     for num in range(start, end+1):
#         if num % 2 == 0:
#             lis.append(num)
#     return lis
#
# print(even_(50))

'''loadstoner project interview question'''

# a = ("Red", "Orange", "Green")
# b = ("abc", "def", "ghi", "jkl", "aaa", "bbb", "ccc", "ddd", "eee")
# c = []
# for i in range(len(b)):
#     c.append((b[i], a[i % len(a)]))
#
#     # if i < len(a):
#     #     c.append((b[i], a[i]))
#     # else:
#     #     c.append((b[i], a[i%len(a)]))
#
# print(c)

'''pattern printing'''

# for i in range(1, 6):
#     print(f"{'* ' *i:^10}")

# for i in range(5, 0, -1):
#     print(f"{'* ' *i:^10}")

# pat = ''
# for i in range(1, 6):
#     pat = pat + ' ' + str(i)
#     print(f"{pat:^10}")

# pat = ''
# alp = ['a', 'b', 'c', 'd', 'e']
# for ch in alp:
#     pat = pat + ' ' + ch
#     print(f"{pat:^10}")


'''76 Write a program to map a product to a company and build a dictionary with company and list of products pair'''

# all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
#                 'iOS', 'Google Drive', 'One Drive']
#
#  # Pre-defined products for different companies
# apple_products = {'iPhone', 'Mac', 'iWatch'}
# google_products = {'Gmail', 'Maps', 'Google Drive'}
# msft_products = {'Windows', 'One Drive'}
#
# po = {apple_products, google_products, msft_products}
# from collections import defaultdict
# d = defaultdict(list)
# d = {}

# from collections import defaultdict
# dd = defaultdict(list)
# path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\text1.txt"
# d = {}
# with open(path) as f:
#     for line in f:
#         line.strip()
#         l = line.split()
#         for word in l:
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
# print(d)

'''hexadecimal to binary conversion'''

'''HCF and LCM'''

# def hcf(a, b):
#     temp = sorted((a, b))
#     lis = [temp[0] // num for num in range(1, 10) if temp[0] % num == 0]
#     for num in lis:
#         if temp[-1] % num == 0:
#             return num
#             # print(f"HCF of {a} and {b} is {num}")
#             # break
#     else:
#         return 1
#         print(f"HCF of {a} and {b} is {1}")

# print(hcf(18, 32))

# def hcf(*a):
#     temp = sorted((a))
#     lis = [temp[-2] // num for num in range(1, 10) if temp[-2] % num == 0]
#     for num in lis:
#         if temp[-1] % num == 0:
#             return num
#             # print(f"HCF of {a} is {num}")
#             # break
#     else:
#         return 1
#         # print(f"HCF of {a} is {1}")
#
# hcf(24, 36, 12)

# def lcm(a, b):
#     n1 = hcf(a, b)
#     print(n1)
#     res = a // n1 * b // n1 * n1
#     return f"lcm of {a} and {b} is {res}"

# print(lcm(18, 27))

# def hcf(*a):
#     temp = sorted((a))
#     print(temp)
#     r = list(range(1, 10))
#     print(r)
#     lis = []
#     # lis = [[temp[-2] // num, num] for num in range(1, 10) if temp[-2] % num == 0]
#     # lis = [temp[-2] // num for num in range(1, 10) if temp[-2] % num == 0]
#     for num in r:
#         if temp[-2] % num == 0:
#             lis.extend((temp[-2] // num, num))
#     print(lis)
#     lis1 = sorted(lis, reverse=True)
#     # l = sorted(lis + r)
#     # print(l)
#     for num in lis1:
#         if temp[-1] % num == 0:
#             return num
#             # print(f"HCF of {a} is {num}")
#             # break
#     else:
#         return 1
#         # print(f"HCF of {a} is {1}")

# def hcf(*a):
#     temp = sorted((a))
#     lis = []
#     for num in range(1, 10):
#         if temp[0] % num == 0:
#             lis.extend((temp[0] // num, num))
#     lis1 = sorted(set(lis), reverse=True)
#     # print(lis1)
#     for num in lis1:
#         s = [t % num for t in temp]
#         # print(s)
#         if sum(s) ==  0:
#             return num
#         else:
#             continue
# # print(hcf(136, 170, 255))
# # print(hcf(15, 20, 25))
# def lcm(*a):
#     n1 = hcf(*a)
#     res = prod((num//n1 for num in a))
#     res1 = hcf(res, n1)
#     mul = 0
#     if res1 == n1:
#         mul = n1
#     else:
#         mul = n1 // res1
#     print(res1)
#     return f"HCF of {a} is {n1} and LCM is {res*mul}"
# print(lcm(5536, 3332))
# print(lcm(832, 1658))
# print(lcm(15, 20, 25))
# print(lcm(184, 230, 276))
# print(lcm(136, 170, 255))

'''HCF new'''
# lis = []
# def enter_num():
#     tn = int(input("HCF for 2 numbers or 3 numbers? enter 2 or 3: "))
#     if tn == 2:
#         num1 = int(input("number1 : "))
#         num2 = int(input("number2 : "))
#         lis.append(num1)
#         lis.append(num2)
#     elif tn == 3:
#         num1 = int(input("number1 : "))
#         num2 = int(input("number2 : "))
#         num3 = int(input("number3 : "))
#         lis.append(num1)
#         lis.append(num2)
#         lis.append(num3)
#     else:
#         print("enter either 2 or 3 numbers")
#         return enter_num()
# enter_num()
# lis = sorted(lis)
# p =[]
# for num in lis:
#     for n in range(2, (num//2)+1):
#         if num % n == 0:
#             break
#         else:
#             pass
#     else:
#         p.append(num)
# p = sorted(p)
# print(p)
# if len(p) > 1:
#     print(f"HCF is {1}")
# elif len(p) == 1 and p[0] > lis[0]:
#     print(f"HCF is {1}")
# elif len(p) == 1 and p[0] == lis[0]:
#     while p[-1] < lis[-1]:
#         temp = p[-1]+p[0]
#         p.append(temp)
#     if set(lis).issubset(set(p)):
#         print(f"HCF is {p[0]}")
#     else:
#         print(f"HCF is {1}")
# elif len(p) == 0 and len(lis) == 3:
#     for n in range(lis[0], 2, -1):
#         if lis[1] % n == 0 and lis[2] % n == 0:
#             print(f"HCF of {lis} is {n}")
#     else:
#         print(f"HCF of {lis} is {1}")
# elif len(p) == 0 and len(lis) == 2:
#     for n in range(lis[0], 2, -1):
#         if lis[1] % n == 0:
#             print(f"HCF of {lis} is {n}")
#             break
#     else:
#         print(f"HCF of {lis} is {1}")


'''Half solid diamond'''
'''
3
44
555
6666
555
44
3
'''
'''1st'''
s = int(input("Enter the size of the diamond pattern to be printed : "))  #for even input it will be input +1
n = int(input("Enter the starting number of diamond pattern : "))
# s = 7  #'''size of the diamond (length or width)'''
# n = 3  #'''Starting input to be printed'''
r1 = list(range(1, (s//2)+2))
r2 = list(reversed(r1))
r2.pop(0)
r = r1 + r2
temp = ''
count = 0
for i in r:
    for j in range(1, i+1):
        temp += str(n)
    print(temp)
    count += 1
    if count < s//2 +1:
        n += 1
    else:
        n -= 1
    temp = ''

'''2nd'''
s = int(input("Enter 'even' number as size of the diamond pattern  : "))   #for odd input it will odd-1
n = int(input("Enter the starting number of diamond pattern: "))
# s = 8  #'''size of the diamond '''
# n = 1  #'''Starting input to be printed'''
r1 = list(range(1, (s//2)+1))
r2 = list(reversed(r1))
r = r1 + r2
temp = ''
count = 0
for i in r:
    for j in range(1, i+1):
        temp += str(n)+" "
    temp = temp.replace(' ', '*')
    temp = temp[::-1].replace('*', '', 1)
    print(temp[::-1])
    count += 1
    if count < s//2:
        n += 1
    elif count == s//2:
        n += 0
    else:
        n -= 1
    temp = ''

'''3rd'''
def input_():
    s1 = int(input("Enter only 'even' number as size of the diamond pattern  : "))
    if s1 % 2 == 0:
        return s1
    else:
        print("Expected size Even, but entered odd")
        return input_()
s = input_()
n = int(input("enter the starting number of diamond pattern: ")) - 1
r1 = list(range(1, (s//2)+1))
r2 = list(reversed(r1))
r = r1 + r2
temp = ''
count = 0
for i in r:
    for j in range(1, i+1):
        if count < s // 2:
            n += 1
        elif count == s // 2:
            n = n1 - (s-i) + j
        else:
            n = n2 - i + j
        temp += str(n) + " "
    temp = temp.replace(' ', '*')
    temp = temp[::-1].replace('*', '', 1)
    temp1 = temp[::-1]
    n1 = n
    n2 = n - i
    print(temp1)
    count += 1
    temp = ''

'''4th'''
s = int(input("Enter the height of the diamond pattern to be printed : "))
#for even input output height will be input +3, for odd output height will be input +2
n = int(input("enter the starting number of diamond pattern: "))
r1 = list(range(n-1, n+(s//2 + 1)))
r2 = list(reversed(r1))
r2.pop(0)
r = r1 + r2
# print(r)
temp = ''
filler1 = ''
filler2 = ''
for i in r:
    for j in range(n, i + 1):
        filler1 = filler1 + ' ' + str(j)
        filler2 = str(j) + ' ' + filler2
    if 10 > i >= n:
        temp = '*' + filler1 + filler2[1:len(filler1)] + '*'
    elif i >= 10:
        temp = '*' + filler1 + filler2[2:len(filler1)] + '*'
    else:
        temp = '*'
    print(temp)
    filler1 = ''
    filler2 = ''

'''4th same as above but a bit complex and raw one....can be simplified'''
# s = int(input("Enter the height of the diamond pattern to be printed : "))
# #for even input output height will be input +3, for odd output height will be input +2
# n = int(input("enter the starting number of diamond pattern: "))
# r1 = list(range(n-1, n+(s//2 + 1)))
# r2 = list(reversed(r1))
# r2.pop(0)
# r = r1 + r2
# print(r)
# temp = ''
# filler1 = ''
# filler2 = ''
# for i in r:
#     for j in range(n, i + 1):
#         filler1 = filler1 + ' ' + str(j)
#         filler2 = str(j) + ' ' +  filler2
#     # print(filler)
#     if 10 > i >= n:
#         # temp = '*' + filler1 + filler1[:len(filler1) - 1][::-1] + '*'
#         temp = '*' + filler1 + filler2[1:len(filler1)] + '*'
#     elif i >= 10:
#         # temp = '*' + filler1 + filler1[:len(filler1) - 2][::-1] + '*'
#         temp = '*' + filler1 + filler2[2:len(filler1)] + '*'
#     else:
#         temp = '*'
#     # temp = ' '.join(temp)
#     print(temp)
#     filler1 = ''
#     filler2 = ''





# for i in r:
#     filler = filler + str(i)
#     if len(temp) > 1:
#         temp = '*' + filler + filler[:len(filler)-1][::-1] + '*'
#         # temp = temp.replace('0', '')
#     else:
#         temp = '*' + str(i)
#     temp = temp.replace('0', '')
#     # filler = filler.replace(filler[-1], '')
#     print(temp)



#
#
# s = int(input("Enter the height of the diamond pattern to be printed : "))  #for even input it will be input +1
# n = int(input("Enter the starting number of diamond pattern : "))
# # s = 7  #'''size of the diamond (length or width)'''
# # n = 3  #'''Starting input to be printed'''
# # r1 = list(range(1, (s//2)+2))
# r1 = list(range(s//2 + 1))
# r2 = list(reversed(r1))
# r2.pop(0)
# r = r1 + r2
# print(r)
# temp = ''
# filler = ''
# count = 0
# for i in r:
#     c1 = list(range(i+1))
#     c2 = list(reversed(c1))
#     c2.pop(0)
#     c = c1 + c2
#     # print(c)
#     for j in c:
#         filler += str(j)
#     temp = '*' + filler + '*'
#     temp = temp.replace('0', '')
#     temp = ' '.join(temp)
#     print(temp)
#     temp = ''
#     filler = ''

    #
    # for j in range(1, i+1):
    #     temp += str(n)
    # print(temp)
    # count += 1
    # if count < s//2 +1:
    #     n += 1
    # else:
    #     n -= 1
    # temp = ''










