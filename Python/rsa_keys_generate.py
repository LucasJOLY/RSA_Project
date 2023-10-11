import random

def cribleEratosthene(nombre):
    estPremier = [True] * (nombre + 1)
    estPremier[0] = estPremier[1] = False

    # Marque les nombres composés
    p = 2
    while p ** 2 <= nombre :
        if estPremier[p] :
            for i in range(p ** 2, nombre + 1, p) :
                estPremier[i] = False
        p += 1

    # Retourne la liste des nombres premiers
    nombresPremiers = [i for i in range(2, nombre + 1) if estPremier[i]]
    return nombresPremiers

def estPremier(entier) :
    if entier < 2:
        return False
    listePremiers = cribleEratosthene(entier)
    return entier in listePremiers

def nombreAleatoire(chiffres) :
    nonZero = True
    nombre = ""
    for i in range (0, chiffres) :
        if nonZero :
            chiffre = random.randint(1,9)
            nonZero = False
        else :
            chiffre = random.randint(0,9)
        nombre += str(chiffre)
    return int(nombre)

def nombrePremier(chiffres) :
    while True :
        nombre = nombreAleatoire(chiffres)
        if estPremier(nombre) :
            return nombre

# fonction qui calcule plus grand commun diviseur
def pgcd(a, b):
    # algo euclide
    #on rentre dans la boucle et on en sort qund b = 0
    while b:

        a, b = b, a % b  # avec a % b on divise a par b et le reste est stocké dans a  et on échange a avec b de sorte que b devienne le plus petit des deux nombres.
    return a

# fonction qui génère la valeur d
def generer_d_aleatoire(p, q, ):
    n = p * q # on calcule n comme vu dans le cours
    phi = (p - 1) * (q - 1) # on calcule phi comme vu dans le cours
    while True:
        # dans cette boucle on gérère un nombre
        d = random.randint(1,100)
        if pgcd(d, phi) == 1:
            return d
# Fonction pour trouver d : l'inverse de e modulo phi
def mod_inverse(d, phi):
    # Pour calculer l'inverse modulaire on se base sur l'algorythme d'Euclide étendu
    e = 0

    # On initialise x1, x2, y1, et y2 à des valeurs spécifiques, généralement x1 = 1, x2 = 0, y1 = 0, et y2 = 1
    x1, x2, y1, y2 = 1, 0, 0, 1

    # on bucle jusqu'a ce que phi soit égal à 0
    while phi != 0:

        # pour chaque itération :
        # q = d // phi ---- d = phi ----- phi = d % phi
        q, d, phi = d // phi, phi, d % phi
        # x1 = x2  et x2 = x1- q * x2
        x1, x2 = x2, x1 - q * x2
        # y1 = y2  et y2 = y1- q * y2
        y1, y2 = y2, y1 - q * y2
    # une fois que phi = 0
    # l'inverse modulaire e est égal a x1
    e = x1
    #donc on renvoie e modulo d. Cela signifie que e est l'inverse de d modulo phi
    return e % d