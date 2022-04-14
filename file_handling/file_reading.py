import os
from collections import defaultdict, Counter
from itertools import islice, zip_longest


'''WAP to read all the lines in a file without loading file in a memory'''

path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.txt"

# with open(path) as f:
#     print(list(f))
#     for line in f:
#         print(line)

'''WAP to count the number of lines present in a file'''

# with open(path) as f:
#     count = 0
#     for line in f:
#         count += 1
#     print(count)

'''WAP to print line number and line from the file'''

# path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.txt"

# with open(path) as f:
#     count = 0
#     for line in f:
#         count += 1
#         print(count, line)
#
# '''using enumerate'''

# with open(path) as f:
#     for line_no, line in enumerate(f, start=1):
#         print(line_no, line)

'''WAP to count the number of words in the given file'''

# with open(path) as f:
#     words = 0
#     for line in f:
#         words += len(line.split())
#     print(words)

# with open(path) as f:
#     for line_no, line in enumerate(f, start=1):
#         print(line_no, line)
#

# with open(path) as f:    # try again
#     print(f.read().count(" ")+1)

''' WAP to print the lines from last to first'''

# with open(path) as f:
#     for line in reversed(list(f)):
#         print(line)

'''WAP to count the number of spaces in the given file'''

# with open(path) as f:
#     count = 0
#     for line in f:
#         count += line.count(" ")
#     print(count)
#     # print(f.read().count(" "))
#
# with open(path) as f:
#     count = 0
#     for line in f:
#         for char in line:
#             if char == " ":
#                 count += 1
#     print(count)

'''WAP to count the number of words that are starting with vowels'''

# with open(path) as f:
#     count = 0
#     for line in f:
#         for word in line.split():
#             if word[0].lower() in "aeiou":
#                 count += 1
#     print(count)

'''WAP to create a dictionary of word and its count pair in the given file'''


# with open(path) as f:
#     dd = defaultdict(int)
#     for line in f:
#         for word in line.split():
#             dd[word] += 1
# print(dict(dd))
#
# with open(path) as f:
#     d = {}
#     for line in f:
#         for word in line.split():
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#     print(d)

'''WAP to extract all the IP addresses from access-log.txt file'''

file = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\access-log.txt"

# with open(file) as f:
#     lis = []
#     for line in f:
#         if line.strip():   # its IMP line should be in each program of file handling, will check for empty line
#             s = line.split()
#             lis.append(s[0])
#     print(lis)
#
# with open(file) as f:
#     lis = []
#     for line in f:
#         if line.strip():
#             s = line.split()
#             for word in s:
#                 if word.count(".") == 3 and :
#                     lis.append(word)
#     print(lis)

'''WAP to create a dictionary of IP addresses and their count'''

# with open(file) as f:
#     d = {}
#     for line in f:
#         if line.strip():
#             s = line.split()
#             if s[0] not in d:
#                 d[s[0]] = 1
#             else:
#                 d[s[0]] += 1
#     print(d)
#
# with open(file) as f:
#     dd = defaultdict(int)
#     for line in f:
#         if line.strip():
#             s = line.split()
#             dd[s[0]] += 1

    # print(dict(dd))

'''using Counter class'''
from collections import Counter

file = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\access-log.txt"

# with open(file) as f:
#     lis = []
#     for line in f:
#         if line.strip():
#             s = line.split()
#             lis.append(s[0])
# ip = Counter(lis)
# ip1 = Counter(lis)
# print(dict(ip))
# print(dict(ip1))
# res = ip.most_common()
# print(res)
# print(list(reversed(res)))
# print(ip.most_common(2))

'''WAP to print nth line in a file'''

# with open(file) as f:
#     n = 5
#     for line in f:
#         n = n - 1
#         if n == 0:
#             print(line)

# n = 5
# with open(path) as f:
#     for line_no, line in enumerate(f, start=1):
#         if line_no == n:
#             print(line)

# '''using islice class'''
#
from itertools import islice

# n = 5
# with open(path) as f:
#     res = islice(f, n-1, n)
#     print(list(res))

'''WAP to print first n lines'''
# n = 3
# with open(path) as f:
#     print(list(islice(f,n)))

# n = 3
# with open(path) as f:
#     for line_no, line in enumerate(f, start=1):
#         if line_no <= n:
#             print(line)

'''WAP to print last n lines'''

# n = 3
# with open(path) as f:
#     count = 0
#     for line in f:
#         count += 1
#     f.seek(count-n)
#     res = islice(f, count)    ## try again
#     print(list(res))

'''WAP to print last n lines'''
# n = 3
# with open(path) as f:
#     count = 0
#     for line in f:
#         count += 1
#     f.seek(0)
#     res = islice(f, count-n, count)    # 4, 7
#     print(list(res))
#
# '''using deque class'''

from collections import deque
#
n = 3
with open(path) as f:
    lines = deque(f, n)
    print((list(lines)))

'''WAP to copy the content of sample.txt into different file'''

path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.txt"
file = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\file1.txt.py"

# with open(path, "r") as f_read, open(file, "w") as f_write:
#         for line in f_read:
#             f_write.write(line)

################## 10the feb 2022 ################################
'''Assignment'''##########################
'''WAP to find the length of each line in a text file'''
path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.txt"

# with open(path) as f:
#     dd = defaultdict(int)
#     for line in f:
#         dd[line] = len(line)
#     print(dict(dd))

'''Extracting messages from sample.log'''

fsample = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.log"

# with open(fsample) as f:
#     lis = []
#     for line in f:
#         s = line.split()
#         if line.strip() and s[2] not in lis:
#             lis.append(s[2])
#     print(lis)


'''Counting number of INFO, WARN, TRACE message'''

# with open(fsample) as f:
#     lis = []
#     for line in f:
#         s = line.split()
#         if line.strip():
#             lis.append(s[2])
# count = Counter(lis)
# print(count)

'''reading countries from football.txt'''

footf = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\football.txt"

# with open(footf, encoding ="UTF-8") as f:
#     lis = []
#     for line in f:
#         s = line.split("\t")
#         if line.strip() and s[1]not in lis:
#             lis.append(s[1])
#     print(lis[1:])


'''least and most occurrence of the word'''

path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.txt"
fsample = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.log"
#
# with open(fsample) as f:
#     lis = []
#     for line in f:
#         if line.strip():
#             s = line.split()
#             for word in s:
#                 if word.isalnum():
#                     lis.append(word)
# count = Counter(lis)
# order = count.most_common()
# print(f"most occurrence word '{order[0][0]}' and least occurrence word '{order[-1][0]}'")

# with open(fsample) as f:
#     dd = defaultdict(int)
#     for line in f:
#         if line.strip():
#             s = line.split()
#             for word in s:
#                 if word.isalnum():
#                     dd[word] += 1
# count = Counter(dd)
# order = count.most_common()
# print(f"most occurrence word '{order[0][0]}' and least occurrence word '{order[-1][0]}'")


"""11. Write program to read a random line in a file. (ex. 50, 65, 78th line)"""

path = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\sample.txt"
file = r"C:\Users\Abhijit\PycharmProjects\Alpha3_Abhi\file_directory\txt_log_files\football.txt"



# with open(file) as f:
#     count = 0
#     for line in f:
#         count += 1
#         if count < 79:
#             if count in (50,65,78):
#                 print(line)
#             else:
#                 continue
#         else:
#             break
#
# print(count)


