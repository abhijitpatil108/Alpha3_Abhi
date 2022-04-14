'''1) WAP to print the number of occurrences of characters in a string without using inbuilt functions'''
#
# s = "helloworld"
# d = {}
# for char in s:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
# print(d)

'''2) WAP to get the indexes of each item in the below list'''
#
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
#
# d = {}
# for index, item in enumerate(names):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
# print(d)

'''3) grouping files with same extensions'''
#
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
#
# d = {}
# for file in files:
#     s = file.split(".")
#     if s[1] not in d:
#         d[s[1]] = [s[0]]
#     else:
#         d[s[1]] += [s[0]]
# print(d)


'''4) WAP to create a dictionary with only the repeated characters and count of the same'''

string = "hello"

# d={}
# for char in string:
#     if string.count(char) > 1:
#         d[char] = string.count(char)
# print(d)

# string = "hello"
# d={}
# lis = list(string)
# for char in lis:
#     if lis.count(char) > 1:
#         d[char] = lis.count(char)
# print(d)

'''5) reverse the values in dictionary if the values is of type string'''

d = {'a': "hello", 'b': 100, 'c': 10.1, 'd': "world"}

# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
# print(d)
#

'''6) WAP to get all the duplicate items and the number of times the items is repeated in the list'''

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
#
# d = {}
# for name in names:
#     if names.count(name) > 1:
#         d[name] = names.count(name)
# print(d)

'''7) grouping flowers and animals in the below list'''

# items = ['lotus=flower', 'lily=flower', 'cat=animal', 'sunflower=flower', 'dog=animal']
#
# d = {}
# for type in items:
#     s = type.split("=")
#     if s[1] not in d:
#         d[s[1]] = [s[0]]
#     else:
#         d[s[1]] += [s[0]]
# print(d)

'''8) grouping even and odd numbers'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # #o/p==> {1: [1, 3, 5, 7, 9], 0: [2,4,6,8,10]}
#
# d = {1:[], 0: []}
# for num in numbers:
#     if num % 2 != 0:
#         d[1] += [num]
#     else:
#         d[0] += [num]
# print(d)

'''9) creating dictionary of city and population using Dict comprehension'''
#
# cities = ['Tokyo', 'Delhi', 'Shanghai', 'SaoPaulo', 'Mumbai']
# population = ['38,001,000', '25,703,168', '23,740,778', '21,065,245', '21042,538']
#
# d = {item: values for item, values in zip(cities, population)}
# d1 = {cities[i]: population[i] for i in range(len(cities))}
# print(d)
# print(d1)

'''10) Write a program to flip keys and values'''

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d1 = {}
# for key, value in d.items():
#     d1[value] = key
# print(d1)

'''7th Feb 2022'''
'''10) '''
# s = [(4,56,78), ('one', 'two', 'three')]
#
# d = {key: value for key, value in zip(s[1], s[0])}
# print(d)

'''6)'''
# l = [1,2,2,3,4,4,5,5,5,6,7,7,8,8,8, 88, 99, 100]
# # even_ = [l[i] for i in range(len(l)) if i % 2 == 0]
# # odd_ = [l[i] for i in range(len(l)) if i % 2 != 0]
# # d = {"even" : even_, "odd": odd_}
# d = { "even": [l[i] for i in range(len(l)) if i % 2 == 0], "odd": [l[i] for i in range(len(l)) if i % 2 != 0]}
# print(d)

'''2)'''
# d = {'a':'hello', 'b': 100, 'c': 10.1, 'd':'world'}
# d1 = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(d1)

'''4)'''
# cities = ['tokyo', 'Delhi']
# population = ['123', '234']
# d = {city: population for city, population in zip(cities, population)}
# print(d)

'''9)'''
# list_ = ['food@table', 'lily@flower', 'human@walk', 'being@work']
# d = {item.split("@")[0]: item.split("@")[1] for item in list_}
# print(d)

'''7)'''
# D = {'names': 'apple', 'ID': 52778}
# d = {'names': 'apple', 'ID': 657678}
# D = {1: 2, 2: 3}
# d = {4: 5, 6: 7}
# print({**D, **d})
# print(d1)
# dict_ = {key: value for key, value in d1.items()}
# dict_ = {key: value for key, value in zip(D.keys(), d.values())}
# print(dict_)