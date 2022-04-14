## WAP to create a list of sqaures for the elements in the below list

# l = [1, 2, 3, 4, 5]
#
# lis = []
# i = 0
# for item in l:
#     lis.append(l[i]*l[i])
#     i += 1
# print(lis)

### The better way is below

# l = [1, 2, 3, 4, 5]
#
# lis = []
# for item in l:
#     lis.append(item ** 2)
# print(lis)


################################ Comprehension  #############################################
################################ list Comprehension  #############################################
################################ list Comprehension  #############################################

### we can not use loop control statements inside the comprehension

# l = [1, 2, 3, 4, 5]
#
# lis = [ item** 2 for item in l]
# print(lis)


### WAP to create a list of tuples which is having index and its cooorespoding item.

# l = ["python", 10, 3.2, "selenium", "java"]
# # lis = [ (index, item) for index, item in enumerate(l)]
# lis = [ item for item in enumerate(l)]
# print(lis)
#
# l = ["python", 10, 3.2, "selenium", "java"]
# lis = []
# for item in enumerate(l):
#     # lis.append((index, item))
#     lis.append(item)
# print(lis)

# l = {"python", 10, 3.2, "selenium", "java"}
# # lis = [ (index, item) for index, item in enumerate(l)]
# l.pop(item for item in l)
# print(lis)


### WAP to create a list of even numbers from the below list

# l = ["python", 10, 3.2, "selenium", "java"]
#
# l = list(range(11))
# lis = []
# for item in l:
#     if item % 2 == 0:
#         lis.append(item)
# print(lis)
#
# l = list(range(11))
# lis = [item for item in l if (item % 2 == 0)]
# print(lis)

# l = list(range(11))
# lis = []
# lis1 = []
# for item in l:
#     if item % 2 == 0:
#         lis.append(item)
#     else:
#         lis1.append(item)
# print(lis)
# print(lis1)

# l = list(range(11))
# even = [item for item in l if (item % 2 == 0)]
# odd = [item for item in l if (item % 2 != 0)]
# print(even)
# print(odd)

### WAP to create a list using the following list if the word is of even length, store the word as it is.
## if it is of odd length , reverse the word and store it.

# l = ["python", "Node 35", "selenium", "java"]
# lis = []
# for item in l:
#     if len(item) % 2 == 0:
#         lis.append(item)
#     else:
#         lis.append(item[::-1])
# print(lis)
#
# l = ["python", "Node 35", "selenium", "java"]
# lis = [item if (len(item) % 2 == 0) else (item[::-1]) for item in l]
# print(lis)

## WAP to create a list from the following list if the elements are of type string, reverse it
## else keep them as it is

# l = ["java", "python", 10, True, 1.4, "c++", "ruby"]
# lis = [item[::-1] if isinstance(item, str) else item for item in l]
# print(lis)

## WAP to create a list from the following list if the elements are of type string, keep them as it is
## else reverse it

# l = ["java", "python", 10, True, 1.4, "c++", "ruby"]
# lis = [str(item)[::-1] if not isinstance(item, str) else item for item in l]
# print(lis)

## Write a list comprehension to create a list with a string staring with vowels.

# l = ["amazon", "flipkart", "walmart", "gmail", "yahoo"]
# vowels = [item for item in l if item[0] in "aeiouAEIOU"]
# print(vowels)

#Asssignment
#converting all list for loop programs using list comprehension
###################################################################

################################ set Comprehension  #############################################
################################ set Comprehension  #############################################

#write a set comprehension to create a set of squares from 1 to 10

# s = [(item ** 2) for item in range(1, 11)] ## creating a list
# print(s)
#
# s = {(item ** 2) for item in range(1, 11)} ## creating a set
# print(s)

#write a set comprehension to create a set of tuples index and the item

# s = {(item) for item in enumerate(range(11))}
# print(s)
#
# l = ["amazon", "flipkart", "walmart", "gmail", "yahoo"]
# s = {(item, l[item]) for item in range(len(l))}
# print(s)
#
# s = {(index, item) for index, item in enumerate(l)}
# print(s)
#
# s = {item for item in enumerate(l)}
# print(s)

#write a set comprehension to create a set of tuples with item and its length pair

# se = {"amazon", "flipkart", "walmart", "gmail", "yahoo"}
# s = {(item, len(item)) for item in se}
# print(s)

#############################################################################################
############## Re-write all lsit programs using comprehension ################################


## 1) Wrtie a program to print index and its corresponding element.

# l = ["python", 10, 3.2, "Selenium", "Japan"]
# lis = []
# for item in range(len(l)):
#     lis.append((item, l[item]))
# print(lis)
#
# ##using comprehension
# l = ["python", 10, 3.2, "Selenium", "Japan"]
# lis = [item for item in enumerate(l)]
# print(lis)

