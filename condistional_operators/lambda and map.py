
#######################################################################################################
'''                   lambda function                              '''
#######################################################################################################

'''WLF to check if the given number is even or not'''
# l = [1, 2, 3, 4]
# #
# even = lambda a,b,c,d: a % 2 == 0
# even_lis = lambda a: a % 2 == 0
# even_ = lambda a: f"{a} is even" if a % 2 == 0 else f"{a} is odd"
# print(list(map(even_lis, l)))
# print(list(map(even_, l)))
#
# print(list(map(lambda a: f"{a} is even" if a % 2 == 0 else f"{a} is odd", l)))


# even_ = lambda n: n % 2 == 0
# add_ = lambda n: n+n
#
# print(even_(5))
# print(add_(5))

'''WLF that multiplies two numbers'''

# multi = lambda a, b: a*b
# print(multi(4, 5))

'''WLF that returns last elements of the sequence'''

# def ls(*a):
#     return a[-1],a[0]
#
# res = ls([1,2,3], (1,2))
# print(res)
#
# last_ = lambda *a: a[-1]
# print(last_([1,2,3], (1,2)))
# #
# # last = lambda a: a[-1]
# # print(last("hello"))
#
# last = lambda a, b: (a,b)[0]
# print(last("hello", [1,2,3,4]))

'''WLF that checks if the given string is palindrome or not'''

# ch_pal = lambda a:f"{a} is palindrome" if a == a[::-1] else f"{a} is not palindrome"
# print(ch_pal("mom"))

# ch = lambda a: f"{a} is palindrome" if a[::-1] == a else f"{a} is not a palindrome"
# print(ch("sis"))
#
# ch = lambda a: a[::-1] == a
# print(ch("sis"))
# print(ch("python"))

# check = lambda a: f"{a} is a palindrome" if (a == a[::-1]) else f"{a} is not a palindrome"
# print(check("mom"))

'''WLF that checks whether the number is even or odd and print the number in both the case'''

# even_odd = lambda num: f"{num} is a even number" if num % 2 == 0 else f"{num} is a odd number"
# print(even_odd(4))

#######################################################################################################
'''                   map function                              '''
#######################################################################################################

# list_ = ["hello", "mom", "dad", "hai"]

# print(list(map(lambda word: word == word[::-1],list_)))
# print(list(map(lambda word: f"{word} is palindrome" if word == word[::-1] else f"{word} is not a palindrome",list_)))

# check = lambda a: f"{a} is a palindrome" if (a == a[::-1]) else f"{a} is not a palindrome"
# check1 = lambda a: a == a[::-1]
# print(list(map(check1,list_)))
# print(list(map(check, list_)))

'''WMF that checks if the given list of numbers are even or odd'''
#
# list1 = [1,2,3,4,5]
# list2 = [10,11,12,13,14]

# print(list(map(lambda num1, num2: num1+num2, list1, list2)))
# print(list(map(lambda num :f"{num}: even" if num % 2 == 0 else f"{num}: odd", [*list1, *list2])))


# even_odd = lambda num : f"{num} is even" if num % 2 ==


# even_odd = lambda num, num1 : f"{num} is a even number" if num % 2 == 0 else f"{num} is a odd number"
# print(list(map(even_odd, list1, list2)))

'''WAP to return the strings which are starting with vowels'''


# words_ =["python", "and", 'its', "easy", "language"]
# print(list(filter(lambda word:word[0].lower() in "aeiou", words_))) #filter
#
# print(list(filter(None ,(1,2,0,True, 0.0)))) #filter


# print(list(map(lambda word:word if word[0].lower() in "aeiou" else f"{word} not starting with vowel", words_)))
# # vowel_word = lambda word: word if word[0].lower() in "aeiou" else f"{word} not starting with vowel"
# # print(list(map(vowel_word, words_)))
# # print(list(filter(lambda word:word[0].lower() in "aeiou", words_)))
# print(list(filter(None ,(1,2,0,True, 0.0))))


'''for using only if condition, we can use filter IPO map'''

'''assignments'''
''' ######## 7th feb 2022 ########## '''
'''map1) wap to convert all the string in the list to upper case using map'''
#
# sentence = "Hello world"
#
# print(list(map(str.upper, sentence.split()))) #we can directly pass inbuilt function


'''map2) to convert all the negative numbers in the list to positive number '''

# lis = [-1, 2, -3, 4, -5, 5, 5]
# print(list(map(lambda num: abs(num), lis)))

'''map3) WAP that returns the list of numbers raised to the power of their indies using map '''

# l = [2, 4, 6, 8]
# res = map(lambda item: item[0] ** item[1], enumerate(l))
# print(list(res))

# def func(item):
#     return item[1]**item[0]
#
# res = map(func, enumerate(l))
# print(list(res))




'''map4) WAP that returns all the words in lower case in the given sentence'''





'''map5) WAP to get list of lengths of each word'''

# sentence = "Welcome to python"
# print(list(map(len,sentence.split())))
# res = map(lambda word:{word:len(word)}, sentence.split())
# print(list(res))

# len_ = map(len, sentence.split())
# print(len_)
# print(list(len_))

'''WAP to get list of tuples of character and its ascci value pair'''
#
# word = "hello"
# def conv(a):
#     for char in a:
#         return char, ord(char)
#
# res = map(conv, word)
# print(list(res))

'''WAP to add the following list elements simultaneously  '''

# a = [1, 2, 3, 4]
# b = [2, 4, 6, 8]
#
# def add(item1, item2):
#     return item1+item2
#
# res = map(add, a, b)
# print(list(res))

# a = [1, 2, 3, 4, 9]
# b = [2, 4, 6, 8]
#
# add = lambda a,b: a+b
# print(list(map(add, a,b)))

# a = [1, 2, 3, 4]
# s = list(enumerate(a))

# print(list(map(lambda a: a[0]*a[1], enumerate(a))

