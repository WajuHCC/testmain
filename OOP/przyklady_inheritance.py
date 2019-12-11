class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    @property
    def is_alive(self):
        return self.energy > 0

    def move(self, distance):
        self.energy -= 0.1 * distance
        if self.is_alive:
            return distance
        return self.is_alive

    def eat(selfself, calories):
        self.energy += 0.2 * calories

class Dog(Animal):

    def bark(self):
        print ("How How")
        self.energy -= 0.01

a = Animal("Zenek")
azor = Dog("Azor")
print(a.move(50))
