# Object-Oriented Programming #

import sys

class Student:
    def __init__(self, name, house):  # __init__ is a special method that is called when an object is created.
        if not name:
            # sys.exit("Missing name")
            # raise Exception("Missing name")
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f'{self.name} from {self.house}'


# attributes is a variable that belongs to an object.
# instance variables are attributes that are specific to an instance of a class.
# methods are functions that belong to an object.


def main():
    student = get_student()
    print(f'{student.name} from {student.house}')
    print(student)

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
    return Student(name, house)



# tuple is immutable. list is mutable. tuple is faster than list.

if __name__ == "__main__":
    main()