'''1. Write a program to find the length of the string without using inbuilt function (len)'''
from itertools import count
from collections import Counter
# string_ = "hello"
# count = 0
# for char in string_:
#     count += 1
# print(count)

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

