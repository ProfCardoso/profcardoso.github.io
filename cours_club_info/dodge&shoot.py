# Dodge & Shoot (Pyxel) — 128x128
# Déplacement : flèches (ou ZQSD)
# Tir : ESPACE
# Lancer : ENTREE depuis le menu
# Recommencer : R (game over)
# Quitter : ECHAP
import pyxel
import random

LARGEUR = 128
HAUTEUR = 128

# ----------------------------
# Variables globales du jeu
# ----------------------------
etat = "menu"          # "menu", "jeu", "fin"
meilleur_score = 0

# Joueur
joueur_x = 0
joueur_y = 0
joueur_l = 6
joueur_h = 6
vitesse_joueur = 1.6

# Gameplay
score = 0
vies = 3
invincibilite = 0

# Objets
tirs = []      # liste de dictionnaires {"x":..., "y":..., "vitesse":...}
ennemis = []   # liste de dictionnaires {"x":..., "y":..., "l":..., "h":..., "vitesse":..., "mort":...}

# Timers
frame = 0
cooldown_tir = 0
timer_spawn = 0


# ----------------------------
# Fonctions utilitaires
# ----------------------------
def borne(valeur, mini, maxi):
    """Force valeur à rester entre mini et maxi."""
    if valeur < mini:
        return mini
    if valeur > maxi:
        return maxi
    return valeur


def collision_rectangles(r1, r2):
    """Retourne True si deux rectangles (x,y,l,h) se chevauchent."""
    x1, y1, l1, h1 = r1
    x2, y2, l2, h2 = r2
    return (
        x1 < x2 + l2 and
        x1 + l1 > x2 and
        y1 < y2 + h2 and
        y1 + h1 > y2
    )


# ----------------------------
# Initialisation / reset
# ----------------------------
def reinitialiser_partie():
    """Réinitialise une partie (score, vies, positions, listes...)."""
    global joueur_x, joueur_y, score, vies, invincibilite
    global tirs, ennemis
    global frame, cooldown_tir, timer_spawn

    joueur_x = LARGEUR // 2
    joueur_y = HAUTEUR - 16

    score = 0
    vies = 3
    invincibilite = 0

    tirs = []
    ennemis = []

    frame = 0
    cooldown_tir = 0
    timer_spawn = 0


# ----------------------------
# Création d'objets
# ----------------------------
def creer_tir():
    """Ajoute un tir à la liste."""
    tirs.append({
        "x": joueur_x + joueur_l // 2,
        "y": joueur_y - 2,
        "vitesse": 3.2
    })


def creer_ennemi():
    """Ajoute un ennemi en haut de l'écran."""
    taille = random.choice([5, 6, 7])
    vitesse = 0.8 + random.random() * 0.9 + min(1.2, score * 0.01)
    x = random.randint(0, LARGEUR - taille)

    ennemis.append({
        "x": x,
        "y": -taille,
        "l": taille,
        "h": taille,
        "vitesse": vitesse,
        "mort": False
    })


# ----------------------------
# Mises à jour (logique du jeu)
# ----------------------------
def gerer_menu():
    """Gestion de l'écran menu."""
    global etat
    if pyxel.btnp(pyxel.KEY_RETURN):
        reinitialiser_partie()
        etat = "jeu"


def gerer_fin():
    """Gestion de l'écran de fin."""
    global etat
    if pyxel.btnp(pyxel.KEY_R):
        reinitialiser_partie()
        etat = "jeu"
    # option : retour menu si besoin (ENTREE)
    # if pyxel.btnp(pyxel.KEY_RETURN):
    #     etat = "menu"


def deplacer_joueur():
    """Met à jour la position du joueur selon le clavier."""
    global joueur_x, joueur_y

    dx = 0
    dy = 0

    if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
        dx -= 1
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
        dx += 1
    if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
        dy -= 1
    if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
        dy += 1

    joueur_x += dx * vitesse_joueur
    joueur_y += dy * vitesse_joueur

    joueur_x = borne(joueur_x, 0, LARGEUR - joueur_l)
    joueur_y = borne(joueur_y, 0, HAUTEUR - joueur_h)


def gerer_tirs():
    """Création + déplacement + suppression des tirs."""
    global cooldown_tir, tirs

    # Tir (avec cooldown)
    if pyxel.btnp(pyxel.KEY_SPACE) and cooldown_tir == 0:
        creer_tir()
        cooldown_tir = 6

    # Déplacement
    for tir in tirs:
        tir["y"] -= tir["vitesse"]

    # Suppression hors écran
    tirs = [t for t in tirs if t["y"] > -4]


