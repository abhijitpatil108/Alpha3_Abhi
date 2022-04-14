import csv
from collections import defaultdict



path = r"/file_directory/csv_files\sample.csv"

# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     print(read_obj)                   # iterative object
#     for row in read_obj:
#         print(row)                    # read each row of csv file as list
#
# with open(path) as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row)                     # read each row of csv file as dictionary

# '''writing into csv file'''

# with open("example.csv", "w") as csv_:
#     write_obj = csv.writer(csv_)
#     write_obj.writerow(['x', 'y', 'z'])
#
#     write_obj.writerows([(1,2,3), (4,5,6), (7,8,9)])

# with open("example.csv", "w") as csv_writer:
#     dictwriter_obj = csv.DictWriter(csv_writer, ['x', 'y', 'z'])
#     dictwriter_obj.writeheader()
#     dictwriter_obj.writerow({'x': 10, 'y': 20, 'z': 30, })
#

'''WAP to read all the names of the employees in employees.csv file'''

path = r"/file_directory/csv_files\employees.csv"

# with open(path) as f:
#     ro = csv.reader(f)
#     for row in ro:
#         print(row[0])

'''WAP to print only salaries that are > 70000'''
# with open(path) as f:
#     ro = csv.reader(f)
#     for row in ro:
#         if row[-1].isnumeric() and int(row[-1]) > 70000:
#             print(row[-1])

# with open(path) as f:
#     ro = csv.reader(f)
#     next(ro)      ### this will move the curser to next line/row
#     for row in ro:
#         if int(row[-1]) > 70000:
#             print(row[-1], end=" ")

'''WAP to print only names with salaries that are > 70000'''

# with open(path) as f:
#     ro = csv.reader(f)
#     for row in ro:
#         if row[-1].isnumeric() and int(row[-1]) > 70000:
#             print(row[0], end=" ")


'''WAP to group male and female employees in the file'''

# with open(path) as f:
#     ro = csv.reader(f)
#     d = {"male":[], "female":[]}
#     for row in ro:
#         if row[1] == "male":
#             d["male"] += [row[0]]
#         elif row[1] == "female":
#             d["female"] += [row[0]]
#     print(d)


'''WAP to group employees based on their team'''

# with open(path) as f:
#     ro = csv.reader(f)
#     d = {}
#     next(ro)
#     for row in ro:
#         if row[2] not in d:
#             d[row[2]] = []
#     print(d)
#     f.seek(0)
#     next(ro)
#     for row in ro:
#         if row[2] == list(d.items())[0][0]:
#             d[list(d.items())[0][0]] += row[0]
#         elif row[2] == list(d.items())[1][0]:
#             d[list(d.items())[1][0]] += row[0]
#         elif row[2] == list(d.items())[2][0]:
#             d[list(d.items())[2][0]] += row[0]
#         if row[2] == list(d.items())[3][0]:
#             d[list(d.items())[3][0]] += row[0]
#
#     print(d)

# with open(path) as f:
#     ro = csv.reader(f)
#     next(ro)
#     dd = defaultdict(list)
#     for row in ro:
#         dd[row[2]] += [row[0]]
#     print(dict(dd))




'''WAP to sort the shares in the test.csv based on the share price '''

path = r"/file_directory/csv_files\test.csv"

# with open(path) as f:
#     ro = csv.DictReader(f)
#     l = list(ro)
#     res = sorted(l, key = lambda d: float(d["price"]))
#     print(list(res))


'''WAP to add all the share in test.csv file'''

# with open(path) as f:
#    ro = csv.reader(f)
#    shares = 0
#    next(ro)
#    for row in ro:
#        shares += int(row[1])
# print(shares)

#######################  11th Feb 2022  ##################################
################# assignments on vaccination status ######################

path = r"/file_directory/csv_files\vaccination_data.csv"
'''latest updated countries vaccination'''
# d = {}
# with open(path) as f:
#     ro = csv.DictReader(f)
#     next(ro)
#     dd = defaultdict(list)
#     for row in ro:
#         latest = row["DATE_UPDATED"]
#         dd[latest] += [(row["COUNTRY"], row["TOTAL_VACCINATIONS"])]
# res = sorted(dd.items())
# print(res[-1])
#



