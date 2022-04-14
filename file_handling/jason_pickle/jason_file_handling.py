# dump(), dumps()


import json


# a = {"hei": 3, "hello": 5}
# a = [1,2,3,4]
# print(type(a))
# b = json.dumps(a)
# print(b)
# print(type(b))
# # s1 =json.dumps(s)
# # print(s1)
# c = json.loads(b)
# print(c)
# print(type(c))

a = {"a": 1, "b": 2, "c": 3}

with open("sample.json", "a") as f:
    json.dump(a, f)


