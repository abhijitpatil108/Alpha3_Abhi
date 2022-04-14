'''default sorting the collection datatypes'''

from file_handling.jason_pickle import jason_file_handling






# s = "hello"
# print(sorted(s))
#
# l = [1, 4, 7, 8, 2, 8, 10]
# print(dict.fromkeys(l))
# print(type(enumerate(l)))
# print(enumerate(l))
# print(sorted(l))
# print(l.sort())
# print(l)

#
# l1 = ['python', 'java', 'ruby', 'c', 'perl']
# print(sorted(l1))
#
# t = (1, 4, 7, 8, 2, 8, 10)
# print(sorted(t))
#
# s1 = {'python', 'java', 'ruby', 'c', 'perl'}
# print(sorted(s1))
#
# d = {'gmail': 5, 'facebook': 8, 'google': 6, 'instagram': 9}
# print(d.fromkeys(d))
# print(d)
# print(d.setdefault("ipl"))
# a = d.items()
# print(a)
# print(type(a))

# print(d.get("hi"))
# # print(sorted(d))
# print(sorted(d.items(), key=len))
# #

# s = "hello"
# print(sorted(s, reverse=True))
#
# l = [1, 4, 7, 8, 2, 8, 10]
# print(sorted(l, reverse=True))
#
# l1 = ['python', 'java', 'ruby', 'c', 'perl']
# print(sorted(l1, reverse=True))
#
# t = (1, 4, 7, 8, 2, 8, 10)
# print(sorted(t, reverse=True))
#
# s1 = {'python', 'java', 'ruby', 'c', 'perl'}
# print(sorted(s1, reverse=True))

# print("hello", end = " ")
# print("hello")
# d = {'gmail': 5, 'facebook': 8, 'google': 6, 'instagram': 9}
# print(sorted(d, reverse=True))
# # print(sorted(d, key=d[keys]))
# print(sorted(d.items(), reverse=True))


'''Custom sorting'''
##################################

'''WAP to sort the elements presents in the list based on their length'''

# l1 = ['python', 'java', 'ruby', 'c', 'perl']

# print(sorted(l1, key=len))

'''WAP to find longest and sortest word in the following string'''

# sentence = "python is a programming language"
# word = sorted(sentence.split(), key=len)
# print(f"longest word is {word[-1]} and shortest word is {word[0]}")
# # #or
# shortest, *rest, longest = sorted(sentence.split(), key=len)
# print(f"longest word is {longest} and shortest word is {shortest}")

'''WAP to print longest and shortest words along with their lengths in the below sentence'''

# sentence = "python is a programming language"
# shortest, *rest, longest = sorted(sentence.split(), key=len)
# print(f"longest word is {(longest, len(longest))} and shortest word is{(shortest, len(shortest))}")
# words = sorted(sentence.split(), key=len)
# d = {word: len(word) for word in words}
# print(f"longest word is {d[-1]} and shortest word is {d[0]}")

'''WAP to sort the below list elements based on the last character of each string'''

# l = ['python', 'java', 'ruby', 'c', 'perl']

# def last_item(ele):
#     return ele[-1]
#
# # print(sorted(l, key= last_item))
#
# print(sorted(l, key= lambda a: a[-1]))

'''WAP to sort below list based on first character of each element'''

'''sorting a dictionary based on its key'''

# d = {'gmail': 5, 'facebook': 8, 'google': 6, 'instagram': 9}
# based on ASCII value
# print(sorted(d))
# print(sorted(d.keys()))
# print(sorted(d.items()))
#
# # based on key (here len)
#
# print(sorted(d, key=len))
# print(sorted(d.keys(), key=len))
# print(sorted(d.items(), key=len)) # as len wil compare length of tuple, so will return list as it is
# print(sorted(d.items(), key=lambda item: len(item[0])))

# after sorting if you want to get the dictionary of an output just print the output using dict
# print(dict(sorted(d.items(), key=lambda item: len(item[0]))))




'''WAP to sort the dictionary based on keys last item'''

# d = {'gmail': 5, 'facebook': 8, 'google': 6, 'instagram': 9}
#
# # print(dict(sorted(d.items(),key=lambda item: item[0][-1])))
#
# print(dict(sorted(d.items(),key=lambda item: item[-1]))) # based o value

'''WAP to sort a dictionary based on values '''

# d = {'gmail': 5, 'facebook': 8, 'google': 6, 'instagram': 9}
# print(dict(sorted(d.items(), key=lambda item: item[-1])))
# print(dict(sorted(d.items(), key=lambda item: d[])))
# print(dict(sorted(d, key=lambda a: d[a])))

# try to find out any other method to solve above program

'''WAP to sort the below list based on the temp'''
# temperatures = [('Delhi', 32), ('Mumbai', 27), ('Kolkata', 30), ('Chennai', 35)]
#
# print(sorted(temperatures, key=lambda item: item[-1]))


'''WAP to get the most repeated word'''

# sentence = "hi how are you how is your health"
# s = sentence.split()
#
# d = {word: s.count(word) for word in s}
# most = sorted(d.items(), key=lambda item: item[-1])
# print(most[-1][0])

'''WAP to print the longest word with its length'''

# sentence = "python is programming language and programming is fun"
# s = sentence.split()
#
# d = {word: len(word) for word in s}
# long_ = sorted(d.items(), key=lambda item: item[-1])
# print(long_[-1])

