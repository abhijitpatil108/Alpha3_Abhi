''' r"." will match each and anything and everything inside the string except new line.
But it must be used as raw string '''
import re


# greeting = "Hello world welcome to the regular expression in python hello \toword regular expression"
#
# res1 = re.findall(".",greeting)
# res2 = re.findall(r".",greeting)
# print(res1)
# print(res2)
# word = "andnshioddnvba"
# res = re.findall(r".*a", word)
# # res = re.findall(r"a*", word)
# print(res)

'''find out al words starts with h or H'''
# sentence = "Hello world hi how are a h$ you"
# res1 = re.findall(r"\bh\S*\b",sentence,re.IGNORECASE)  # ['Hello', 'hi', 'how', 'h']
# res2 = re.findall(r"\bh\S+\b",sentence,re.IGNORECASE)    # ['Hello', 'hi', 'how']
# res3 = re.findall(r"\bh\S*",sentence,re.IGNORECASE)   # ['Hello', 'hi', 'how', 'h$']
# print(res1)
# print(res2)
# print(res3)

# check = "hi $123 hello $24 check"
# # res = re.findall(r"[$]", check)
# res = re.findall(r"[$]\d+", check)   # ['$123', '$24']
# # res = re.findall(r"$\d+", check)   # []
# print(res)

'''find out only special characters'''

# sentence = "Hi good morning $  python@3.8 selenium_webdriver"
# res = re.findall(r"[]", sentence)
# print(res)

