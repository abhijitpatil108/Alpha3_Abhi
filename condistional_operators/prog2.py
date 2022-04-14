# Write a program to check if the given element is present in collection or not?

c = input("enter a string :")
b = input("enter a character :")
if c.find(b) != 0:
    print(f"{b} is not present in a string")
else:
    print(f"{b} is present in a string")