'''WAP to print the non repeated longest word with its length'''
# sentence = "python is programming language and programming is fun"
#
# s = sentence.split()
#
# d = {word: len(word) for word in s if s.count(word) == 1}
# long_ = sorted(d.items(), key=lambda item: item[-1])
# print(long_[-1])

'''sort the below list based on names'''

# l = [{'name': 'Ram', 'class': 6, 'age': 12}, {'name': 'Shyam', 'class': 12, 'age': 18}, {'name': 'John', 'class': 8, 'age': 14}]

# print(sorted(l, key =lambda item: item['name']))
# print(sorted(l, key =lambda item: item['age']))               # based on age
# print(sorted(l, key =lambda item: item['class']))             # based on class


'''WAP to sort the elements presents in the list based on their length'''

# l1 = ['python', 'java', 'ruby', 'c', 'perl']
# print(sorted(l1, key=len))



'''WAP to find longest and sortest word in the following string'''

# sentence = "python is a programming language"
# s = sentence.split()
# s1 = sorted(s, key=len)
# print(f"longest word is {s1[-1]} and shortest word is {s[0]}")


'''WAP to print longest and shortest words along with their lengths in the below sentence'''

# sentence = "python is a programming language"
# s = sentence.split()
# s1 = sorted(s, key=len)
# d = {}
# d[s1[0]] = len(s1[0])
# d[s1[-1]] = len(s1[-1])
# print(d)

'''WAP to sort the below list elements based on the last character of each string'''

# l = ['python', 'java', 'ruby', 'c', 'perl']
# print(sorted(l, key=lambda a: a[-1]))



'''WAP to sort below list based on first character of each element'''

'''sorting a dictionary based on its key'''

# d = {'gmail': 5, 'facebook': 8, 'google': 6, 'instagram': 9}
# print(sorted(d.items(), key=lambda s: s[0]))
#


'''WAP to sort the dictionary based on keys last item'''

# d = {'gmail': 5, 'facebook': 8, 'google': 6, 'instagram': 9}
# print(sorted(d.items(), key=lambda a: a[0]))

'''WAP to sort a dictionary based on values '''

# d = {'gmail': 5, 'facebook': 8, 'google': 6, 'instagram': 9}
# print(sorted(d.items(), key=lambda a: a[1]))


'''WAP to sort the below list based on the temp'''
# temperatures = [('Delhi', 32), ('Mumbai', 27), ('Kolkata', 30), ('Chennai', 35)]
# print(sorted(temperatures, key=lambda a: a[1]))


'''WAP to get the most repeated word'''

# sentence = "hi how are you how is your health"
# l = sentence.split()
# d = {word: l.count(word) for word in l}
# s = sorted(d.items(), key=lambda a: a[1])
# print(f"most repeated word is {s[-1][0]}")

'''WAP to print the longest word with its length'''

# sentence = "python is programming language and programming is fun"
# l = sentence.split()
# d = {word: len(word) for word in l}
# s = sorted(d.items(), key=lambda a: a[1])
# print(f"longest word is {s[-1]}")



'''WAP to print the non repeated longest word with its length'''
# sentence = "python is programming language and programming is fun"
# l = sentence.split()
# d = {word: len(word) for word in l if l.count(word) == 1}
# s = sorted(d.items(), key=lambda a: a[1])
# print(f"non repeated longest word is {s[-1][0]}")
#



'''sort the below list based on names'''

# l = [{'name': 'Ram', 'class': 6, 'age': 12}, {'name': 'Shyam', 'class': 12, 'age': 18}, {'name': 'John', 'class': 8, 'age': 14}]
#
# print(sorted(l, key=lambda a: a['name']))


'''sort the below list based on highest marks first and based on age in marks are same'''
# l = [('Alison', 50, 18), ('David', 75, 20), ('Terence', 75, 12),  ('Jimmy', 90, 22), ('John', 45, 12)]
# s = sorted(l, key=lambda a: (a[1], a[2]))
# print(s)


# s = "hello"
#
# # print("Hi \\tha \\nk you")
# print(r"Hi \tha\nk you")
# # print(r'Hi tha'nk you')

# a = "how are you hope you are fine"
# # print(a.find("you"))
# # print(a.count("you"))
# s = a.split(" ", 2)
# print(s)
# s1 = a.rsplit(" ", 2)
# print(s1)
# print(s[4].startswith("you"))

# print(l)
# sp = a.count(" ")
# # print(sp)
# # print(a.startswith("you",)

# d = dict(a=1,b=2)
# print(dict(d.items()))
# print(d.keys())
# print(d.values())

# def asc(a):
#     for ch in a:
#         def ascc(ch):
#             return ord(ch)
#         print(ord(ch))


from collections import defaultdict
# s = "hello"
# d = dict.fromkeys(s,asc(s))

# d = {ch:ord(ch) for ch in s}
# print(d)
# print(list(range(3,30,3)))

# s = "hello"
# l = [1,2,3,4]
# t = (1,2,3)
#
# d = {'a': 1, 'b': 2}
# s1 ={4,3,2,1}
# s2 = {1,2,3,4,5,6,7,8,9}
# print(s2)
# print(list(enumerate(s)))
# print(list(enumerate(l)))
# print(list(enumerate(t)))
# print(list(enumerate(d)))
# print(list(enumerate(s1)))
# print(list(enumerate(s2)))

# a = 10
# def fun():
#     a += 20
#
# fun()
#
# print(a)

a = 'AABBCCCDAACD'

s = ""
count = 1
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        count += 1
    else:
        s = s+str(count)+a[i]
        count = 1
if a[-1] != a[-2]:
    s = s+str(count)+a[-1]

print(s)


