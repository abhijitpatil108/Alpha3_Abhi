# # # Q ) Write a program to check given string starting with vowel or not.
# #
# s = input("string : ")
# l = "aeiouAEIOU"
# if l.rfind(s[0]) != -1:
#     print(f"{s} is staring with Vowel")
# else:
#     print(f"{s} is not staring with Vowel")
#
# #
# s = input("string : ")
# l = "aeiouAEIOU"
# if s[0] in l:
#     print(f"{s} is staring with Vowel")
# else:
#     print(f"{s} is not staring with Vowel")
# #
# # # Q ) Write a program to check given string ending with vowel or not.
# s = input("string : ")
# l = "aeiouAEIOU"
# if s[-1] in l:
#     print(f"{s} is ending with Vowel")
# else:
#     print(f"{s} is not ending with Vowel")
# #
# s = input("string : ")
# l = "aeiouAEIOU"
# if l.rfind(s[-1]) != -1:
#     print(f"{s} is ending with Vowel")
# else:
#     print(f"{s} is not ending with Vowel")
#
#  # Q ) check if the string is palindrome or not
#
# string = input("enter a string : ")
# string.lower()
# if string == string[::-1]:
#      print(f"{string} is palindrome")
# else:
#      print(f"{string} is not palindrome")
#
# #Wrtie a program to check if the integer is palindrom or not
#
# s = input("enter a number: ")
# str(s)
# if s == s[::-1]:
#      print(f"{s} is palindrome")
# else:
#      print(f"{s} is not palindrome")
#
# s = input("enter an input : ")
# str(s)
#
# if s.lower() == s.lower()[::-1]:
#      print(f"{s} is palindrome")
#
# else:
#      print(f"{s} is not palindrome")

# s = input("enter an input : ")
# str(s)
#
# print(f"{s} is palindrome" if s.lower() == s.lower()[::-1] else f"{s} is not palindrome")
# input()

# Write a program to check if the iterable has even number of elements.
#
# s = {10, 20, 30, 40}
#
# if len(s) % 2 == 0:
#     print(f"{s} has even number of elements")
# else:
#     print(f"{s} has odd number of elements")

# write a program to check if the first digit in the given number is even or odd

# s = input("enter a number : ")
# t = str(s)
#
# if int((t[0])) % 2 == 0:
#     print(f"first digit of {s}  even number")
# else:
#     print(f"first digit of {s}  odd number")
# #
# s = str(input("enter a number : "))
#
# if int((s[0])) % 2 == 0:
#     print(f"first digit of {s}  even number")
# else:
#     print(f"first digit of {s}  odd number")

# Using in-line if else
# s = str(input("enter a number : "))
#
# print(f"first digit of {s}  even number" if int((s[0])) % 2 == 0 else f"first digit of {s}  odd number")

# write a program to print greatest of 3 numbers

# s1 = input("enter 3 numbers : ")
# s = [int(s1[0]), int(s1[1]), int(s1[2])]
# s.sort()

# s = [11, 22, 20]
# print(max(s))

# s1 = input("enter 3 numbers : ")
# s = [int(s1[0]), int(s1[1]), int(s1[2])]
# print(max(s))

# s1 = int(input(" enter number 1 : "))
# s2 = int(input(" enter number 2 : "))
# s3 = int(input(" enter number 3 : "))
#
# s = [s1, s2, s3]
# s.sort()
# print(s[-1])
# max(s)

# s1 = int(input(" enter number 1 : "))
# s2 = int(input(" enter number 2 : "))
# s3 = int(input(" enter number 3 : "))
#
# print(max(s1, s2, s3))

# s1 = int(input(" enter number 1 : "))
# s2 = int(input(" enter number 2 : "))
# s3 = int(input(" enter number 3 : "))

# if s1 > s2 and s1 > s3:
#     print(s1)
# elif s2 > s3:
#     print(s2)
# else:
#     print(s3)

# print(s1 if s1 > s2 and s1 > s3 else s2 if s2 > s3 else s3)
#
#
# s1 = list(input("enter 3 numbers : "))
# s = [int(s1[0]), int(s1[1]), int(s1[2])]
# print(max(s))
#
# print(s[-1])
# print(s)

# s = list(input("Enter 3 numbers : "))
# s1 = int(s)
# #s.sort(reverse=True)
# s1.sort()
# print(s1[-1])


# write a program to check if the entered character is vowel or not, if the char is an vowel,
# create a dictionary with char as key and ASCCI value of the char as value

s = input("enter a character : ")
s1 = "aeiouAEIOU"
if s1.rfind(s) == -1:
    print(f"{s} is no an Vowel")
else:
    print(dict({s: ord(s)}))

