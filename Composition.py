
class Dog:
    def __init__(self, n, b, o):
        self.name = n
        self.breed = b
        self.owner = o

class Person:
    def __init__(self, n):
        self.name = n

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Brussel Griphon", mick )
print(stan.owner.name)
