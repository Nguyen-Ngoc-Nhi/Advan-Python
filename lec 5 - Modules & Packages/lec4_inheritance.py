class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self, name_only = False):
        if name_only:
            print(f"name is {self.name}")
        else:
            print(f"name is {self.name}, age is {self.age}")
macron = Person("Macron", 48)
macron.print()
