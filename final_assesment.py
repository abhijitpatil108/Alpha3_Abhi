
# def rotate_string(s, n):
#     # res = s
#     count = n #2
#     while count > 0:
#         # res = res[-1] + res[:-1]
#         s = s[-1] + s[:-1]
#         count -= 1
#     return s
#
#
# def r_s(s, n):
#     return s[len(s)-n:]+s[:len(s)-n]
# print(r_s("helloworld", 3))
#
# print(rotate_string("helloworld", 3))


# def rotate_string_1(string, n):
#     temp = list(string)
#     for _ in range(n):
#         key_ = temp.pop()
#         temp.insert(0,key_)
#     out = "".join(temp)
#     return out
#
# print(rotate_string_1("helloworld", 2))
#

# sentence = "hello world welcome"
# s = sentence.split()
# s.sort(key=len,reverse=True)
# s1 = sorted(s, key=len,reverse=True)
# print(s[0])
# print(s1[0])

'''1)'''
s = "Hello welcome to python"
print(s.replace(" ", ","))

s ="abcdbjdabcdvnidsjvoabcd"
temp = s.split("abcd") # []
# temp = "".join(temp) # ""
print(len(temp)-1)
# output = (len(s)-len(temp))//len("abcd")
# print(output)