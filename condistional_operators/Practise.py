""" 1) WAP to create a list of squares for the elements in the below list"""
# l = [1, 2, 3, 4, 5]
#
# lis = [(item*item) for item in l]
# print(lis)


""" 2) create list of tuples of index and its corresponding item in the list """
# l = ["python", 10, 3.2, "selenium", "Java"]
#
# lis = [item for item in enumerate(l)]
# print(lis)


""" 3) list of even numbers """
# l = list(range(10))
#
# lis = [num for num in l if num % 2 == 0]
# print(lis)

""" 4) list of even and odd """
# l1 = list(range(20))
# lis = [[num for num in l1 if num % 2 == 0], [num for num in l1 if num % 2 != 0]]
# print(lis)
# def even(lis):
#     lis_even = []
#     lis_odd = []
#     for num in lis:
#         if num % 2 == 0:
#             lis_even.append(num)
#         else:
#             lis_odd.append(num)
#     return lis_even, lis_odd
#
# print(list(even(l)))
#
# def even(l):
#     lis = [[num for num in l if num % 2 == 0], [num for num in l if num % 2 != 0]]
#     return lis
# print(even(l1))

""" 5) if even store as it is else reverse and store it """
# l = ["python", "Node JS", "selenium", "Java"]
#
# lis = [word if len(word) % 2 == 0 else word[::-1] for word in l]
# print(lis)

""" 6) reverse if it is a string else keep it as it is """
# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
#
# lis = [item[::-1] if isinstance(item, str) else item for item in list_]
# print(lis)

""" 7) list of words starting with vowel """
# files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]
#
# lis = [word for word in files if word[0].lower() in "aeiou"]
# print(lis)

""" 8) set comprehension to create a set of squares from 1 to 10"""

# set_ = set(num*num for num in range(1, 11))
# print(set_)


""" 9) set of tuples with index and item """
# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
#
# set_ = set(item for item in enumerate(list_))
# print(set_)

""" 10) set of tuples with item and its length pair """
# files = ("Amazon", "flipkart", "walmart", "gmail", "yahoo")
#
# set_ = set((item, len(item)) for item in files)
# print(set_)

""" 11) WAP to create a dictionary with item and its index pair"""
# string = "hello"
#
# #
# # #d = {item: index for index, item in enumerate(string)}
# # d = {index: item for index, item in enumerate(string)}
# d = {i: string[i] for i in range(len(string))}
# print(d)

""" 12) WAP to create a dictionary with word and its length pair"""
# sentence = "hello world welcome to python"
# lis = sentence.split()
#
# d = {word: len(word) for word in lis}
# print(d)

""" 13) create a dictionary of character and its count"""
# s = "hello world"
# set_ = set(s)
#
# d = {char: s.count(char) for char in set_}
# print(d)

""" 14) create a dictionary of word and its count"""
# sentence = "python is a language, python programming is easy"
# lis_ = sentence.split()
# set_ = set(sentence.split())
# print(lis_)
# d = {word: lis_.count(word) for word in lis_}
# d = {word: sentence.count(word) for word in set_ if len(word) > 1}
# print(d)


""" 15) dictionary with word and its count pair only if the word is of even length"""

# sentence = "python is a language, python programming is easy"
#
# lis_ = sentence.split()
# d = {word: lis_.count(word) for word in lis_ if len(word) % 2 == 0}
# print(d)

""" 16) dictionary with index and word pair if the word is of odd length reverse it,
else keep it as is"""

# sentence = "python is a language, python programming is easy"
#
# lis_ = sentence.split()
# d = {index: word[::-1] if len(word) % 2 != 0 else word for index, word in enumerate(lis_)}
# print(d)


""" 17) word and length pair only if the word is starting with vowel """
#
# sentence = "python is a language, python programming is easy"
#
# lis_ = sentence.split()
# d = {word: len(word) for word in lis_ if word[0].lower() in "aeiou"}
# print(d)

""" 18) index and word pair if word is of type string reverse it """
# list_ = ["python", 17, 9, "java", 19.9, 4+0j, "ruby", "c++"]
# #
# d = {index: word[::-1] if isinstance(word, str) else word for index, word in enumerate(list_)}
# print(d)


""" 19) index and word pair if word is of type string keep it as it else reverse it """
# list_ = ["python", 17, 9, "java", 19.9, 4+0j, "ruby", "c++"]
#
# d = {index: str(word)[::-1] if isinstance(word, (int, float, complex)) else word for index, word in enumerate(list_)}
# print(d)

""" 20) flip keys and values in a dictionary """
# dict_ = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#
# d = {values: keys for keys, values in dict_.items()}
# print(d)

""" 21) char and ascii value pair """
# string = "python"
#
# d = {char: ord(char) for char in string}
# print(d)

'''WAP to create a dictionary to count the number of occurrences of each character'''

# s = "heelllo"
# # s = set(s)
# # print(s)
#
# d = {}
# i = 1
# # # d = {char: s.count(char) for char in s}
# d = {char: i if char not in d else (i+1) for char in s}

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

# def num_(start, end):
#     if start < 1:
#         return
#     else:
#         print(start, end =" ")
#         num_(start-1, end)
# num_(10, 1)


'''WRP to add the digits of a number'''

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
#
# def sum_(n, sum=0):
#     if n > 0:
#         sum += n
#         # n = n-1
#         return sum_(n-1, sum)
#     return sum
# print(sum_(5))

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

#######################################################################################################
'''                   lambda function                              '''
#######################################################################################################

'''WLF to check if the given number is even or not'''

# even_ = lambda n: n % 2 == 0
#
# print(even_(5))

'''WLF that multiplies two numbers'''

# multi = lambda a, b: a*b
# print(multi(4, 5))

'''WLF that returns last elements of the sequence'''
#
# last = lambda a: a[-1]
# print(last("hello"))
#
# last = lambda a, b: (a,b)[0]
# print(last("hello", [1,2,3,4]))

'''WLF that checks if the given string is palindrome or not'''

# check = lambda a: f"{a} is a palindrome" if (a == a[::-1]) else f"{a} is not a palindrome"
# print(check("mom"))

'''WLF that checks whether the number is even or odd and print the number in both the case'''

# even_odd = lambda num: f"{num} is a even number" if num % 2 == 0 else f"{num} is a odd number"
# print(even_odd(3))

#######################################################################################################
'''                   map function                              '''
#######################################################################################################

# list_ = ["hello", "mom", "dad", "hai"]
#
# check = lambda a: f"{a} is a palindrome" if (a == a[::-1]) else f"{a} is not a palindrome"
# print(list(map(check, list_)))


'''WMF that checks if the given list of numbers are even or odd'''
#
# list1 = [1,2,3,4,5]
# list2 = [10,11,12,13,14]
# even_odd = lambda num , num1: f"{num} is a even number" if num % 2 == 0 else f"{num} is a odd number"
# print(list(map(even_odd, list1,list2)))

'''WAP to return the strings which are starting with vowels'''

# words_ =["python", "and", 'its', "easy", "language"]
# vowel_word = lambda word: word if word[0].lower() in "aeiou" else f"{word} not starting with vowel"
# print(list(map(vowel_word, words_)))

'''for using only if condition, we can use filter IPO map'''

'''assignments'''
'''map1) wap to convert all the string in the list to upper case using map'''
'''map2) to convert all the negative numbers in the list to positive number '''
'''map3) WAP that returns the list of numbers raised to the power of their indesis using map '''
'''map4) WAP that returns all the words in lower case in the given sentence'''

######################################