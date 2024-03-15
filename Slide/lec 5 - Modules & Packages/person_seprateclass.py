class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        print(f"name is {self.name}, age is {self.age}")