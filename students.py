# with open('students.csv') as file:
#     for line in file:
#         row = line.rstrip().split(',')
#         print(f'{row[0]} is in {row[1]}')


# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         print(f'{name} is in {house}')

students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         # student = {}
#         # student['name'] = name
#         # student['house'] = house
#         student = {'name': name, 'house': house}
#         students.append(student)

# def get_name(student):
#     return student['name']

# def get_house(student):
#     return student['house']
    
# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key=get_house, reverse = True):
#     print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key=lambda student: student['name']):
#     print(f"{student['name']} is in {student['house']}")

import csv

students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name,home in reader:
#         students.append({"name": name, "home": home})

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for student in reader:
#         students.append({"name": student["name"], "home": student["home"]})

# for student in sorted(students, key=lambda student: student['name']):
#     print(f"{student['name']} is from {student['home']}")

name = input("What is your name? ")
home = input("What is your house? ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home": home})

# pillow is a python image library
