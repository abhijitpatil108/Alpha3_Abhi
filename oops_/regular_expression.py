import re

'''Find all the word which ends with o'''
# sentence = "Hello hi world hello how are you ohio"
# res = re.findall(r"\b\w+o\b", sentence)
# print(res)

'''WAP to count the number of occurrences of non special characters'''

# sentence = "hello@world! welcome!!! Python$ hi how are you & where are you"
# res = set(re.findall(r"\w", sentence))
# d = {char:sentence.count(char) for char in res}
# print(d)

'''filter out all the characters except digits and give new string'''

# word = "Hello124&dhddi%bfnf"
# print("".join(re.findall(r"[^\d]", word)))
# print("".join(re.findall(r"\D", word)))
# # res = re.findall(r"\D", word)
# # print(res)
# # s = "".join(res)
# # print(s)

'''Count the characters in each word but ignore special characters'''
# sentence = "hi there! How are you:) How are you doing today"
# res = re.findall(r"\b\w+\b", sentence)
# d = {word:len(word) for word in res}
# print(d)

# res = re.findall(r"\w+", sentence)
# print(res)
# d = {word:len(word) for word in res}
# print(d)

'''count the uppercase and lowercase characters'''

sentence = "Hello World Welcome To Python"

# lower = sum([1 for item in re.findall(r"[a-z]", sentence)])
# # upper = sum([1 for item in re.findall(r"[A-Z]", sentence)])
# upper = len(sentence)-lower-sentence.count(" ")
#
# print(f"number of lowercase characters are {lower}")
# print(f"number of uppercase characters are {upper}")

# print(f"number of lowercase characters are {sum(lower)}")
# print(f"number of uppercase characters are {sum(upper)}")

'''find all the extension of the file present in below string'''

download_message ="""
Downloading file archive.zip to download folder
Downloading file image.jpeg to download folder
Downloading file index.html to download folder
Downloading file python.py to download folder
"""
# res = re.findall("\.\w+", download_message)
# print(res)

'''creating accroname out of list of string'''


'''find the phone number which are valid using pattern'''
# phone_numbers = ['1','108-786-1008', '234-345-34', '2345-345-456', '234-1234-234', '786-108-1008', '123-456-7899']
# numbers = " ".join(phone_numbers)
# res = re.findall(r"\d{3}-\d{3}-\d{4}", numbers)
# print(f"Valid phone numbers are {res}")

# res = []
# for item in phone_numbers:
#     res += re.findall(r"\d{3}-\d{3}-\d{4}", item)
#
# print(res)
#
# for item in phone_numbers:
#     if item in res:
#         print(item)
#     else:
#         print(f"{item} is not valid number")

'''find all the words starting with vowels'''
# message = "The ongoing course is python language in Evolve institution digital university"
# print(re.findall(r"\b[aeiou]\w+", message, re.IGNORECASE))

'''find all the 3 letter words'''
# message = "You are learning the python language in Evolve institution digital university"
# print(re.findall(r"\b\w{3}\b", message))

''' input roman output numbers '''

# I,V,X,L,C,D,M = [1,5,10,50,100,500,1000]
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
given = "MM" #MM VIII
res = 0

# while len(given) > 0:
#     if len(given) == 1:
#         res += d[given[0]]
#         given = given.replace(given[0], "")
#     elif d[given[0]] < d[given[1]]:
#         res += (d[given[1]] - d[given[0]])
#         given = given.replace((given[0] + given[1]), "")
#     elif d[given[0]] >= d[given[1]]:
#         res += (d[given[1]]+d[given[0]])
#         given = given.replace((given[0] + given[1]), "")
#

# while len(given) > 0:
#     if len(given) == 1:
#         res += d[given[0]]
#         given = given.replace(given[0], "")
#     elif d[given[0]] < d[given[1]]:
#         res += (d[given[1]] - d[given[0]])
#         given = given.replace((given[0] + given[1]), "")
#     elif d[given[0]] >= d[given[1]]:
#         res += (d[given[1]]+d[given[0]])
#         given = given.replace((given[0] + given[1]), "")

print(res)


# number = 'A'+'AA'+'AAA'+

# I, II, III, IV, V, VI, VII, VIII, IX, X,L,C,D,M  = [1,2,3,4,5,6,7,8,9,10,50,100,500,1000]
# res = 'IX'
#
# print(d[res])

# print(sum('LXXVIII'))