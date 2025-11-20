import pygame
import sys
from puissance4 import *

# A ne lancer qu'après avoir terminé le fichier puissance4

# Définir les constantes
LARGEUR_CASE = 100
HAUTEUR_CASE = 100
TAILLE_PLATEAU = (7, 6)
COULEUR_FOND = (0, 0, 0)
COULEUR_GRILLE = (255, 255, 255)
COULEUR_JOUEUR1 = (255, 0, 0)
COULEUR_JOUEUR2 = (0, 0, 255)

def afficher_plateau_ecran(plateau, surface):
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            pygame.draw.rect(surface, COULEUR_GRILLE, (j * LARGEUR_CASE, i * HAUTEUR_CASE, LARGEUR_CASE, HAUTEUR_CASE))
            pygame.draw.circle(surface, COULEUR_FOND, (j * LARGEUR_CASE + LARGEUR_CASE // 2, i * HAUTEUR_CASE + HAUTEUR_CASE // 2), min(LARGEUR_CASE, HAUTEUR_CASE) // 2 - 5)
            if plateau[i][j] == "X":
                pygame.draw.circle(surface, COULEUR_JOUEUR1, (j * LARGEUR_CASE + LARGEUR_CASE // 2, i * HAUTEUR_CASE + HAUTEUR_CASE // 2), min(LARGEUR_CASE, HAUTEUR_CASE) // 2 - 10)
            elif plateau[i][j] == "O":
                pygame.draw.circle(surface, COULEUR_JOUEUR2, (j * LARGEUR_CASE + LARGEUR_CASE // 2, i * HAUTEUR_CASE + HAUTEUR_CASE // 2), min(LARGEUR_CASE, HAUTEUR_CASE) // 2 - 10)

def main():
    pygame.init()

    largeur_fenetre = TAILLE_PLATEAU[1] * LARGEUR_CASE
    hauteur_fenetre = TAILLE_PLATEAU[0] * HAUTEUR_CASE
    taille_fenetre = (largeur_fenetre, hauteur_fenetre)

    fenetre = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Puissance 4")

    plateau = creer_plateau()
    joueur_actuel = "X"

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                colonne = event.pos[0] // LARGEUR_CASE
                if 0 <= colonne <= 6 and placer_pion(plateau, colonne, joueur_actuel):
                    if verifier_victoire(plateau, joueur_actuel):
                        print(f"Le joueur {joueur_actuel} a gagné !")
                        pygame.quit()
                        sys.exit()
                    else:
                        joueur_actuel = "O" if joueur_actuel == "X" else "X"

        fenetre.fill(COULEUR_FOND)
        afficher_plateau_ecran(plateau, fenetre)
        pygame.display.flip()

        clock.tick(30)  # Limiter le taux de rafraîchissement à 30 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
