class Vehicle:
    owner = ""
    fixed = False
    def __init__(self, owner):
        self.owner = owner
    def getModel(self):
        pass
    def getName(self):
        return self.owner
    def setStatus(self, status):
        self.fixed = status
    def getStatus(self):
        if self.fixed:
            return "Fixed"
        else:
            return "Broken !"
    def display(self):
        return self.getModel() + "," \
               + self.getName() + "," \
               + self.getStatus() + "\n"

class Car(Vehicle):
    pass
class Moto(Vehicle):
    pass

class C1(Car):
    def getModel(self):
        return "C1"

class ClasseA(Car):
    def getModel(self):
        return "ClasseA"

class Kawasaki(Moto):
    def getModel(self):
        return "Kawasaki"

class Ducati(Moto):
    def getModel(self):
        return "Ducati"

myDuc = Ducati("John")
print(myDuc.display())