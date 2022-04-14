# # # ## write a program to print greatest of 3 numbers
# # print("write a program to print greatest of 3 numbers")
# #
# s1 = int(input(" enter number 1 : "))
# s2 = int(input(" enter number 2 : "))
# s3 = int(input(" enter number 3 : "))
#
# s = [s1, s2, s3]
# print(max(s))
#
# s.sort()
# print(s[-1])
#
# print(s1 if s1 > s2 and s1 > s3 else s2 if s2 > s3 else s3)
# print(s3 if s3/(s1+s2) >=1 else s1 if s1 > s2 else s3)

# #
# # ##########################################################################
# #
# # # Write a program to check if the entered character is a vowel or not, if the char is a vowel,
# # # create a dictionary with char as key and ASCII value of the char as value

# s = input("Enter any character : ")
# d = dict()
# if s in "aeiouAEIOU":
#     d[s] = ord(s)
#     print(f"{s} is a Vowel")
#     print(d)
# else:
#     print(f"{s} is not a Vowel")

# # print('''Write a program to check if the entered character is a vowel or not.
# # If the char is a vowel, create a dictionary with char as key and ASCII value of the char as value.''')
# # s = input("enter a character : ")
# # s1 = "aeiouAEIOU"
# # if s1.rfind(s) != -1:
# #     print(f"{s} is a Vowel")
# #     print(dict({s: ord(s)}))
# # else:
# #     print(f"{s} is not a Vowel")
# #
# #
# # ##########################################
# #
# # s = input("enter a character : ")
# # if s in "aeiouAEIOU":
# #     print(f"{s} is a Vowel")
# #     print(dict({s: ord(s)}))
# # else:
# #     print(f"{s} is not a Vowel")
# #
# # #########################################
#
# s = input("enter a character : ")
# s1 = "aeiouAEIOU"
# if s.isalpha() and s in s1:
#     print(f"{s} is a Vowel")
#     print(dict({s: ord(s)}))
# elif s.isalpha() and s not in s1:
#     print(f"{s} is not a Vowel")
# elif s and not s.isspace():
#     print("VIP characters and Numbers are not allowed in this program")
# elif bool(s) is False:
#     print("No character was entered")
# elif s.isspace():
#     print("Don't give some space :)")

# ################################################
#
# char = "a"
# d = {}
# if char.lower() in "aeiou":
#     d[char] = ord(char)
#     print(d)
#

#
#marks = int(input("Enter the marks : ")


## # Write a program to print 10 to 1

# for item in range(10, -1, -1):
#     print(item, end = " ")

#
# n = 10
# while n > 0:
#     print(n)
#     n -= 1
#
#
# ### Write a program to print -1 to -10

# for item in range(-1, -11, -1):
#     print(item, end = '')

# n = -1
# while n >= -10:
#     print(n, end ='')
#     n -= 1

### Write a program to print -10 to -1

# n = -10
# while n < 0:
#     print(n)
#     n += 1

### Write a program to print even numbers from 1 to 50
#
# for item in range(2, 51, 2):
#     print(item, end=" ")
# print()
# n = 2
# while n <= 50:
#     print(n, end = ' ')
#     n += 2
# print()

# n = 1
# while n <= 50:
#     if n % 2 == 0:
#         print(n, end = ' ')
#     n += 1
#
# n = 0
# while n <= 50:
#     print(n)
#     n += 2
#
# n = int(input("enter a number : "))



### Write a program to print all the characters in a string.

# s = "hello"
# print(s)
# for item in s:
#     print(item, end = '')
# print()
# print(s[:])

# s = "hello"
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

### Write a program to print all the characters in a list.

# s = [1, 2, 3, 4, 4]
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

### Write a program to print all the characters in a tuple.
#
# s = (1, 2, 3, 4, 4)
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1
#
### Write a program to print all the characters in a set.
#
# s = {3, 6, 8, 9, 10}
# #
# # while set(s):
# #       print(s.pop(), end = ' ')
#
# for item in s:
#     print(item, end = ' ')

# s = {"hi", 6, 8.5, 9, "ho"}
# for item in s:
#     print(item, end = ' ')

