# POO !!!

class MyClass:
    x = 1

monObj1 = MyClass()
monObj2 = MyClass()

print(monObj1.x)
print(monObj2.x)

monObj1.x = 42
print(monObj1.x)
print(monObj2.x)

print(MyClass.x)

print(dir(monObj1))
print(type("test"))

print("test".upper())

class MyClass2:
    x = 2
    y = 1
    def maFonction(self):
        self.x = 42
        print("ok", self.x)
    def getX(self):
        return self.x
    def setX(self, newX):
        self.x = newX

monObj2 = MyClass2()
monObj2.maFonction()

monObj3 = MyClass2()
monObj3.setX(24) # à penser comme MyClass2.setX(monObj3, 24)
print(monObj2.getX())
print(monObj3.getX())

# Initialisateur
class MyClass3:
    x = 3
    def __init__(self, n):
        self.x = n

monObj4 = MyClass3(55)
print(monObj4.x)