'''without context manager'''

# f = open("sample.txt", "r")
# print(f)
# print(f.closed)  # False
# f.close()
# print(f.closed)   # True

'''Using context manager'''

# with open("sample.txt") as f:
#     print(f)
#     print(f.closed)  # False
#
# print(f.closed)   # True

import os

# with open("sample.txt") as f:
#     print(f.closed)         # False
#     print(f.mode)           # r
#     print(f.name)           # sample.txt
#     print(f.readable())     # True
#     print(f.writable())     # False

'''whenever we want to open and write the file at the same time, then we should add + sign to mode'''

# with open("sample.txt", "r+") as f:
#     print(f.readable())         # True
#     print(f.writable())         # True

file = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.txt"

# with open(file) as f:
#     data = f.read()
#     print(data)
#     print(f.read(10))

# with open(file) as f:
#     data = f.read()
#     print(data)
#     print(f.tell())
#     f.seek(file.find("Welcome"))
#     print(f.read())
#     # print(f.readline(5))

# print(max("hi", "hello", "how", key=len))

