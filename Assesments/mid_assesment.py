'''3)'''
a = 'AABBCCCDAACD'
# o/p => 2A2B3C1D2A1C1D

s = ""
count = 1
for i in range(len(a) - 1):

    if a[i] == a[i + 1]:
        count += 1
    else:
        s = s + str(count) + a[i]
        count = 1
if a[-1] != a[-2]:
    s = s + str(count) + a[-1]

print(s)

# l = [1,2,3,4]
# s = {item for item in l}
# s = set(item for item in l)
# print(s)
# print(type(s))