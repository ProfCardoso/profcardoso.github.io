import time
from random import randint

messagesDebug = False
debugMode = False

J1cooBateau1 = []
J1cooBateau2 = []
J1cooBateau3 = []
J1cooBateau4 = []
J1cooBateau5 = []

J2cooBateau1 = []
J2cooBateau2 = []
J2cooBateau3 = []
J2cooBateau4 = []
J2cooBateau5 = []


plateauJ1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Plateau joueur 1
]

plateauJ2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Plateau joueur 2
]

mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9 #On assigne chaque lettre à un chiffre
}

def printDebug(message):
    if messagesDebug == True:
        print("DEBUG:", message)

def verifPlacement(plateau, taille):
    """
    Vérifie que tous les bateaux ne soient ni placés en diagonale, ni trop grands, ni trop petits et ni chevauchants d'autres bateaux
    """
    lettresAutorisees = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    chiffresAutorises = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    verifTaille = False
    while verifTaille == False:
        cooBateauDebutValide = False
        cooBateauFinValide = False
        while cooBateauDebutValide == False: #Tant que les coordonnees ne sont pas valides : on redemande de les taper
            cooBateauDebut = input(("Donnez les coordonnées du premier point du bateau de taille " + str(taille) + " : "))
            if len(cooBateauDebut) != 2: #si la taille n'est pas égale à 2
                print("Veuillez rentrer des coordonnées valides avec une seule lettre et un seul chiffre !")
            else:
                cooBateauDebut = list(cooBateauDebut) # On met dans une liste les coordonnees, qui sont en string. La lettre est séparée du chiffre
                if cooBateauDebut[0] not in lettresAutorisees or cooBateauDebut[1] not in chiffresAutorises: #On vérifie si les lettres et les chiffres sont valides
                    print("Les caractères ne sont pas valides! Veuillez rentrer une lettre de A à J et un chiffre de 0 à 9 !")
                else:
                    cooBateauDebutValide = True #On sort de la boucle si tout est valide

        while cooBateauFinValide == False:
            cooBateauFin = input(("Donnez les coordonnées du dernier point du bateau de taille " + str(taille) + " : "))
            if len(cooBateauFin) != 2:
                print("Veuillez rentrer des coordonnées valides avec une seule lettre et un seul chiffre !")
            else:
                cooBateauFin = list(cooBateauFin)
                if cooBateauFin[0] not in lettresAutorisees or cooBateauFin[1] not in chiffresAutorises: #On vérifie si les lettres et les chiffres sont valides
                    print("Les caractères ne sont pas valides ! Veuillez rentrer une lettre de A à J et un chiffre de 0 à 9 !")
                else:
                    if cooBateauFin[0] not in cooBateauDebut and cooBateauFin[1] not in cooBateauDebut: #Vérifie si le bateau est bien placé de manière droite (pas en diagonale)
                        print("Le bateau ne peut pas être placé en diagonale !")
                    else:
                        cooBateauFinValide = True #On sort de la boucle si tout est valide
        correspondancePremierPoint = mapping[cooBateauDebut[0]] #On fait le mapping pour que les lettres des points de coordonnées soient adaptées en chiffre
        correspondanceDeuxiemePoint = mapping[cooBateauFin[0]] #On fait le mapping pour que les lettres des points de coordonnées soient adaptées en chiffre
        printDebug("correspondance Premier point : "+ str(correspondancePremierPoint))
        printDebug("correspondance Deuxième point : "+ str(correspondanceDeuxiemePoint))
        printDebug("Bateau debut [1] " + str(cooBateauDebut[1]))
        printDebug("Bateau fin [1] " + str(cooBateauFin[1]))

        #Vérification à l'horizontale
        if cooBateauDebut[1] == cooBateauFin[1]: #Si les chiffres des points de coordonnées sont les mêmes (donc si on est sur la même ligne à l'horizontale)
            if correspondancePremierPoint < correspondanceDeuxiemePoint: #Si la lettre du premier point est plus petite que la lettre du deuxième point
                if taille == correspondanceDeuxiemePoint-correspondancePremierPoint+1:
                    for i in range(correspondancePremierPoint, correspondanceDeuxiemePoint+1): #On vérirife pour chaque case de la ligne
                        if plateau[int(cooBateauDebut[1])] [i] == 1: #Si il y a déjà un bout de bateau
                            print("Il y a un obstacle à l'emplacement de votre bateau, veuillez réessayer")
                            return verifPlacement(plateau, taille) #On relance la fonction du début
                    verifTaille = True #Sinon on continue
                    return cooBateauDebut, cooBateauFin
                else:
                    print("Ces coordonnées ne correspondent pas à un bateau de taille", taille)
            if correspondancePremierPoint > correspondanceDeuxiemePoint: #Si la lettre du premier point est plus grande que la lettre du deuxième point
                if taille == correspondancePremierPoint-correspondanceDeuxiemePoint+1:
                    for i in range(correspondanceDeuxiemePoint, correspondancePremierPoint+1): #On vérifie pour chaque case de la ligne
                        if plateau[int(cooBateauDebut[1])] [i] == 1: #Si il y a déjà un bout de bateau
                            print("Il y a un obstacle à l'emplacement de votre bateau, veuillez réessayer")
                            return verifPlacement(plateau, taille) #On relance la fonction du début
                    verifTaille = True #Sinon on continue
                    return cooBateauDebut, cooBateauFin
                else:
                    print("Ces coordonnées ne correspondent pas à un bateau de taille", taille)

        #Vérification à la verticale
        if cooBateauDebut[0] == cooBateauFin[0]: #Si les lettres des points de coordonnées sont les mêmes (donc si on est sur la même colonne à la verticale)
            if int(cooBateauDebut[1]) < int(cooBateauFin[1]): #Si le chiffre du premier point est plus petit que le chiffre du deuxième point
                if taille == int(cooBateauFin[1])- int(cooBateauDebut[1])+1:
                    for i in range(int(cooBateauDebut[1]), int(cooBateauFin[1]) + 1):
                        if plateau[i] [correspondancePremierPoint] == 1:
                            print("Il y a un obstacle à l'emplacement de votre bateau, veuillez réessayer")
                            return verifPlacement(plateau, taille)
                    verifTaille = True
                    return cooBateauDebut, cooBateauFin
                else:
                    print("Ces coordonnées ne correspondent pas à un bateau de taille", taille)
            if int(cooBateauDebut[1]) > int(cooBateauFin[1]): #Si le chiffre du premier point est plus grand que le chiffre du deuxième point
                if taille == int(cooBateauDebut[1])- int(cooBateauFin[1])+1:
                    for i in range(int(cooBateauFin[1]), int(cooBateauDebut[1]) + 1):
                        if plateau[i] [correspondancePremierPoint] == 1:
                            print("Il y a un obstacle à l'emplacement de votre bateau, veuillez réessayer")
                            return verifPlacement(plateau, taille)
                    verifTaille = True
                    return cooBateauDebut, cooBateauFin
                else:
                    print("Ces coordonnées ne correspondent pas à un bateau de taille", taille)