## # Write a program to print 1 to 10 using for loop
#
# for n in range(1, 11):
#     print(n)

## # Write a program to print 10 to 1 using for loop
#
# for n in range(10, 0, -1):
#     print(n)

# ## # Write a program to print even numebrs from 1 to 10 using for loop
# #
# for n in range(1, 12, 2):
#     print(n-1)
#
# for n in range(0, 11, 2):
#     print(n)

# for n in range(1, 11):
#     if n % 2 == 0:
#         print(n)

# ## # Write a program to print odd numebrs from 1 to 10 using for loop
# #
# for n in range(1, 11, 2):
#     print(n)
#
## # Write a program to print from -1 to -10 using for loop
#
# for n in range(-1, -11, -1):
#     print(n)

## # Write a program to print from -10 to -1 using for loop
#
# for n in range(-10, 0):
#     print(n)

## # Write a program to print all the characters in a string

# s = "python"
# for item in range(len(s)):
#     print(s[item])

# s = "python"
# for item in s:
#     print(item)


# s = "python"
# for item in range(len(s), 0, -1):
#     print(s[item-1])

## # Write a program to print all the characters from list

# s = [1, 2, 3, 4]
# for item in range(len(s)):
#     print(s[item])
#
# s = [1, 2, 3, 4]
# for item in s:
#     print(item, end = " ")


## # Write a program to print all the characters from tuple


# s = (1, 2, 3, 4)
# for item in range(len(s)):
#     print(s[item])


## # Write a program to print all the characters from set


# s = {1, 2, 3, 4}
# for item in range(len(s)):
#     print(s.pop())
# print(s)
#
# s = {5, 2, 3, 4}
# for item in s:
#     print(item)
# print(s)

# s = {'python', 'welcome', 'to'}
# for item in s:
#     print(item, end = " ")
# print(s)


### trevesing through dictionaries ########

# d = {'one':1, 'two':2, 'three':3}
#
# for key in d:
#     print(key, d[key], sep="-->")
#     print(key)

# Write a program to print index and the element in  a the string.

# s = "python"
# for item in range(len(s)):
#     # print(s.index(item))
#     print(item, s[item], sep="->", end = " ")

# s = "hello"
# a = enumerate(s)
# # print(list(a))
# # #
# for item in a:
#     print(item)

# for item in range(len(s)):
#     print(item, s[item])

# for item1, item2 in a:
#     print(item1, item2)

# s = "hello"
# a = enumerate(s)
# for index, value in a:
#     print(index, "-->", value)
# #
#     # print(item[0], item[1])


# l1 = {9, 2, 4, 2, 6, 8, 2, 10}
# # # n1, n2, *rest = l1
# n6, n5, n4, n3, n2, n1 = l1
# print(n1, n2, n3, n4, n5, n6)

# print(reversed[l1])
# print(n1, n2, rest)
# print(n1, n2, *rest)

# l1 = [9, 2, 4, 2, 6, 8, 2, 10]
# l1.sort(reverse=True)
# print(l1)

# n1, n2, *rest = l1
# print(n1, n2, rest)
# print(n1, n2, *rest)
# print(l1)

# l1 = (9, 5, 4, 1, 6, 8, 1, 10)
# n1, n2, *rest = l1
# print(n1, n2, rest)

## write a prog to traverse trough string in reverse order

# s = "python"
# print(s[::-1], end='')
# for item in range(len(s), 0, -1):
#     print(s[item-1])
# for item in range(len(s)-1, -1, -1):
#     print(s[item])
# print(s[::-1])
# for item in reversed(s):
#     print(item, end = " ")

## write a prog to count the characters present in the given string without using len()
#
# string = "python"
# count = 0
# # for item in string:
# for _ in string:
#     count += 1
# print(count)


#### write a prog to print even indexed characters in the string

# string = "python"
# count = 0
# # for item in string:
# for _ in string:
#     if count % 2 == 0:
#       print(string[count])
#     count += 1

# string = "python"
#
# # for item in range(0, len(string), 2):
# #     print(string[item])
#
# for item in string[::2]:
#     print(item)

