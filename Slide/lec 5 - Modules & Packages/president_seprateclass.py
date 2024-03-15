import person_seprateclass

class President(person_seprateclass.Person):
    def __init__(self, name, age, term):
        super().__init__(name,age)
        self.__term = term
    def _get_term(self):
        return self.__term
    def print(self):
        print(f"My term is {self.__term}") #the name "term" here is private
        super().print()
        
