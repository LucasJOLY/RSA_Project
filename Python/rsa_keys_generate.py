import random

#Genère une liste de nombre premiers de 2 à n
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

#Vérifie si entier est un nombre premier
def estPremier(entier) :
    if entier < 2:
        return False
    listePremiers = cribleEratosthene(entier)
    return entier in listePremiers

#Génère un nombre aléatoire à n chiffres
def nombreAleatoire(chiffres) :
    if chiffres == 1 : #Pour un seul chiffre, on génère un nombre entre 0 et 9
        return random.randint(0, 9)
    nonZero = True
    nombre = ""
    for i in range (0, chiffres) : #Sinon, le premier chiffre ne peut pas être zéro
        if nonZero :
            chiffre = random.randint(1,9)
            nonZero = False
        else :
            chiffre = random.randint(0,9)
        nombre += str(chiffre)
    return int(nombre)

#Genère un nombre premier de n chiffres
def nombrePremier(chiffres) :
    while True :
        nombre = nombreAleatoire(chiffres)
        if estPremier(nombre) :
            return nombre




def pgcd(a, b):
    listeA = []
    listeB = []
    listeQ = []
    listeR = []
    listeA.append(a)
    listeB.append(b)

    while b != 1:
        q = a // b

        r = a % b

        listeQ.append(q)
        listeR.append(r)
        a = b
        b = r
        listeA.append(a)
        listeB.append(b)
    return listeR[-1]



def euclide8etendu(a, b):
    if(a < b):
        a, b = b, a
    listeA = []
    listeB = []
    listeQ = []
    listeR = []
    listeA.append(a)
    listeB.append(b)

    while b != 1:
        q = a // b

        r = a % b

        listeQ.append(q)
        listeR.append(r)
        a = b
        b = r
        listeA.append(a)
        listeB.append(b)

    newA = listeA[- 2]
    newB = listeB[- 2]
    u = 1
    v = -listeQ[-1]

    for i in range(len(listeA)-2):
        oldU = u
        oldV = v
        newA = listeA[- 3 - i]
        u = v
        newB = newA
        v = oldU - listeQ[- 2 - i] * oldV
    return listeR[-1],u, v







def generer_d_aleatoire(phi):
     while True:
         # dans cette boucle on gérère un nombre
         d = random.randint(2, phi-1)
         if euclide8etendu(d, phi)[0] == 1:
             return d


while True:
     try:
         p = int(input("Combien de chiffres pour p ? "))
         q = int(input("Combien de chiffres pour q ? "))
         if isinstance(p, int) and isinstance(q, int) :
             p = nombrePremier(p)
             q = nombrePremier(q)
             break;
     except ValueError:
         print("Veuillez entrer des nombres entiers valides. \n")


#
phi = (p-1)*(q-1)
n = p*q
d = generer_d_aleatoire(phi)
e = euclide8etendu(d, phi)[1]
if(e < 0):
    e = e + phi

# affiche les clés générées
print("\nClé publique (n, e) :")
print("n =", n)
print("e =", e)
print("\nClé privée (n, d) :")
print("n =", n)
print("d =", d)

# M = 12345
# C = M**e % n
# print("Message encodé : ", C)
#
# M = C**d % n
# print("Message décodé : ", M)
