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

#################### 27 Jan 2022 #############################################################
###############################################################################################
# #  Write a program to check if the marks given falls under following categories and print the results based on marks
# # if marks < 35 print fail
# # if 35 < marks < 60 print second class
# # if 60 < marks < 75 print First Class
# # if marks>75 print distinction
###############################################################################################

# marks = int(input("Enter your marks : "))
#
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
# string = input(r"enter a string with special characters : ")
# i = 0
# # j = 0
# for item in string:
#     if item.isalnum():
#         i += 1
# print((len(string))-i)
# #     else:
# #         j += 1
# # print(j)

###############################################################################################
### Assignment : write a program to count capitel letters and small letters in the string.
###############################################################################################

# string = input(r"enter a string with special characters : ")
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

string = "ABHI_patil1234"
# string = input(r"enter a string with special characters : ")
small = 0
capital = 0
for item in string:
    if item.islower():
        small += 1
    elif item.isupper():
        capital += 1
print("Number of small Characters : ", (small))
print("Number of Capital Characters : ", (capital))