def ajouterAuPlateau(plateau,cooBateauDebut,cooBateauFin):
    """
    Ajoute toutes les coordonnées des bateaux sur le plateau
    """
    cooBateau = []
    printDebug("On rajoute :"+ str(cooBateauDebut) + str(cooBateauFin))
    if cooBateauDebut[0] == cooBateauFin[0]:
        #bateau à l'horizontale
        printDebug("   Bateau à l'horizontale")
        for i in range (cooBateauDebut[1], cooBateauFin[1]+1):
            printDebug("On rajoute le point " + str(cooBateauDebut[0]) +","+ str(i))
            plateau[cooBateauDebut[0]] [i] = 1
            cooBateau += [[cooBateauDebut[0], i]]
    if cooBateauDebut[1] == cooBateauFin[1]:
        #bateau à la verticale
        printDebug("   Bateau à la verticale")
        for i in range (cooBateauDebut[0], cooBateauFin[0]+1):
            printDebug("On rajoute le point " + str(i) +","+ str(cooBateauDebut[1]))
            plateau[i] [cooBateauDebut[1]] = 1
            cooBateau += [[i, cooBateauDebut[1]]]
    return cooBateau





def affichage(plateauJ1, plateauJ2):
    """
    Affiche le plateau des deux joueurs
    """    
    print("")
    print("       PLATEAU JOUEUR 1")
    print("")
    print("   A  B  C  D  E  F  G  H  I  J")
    for i in range(len(plateauJ1)):
        print(i, end = " ")
        for t in range(len(plateauJ1[i])):
            if plateauJ1[i] [t] == 0 or plateauJ1[i] [t] == 1:
                print(" - ", end = "")
            if plateauJ1[i] [t] == 2:
                print(" • ", end = "")
            if plateauJ1[i] [t] == 3:
                print(" X ", end = "")
        print("")
    print("")
    print("       PLATEAU JOUEUR 2")
    print("")
    print("   A  B  C  D  E  F  G  H  I  J")
    for i in range(len(plateauJ2)):
        print(i, end = " ")
        for t in range(len(plateauJ2[i])):
            if plateauJ2[i] [t] == 0 or plateauJ2[i][t] == 1:
                print(" - ", end="")
            if plateauJ2[i] [t] == 2:
                print(" • ", end = "")
            if plateauJ2[i] [t] == 3:
                print(" X ", end = "")
        print("")

