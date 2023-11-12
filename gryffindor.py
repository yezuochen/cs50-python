students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Luna", "house": "Ravenclaw"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Ginny", "house": "Gryffindor"},
]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)


# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"


# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# for student in students:
    # gryffindors.append({"name": student, "house": "Gryffindor"})

# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)

# for i in range(len(students)):
#     print(i+1, students[i])

for i, student in enumerate(students):
    print(i+1, student)