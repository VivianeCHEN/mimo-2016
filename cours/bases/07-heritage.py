# Héritage et polymorphisme

# Exemple 1
class Animal:
    name = "The animal"
    nbLegs = 0
    def whoami(self):
        print("I am an animal")

class Dog(Animal):
    nbLegs = 4
    def whoami(self):
        super().whoami()
        print("I am a dog")

jerry = Animal()
droopy = Dog()

print(jerry.nbLegs)
print(droopy.nbLegs)

print(jerry.name)
print(droopy.name)

jerry.whoami()
droopy.whoami()

# Exemple 2
class Rectangle:
    def __init__(self, longueur=30, largeur=15):
        self.longueur, self.largeur, self.name\
            = longueur, largeur, "rectangle"

class Carre(Rectangle):
    """Sous-classe de Rectangle"""
    def __init__(self, cote=20):
        super().__init__(self, cote, cote)
        self.name = "carre"