def placement(plateau, taille):
    """
    Demande aux joueurs d'entrer les coordonnées des bateaux qu'ils veulent placer, avec une taille à respecter
    """
    cooBateau = []
    coordonnees = verifPlacement(plateau, taille) #On applique tout le process de verification (on demande au joueur les points, on vérifie si ils sont valides...) et on récupère les coordonnées des deux extrémités du bateau
    printDebug("Voici vos coordonnées : " + str(coordonnees)) #On lui montre ses coordonnées

    #Premier Point
    premierTermePremierPoint = coordonnees[0] [0] #On sélectionne la lettre du premier point
    printDebug("Voici la lettre de votre premier point " + str(premierTermePremierPoint))
    deuxiemeTermePremierPoint = int(coordonnees[0] [1]) #On sélectionne le chiffre du premier point
    correspondancePremierTermePremierPoint = mapping[premierTermePremierPoint] #On transforme la lettre du premier point de coordonnées en un int
    printDebug("Voici le deuxième terme du premier point : " + str(deuxiemeTermePremierPoint))

    #Deuxieme point
    premierTermeDeuxiemePoint = coordonnees[1] [0] #On sélectionne la lettre du deuxième point
    printDebug("Voici la lettre de votre deuxième point : " + str(premierTermeDeuxiemePoint))
    deuxiemeTermeDeuxiemePoint = int(coordonnees [1] [1]) #On sélectionne le chiffre du deuxième point
    correspondancePremierTermeDeuxiemePoint = mapping[premierTermeDeuxiemePoint] #On transforme la lettre du deuxième point de coordonnées en un int
    printDebug("Voici le deuxième terme du deuxième point : " + str(deuxiemeTermeDeuxiemePoint))

    #Placement à l'horizontale
    if deuxiemeTermePremierPoint == deuxiemeTermeDeuxiemePoint: #On vérifie si les point sont sur la même ligne à l'horizontale (si les chiffres des 2 points sont les mêmes)
        if correspondancePremierTermePremierPoint < correspondancePremierTermeDeuxiemePoint: #Si le chiffre qui correspond à la lettre du premier point est plus petit que le chiffre qui correspond à la lettre du deuxième point
            for i in range(correspondancePremierTermePremierPoint, correspondancePremierTermeDeuxiemePoint+1): #Boucle qui va du chiffre qui correspond à la lettre du premier point au chiffre qui correspond à la lettre du deuxième point
                plateau [deuxiemeTermePremierPoint] [i] = 1 #Pour chaque point on place un bout du bateau
                cooBateau = cooBateau + [[deuxiemeTermePremierPoint] + [i]] #On remplie la variable cooBateau qui stocke chaque point de coordonnée de chaque bout du bateau
            printDebug(cooBateau)
        if correspondancePremierTermePremierPoint > correspondancePremierTermeDeuxiemePoint: #Si le chiffre qui correspond à la lettre du premier point est plus grand que le chiffre qui correspond à la lettre du deuxième point
            printDebug(str(correspondancePremierTermePremierPoint) + " " + str(correspondancePremierTermePremierPoint))
            for i in range(correspondancePremierTermeDeuxiemePoint, correspondancePremierTermePremierPoint+1): #Boucle qui va du chiffre qui correspond à la lettre du deuxième point au chiffre qui correspond à la lettre du premier point
                plateau [deuxiemeTermePremierPoint] [i] = 1 #Pour chaque point on place un bout du bateau
                cooBateau = cooBateau + [[deuxiemeTermePremierPoint] + [i]] #On remplie la variable cooBateau qui stocke chaque point de coordonnée de chaque bout du bateau
            printDebug(cooBateau)

    #Placement à la verticale
    if premierTermePremierPoint == premierTermeDeuxiemePoint: #On vérifie si les point sont sur la même colonne à la verticale (si les lettres des 2 points sont les mêmes)
        if deuxiemeTermePremierPoint < deuxiemeTermeDeuxiemePoint: #Si le chiffre du premier point est plus petit que le chiffre du deuxième point
            for i in range(deuxiemeTermePremierPoint, deuxiemeTermeDeuxiemePoint+1): #Boucle qui va du chiffre du premier point au chiffre du deuxième point
                plateau [i] [correspondancePremierTermePremierPoint] = 1 #Pour chaque point on place un bout du bateau
                cooBateau = cooBateau + [[i] + [correspondancePremierTermePremierPoint]] #On remplie la variable cooBateau qui stocke chaque point de coordonnée de chaque bout du bateau
            printDebug(cooBateau)
        if deuxiemeTermePremierPoint > deuxiemeTermeDeuxiemePoint: #Si le chiffre du premier point est plus grand que le chiffre du deuxième point
            for i in range(deuxiemeTermeDeuxiemePoint, deuxiemeTermePremierPoint+1): #Boucle qui va du chiffre du deuxième point au chiffre du premier point
                plateau [i] [correspondancePremierTermePremierPoint] = 1 #Pour chaque point on place un bout du bateau
                cooBateau = cooBateau + [[i] + [correspondancePremierTermePremierPoint]] #On remplie la variable cooBateau qui stocke chaque point de coordonnée de chaque bout du bateau
            printDebug(cooBateau)
    return cooBateau

