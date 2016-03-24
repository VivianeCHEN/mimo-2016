# Fonctions

def maFonction():
    print('ma super fonction')

maFonction()

def foisdeux(x):
    return x * 2

print(foisdeux(12))

# Exercice 1: écrire une fonction qui prend
# une liste l en parametre et return True
# si il y a plus de 5 éléments et False sinon

def fonctionInutile1(l):
    if len(l) > 5:
        return True
    else:
        return False

print(fonctionInutile1([]))
print(fonctionInutile1([1,2]))
print(fonctionInutile1([1,2,3,4,5,6,7]))

# Exemples d'appels invalides
#print(fonctionInutile1("allo"))
#print(fonctionInutile1(4545))

# Exercice 2: faire une fonction
# qui prend un entier n en paramètre
# et renvoie la liste des n premiers
# nombres pairs.
# Une fois avec une boucle et une fois sans

def fonctionInutile2(n):
    if (n > 0):
        pairs = []
        i = 2
        while (len(pairs) < n):
            pairs.append(i)
            i += 2
        return pairs
    else:
        print("FAUTE")

print(fonctionInutile2(-12))
print(fonctionInutile2(0))
print(fonctionInutile2(1))
print(fonctionInutile2(2))
print(fonctionInutile2(3))