### 2) Wrtie a program to print elements in the list in reverse order

# l = ["python", 10, 3.2, "Selenium", "Japan"]
# lis = []
# for item in reversed(l):
#     lis.append(item)
# print(lis)
#
# # ##using comprehension
# l = ["python", 10, 3.2, "Selenium", "Japan"]
# lis = [item for item in reversed(l)]
# print(lis)

## 3) Wrtie a program to print alternate elements in the list

# l = ["python", 10, 3.2, "Selenium", "Japan"]
#
# for item in l[::2]:
#     print(item, end = " ")
# print()
#
# # # ##using comprehension
# l = ["python", 10, 3.2, "Selenium", "Japan"]
# lis = [item for item in l[::2]]
# print(lis)

### 4) Wrtie a program to print only integers present in the list

# l = ["python", 10, 3.2, True, "Selenium", "Japan"]
# for item in l:
#     if isinstance(item, int):
#         print(item)
#
# # # # ##using comprehension
# l = ["python", 10, 3.2, True, "Selenium", "Japan"]
# lis = [item for item in l if type(item) is int]
# print(lis)

## 5) Wrtie a program to print the string which are of even length in the list
#
# l = ["python", 10, 3.2, True, "Selenium", "Japan"]
# lis =[]
# for item in l:
#     if isinstance(item, str) and len(item) % 2 == 0:
#         lis.append(item)
# print(lis)
# #
# # ## using comprehension
# l = ["python", 10, 3.2, True, "Selenium", "Japan"]
# lis = [item for item in l if isinstance(item, str) and len(item) % 2 == 0]
# print(lis)

### 6) Wrtie a program to print the elements in the list if element is of even length print as it
## and if of odd length then reverse and print
#
# l = ["python", 10, 3.2, True, "Selenium", "Japan"]
# lis =[]
# for item in l:
#     if isinstance(item, str) and len(item) % 2 == 0 or not isinstance(item, str):
#         lis.append(item)
#     else:
#         lis.append(item[::-1])
# print(lis)
#
# l = ["python", 10, 3.2, True, "Selenium", "Japan"]
# lis = [item if isinstance(item, str) and len(item) % 2 == 0 or not isinstance(item, str) else item[::-1] for item in l]
# print(lis)


### 7) Wrtie a program to reverse inside the list if the element is of typr string or else keep it as it is.
#
#
# l = ["python", 10, 10.5, "Selenium", "Japan"]
# lis = []
# for item in l:
#     if isinstance(item, str):
#         lis.append(item[::-1])
#     else:
#         lis.append(item)
# print(lis)
#
# ##Using comprehension
#
# l = ["python", 10, 10.5, "Selenium", "Japan"]
# lis = [item[::-1] if isinstance(item, str) else item for item in l]
# print(lis)

### 8) Wrtie a program to to print the elements which are starting with vowel in list.

# files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]
# lis = []
# for item in files:
#     if item[0] in "aeiouAEIOU":
#         lis.append(item)
# print(lis)
#
# ## Using comprehension
#
# l = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]
# vowel = [item for item in l if item[0].lower() in "aeiou"]
# print(vowel)

### 9) Wrtie a program to to print all the extensions in the follwing list.

# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
# # a = files[0].split(".")
# # print(a[1])
# ext = []
# for item in files:
#     # a = item.split(".")
#     ext.append(item.split(".")[1])
#     # ext.append(ext[item][1])
# print(ext)
#
# ### using comprehension
# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
# ext = [item.split(".")[1] for item in files]
# print(ext)

### 10) Wrtie a program to print the file name if the file name is of odd name.

# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
# lis = []
# for item in files:
#     if len(item.split(".")[0]) % 2 != 0:
#         lis.append(item.split(".")[0])
# print(lis)
#
#
# ### using comprehension
# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
# odd = [item.split(".")[0] for item in files if len(item.split(".")[0]) % 2 != 0]
# print(odd)

##############################################################################################
############################# Dictionary comprehension ########################################
## IMP in dictionary you can not use loop control statements and also assignment operator


#### WAP to create a dictionary with item and its index pair

# string = "hello"
# d = {}
# for item in enumerate(string):
#     d[item] = index
# print(d)

##using comprehension
# string = "hello"
# d = {index: item for index, item in enumerate(string)}
# print(d)

#### WAP to create a dictionary with word and its length pair

# string = "hello welcome to python"
# s = string.split()
# d = {}
# for index, item in enumerate(s):
#     d[item] = len(item)
# print(d)
#
# ## using comprehension
#
# string = "hello welcome to python"
# s = string.split()
# d = {item: len(item) for index, item in enumerate(s)}
# print(d)


#### WAP to create a dictionary with character  and its count pair

# string = "hello"
# s = set(string)
# d = {char: string.count(char) for char in s}
#
# print(d)
# d = {}
# for item in s:
#     d[item] = s.count(item)
# print(d)

