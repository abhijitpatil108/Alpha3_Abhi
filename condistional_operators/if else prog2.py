# Write a program to check if the given iterable is empty or not?

# s = input("enter a string : ")
# if len(s) > 0:
#     print(f"{s} is not empty")
# else:
#     print(f"{s} is empty")

s = input("enter an iterable : ")
if bool(s):
    print(f"{s} is not empty")
else:
    print(f"{s} is empty")

# we can even simplify above code like below, instead of using if bool(s) we can directly we can use if s

s = input("enter an iterable : ")
if s:
    print(f"{s} is not empty")
else:
    print(f"{s} is empty")