#### write a prog to print the digits presents inside a string
#
# string = "python2welcome"
#
# for ele in string:
#     if ele.isdigit():
#         print(ele)

# string = "python2welcome"
# #
# for ele in string:
#     if "0" <= ele <= "9":
#         print(ele)

#### write a prog to count the number of  digits presents inside a string

#
# string = "python2we34lcome"
# i = 0
# for ele in string:
#     if "0" <= ele <= "9":
#         i += 1
# print(i)

###############################################################################################
# #  Write a program to check if the marks given falls under following categories
# #and print the results based on marks
# # if marks < 35 print fail
# # if 35 < marks < 60 print secondclass
# # if 60 < marks < 75 print FirstClass
# # if marks>75 print distinction
###############################################################################################

# marks = int(input("Enter your marks : "))
# #
# rf = range(0, 35)
# r2 = range(35, 60)
# r1 = range(60, 75)
# rd = range(75, 100)
#
# print("fail" if marks < 35 else "Second Class" if 35 <= marks < 60 else "First Class" if 60 <= marks < 75 else "Distinction")
#
# print("fail" if marks in rf else "Second Class" if marks in r2 else "First Class" if marks in r1 else "Distinction")
#
# rList = [(rf, "fail"), (r2, "Second Class"), (r1, "First Class"), (rd, "Distinction")]
# i = 0
# for item in rList:
#     if marks in rList[i][0]:
#         print(rList[i][1])
#     i += 1

###############################################################################################
### Assignment : write a program to count the number of special characters in the string.
###############################################################################################

# string = r"Pyth__@@on_alpha@3\\n"
# # string = input(r"enter a string with special characters : ")
# i = 0
# j = 0
# for item in string:
#     if item.isalnum():
#         i += 1
#     else:
#         j += 1
# print((len(string)) - i)
# print(j)
# from itertools import zip_longest
#
# s1 = "Are"
# s2 = "you"
# s3 = "fine"
# for item in zip_longest(s1, s2, s3):
#     print(item)

###############################################################################################
### Assignment : write a program to count capitel letters and small letters in the string.
###############################################################################################

# string = input(r"enter a string : ")
# i = 0
# j = 0
# for item in string:
#     if item.islower():
#         i += 1
#     else:
#         j += 1
# print("Number of small Characters : ", (i))
# print("Number of Capital Characters : ", (j))
## The special charcters and numbers will also be treated as Capitals in above prog as defalut condition
#gets applied for both



###########

# string = input(r"enter a string with special characters : ")
# # string = "Hello"
# i = 0
# small = 0
# capital = 0
# other = 0
# while i < len(string):
#     if string[i].islower():
#         small += 1
#
#     elif string[i].isupper():
#         capital += 1
#     else:
#         other += 1
#     i += 1
#
# print("Number of small Characters : ", (small))
# print("Number of Capital Characters : ", (capital))

###########

# string = "1ABHI_patil1234"
# # string = input(r"enter a string with special characters : ")
# small = 0
# capital = 0
# for item in string:
#     if item.islower():
#         small += 1
#     elif item.isupper():
#         capital += 1
# print("Number of small Characters : ", (small))
# print("Number of Capital Characters : ", (capital))

##################################################################################################
##################### Travesing through list ################### 27 Jan 2022
##################################################################################################

# l = ["python", 10, 3.2, "Selenium", "Japan"]

# for item in l:
#     print(item, end = " ")
# print()
# for item in range(len(l)):
#     print(item, end=" ")
#     print()
#     print(l[item], end=" ")


### Wrtie a program to print index and its corresponding element.
#
# l = ["python", 10, 3.2, "Selenium", "Japan"]
#
# # for item in l:
# #     print(item, end = " ")
# # print()
# for item in range(len(l)):
#     print(item, l[item], sep="==>")


# l = ["python", 10, 3.2, "Selenium", "Japan"]
# i = 0
# for item in l:
#     print(i, item, sep="==>")
#     i += 1

# for index, item in enumerate(l):
#     print(index, item, sep="==>")
#
### Wrtie a program to print elements in the list in reverse order (in 3 ways)

