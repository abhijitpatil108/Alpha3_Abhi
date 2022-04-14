'''Write a generator function to yeild even numbers in the range 1-50'''
#
# def even_():
#     for item in range(1, 11):
#         if item % 2 == 0:
#             yield item      # function acts like as a generator.
#             # return item     # function acts like normal function
#
# even_numbers = even_()
# print(id(even_numbers))
# print(type(even_numbers))
# print(even_numbers)                # generator object address when yield is in function
# print(list(even_numbers))
# next_res = next(even_numbers)
# print(id(next_res))
# print(next_res)
#
# for item in even_numbers:
#     print(item)


#
# #generator expression
#
# even_ = (item for item in range(1, 51) if item % 2 == 0)
# # print(even_)   # generator object address
# # print(next(even_))  # only 2
# print(list(even_))  # it will print list except 2 as it's already printed in above line

'''WAGF&E to yield names starting with vowels in given list'''

# names = ['john', 'eve', 'bob', 'emma', 'ana']

# def vowels_(lis):
#     print(lis)
#     for name in lis:
#         if name[0].lower() in "aeiou":
#             yield name
#
# res = vowels_(names)
# print(list(res))

# name_vowel = (name for name in names if  name[0].lower() in "aeiou")
# print(next(name_vowel))
# print(list(name_vowel))
#
# def vowels_(a):
#     for item in a:
#         if item[0].lower() in "aeiou":
#             yield item
#
# vowels_names = vowels_(names)
# print(list(vowels_names))
#
# vowels_ = (item for item in names if item[0].lower() in "aeiou" )
# print(list(vowels_))

'''WAGF&E to yield length of each line in a file only if the line is not empty'''

# file = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.txt"
#
# def file_():
#     with open(file) as f:
#         for line in f:
#             if line.strip():
#                 yield line
#
# # for line in file_():
# #     print(line)
# # OR
# print(list(file_()))

# with open(file) as f:
#     line_ = (line for line in f if line.strip())
#     print(list(line_))

# def file_():
#     with open(file) as f:
#         for line in f:
#             if line.strip():
#                 yield len(line)
#
# line_ = file_()
# print(list(line_))

# # generator expression
# with open(file) as f:
#     line_ = (len(item) for item in f if item.strip())
#     print(list(line_))
#


''' '''