##(try below again)
# i = 1
# for item in s:
#     d[item] = i
#     if d[item] == item:
#         d[item] = i + 1
# print(d)

# ###Using comprehension
# d = {item: string.count(item) for item in s}
# print(d)

#### WAP to create a dictionary of words and its count

# string = "python java selenium python selenium"
# s = string.split()
# d = {word: s.count(word) for word in s}
# print(d)

# string = "python java selenium python selenium"
# s = string.split()
# d = {}
# i = 1
# for word in s:
#     d[word] = 1
#     if word in d:  ### try again###############
#         d[word] = i+1
# print(d)

### WAP to create a dictionary of word and its count pair only if the word is of even length

# string = "python java selenium python selenium c"
# s = string.split()
# d = {word: s.count(word) for word in s if len(word) % 2 == 0}
# print(d)
#
# string = "python java selenium python selenium c"
# s = string.split()
# d = {}
# for word in s:
#     if len(word) % 2 == 0:
#         d[word] = s.count(word)
# print(d)

#### WAP to create a dictionary with index and word pair if the word is of odd length, reverse it else
## keep it as it is

# string = "welcome to python its an easy language"
# words = string.split()
# d = {index: word if len(word) % 2 == 0 else word[::-1] for index, word in enumerate(words)}
# print(d)

### comprehension method drawback==> to use comprehensin for creating dictionary the key shuld be same for
## for different values. ( you can refer above program for the same.

# string = "welcome to python its an easy language"
# words = string.split()
# d = {}
# for index, word in enumerate(words):
#     if len(word) % 2 == 0:
#         d[index] = word
#     else:
#         d[index] = word[::-1]
# print(d)


#### WAP to create a dictionary with word and its length pair only if the word is staring with vowel.
#
# string = "welcome to python its an easy language"
# words = string.split()
# d = {word: len(word) for word in words if word[0].lower() in "aeiou"}
# print(d)
#
# string = "welcome to python its an easy language"
# words = string.split()
# d = {}
# for word in words:
#     if word[0].lower() in "aeiou":
#         d[word] = len(word)
# print(d)

#### WAP to create a dictionary of item and its index pair if the item is of string datatype, reverse it
#

# lis = ["hi", 10, 3.5, "python", (1, 2)]
# d = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(lis)}
# print(d)

#### WAP to create a dictionary with index and word pair, if word is of type string, keep it as it is else reverse

# lis = ["hi", 10, 3.5, "python", (1, 2), True]
# d = {index: str(item)[::-1] if not isinstance(item, str) else item for index, item in enumerate(lis)}
# print(d)

#### WAP to to flip keys and values in a dictionary

# d = {'a': 1,'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# d1 = {value: key for key, value in d.items()}
# print(d1)

# # d1 = {values: item for item, values in d.items()}
# d1 = {d[key]: key for key in d}
# print(d1)


#### WAP to create a dictionar of character and its ascii value pair

# string = "hello"
# d = {char: ord(char) for char in string}
# d = {ord(char): char for char in string}
# print(d)

# s1 = "jan feb march"
# s1l = s1.split()
# s2 = "01 02 03"
# s2l = s2.split()
#
# for item in zip(s1l, s2l):
#     print(item)
#
# s = [item for item in zip(s1l, s2l)]
# print(s)


""" index of first occurrence of the given element in the list"""

# numbers = [10, 40, 20, 80, 20, 40, 30]
# num = 20
# # print(enumerate(numbers))
# # print(list(enumerate(numbers)))
#
# for index, item in enumerate(numbers):
#     if item == num:
#         print(f"index of first occurrence of {num} is {index}")
#         break


# s = [item[0] for item in enumerate(numbers) if item[1] == num]

# s = [item( for item in list(enumerate(numbers)) if item[1] == num]
# print(f"index of first occurrence of {num} is {s}")

# s = "hello"
# print(enumerate(s))
# for index, item in enumerate(s):
#
#     print(index, end =" ")

# t = (1, 2, 3, 3, 4, 3, 5)
# num = 3
# lis = list(enumerate(t))
# print(lis)
# lis1 = list(reversed(lis))
# for index, item in lis1:
#     if item == num:
#         print(f"index of last occurrence of {num} is {index}")
#         break


# prime = []
# for num in range(1,100):
#     for n in range(2,num):
#         if num % n == 0:
#             break
#     else:
#         prime.append(num)
#
# print(prime)
# print("hello")

from collections import defaultdict
""" element and its indices pair """
# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
#
# dd = defaultdict(list)
#
# for index, name in enumerate(names):
#     dd[name] += [index]
#
# print(dict(dd))

""" flip key and value """

# d = {"a": 1, "b": 2, "c": 3}
#
# dd = {}
# for key, values in d.items():
#     dd[values] = key
# print(dd)