# l = ["python", 10, 3.2, "Selenium", "Japan"]
# # i = 0
# for item in reversed(l):
#     print(item, end = " ")
#     # i += 1
# #
# l = ["python", 10, 3.2, "Selenium", "Japan"]
# for item in l[::-1]:
#     print(item, end = " ")

#
# l = ["python", 10, 3.2, "Selenium", "Japan"]
# for i in range(len(l)-1, -1,-1):
#     print(l[i], end = " ")


### Wrtie a program to print alternate elements in the list

# l = ["python", 10, 3.2, "Selenium", "Japan"]
#
# for item in l[::2]:
#     print(item, end = " ")
# print()
# for item in l[1::2]:
#     print(item, end = " ")

# l = ["python", 10, 3.2, "Selenium", "Japan"]
#
# i = 0
# for item in l:
#     if i % 2 == 0:
#         print(item, end=" ")
#     i += 1


### Wrtie a program to print only integers present in the list

# l = ["python", 10, 3.2, "Selenium", "Japan"]
# for item in l:
#     if isinstance(item, int):
#         print(item, end = " ")

# l = ["python", 10, 3.2, "Selenium", "Japan"]
# i = 0
# for item in l:
#     if l[i] :  #modifiy
#         print(item, end = " ")
#     i += 1

### Wrtie a program to print only integers present in the list
#
# l = ["python", 10, 3.2, "Selenium", "Japan"]
# for item in l:
#     if isinstance(item, (int, float, complex)):
#         print(item, end=" ")

### Wrtie a program to print length of each string in the list

# l = ["python", 10, 3.2, "Selenium", "Japan"]
#
# for item in l:
#     if isinstance(item, str):
#         print(item, len(item), sep = "==>")


### Wrtie a program to print the string which are of even length in the list

# l = ["python", "Selenium", "Japan"]
# lis =[]
# for item in l:
#     if len(item) % 2 == 0:
#         lis.append(item)
# print(lis)

# l = ["python", "Selenium", "Japan"]
# lis =[]
# for item in l:
#     if len(item) % 2 == 0:
#         lis.append(item)
# print(lis)

### Wrtie a program to print the elements in the list if element is of even length print as it and if of odd
## length then reverse and print
#
# l = ["python", "Selenium", "Japan"]
# lis =[]
# for item in l:
#     if len(item) % 2 == 0:
#         lis.append(item)
#     else:
#         lis.append(item[::-1])
# print(lis)

# l = ["python", "Selenium", "Japan"]
# # lis =[]
# for item in l:
#     if len(item) % 2 == 0:
#         l.append(item)
#     else:
#         l.append(item[::-1])
# print(l)


# l = ["python", "Selenium", "Japan"]
# dict = {}
# for item in l:
#     if len(item) % 2 == 0:
#         lis.append(item)
#     else:
#         lis.append(item[::-1])
#
# print(dict[item] = "even"})

### Wrtie a program to reverse inside the list if the element is of typr string or else keep it as it is.
#

# l = ["python", 10, 10.5, "Selenium", "Japan"]
# lis = []
# for item in l:
#     if isinstance(item, str):
#         lis.append(item[::-1])
#         # print(item[::-1])
#     else:
#         lis.append(item)
# print(lis)

# l = ["python", 10, 10.5, "Selenium", "Japan"]
# for item in l:
#     if isinstance(item, str):
#         l.append(item[::-1])
#         l.remove(item)
#         # print(item[::-1])
# print(l)

### Wrtie a program to to print the elements which are starting with vowel in list.

# files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]
#
# for item in files:
#     if item[0] in "aeiouAEIOU":
#         print(item)
#
### Wrtie a program to to print all the extensions in the follwing list.

# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
# lis = []
# i = 0
# for item in files:
#     lis.append(files[i].split("."))
#     print(lis[i][1])
#     i += 1

### Wrtie a program to print the file name if the file name is of odd name.

# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
# lis = []
# i = 0
# for item in files:
#     lis.append(files[i].split("."))
#     if len(lis[i]) % 2 != 0:
#         print(lis[i][0])
#     # else:
#     #     i += 1


# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
#
# for item in files:
#     a = item.split(".")
#     if len(a[0]) % 2 == 0:
#         pass
#     else:
#         print(a[0])

