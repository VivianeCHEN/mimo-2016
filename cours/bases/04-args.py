# Fonctions avancées

def myFonction(p1, p2 = 1):
    """
    My awesome multiplication function
    :param p1: this is parameter 1
    :param p2: this is parameter 2
    :return: just p1 * p2
    """
    return p1 * p2

print(myFonction(2, 2))
print(myFonction(2))

print(myFonction(p2=4,p1=3))

# Arguments multiples
def mySum(*args):
    res = 0
    for num in args:
        res += num
    return res

print(mySum(1, 2))
print(mySum(1, 2, 3, 4, 5))

# Scoping (local vs global)
x = 0
def f1():
    global x
    x = 2

f1()
print(x)