def tirJoueur(plateau, cooBateau):
    """
    Demande à un des joueurs les coordonnées du point ou il veut tirer sur le plateau de l'adversaire, si il n'a pas déjà tiré à cet emplacement
    """
    verifTir = False
    cooTir = ""
    lettresAutorisees = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    chiffresAutorises = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while verifTir == False :
        cooTir = list(input("Coordonnées du tir : "))
        if len(cooTir) != 2: #si la taille n'est pas égale à 2
            print("Veuillez rentrer des coordonnées valides avec une seule lettre et un seul chiffre !")
        else:
            #cooTir = list(cooTir)
            if cooTir[0] not in lettresAutorisees or cooTir[1] not in chiffresAutorises: #On vérifie si les lettres et les chiffres sont valides
                print("Les caractères ne sont pas valides! Veuillez rentrer une lettre de A à J et un chiffre de 0 à 9 !")
            else:
                cooTir = [int(cooTir[1]), int(mapping[cooTir[0]])]
                if plateau[cooTir[0]][cooTir[1]] == 2 or plateau[cooTir[0]][cooTir[1]] == 3 :
                    print("Vous avez déjà tiré ici ! Réessayez !")
                else:
                    verifTir = True
    printDebug("Coordonnées du tir Joueur" + str(cooTir))
    endroitSurPlateau = plateau[cooTir[0]] [cooTir[1]]
    if endroitSurPlateau == 1:
        printDebug("Le tir est tombé sur un bateau")
        plateau[cooTir[0]] [cooTir[1]] = 3
        cooBateau = supprimerPointBateau(cooTir, cooBateau)
        verifBateauCoule(cooBateau, "Joueur")
    if endroitSurPlateau == 0:
        printDebug("Le tir est tombé dans l'eau")
        plateau[cooTir[0]] [cooTir[1]] = 2
    return plateau, cooBateau

def supprimerPointBateau(cooTir, cooBateaux):
    """
    Enlève des listes les points de bateaux touchés par des tirs adverses
    """
    for bateau in cooBateaux:
        if cooTir in bateau:
            bateau.remove(cooTir)
    return cooBateaux