### Wrtie a program to return index of the first occurance of the given element.

# numbers = [10, 40, 20, 80, 20, 40, 30]
# num = 90
#
# for index, item in enumerate(numbers):
#     if item == num:
#         print(index)
#         break
# else:
#     print("element is not present")


# print(numbers.index(num))
# for item in numbers:
#     if num in
# i = 0
# if num in numbers:
#     print(num[i])


############## Prime Number ################## Prime Number ########################

# n = 9
# for i in range(2, n):
#     if n % i == 0:
#         print("not a prime number")
#         break
#
# else:
#     print("it is a prime number")

#### generate a prime number list from 0 to 10.

# for n in range(10):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         # print("not a prime number")
#         else:
#            print(n, end = ' ')

# for item in range(2, 2):

#
# for n in range(2,10):
#     for item in range(2, n):
#         if n % item == 0:
#             break
#     # print("not a prime number")
#     else:
#         print(n)

### Write a program to print all the elements other than the given element.

# numbers = [10, 40, 20, 80, 20, 40, 30]
# n = 20
#
# for num in numbers:
#     if n == num:
#         continue
#     print(num)

### Write a program to print all the palindrome in the given list.
#
# l = ["python", "dad", "hai", "malayalam", "madam", "non"]
# for item in l:
#     if item == item[::-1]:
#     # if item == reversed(item):   *********check why its not working
#         print(item)


#################### traversing through set ######################################################
#################### traversing through set ######################################################

## write a program to traverse trough set and print each element.

# set = {"python", "dad", "hai", "malayalam", "madam", "non"}
#
# for item in set:
#     print(item)

### Write a program to print all the palindrome in the given list.

# set = {"python", "dad", "hai", "malayalam", "madam", "non"}
#
# for item in set:
#     if item == item[::-1]:
#         print(item)

### Write a program to print elements in the set in reverse order.
#######we can not do as set is not sequence.

### Write a program to remove given element from set.
# set = {"python", "dad", "hai", "malayalam", "madam", "non"}
# ele = "hai"
# set.discard(ele)
# print(set)

# set = {"python", "dad", "hai", "malayalam", "madam", "non"}
# ele = "hai"
# for item in set:
#     if ele == item:
#         set.discard(item)
#         break
# print(set)

### Write a program to create a set with list elements if the element is palindrome.

# list1 = ["python", "dad", "hai", "malayalam", "madam", "non"]
# set1 = set()
#
# for item in list1:
#     if item == item[::-1]:
#         set1.add(item)
# print(set1)

# list1 = ["python", "dad", "hai", "malayalam", "madam", "non"]
# set1 = set()
#
# for item in list1:
#     if item == item[::-1]:
#         set1.update([item])
# print(set1)

#####Can you traverse through a multiple list at a time?==> yes using zip function

# s1 = "how"
# s2 = "are"
# s3 = "you"
# for item in zip(s1, s2, s3):
#     print(item)
#
# s1 = "how"
# s2 = "are"
# s3 = "you"
# for item1, item2, item3 in zip(s1, s2, s3):
#     print(item1, item2, item3, sep = "=>")

#
# s1 = "are"
# s2 = "you"
# s3 = "fine"
# for item in zip(s1, s2, s3):
#     print(item)
# (to avoid data loss we need to import zip_longest from intertools)

# from itertools import zip_longest
# #
# s1 = "are"
# s2 = "you"
# s3 = "fine"
# lis = []
# for item in zip_longest(s1, s2, s3):
#     lis.append(item)
# print(lis)

# for i in range (1, 1):
#     print(i)



#################### traversing through dictionary ######################################################
#################### traversing through dictionary ######################################################

### Wrtie a program to print keys in a dictionary

# d = {"a":1, "b":2, "c":3, "d":4, "e":5}
#
# print(d.items())
# print(d.keys())
# for key in d:
#     print(key, end = " ")

## d.keys()
# for key in d.keys():
#     print(key, end =" ")

# # using d.items()
# for key, value in d.items():
#     print(key, end =" ")

### Wrtie a program to print only the values from the dictionary

