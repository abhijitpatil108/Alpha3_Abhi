
'''WAP to return even values from the below list'''

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l1 = ["hello", "are", "orange"]
# even_ = lambda a: a % 2 == 0
# vowel = lambda a: a[0].lower() in "aeiou"
# print(list(filter(even_, l)))
# print(list(filter(vowel, l1)))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def even_(num):
#     if num % 2 == 0:
#         return 1    # return should be always boolean will return 2, 4, 6, 8
# res = filter(even_, l)
# print(list(res))

# def even(num):
#     if num % 2 == 0:
#         return 1
#
# evens = filter(even, l)
# print(list(evens))
#
# '''WAP that returns a list of strings with odd length'''
#
# sentence = "welcome to python"
#
# odd = lambda a: len(a) % 2 != 0
# print(list(filter(odd, sentence.split())))

# def string(word):
#     if len(word) % 2 != 0:
#         return word
#
# odd = filter(string, sentence.split())
# print(list(odd))

'''WAP which returns all the words staring with vowels in the given sentence'''

# sentence = "hello hai how are you"
#
# vowels = lambda a: a[0].lower() in "aeiou"
#
# print(list(filter(vowels, sentence.split())))

#
# # def vowels(word):
# #     if word[0].lower() in "aeiou":
# #         return word
#
# vowels = lambda word: word[0].lower() in "aeiou"
#
# res = filter(vowels, sentence.split())
# print(list(res))

# vowels_ = lambda a: a[0].lower() in "aeiou"
# print(list(filter(vowels_, sentence.split())))
#
