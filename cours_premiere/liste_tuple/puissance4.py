# TP BONUS : PUISSANCE 4

def creer_plateau():
    '''
    Créer et renvoie une liste de listes d'éléments vides " "
    de 7 de largeur sur 6 de hauteur
    '''
    pass


def verifier_lignes(plateau,joueur):
    '''
    Vérifie dans un plateau si le symbole d'un joueur donné en
    paramètre forme une ligne de 4 dans chacunes des lignes,
    et renvoie True si oui, False sinon.
    '''
    pass

def verifier_colonnes(plateau, joueur):
    '''
    Vérifie dans un plateau si le symbole d'un joueur donné en
    paramètre forme une ligne de 4 dans chacunes des colonnes,
    et renvoie True si oui, False sinon.
    '''
    pass

def verifier_diagonales_descendantes(plateau, joueur):
    '''
    Verifie dans un plateau si le symbole d'un joueur donné en
    paramètre forme une ligne de 4 dans chacunes des diagonales descendantes,
    et renvoie True si oui, False sinon.
    '''
    pass
                
                
def verifier_diagonales_montantes(plateau, joueur):
    '''
    Verifie dans un plateau si le symbole d'un joueur donné en
    paramètre forme une ligne de 4 dans chacunes des diagonales montantes,
    et renvoie True si oui, False sinon.
    '''
    pass
                    
def verifier_victoire(plateau, joueur):
    '''
    Lance chaque fonctions de vérifications de conditions de victoires,
    et renvoie True si un des joueurs, donné en paramètre, gagne sur le plateau,
    donné en paramètre.
    '''
    # Vérifier les lignes

    # Vérifier les colonnes

    # Vérifier les diagonales descendantes

    # Vérifier les diagonales montantes

    return False

def placer_pion(plateau, colonne, joueur):
    '''
    Place le pion du joueur donné en paramètre dans la colonne donné
    en paramètre sur le plateau. Si il est possible de placer le pion,
    la fonction renverra True, False sinon.
    '''
    pass

def afficher_plateau(plateau):
    '''
    Fonction qui affiche le plateau donné en paramètre et qui ne renvoie rien
    '''
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * (7 + 2 * (len(plateau[0]) - 1)))

def jouer():
    '''
    Fonction de jeu du puissance 4
    '''
    plateau = creer_plateau()
    joueurs = ["X", "O"]
    tour = 0

    while True:
        joueur_actuel = joueurs[tour % 2]

        afficher_plateau(plateau)

        colonne = int(input(f"Joueur {joueur_actuel}, choisissez une colonne (0-6) : "))

        if 0 <= colonne <= 6 and placer_pion(plateau, colonne, joueur_actuel):
            if verifier_victoire(plateau, joueur_actuel):
                afficher_plateau(plateau)
                print(f"Le joueur {joueur_actuel} a gagné !")
                break
            elif all(plateau[i][colonne] != " " for i in range(len(plateau))):
                afficher_plateau(plateau)
                print("Match nul !")
                break
            else:
                tour += 1
        else:
            print("Colonne invalide. Veuillez choisir une colonne entre 0 et 6.")


if __name__ == "__main__":
    jouer()
