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
        self.__term = term
    def _get_term(self):
        return self.__term
    def print(self):
        print(f"My term is {self.__term}") #the name "term" here is private
        super().print()
        
macron = President("Macron", 48, "2020 - 2035")
print(f"Macron term is {macron._get_term()}")
