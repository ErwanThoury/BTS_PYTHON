from math import *
tableau = []
maxDansTableau = True  #Vérification double base
neufDansTableau = True #Vérification présence de neuf
maxim = 0 # Pour eviter le saisies du style 1111111111
while maxDansTableau == True or neufDansTableau == True or maxim == 0: #Boucle qui continue tant que le nombre entré n'est pas conforme
    tableau = []
    maxDansTableau = False
    neufDansTableau = False
    longueur = 1
    while longueur != 10: #Boucle vérifiant la longueur
        nombreEntrer = input("Entrer une valeur à dix chiffres avec un nombre maximum compris en un exemplaire et aucun 9: ")
        try:
            longueur = len(nombreEntrer)
            test = int(nombreEntrer)
        except:
            longueur = 1 

    nombreEntrer = int(nombreEntrer)
    div = 1000000000
    nombreGarder = nombreEntrer # Pour la phrase finale
    leNombre=nombreGarder
    maxim=0

    for i in range(0,10,1): #Mise dans un tableau du nombre
        nombreEntrer = floor(nombreGarder / div)
        nombreGarder = nombreGarder - (nombreEntrer * div)
        tableau.append(nombreEntrer)
        div /= 10
        
    maximum=tableau[0]
    for i in range(1,10,1): #For déterminant le maximum
        if tableau[i]>maximum and tableau[i]!=9: 
            maximum=tableau[i]
            maxim=int(maximum)
    tableau.remove(maximum)
    if maxim in tableau: #Verification pour voir si il n'y pas double maxim
        maxDansTableau = True
    if 9 in tableau: #Verification pour voir si il n'y a pas de Neuf
        neufDansTableau = True
    mult= 100000000
    rajout=0
    for i in range (0,9,1): #Petit calcul de conversion du tableau en nombre
        rajout+=tableau[i]*mult
        mult=mult/10

    base=maximum
    resultat=0
    b=8
    for i in range (0,9,1): #Petit calcul pour convertir en base 10
        resultat+=tableau[b]*(maximum**(i))
        b-=1
print(" Le nombre ",leNombre," a pour base ",maximum,".\n Le nombre à convertir est ", rajout,".\n Sa conversion retourne retourne le nombre ",resultat," en base 10.")     
input()




