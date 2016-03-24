# Fichiers

# Exemples d'ouverture de fichiers courants
# monFichier = open("fichier.txt", "r", encoding="utf-8")
# monFichier = open("fichier.txt", "w", encoding="utf-8")
# monFichier = open("fichier.txt", "a", encoding="utf-8")

# Lecture
monFichier = open("fichier.txt")

# Pour ligne la ligne suivante
print(monFichier.readline())
print(monFichier.readline())

# Pour lire les lignes via une boucle sur chaque ligne
for ligne in monFichier:
    print(ligne)

# Ne pas oublier de fermer un fichier après utilisation
monFichier.close()

# Ecriture
monFichier2 = open("fichier2.txt",
                   "w",
                   encoding="utf-8")
monFichier2.write("Testttt")
monFichier2.close()

mesLignes = ["ligne 1\n", "ligne 2\n", "ligne 3\n" ]
monFichier3 = open("fichier3.txt",
                   "w",
                   encoding="utf-8")
monFichier3.writelines(mesLignes)
monFichier3.close()

# Demander une information en ligne de commande à l'utilisateur
maQuestion = input("Quel jours sommes nous ? ")
print(maQuestion)

# Exercice: Faire une fonction qui
# demande un prénom et l'ajoute à un fichier
# "prenoms.txt" en boucle jusqu'à ce l'utilisateur
# tape "exit"

def myPrompt():
    nom = ""
    fichierPrenom = open("prenoms.txt",
                   "w",
                   encoding="utf-8")
    while nom != "exit":
        nom = input("Quel prénom?")
        fichierPrenom.write(nom + "\n")
    fichierPrenom.close()

myPrompt()