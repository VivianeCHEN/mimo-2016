# Bases

# Assignation de variables
a = 2
b = 4

# assignations multiples
a, b = 2, 3

# Afficher une valeur
print("La variable a est :", a)

# Afficher le type d'une variable
print(type(b))

# Structures de controles

# IF
if a > 2:
    print('a > 2')

if a <= 2:
    print('a <= 2')
    if a <= 1:
        print('a <= 1')
else:
    print('a > 2')

# WHILE
while a < 42:
    a = a + 1
print(a)

print("voici une super chaine\nde caractères")

# FOR
for i in "superchaine":
    print(i)

# création d'un tableau d'entiers
montableau = ['a', 'b', 's']

tab = [1, 2, 3]
for i in tab:
    print(i)

## TYPES
a = 2 # entier
c = "chaine" # string
tab = [] # liste vide
tab2 = [33, 44, 55]
liste = [tab, tab2]

print(tab2)
print(liste)

# accéder directement à un élément
print(tab2[1])

# Test de présence
print(33 in tab2)
print(333 in tab2)
if (44 in tab2):
    print('44 est la !')
else:
    print('44 est pas la !')
if (444 in tab2):
    print('444 est la !')

if True and not(444 in tab2):
    print('444 est pas la !')


# Taille: len
print(len(tab2))

# Aide
help(range)

b=list(range(1,10,2))
print(b)

# modification de liste
superliste = [56, 12, 68, 34, 88, 96]

# ajouter un élément
superliste.append(100)
print(superliste)

superliste.sort()
print(superliste)

superliste.pop()
print(superliste)

print(superliste.index(68))

# liste variée
l1 = [1, "ok", [42, 'b'], 5]

# interval d'index
print(l1[0])
print(l1[1])

print(l1[1:3])
print(l1[2:2])

l1[1:3] = [12]

print(l1)

# Table de hash, tableau associatif
ht1 = {}
ht1["age"] = 12
ht1["ville"] = "Paris"
ht1["cheveux"] = "blond"

print(ht1["age"])

ht2 = dict(age=3, ville="Bordeaux", cheveux="roux")
print(ht2)

# méthodes sur les Hash tables
print(sorted(ht1.keys()))
print(ht1.values())