def verifBateauCoule(cooBateaux, joueur):
    """
    Vérifie si le bateau est coulé afin de l'indiquer aux joueurs
    """
    if joueur == "Joueur":
        for i in range(len(cooBateaux)):
            printDebug("cooBateaux[i]" + str(cooBateaux[i]))
            if all(len(str(sous_liste)) == 0 for sous_liste in cooBateaux[i]): #On vérifie si tous les points du bateaux sont vides
                print("Coulé !")
                cooBateaux[i] = [000]


def verifVictoire(cooBateaux):
    """
    Vérifie s'il reste encore des bateaux aux joueurs
    """
    verif = 0
    for i in range(len(cooBateaux)) :
        if cooBateaux[i] == [000] :
            verif += 1
    if verif == 5 :
        return True

def jeu(plateauJ1, plateauJ2, mapping, J1cooBateau1, J1cooBateau2, J1cooBateau3, J1cooBateau4, J1cooBateau5, J2cooBateau1, J2cooBateau2, J2cooBateau3, J2cooBateau4, J2cooBateau5):
    """
    Réunie toutes les fonctions afin de permettre l'exécution du programme et le lancement du jeu
    """
    print(r"""
    
     _____                                                                   _____
    ( ___ )-----------------------------------------------------------------( ___ )
     |   |                                                                   |   |
     |   |  ____        _        _ _ _        _   _                  _       |   |
     |   | | __ )  __ _| |_ __ _(_) | | ___  | \ | | __ ___   ____ _| | ___  |   |
     |   | |  _ \ / _` | __/ _` | | | |/ _ \ |  \| |/ _` \ \ / / _` | |/ _ \ |   |
     |   | | |_) | (_| | || (_| | | | |  __/ | |\  | (_| |\ V / (_| | |  __/ |   |
     |   | |____/ \__,_|\__\__,_|_|_|_|\___| |_| \_|\__,_| \_/ \__,_|_|\___| |   |
     |___|                                                                   |___|
    (_____)-----------------------------------------------------------------(_____)

    """) #Plus d'interpretation des antislashs (laisser le r)

    time.sleep(2)
    affichage(plateauJ1, plateauJ2)
    
    print("Le joueur 1 commence à placer ses bateaux !")
    time.sleep(1)
    J1cooBateau1 = placement(plateauJ1, 5)
    J1cooBateau2 = placement(plateauJ1, 4)
    J1cooBateau3 = placement(plateauJ1, 3)
    J1cooBateau4 = placement(plateauJ1, 3)
    J1cooBateau5 = placement(plateauJ1, 2)
    print("Au joueur 2 de placer ses bateaux !")
    time.sleep(1)
    J2cooBateau1 = placement(plateauJ2, 5)
    J2cooBateau2 = placement(plateauJ2, 4)
    J2cooBateau3 = placement(plateauJ2, 3)
    J2cooBateau4 = placement(plateauJ2, 3)
    J2cooBateau5 = placement(plateauJ2, 2)
    
    J1cooBateaux = [J1cooBateau1, J1cooBateau2, J1cooBateau3, J1cooBateau4, J1cooBateau5]
    J2cooBateaux = [J2cooBateau1, J2cooBateau2, J2cooBateau3, J2cooBateau4, J2cooBateau5]

    affichage(plateauJ1, plateauJ2)
    time.sleep(1)
    print("Tous les bateaux sont placés !")
    time.sleep(3)
    while True:
        print("Au joueur 1 de tirer !")
        plateauJ2, J2cooBateaux = tirJoueur(plateauJ2,J2cooBateaux)
        time.sleep(0.5)
        if verifVictoire(J2cooBateaux) == True :
            affichage(plateauJ1, plateauJ2)
            print("Le joueur 1 a gagné !")
            return
        print("Au tour du joueur 2 !")
        plateauJ1, J1cooBateaux = tirJoueur(plateauJ1, J1cooBateaux)
        time.sleep(0.5)
        affichage(plateauJ1, plateauJ2)
        if verifVictoire(J1cooBateaux) == True :
            print("Le joueur 2 a gagné !")
            return


jeu(plateauJ1, plateauJ2, mapping, J1cooBateau1, J1cooBateau2, J1cooBateau3, J1cooBateau4, J1cooBateau5, J2cooBateau1, J2cooBateau2, J2cooBateau3, J2cooBateau4, J2cooBateau5)