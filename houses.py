# CS50: Et Cetera

# set

students = [
    {"name": "Hermione Granger", "house": "Gryffindor"},
    {"name": "Luna Lovegood", "house": "Ravenclaw"},
    {"name": "Cho Chang", "house": "Ravenclaw"},
    {"name": "Ginny Weasley", "house": "Slytherin"},
    {"name": "Cedric Diggory", "house": "Hufflepuff"}
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

