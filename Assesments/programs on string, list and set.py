'''1) WAP to remove all duplicate elements in the list'''

# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# for item in names:
#     if names.count(item) > 1:
#         names.remove(item)
# print(names)

'''simpler way'''
# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# print(set(names))

'''2) WAP to print all numeric values in a list'''

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# # for item in items:
# #     if not isinstance(item, str):
# #         print(item)
'''Better way and more accurate way'''
# for item in items:
#     if isinstance(item, (int, float, complex)):
#         print(item, end = ' ')

'''3) WAP to sum all even numbers in the given string'''

# sentence = "hello 123 world 567 welcome to 9724 python"
# sum = 0
# for item in sentence:
#     if item.isdigit() and int(item) % 2 == 0:
#         sum += int(item)
# print(sum)

'''another way'''
# sentence = "hello 123 world 567 welcome to 9724 python"
# sum = 0
# for item in sentence:
#     if "0" <= item <= "9" and int(item) % 2 == 0:
#         sum += int(item)
# print(sum)


'''4) WAP to create a set with all the languages which starts with "p" / "P"'''

# languages = ['Python', 'Java', 'Perl', 'PHP', 'python', 'JS', 'c++', 'JS', 'python', 'Ruby']
# #
# sp = set()
# for item in languages:
#     if item[0] in "pP":
#         # sp.add(item)
#         sp.update({item})
# print(sp)


'''5) Build a list with only even length string'''

# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
#
# lis = []
# for item in names:
#     if len(item) % 2 == 0:
#         lis.append(item)
# print(lis)


'''6) Reverse the item of a list if the item is of odd length string otherwise keep the item as it is'''

# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
#
# reverse = []
# for item in names:
#     if len(item) % 2 != 0:
#         reverse.append(item[::-1])
#     else:
#         reverse.append(item)
# print(reverse)



'''7) WAP to print the sum of entire list and sum of only internal list'''

# l = [[1,2,3], [4,5,6], [7,8,9]]
#
# sum1 = l[0][0] + l[0][1] + l[0][2]
# sum2 = l[1][0] + l[1][1] + l[1][2]
# sum3 = l[2][0] + l[2][1] + l[2][2]
# sum4 = sum1 + sum2 + sum3
# print("sum of internal first list : ", sum1)
# print("sum of internal second list : ", sum2)
# print("sum of internal third list : ", sum3)
# print("sum of entire list : ", sum4)
#
# sum_entire = 0
# for lis in l:
#     i = 1
#     sum_internal = 0
#     for item in lis:
#         if i < 4:
#             sum_internal += item
#             i += 1
#     print(f"sum of internal list{i} is {sum_internal}")
#     sum_entire += sum_internal
# print(f"sum of internal list{i} is {sum_entire}")

#
# sumTotal = 0
# i = 1
# for lis in l:
#     sum = 0
#     for item in lis:
#             sum += item
#     print(f"Sum of internal list{i} is : ", sum)
#     sumTotal += sum
#     i += 1
# print(f"Sum of entire list is : ", sumTotal)

# l = [[1,2,3], [4,5,6], [7,8,9]]
# outer_list_sum = 0

# for item in l:
#     internal_sum = 0
#     for ele in item:
#         internal_sum += ele
#     print(internal_sum)
#     outer_list_sum += internal_sum
#
# print(outer_list_sum)

'''8) WAP to print list of prime numbers between 1-100'''

# prime = []
#
# for num in range (2, 100):
#     for item in range(2, num):
#         if num % item == 0:
#             break
#     else:
#         prime.append(num)
# print(prime)

prime = []
for num in range(2, 100):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        prime.append(num)
print(prime)

'''9) Write a program to reverse the list as below'''

# words = ["hi", "hello", "python"]
# # output ['nohtyn', 'olleh', 'ih']
# reverse = []
# for item in reversed(words):
#     reverse.append(item[::-1])
# print(reverse)

'''10) WAP to rotate items of the list'''
#input :
# items = ['apple', 1.2, 'google', '12.6', 26, '100']
#output: [26, '100', 'apple', 1.2, 'google', '12.6']
# k = 2
# n = 0
# for item in items:
#     if n < 2:
#         a = items.pop()
#         items.insert(0, a)
#         n += 1
# print(items)

