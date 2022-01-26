# # # ## write a program to print greatest of 3 numbers
# # print("write a program to print greatest of 3 numbers")
# #
# # s1 = int(input(" enter number 1 : "))
# # s2 = int(input(" enter number 2 : "))
# # s3 = int(input(" enter number 3 : "))
# #
# # s = [s1, s2, s3]
# # print(max(s))
# #
# # s.sort()
# # print(s[-1])
# #
# # print(s1 if s1 > s2 and s1 > s3 else s2 if s2 > s3 else s3)
# #
# # ##########################################################################
# #
# # # Write a program to check if the entered character is a vowel or not, if the char is a vowel,
# # # create a dictionary with char as key and ASCII value of the char as value
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
# # s = input("enter a character : ")
# # s1 = "aeiouAEIOU"
# # if s.isalpha() and s in s1:
# #     print(f"{s} is a Vowel")
# #     print(dict({s: ord(s)}))
# # elif s.isalpha() and s not in s1:
# #     print(f"{s} is not a Vowel")
# # elif s and s.isspace() is False and s.isalpha() is False:
# #     print("VIP characters and Numbers are not allowed in this program")
# # elif bool(s) is False:
# #     print("No character was entered")
# # elif s.isspace():
# #     print("Don't give some space :)")
#
# ################################################
#
# char = "a"
# d = {}
# if char.lower() in "aeiou":
#     d[char] = ord(char)
#     print(d)
#
# #  Write a program to check if the marks given falls under following categories and print the results based on marks
# # if marks < 35 print fail
# # if 35 < marks < 60 print secondclass
# # if 60 < marks < 75 print FirstClass
# # if marks>75 print distinction
#
#marks = int(input("Enter the marks : ")


## # Write a program to print 10 to 1
#
# n = 10
# while n > 0:
#     print(n)
#     n -= 1
#
#
# ### Write a program to print -1 to -10# Write a program to print -1 to -10
#
# n = -1
# while n >= -10:
#     print(n)
#     n -= 1

### Write a program to print -1 to -10# Write a program to print -1 to -10

# n = -10
# while n < 0:
#     print(n)
#     n += 1

### Write a program to print even numbers from 1 to 50

# n = 1
# while n <= 50:
#     if n % 2 == 0:
#         print(n)
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
#
# while set(s):
#       print(s.pop())
#
# s = {"hi", 6, 8.5, 9, "ho"}
#
# while set(s):
#       print(s.pop())

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
#     print(item, s[item], sep="->")


# s = "hello"
# a = enumerate(s)

# print(list(a))

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
#
#     # print(item[0], item[1])


# l1 = {9, 5, 4, 1, 6, 8, 1, 10}
# n1, n2, *rest = l1
# print(n1, n2, rest)

# l1 = (9, 5, 4, 1, 6, 8, 1, 10)
# n1, n2, *rest = l1
# print(n1, n2, rest)

## write a prog to traverse trough in reverse order

# s = "python"
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


string = "python2we34lcome"
i = 0
for ele in string:
    if "0" <= ele <= "9":
        i += 1
print(i)

### Assignment : write a program to count the number of special characters in the string.

### Assignment : write a program to count capitel letters and small letters in the string.




