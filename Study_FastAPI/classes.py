
''' Classes as Types '''


class Person:
    def __init__(self, name:str):
        self.name=name 
        
def get_person_name(one_person:Person):
    return "name : "+one_person.name  

p1 = Person("Yebin")
print(get_person_name(p1))