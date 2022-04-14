# Q ) Write a program to convert lowercase letter to uppercase and uppercase to lowercase



s = input("enter a string : ")

s1 = s.swapcase()
print(f"{s1}")

# # It can be done using below lower() and upper() methods also
s = input("enter a string : ")

if s.islower():
    print(f"{s.upper()}")
elif s.isupper():
    print(f"{s.lower()}")
else:
    print(f"{s} is not an alphabet")
#
char = "n"

if "a" <= char <= "z":
    print(chr(ord(char) - 32))
elif "A" <= char <= "Z":
    print(chr(ord(char) + 32))
else:
    print(f"{char} is not an alphabet")

