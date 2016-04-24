# Exceptions

# Exception division par zero
def divByN(n):
    try:
        print(3/n)
        if n == 3:
            raise ValueError("erreur de valeur")
    except ZeroDivisionError:
        print("Pas possible")
    except ValueError as myerror:
        print(myerror)
        #raise ValueError(myerror)
    else:
        print("else")
    finally:
        print("finally")

divByN(0)
divByN(3)
divByN(4)

# exemple sur l'ouverture d'un fichier
filename = "toto.txt"
myfile = None
try:
    myfile = open(filename)
    for line in myfile:
        print(line)
except EnvironmentError as err:
    print(err)
finally:
    if myfile is not None:
        myfile.close()

# Exemples d'exceptions:
# ArithmeticError, ZeroDivisionError, IndexError,
# IOError, SyntaxError, ...