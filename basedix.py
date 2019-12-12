from math import *
tab = ["2",2,"2",2,"3",3,"4",4,"5",5,"6",6,"7",7,"8",8,"9",9,"A",10,"B",11,"C",12,"D",13,"E",14,"F",15,"G",16]#Tableau pour convertir en Chiffre
tabe = ["A","B","C","D","E","F","G"]#Tableau pour convertir en lettre
long = 1
base = 2
while long != 10 or base not in tab or non == True:
    #Tant que la taille de la donnée entrée n'est pas assez longue ou que la base n'est pas dans le tableau ou tant qu'il y a une lettre dans le nombre à convertir
    a = input("Entrer une valeur à dix chiffres: ")
    if a:
        try: #Permet de le faire uniquement si il n'y a pas d'erreur
            long = len(a) #Donnée utile pour le WHILE
            base = a[0] #base = premier terme de a
            base = tab.index(base) #Recherche dans le tableau
            base = base + 1 #Convertion en nombre
            base = int(tab[base]) #Définition de la base
            conv = int(a[1:]) #Chaine à convertir 
            non = False #Deblocage
        except:
            print("pas de CHANCE vous devez entrer comme premier caractère la base (de 2 à G) et pour les 9 autres caractères uniquement des chiffres!")
            non = True #Retour au while

nombre = conv #Utile pour la fin du programme

resultat = "" #Création de la variable resultat pour final
tableau = [] #Création du tableau pour final

while (conv != 0): #Tant que conv n'est pas égale à 0, ça continue
    reste = conv%base
    if reste > 9:
        for r in range (10,17,1):
            if reste == r:
                    reste = conv%base
                    restaff = tabe[r-10]
                    conv = floor(conv/base)
                    tableau.append(str(restaff))
                    reste = 0
                    restaff = 0
    else:
            reste = conv%base
            conv = floor(conv / base)
            tableau.append(str(reste))
pos = len(tableau)
for i in range (1,len(tableau) + 1,1):
    pos -= 1 
    resultat += str(tableau[pos])
if nombre == 0:
    print(" Le nombre " , a , " a pour base " , base , "\n" , "Le nombre à convertir est " , nombre , "\n" , "Sa conversion retourne le nombre 0 en base " , base)   
else:
    print(" Le nombre " , a , " a pour base " , base , "\n" , "Le nombre à convertir est " , nombre , "\n" , "Sa conversion retourne le nombre" , resultat , " en base " , base)   

input()
