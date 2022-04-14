'''constructor overloading'''

'''method one'''
class Point:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

p0 = Point()
p1 = Point(1, 2)
p2 = Point(1, 2, 3)
p3 = Point(1, 2, 3, 4)
p0 = Point(1)

'''There are other two methods also by which we can '''


'''How to make an object instance of class callable?'''

# class Greeting:
#     def __call__(self, name):
#         return f"Hello {name}"
#
# g = Greeting()
# print(g("Abhi"))


class Squares:
    def __call__(self, numbers):
        return [number ** 2 for number in numbers]

s = Squares()
print(s([1, 2, 3, 4, 5]))

