# # Set and Frozenset

# frozen_set1 = frozenset({'a', 'b', 'c', 'a'})

# frozen_set2 = frozenset({'a', 'b', 'c', 'a'})
# # frozen_set2 = frozen_set1

# normal_set = {1, 2, 3, frozen_set1, frozen_set2}

# print(normal_set)

# # Lambda Expression

# num = (0 if 1 > 2 else (3 if 2 > 1 else 2))

# print(num)

# OOP

class House:
    address = ""

    def __init__(self, address):
        self.address = address
        self.number_of_rooms = 4
        self.number_of_doors = 2


class House1:
    address = ""

    def __init__(self, address):
        self.test = address
        self.number_of_rooms = 4
        self.number_of_doors = 2

class Apartment(House, House1):
    def __init__(self, addr):
        House.__init__(self, addr)
        House1.__init__(self, addr)

h1 = Apartment("Teen Talwar")

print(h1.test)

print(h1.address)

h2 = House("Gulshan")

print(h2.address)

