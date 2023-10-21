# Lecture 6 - File I/O


# names = []

# for _ in range(3):
#     names.append(input("What is your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}!")


# name = input("What is your name? ")

# file = open("names.txt", "a")  #w for write, a for append
# file.write(f"{name}\n")
# file.close()

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("Hello, " + line.rstrip())


# with open("names.txt", "r") as file:
#     for line in file: #file is iterable
#         print("Hello, " + line.rstrip())

#names = []

# with open("names.txt", "r") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"Hello, {name}!")


# with open("names.txt") as file:
#     for name in sorted(file):
#         print(f"Hello, {name.rstrip()}!")


names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}!")