# d = {"a":1, "b":2, "c":3, "d":4, "e":5}

# # # using d.items()
# for item, values in d.items():
#     print(values, end = " ")

# # #using dictionay keys
# for values in d.keys():
#     print(d[values], end = " ")

# # using get()
# for value in d:
#     print(d.get(value), end = " ")
# #
# # #using d.values()
# for value in d.values():
#     print(value, end = " ")


### Wrtie a program to print the items in a  dictionary along with the indices

d = {"a":1, "b":2, "c":3, "d":4, "e":5}

# print(enumerate(d.items()))
# print(list(enumerate(d.items())))
#
# for item in enumerate(d):
#     print(item, end=" ")
# print()
# for keys, values in enumerate(d.items()):
#     print(keys, values, end = " ")
# print()
#
# for index, (keys, values) in enumerate(d.items()):
#     print(index, keys, values, end = " ")
# print()
# for keys, values in list(enumerate(d.items())):
#     print(keys, values, end = " ")

### Wrtie a program to create a dictionary with words and its count pair
# string = "hello world"
# d = {}
# for char in string:
#     d[char] = string.count(char)
# print(d)
#
# string = "hello world"
# s = set(string)
# # print(s)
# d = {}
# for char in s:
#     d[char] = string.count(char)
# print(d)

# string = "hello"
# d = {}
# for char in string:
#     i = 0
#     j = 0
#     if char[i]:
#         d[char[i]] = j+1
#         for d[char[i]] in d:
#             if d[char[i]] == 1:
#                 d[char[i]] == 2
#     i += 1
# print(d)

## (try working on above prog)

# string = "hello"
# d = {}
# for i in string:
#     count = 0
#     for j in string:
#         if i == j:
#             count += 1
#     d[i] = count
# print(d)


# string = "hello"
# d = {}
# for char in string:
#     if char not in d:
#         d[char] =1
#     else:
#         d[char] += 1
# print(d)


# string = "hello"
# d = {}
# for char in string:
#     d[char] += 1
# print(d)

## we can not get the count for charcters with above menthod, to acheive this we need to use defaultdict()
## from collection module

# from collections import defaultdict
# string = "hello"
# dd = defaultdict(int)  ##while creating default dictionary we need to secify the vaule datatype
# print(dd)
# for char in string:
#     dd[char] += 1
# print(dd)

## wtrite a program to create a dictionary with word and its count pair

# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
# i = 0
# k = 0
# for key in lis:
#     d[key] = lis.count(lis[i])
#     i += 1
# print(d)
#     if d[key[k]] == i+1:
#         d[key] = lis.count(lis[i])
# print(d)

### without using count()

# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
# for key in lis:
#     if key not in d:
#         d[key] = 1
#     else:
#         d[key] += 1
# print(d)


### using nested for loops (*********** work on it **********)

# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
#
# for key in lis:
#     count = 0
#     for key in d:
#         d[key] == count
#     count += 1
# print(d)

## using defaultdict

# from collections import defaultdict
#
# string = "Welcome to python and python is easy programming language"
# dd = defaultdict(int)
# lis = string.split()
# for key in lis:
#     dd[key] += 1
# print(dd)


## wtrite a program to create a dictionary with word and its length pair

# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
# i = 0
# for key in lis:
#     d[key] = len(key)
#     i += 1
# print(d)

#### without using inbult method len() ( ***** try again *******)

# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
# i = 0
# for key in lis:
#     if key not in d:
#         d[key]
#
# print(d)


## wtrite a program to create a dictionary with word and its length pair, only if the word is of even length

# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
# i = 0
# for key in lis:
#     if len(key) % 2 == 0:
#         d[key] = len(key)
#         i += 1
# print(d)

# from collections import defaultdict
#
# string = "Welcome to python and python is easy programming language"
# dd = defaultdict(int)
# lis = string.split()
# i = 0
# for key in lis:
#     if len(key) % 2 == 0:
#         d[key] +=
#
# print(d)

#### with word and its length pair only if the wrd is starting with vowel

# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
#
# for key in lis:
#     if key[0] in "aeiouAEIOU":
#         d[key] = len(key)
# print(d)

# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
#
# for key in lis:
#     if key[0] in "aeiouAEIOU":
#         i = 0
#         for char in key:
#             i +=1
#         d[key] = i
# print(d)

#### write a program to create a dictionary with word and its count only if the word is not repeated.

# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
# for key in lis:
#     if lis.count(key) == 1:
#         d[key] = 1
# print(d)


# using nested  (********** try again ***********)
# string = "Welcome to python and python is easy programming language"
# d = {}
# lis = string.split()
# for key in lis:
#     for key in d:
#         d.update(key = 1)
#     d[key] = 1
#
# print(d)

## write a program to reverse the values in a dictionary if the value is of type string.

# d = {"a":"hello", "b":100, "c":10.2, "d":"world"}
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
# print(d)

## write a program to get all the duplicates items and the number of times the item repeated in a list.

# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
# d= {}
# for key in names:
#     if names.count(key) > 1:
#         d[key] = names.count(key)
# print(d)

### try with set (** complete below program)
# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
# s = set{names}
# d= {}
# for key in names:
#     if names.count(key) > 1:
#         d[key] = names.count(key)
# print(d)

## write a program to get following output
# sentence = " hello world welcome to python programming hi there"
# o/p ==> {"h":["hello", "hi"], "w":["world", "welcome"], "t":["to", "there"],"p":["python", "programming"}

####( ***try on below prog*****)
# s = " hello world welcome to python programming hi there"
# lis = s.split()
# d = {}
# print(lis)
# i = 0
# l1 = list()
# for word in lis:
#     d[word[0]] = l1.append(word)
# print(d)
#
#
# s = "hello world welcome to python programming hi there"
# lis = s.split()
# d = {}
# for word in lis:
#     if word[0] not in d:
#         d[word[0]] = [word]
#     else:
#         d[word[0]] += [word]
# print(d)


from collections import defaultdict
#
# string = "hello world welcome to python programming hi there"
# dd = defaultdict(list)
# lis = string.split()
# for word in lis:
#         # dd[word[0]] += [word]
#         dd[word[0]].append(word)
# print(dict(dd))

## write a program to create dictionary with element and its index pair in the given list.

# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
# d = {}
# # a= enumerate(names)
# # print(list(a))
#
# for key, value in enumerate(names):
#     if value not in d:
#         d[value] = [key]
#     else:
#         d[value] += [key]
# print(d)

# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
# dd = defaultdict(list)
# # a= enumerate(names)
# # print(list(a))
#
# for key, value in enumerate(names):
#         dd[value] += [key]
# print(dd)

## write a program to flip key and values.
#
# d = {"a":"hello", "b":"hi", "c":"how", "d":"world"}
# d1 = {}
# for key in d:
#     value = d[key]
#     d1[value] = key
# print(d1)
#
# d = {"a":"hello", "b":"hi", "c":"how", "d":"world"}
# d1 = {}
# for key , value in d.items():
#     d1[value] = key
# print(d1)

# for i in range(1,):
#     print(i)

# for i in range(a):
#     print(i)


###########  29 jan 2022 ################################

#####write a program to print a tuple of character and its ascci value in a string.
#
# string = "python 1 2"
# lis = list()
# i = 0
# for char in string:
#     if "A" <= char <= "Z" or "a" <= char <="z" or "0" <= char <= "9":
#         lis.append((char, ord(char)))
#         i += 1
# print(lis)

# string = "python"
# lis = list()
# i = 0
# for char in string:
#     print((char,ord(char)))
#     i += 1


# string = "python"
# lis = list()
# i = 0
# for char in string:
#     lis.append((char,ord(char)))
#     i += 1
# print(tuple(lis))



#####write a program to check if given number is prime or not.

# num = 11
# for n in range(2, num):
#     if num % n == 0:
#         print("given number is not a prime number")
#         break
# else:
#     print("given number is a prime number")

#####write a program to print the sum of all the digits presents in the string.
#
# string = "python123"
# a = 0
# for item in string:
#     if item.isnumeric():
#         a += int(item)
# print(a)

#####write a program to print all the consonent in the string.

