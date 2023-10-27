# cs50: class methods
# @classmethod decorator is  used to create class methods, so that we can call them without instantiating the class

import random

class Hat:
    # def __init__(self):
    #     self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    # def sort(self, name):
    #     print(name, "is in", random.choice(self.houses))

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# hat = Hat()
# hat.sort("Harry")

Hat.sort("Harry")