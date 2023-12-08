import random

#Vérifie si entier est un nombre premier
def estPremier(entier) :
    if entier < 2 :
        return False
    for i in range(2, entier-1) :
        if(entier % i == 0) :
            return False
    return True

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




def pgcd(a, b) :
    while b > 1 :
        q = a // b

        r = a % b

        a = b
        b = r    
    return r


def euclideEtendu(a, b) :
    listeA = []
    listeB = []
    listeQ = []
    listeR = []
    listeA.append(a)
    listeB.append(b)

    while b != 1 :
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

    for i in range(len(listeA)-2) :
        oldU = u
        oldV = v
        newA = listeA[- 3 - i]
        u = v
        newB = newA
        v = oldU - listeQ[- 2 - i] * oldV
    return listeR[-1],u, v


def dAleatoire(phi) :
     while True :
         # dans cette boucle on gérère un nombre
         d = random.randint(2, phi-1)
         if pgcd(d, phi) == 1 :
             return d


while True :
    try :
        p = int(input("Combien de chiffres pour p ? ")) 
        q = int(input("Combien de chiffres pour q ? "))
        if isinstance(p, int) and isinstance(q, int) :
            p = nombrePremier(p)
            q = nombrePremier(q)
            break;
    except ValueError : 
        print("Veuillez entrer des nombres entiers valides. \n")

print("p ", p)
print("q ", q)
phi = (p-1)*(q-1)
n = p*q
d = dAleatoire(phi)
e = euclideEtendu(d, phi)[1]
while(e < 0) :
    e = e + phi

# affiche les clés générées
print("\nClé publique (n, e) :")
print("n =", n)
print("e =", e)
print("\nClé privée (n, d) :")
print("n =", n)
print("d =", d)

M = 12345
C = M**e % n
print("Message encodé : ", C)

M = C**d % n
print("Message décodé : ", M)
