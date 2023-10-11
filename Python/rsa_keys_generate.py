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
def generer_d_aleatoire(n, phi):
    while True:
        # dans cette boucle on gérère un nombre
        d = random.randint(2, phi-1)
        if pgcd(d, phi) == 1:
            return d
# Fonction pour trouver d : l'inverse de e modulo phi
def inverse_modulaire(d, phi):
    # algorithme d'Euclide étendu

    m0, x0, x1 = phi, 0, 1 # m0 est initialisé à phi et x0 à 0 et x1 à 1
    while d > 1: # on itère jusqu'a ce que d soit inferieur ou égal à 1
    #L'objectif de la boucle est de réduire d à 1 tout en calculant x1 pour obtenir l'inverse modulaire.
        q = d // phi #  q = le quotient de la division de d par phi.
        phi, d = d % phi, phi # phi est mis à jour avec le reste de la division de d par phi et d est mis a jour par la valeur précédente de phi
        x0, x1 = x1 - q * x0, x0  #  formule x0, x1 = x1 - q * x0, x0. Cela permet de garder une trace des coefficients nécessaires pour calculer l'inverse modulaire
    if x1 < 0:
        x1 += m0 # si la valeur de x1 est négative, nous ajoutons m0 pour obtenir une valeur positive Car l'inverse modulaire doit être positif.
    return x1

def calculer_e(d, phi):
    e = inverse_modulaire(d, phi)
    return e


while True:
    try:
        p = int(input("Entrez un nombre premier p : "))
        q = int(input("Entrez un nombre premier q : "))
        if is_premier(p) and is_premier(q):
            break
        else:
            print("Les nombres que vous avez entrés ne sont pas premiers.")
    except ValueError:
        print("Veuillez entrer des nombres entiers valides.")

n = p * q
phi = (p - 1) * (q - 1)

d = generer_d_aleatoire(n,phi)
e = calculer_e(d, phi)


# affiche les clés générées
print("\nClé publique (n, e) :")
print("n =", n)
print("e =", e)

print("\nClé privée (n, d) :")
print("n =", n)
print("d =", d)