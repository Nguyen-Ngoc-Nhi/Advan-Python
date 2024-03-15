# method override    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        print(f"name is {self.name}, age is {self.age}")
        
class President(Person):
    def __init__(self, name, age, term):
        super().__init__(name,age)
        self.term = term
    def print(self):
        super().print()
        print(f"My term is {self.term}")

macron = President("Macron", 48, "2020 - 2035")
macron.print()