# string = "python12345"
# count = 0
# s1 = "aeiouAEIOU"
# for item in string:
#     # if string[i] not in s1 and string[i].isalpha():
#     if item not in s1 and item.isalpha():
#         print(item)
#         count += 1
# print(count)


#####write a program to print a tuple of index and the char in the string

# string = "python12345"
# t = ()
# for index, char in enumerate(string):
#     print((index, char), end = " " )
#
# string = "python12345"
# t = ()
# i = 0
# for index, char in enumerate(string):
#     j = (index, char)
#     print(j, end = " " )
#     i += 1
#
# string = "python12345"
# string = "hello" # we can't use this prog for thsi string
# i = 0
# for item in string:
#     print((string.index(item), item), end = " " )

#####write a program to reverse the string using 3 ways.

# string = "hello"
# print(string[::-1])
#
# string = "hello"
# for item in reversed(string):
#         print(item, end="")
#
# string = "hello"          #( try this again)
# for item in range(len(string)):
#     print(string.rfind(item))


#####write a program to extract only specail character from a string.

# string = r"hello \\n12@*"
# for item in string:
#     if not "a" <= item <= "z" and not "A" <= item <= "Z"
#         print(item, end="")


# string = r"hello \\n12@*"
# for item in string:
#     if not item.isalnum() and not item.isspace():
#         print(item, end="")

#####write a program to check if the given character is present in  a string, if char is present,
# return its index.

# string = "helolo"
# char = "l"
# for index, value in enumerate(string):
#     if char == value:
#         print(char, index, sep = "==>")
#
# string = "hellolol"
# char = "l"
# count = 0
# for item in string:
#     if char == item:
#         i = string.index(item)
#         print(char, i+count, sep="==>")
#         count += 1

### speed ticket

# speed = int(input("enter the speed : "))
# q = input("is it your birthday? : yes or no? ")
# a = "zero ticket"   #(0 to 64)
# b = "small ticket"   #(65 to 75)
# c = "big ticket"     #(more than 75)
# if q.lower() != "yes":
#     if 0 <= speed < 60:
#         print(a)
#     elif 60 <= speed < 75:
#         print(b)
#     else:
#         print(c)
# else:
#     if 0 <= speed < 65:
#         print(a)
#     elif 65 <= speed < 80:
#         print(b)
#     else:
#         print(c)

# speed = int(input("enter the speed : "))
# q = input("is it your birthday? : yes or no? ")
# a = "zero ticket"   #(0 to 60)
# b = "small ticket"   #(61 to 75)
# c = "big ticket"     #(more than 75)
# if q.lower() != "yes":
#     for speed in range(61):
#         print(a)
#         break
#     for speed in range(61, 76):
#         print(b)
#         break
#     for speed in range(76, 200):
#         print(c)
#         break
# else:
#     for speed in range(66):
#         print(a)
#         break
#     for speed in range(66, 81):
#         print(b)
#         break
#     for speed in range(81, 200):
#         print(c)
#         break


### given two integers a and b, print True if one of them is 10
# or if there sum is 10.

# a = 15
# b = 15
# # print("true" if a == 10 or b == 10 or (a+b) == 10 else "False")
#
# print(bool(a) or bool(b) or bool(a+b))

### given an itegers n, print True if it is within range of 10 of 100 or 200

# a = 200
# b = list(range(90,111))
# c = list(range(190,211))
# for item in b or c:
#     if a in b or c:
#         print("True")
#         break
# print(bool(a in range(90,111)) or bool(a in range(190,211)))

### given two integer values, print True if one is negative an one is postive. Except if the parameter
# negative is true, then print True only if both are negative

# -1, 1, False ===> True
# 1, -1, False ===> True
# -1, -1, False==> False
# -4, -5, True ==> True
# a = 2
# b = -3
# par = False
#
# if par is True:
#     print("True" if a < 0 and b < 0 else "False")
# else:
#     print("True" if  a < 0 and b > 0  or b < 0 and a > 0 else "False")


# string = "11 22 33 44"
# i = 0
# for item in string:
#     if string[i] != " ":
#         # lis[(i-1)] += item
#         i += 1
#         pass
#     else:
#         i += 1
# print(string[0: i])




