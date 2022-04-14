'''WARP that prints the number 10, then times'''

# def rec_(n, count=1):
#     if count < 11:
#         print(n, end =" ")
#         return rec_(n, count+1)
#     return
#
# rec_(10)

# def num_(n, count = 1):
#     if count > 10:
#         return
#     print(n)
#     count += 1
#     return num_(n, count)
#
# num_(10)

'''WARP to find the sum first n numbers'''

def sum_(n):
    if n == 1:
        return n
    return n+sum_(n-1)

print(sum_(5))


# def sum_(n, sum = 0):
#     if n > 0:
#         sum += n
#         return sum_(n-1, sum)
#     return sum
#
# print(sum_(5))
#
# def sum_(n, sum =0):
#     sum += n
#     if n == 1:
#         return sum
#     return sum_(n-1, sum)
#
# print(sum_(5))

'''WARP to find the fibonacci series until the given range'''
# n = 20
# lis = [0,1]
# def fibo(num):
#     lis.append(lis[-1]+lis[-2])
#     # check = len(lis)
#     if len(lis) == num:
#         return lis
#     return fibo(num)
#
# print(fibo(n))

'''WARP to print the reverse string values in the list'''
# l = [1, 'hello', 'bye', 2, 'thanks']
# def rev(lis):
#     if lis:
#         s = lis.pop()
#         if isinstance(s, str):
#             print(s[::-1])
#         rev(l)
#     return
# rev(l)

'''check whether the user given number is a factorial or not using recursion'''

# def facto(n, res = 1):
#     res = res*n
#     if n == 1:
#         return res
#     return facto(n-1, res)
#
# print(facto(5))


# def facto(n, start = 1, res =1):
#     res = res*start
#     start += 1
#     if res == n:
#         return f"{n} is a factorial num"
#     elif res > n:
#         return f"{n} is not a factorial num"
#     return facto(n, start,res)
#
# print(facto(90))

# def sum_(n, sum=0):
#     if n > 0:
#         sum += n
#         return sum_(n-1, sum)
#     return sum
#
# print(sum_(5))



# def facto(n):
#     # if n == 0 and n == 1:
#     if n == 1:
#         return n
#     else:
#         return n * facto(n-1)
# num = 120
# a = num
# for num in facto(5):
#     if num in facto(5):
#         print(f"{a} is factorial")
#     else:
#         print(f"{a} is not factorial")

