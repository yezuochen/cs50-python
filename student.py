# Object-Oriented Programming ####

# import sys

class Student:
    def __init__(self, name, house):  # __init__ is a special method that is called when an object is created.
        # if not name:
        #     # sys.exit("Missing name")
        #     # raise Exception("Missing name")
        #     raise ValueError("Missing name")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #     raise ValueError("Invalid house")
        self.name = name
        self.house = house
        # self.patronus = patronus

    def __str__(self):  # __str__ is a special method that is called when an object is printed.
        return f'{self.name} from {self.house}'
    
    @classmethod  # @classmethod
    def get(cls):  # cls is a convention for the class itself.
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    @property  # @property is a decorator that allows us to call a method without parentheses.
    def name(self):
        return self._name
    
    @name.setter # @.setter is a decorator that allows us to change the value of an attribute.
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # getter
    @property
    def house(self):
        return self._house
    
    # setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    # def charm(self):
    #     match self.patronus:
    #         case "Stage":
    #             return "Expecto Patronum!"
    #         case "Otter":
    #             return "Emoji see"
    #         case "Jack Russell Terrier":
    #             return "dog"
    #         case _:
    #             return "/"



# attributes is a variable that belongs to an object.
# instance variables are attributes that are specific to an instance of a class.
# methods are functions that belong to an object.


def main():
    # student = get_student()
    student = Student.get()
    # print(f'{student.name} from {student.house}')
    # student.house = "Nu mber four, ..." # attribute can be changed after the object is created and method __init__.
    print(student)
    # print("Expecto Patronum!")
    # print(student.charm())
    # print(student.house)
    # print(student._house)

# def main():
#     # name, house = get_student()
#     student = get_student()

#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"       
#     # tuple object does not support item assignment

#     # print(f"{student[0]} from {student[1]}")
#     print(f'{student["name"]} from {student["house"]}')

# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     # dict is mutable, so it can be changed.
#     print(f'{student["name"]} from {student["house"]}')

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return name, house
#     # return (name, house)
#     return [name, house]

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name":name, "house": house}

# def get_student():
#     student = Student()   # create an object from the class Student
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # patronus = input("Patronus: ")
    return Student(name, house)



# tuple is immutable. list is mutable. tuple is faster than list.

if __name__ == "__main__":
    main()