def gerer_ennemis():
    """Apparition + déplacement + suppression des ennemis."""
    global timer_spawn, ennemis

    timer_spawn += 1
    frequence = max(10, 40 - score // 2)  # plus le score monte, plus ça spawn vite

    if timer_spawn >= frequence:
        timer_spawn = 0
        creer_ennemi()

    for ennemi in ennemis:
        ennemi["y"] += ennemi["vitesse"]

    ennemis = [e for e in ennemis if e["y"] < HAUTEUR + 8]


def collisions_tirs_ennemis():
    """Gère les collisions entre tirs et ennemis."""
    global tirs, ennemis, score

    nouveaux_tirs = []

    for tir in tirs:
        rect_tir = (tir["x"], tir["y"], 2, 3)
        touche = False

        for ennemi in ennemis:
            rect_ennemi = (ennemi["x"], ennemi["y"], ennemi["l"], ennemi["h"])
            if collision_rectangles(rect_tir, rect_ennemi):
                ennemi["mort"] = True
                score += 1
                touche = True
                break

        if not touche:
            nouveaux_tirs.append(tir)

    tirs = nouveaux_tirs
    ennemis = [e for e in ennemis if not e["mort"]]


def collisions_joueur_ennemis():
    """Gère les collisions entre le joueur et les ennemis."""
    global vies, invincibilite, ennemis

    if invincibilite > 0:
        return

    rect_joueur = (joueur_x, joueur_y, joueur_l, joueur_h)

    for ennemi in ennemis:
        rect_ennemi = (ennemi["x"], ennemi["y"], ennemi["l"], ennemi["h"])
        if collision_rectangles(rect_joueur, rect_ennemi):
            vies -= 1
            invincibilite = 30  # demi-seconde environ
            ennemi["mort"] = True
            break

    ennemis = [e for e in ennemis if not e["mort"]]


def mettre_a_jour_jeu():
    """Logique complète quand on est en 'jeu'."""
    global frame, cooldown_tir, invincibilite, etat, meilleur_score

    frame += 1

    if cooldown_tir > 0:
        cooldown_tir -= 1
    if invincibilite > 0:
        invincibilite -= 1

    deplacer_joueur()
    gerer_tirs()
    gerer_ennemis()
    collisions_tirs_ennemis()
    collisions_joueur_ennemis()

    if vies <= 0:
        meilleur_score = max(meilleur_score, score)
        etat = "fin"


def update():
    """Fonction Pyxel appelée à chaque frame (logique)."""
    if etat == "menu":
        gerer_menu()
    elif etat == "fin":
        gerer_fin()
    else:
        mettre_a_jour_jeu()


# ----------------------------
# Affichage
# ----------------------------
def afficher_menu():
    pyxel.text(32, 30, "DODGE & SHOOT", 7)
    pyxel.text(24, 50, "ENTREE : jouer", 6)
    pyxel.text(16, 62, "Fleches / ZQSD : bouger", 13)
    pyxel.text(16, 72, "ESPACE : tirer", 13)


def afficher_fin():
    pyxel.text(40, 36, "GAME OVER", 8)
    pyxel.text(36, 54, f"Score : {score}", 7)
    pyxel.text(30, 66, f"Meilleur : {meilleur_score}", 10)
    pyxel.text(22, 90, "R : recommencer", 6)


def afficher_jeu():
    # HUD
    pyxel.text(2, 2, f"Score:{score}", 7)
    pyxel.text(88, 2, f"Vies:{vies}", 7)

    # Joueur (clignote si invincibilité)
    if invincibilite == 0 or (frame // 3) % 2 == 0:
        couleur = 11
    else:
        couleur = 1
    pyxel.rect(int(joueur_x), int(joueur_y), joueur_l, joueur_h, couleur)

    # Tirs
    for tir in tirs:
        pyxel.rect(int(tir["x"]), int(tir["y"]), 2, 3, 10)

    # Ennemis
    for ennemi in ennemis:
        pyxel.rect(int(ennemi["x"]), int(ennemi["y"]), ennemi["l"], ennemi["h"], 8)


def draw():
    """Fonction Pyxel appelée à chaque frame (affichage)."""
    pyxel.cls(0)

    if etat == "menu":
        afficher_menu()
    elif etat == "fin":
        afficher_fin()
    else:
        afficher_jeu()


# ----------------------------
# Lancement
# ----------------------------
pyxel.init(LARGEUR, HAUTEUR, title="Dodge & Shoot")
pyxel.mouse(False)
reinitialiser_partie()  # on prépare une partie, mais on démarre en menu
etat = "menu"
pyxel.run(update, draw)