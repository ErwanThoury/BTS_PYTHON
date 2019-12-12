from random import*
from math import*
distance=0 #Entrer dans la boucle
while distance <= 15 or distance >= 100:
    distance=int(input("Entrez la distance avec la porte: ")) #Entrer valeur entre 15(non compris) et 100(non compris également)
pas= randint(4,7) #Sélection nombre de pas max
gagne=pas+1 #Pour distance gagnante
print("Il y a ",distance,"pas de distance, il faut que vous fassiez au maximum ",pas," pas chacun votre tour, bonne CHANCE")
print("------------------------------------------------------------------")
distanceRest=distance #Distance restante pour plus tard
nbPas=0 #Entrer dans la boucle
joueurUn=False
while distanceRest >= 0: #Tant que personne ne FRANCHIT la porte (-1), la boucle continue
    while nbPas<1 or nbPas>pas:
        print("Entrez un nombre de pas entre 1 et",pas)
        nbPas=int(input())
    distanceRest=distanceRest - nbPas #Avancée
    print("Vous avez avancé de",nbPas,"pas, il reste",distanceRest,"de distance")
    nbPas=0 #Réentrer dans la boucle while pour le prochain tour
    print("------------------------------------------------------------------")
    if distanceRest<0:
        print("Bien joué vous avez obtenu la liberté!")
        print("------------------------------------------------------------------")
        joueurUn=True #si True, fin de boucle

    distanceAlt=distanceRest+1 #distance alternative afin de faire gagner ordi   
    if joueurUn==False:
        adversaireGagnant=distanceRest-pas #test victoire
        if adversaireGagnant<0:
            nbPasAd=pas
        else:
           nbPasAd=1 #nombre de pas si on est le laisse sur pos gagnante 
           for i in range(1,gagne,1): #Test de tous les pas
               distanceAlt = distanceAlt-1
               test=distanceAlt%gagne
               if test == 0:
                   nbPasAd = i #Si l'adversaire peut gagner, il gagne
        distanceRest=distanceRest - nbPasAd
        print("Votre adversaire avance de ",nbPasAd," pas, il reste ",distanceRest," pas à faire")
        print("------------------------------------------------------------------")
        if distanceRest<0:
            print("Aie aie aie, c'est le joueur adverse qui sort libre de votre rencontre, pas de CHANCE")
            print("------------------------------------------------------------------")
print("C'est la fin, le roi s'est bien amusé grace à vous")
fin=input("------------------------------------------------------------------")

