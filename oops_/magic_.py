'''validation of data using getter and setter method'''
'''1) radius and circumference example'''
'''2) person example with fname, lname an age attributes'''

class A:
    def __init__(self):
        self._value = 0                  # private variable
        self.value = 10

    def demo(self):                       # public method
        print(self._value)
        print(self.value)

    def _spam(self):                       # private method, we can call this method, but we should not
        print(self._value)
        print(self.value)