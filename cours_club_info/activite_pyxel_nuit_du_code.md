# 🕹️ Découverte de Pyxel – Entraînement à La Nuit du Code
**Première NSI – Python / Programmation de jeux**

# Pyxel : l’essentiel à connaître avant de coder

Pyxel est une bibliothèque Python spécialisée dans la création de **jeux rétro 2D**.  
Un jeu Pyxel repose toujours sur **la même structure**.


## Règles importantes (La Nuit du Code)

Rappel de quelques règles pour la Nuit du Code:

- Taille de fenêtre : 128 × 128

- Pas de copier-coller depuis Internet

- Le jeu doit être jouable

- Une description + mode d’emploi est obligatoire

## Matériel / environnement (à préparer)

Option recommandée (plus simple) :

- Pyxel Studio [(en ligne)](https://www.pyxelstudio.net/) : La Nuit du Code recommande désormais d’utiliser “Pyxel Studio” (version plus récente + console d’erreurs). **ATTENTION** : N'oubliez pas d'enregistrer/noter le lien de votre projet lors de la création de votre jeu !! 

Option locale (via un terminal de commande ou depuis Edupython/Thonny)

- Installer Pyxel via `pip install -U pyxel` ou depuis la gestion d'import de votre logiciel


**Bonus :** vous pouvez récuperer des exemples de jeu pyxel via la commande : `pyxel copy_examples` (copie des scripts d’exemples)

---

## Structure minimale d’un jeu Pyxel

```python
import pyxel # import de la bibliothèque pyxel pour coder votre jeu

def update():
    """
    logique du jeu (calculs, déplacements, collisions)
    """
    pass

def draw():
    """
    affichage à l’écran
    """
    pyxel.cls(0)

pyxel.init(128, 128, title="Mon jeu") # crée la fenêtre du jeu, ici une fenêtre de 128 par 128 pixel, avec pour titre "Mon jeu"

pyxel.run(update, draw) # lance la boucle du jeu, avec en paramètre les fonctions de jeu et de dessin
```


## Fenêtre et affichage

|Fonction|	Rôle|
|:------|:-----|
|pyxel.init(w, h, title="")|	Initialise la fenêtre|
|pyxel.cls(c)|	Efface l’écran avec la couleur c|
|pyxel.text(x, y, txt, c)|	Affiche du texte|
|pyxel.rect(x, y, w, h, c)|	Rectangle plein|
|pyxel.circ(x, y, r, c)|	Cercle plein|

👉 Les couleurs sont numérotées de 0 à 15.

## Gestion du clavier et de la souris

### Clavier

|Fonction|	Descriptions|
|:------|:-----|
|pyxel.btn(KEY)|	Touche maintenue|
|pyxel.btnp(KEY)|	Appui unique|

**Exemples :**

```python
pyxel.btn(pyxel.KEY_RIGHT)
pyxel.btnp(pyxel.KEY_SPACE)
```

### Souris

**Exemples :**
```python
pyxel.mouse_x
pyxel.mouse_y
pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
```


## Variables et logique de jeu
Les jeux Pyxel utilisent :

- des variables (position, score, vies)

- des listes (ennemis, tirs, objets)

- parfois des états de jeu

**Exemple :**

```python
state = "menu"  # menu, play, gameover
score = 0
lives = 3
```
## Des fonctions utiles :

### Collisions (principe simple)

Modéliser les collision entre deux rectangles de tailles différentes:

```python
# x, y sont les positions
# w, h sont les largeurs et hauteurs

def collision(x1, y1, w1, h1, x2, y2, w2, h2):
    """Retourne True si deux rectangles (1 et 2) se chevauchent."""
    return (
        x1 < x2 + w2 and
        x1 + w1 > x2 and
        y1 < y2 + h2 and
        y1 + h1 > y2
    )
```

### Borne 

Fixer des valeurs pour ne pas dépasser les limites (de l'écran ou autre).

```python
def borne(valeur, mini, maxi):
    """Force valeur à rester entre mini et maxi."""
    if valeur < mini:
        return mini
    if valeur > maxi:
        return maxi
    return valeur

```

## Phase 1 – Découverte de jeux Pyxel existants

### Activité 1 : Lecture d’exemples Pyxel

Consigne:
- Lance plusieurs jeux Pyxel d’exemple

- Observe le code

- Complète la fiche ci-dessous (sur une feuille de papier) 🖋️

<div style="display: flex; flex-direction:column;  border: 1px solid #ccc; text-align: center;">
  <strong>Fiche d’observation</strong>
</div>
<div style="display: flex; flex-direction:column;  border: 1px solid #ccc; text-align: left;">
<p>
    1/ Où sont définies les variables principales ?
</p>
<p>
    2/ Que fait la fonction update() ?
</p>
<p>
    3/ Que fait la fonction draw() ?
</p>
<p>
    4/ Comment le joueur est-il contrôlé ?
</p>
<p>
    5/ Quelle idée pourrais-tu réutiliser ?
</p>
</div>


### Activité 2 : Inspiration Nuit du Code
1. Regarde des jeux réalisés lors de précédentes éditions :

2. Quel est l’objectif du jeu ?

3. Quelles sont les commandes ?

4. Qu’est-ce qui rend le jeu intéressant ou amusant ?

## Phase 2 – Création guidée d’un jeu simple

### 🎮 Jeu proposé : « Dodge & Shoot » : Cahier des charges

- Joueur déplaçable

- Ennemis qui apparaissent

- Tirs

- Score

- Vies

- Écran de fin

### Base du jeu

Dans les codes proposés par la suite, nous n'utiliserons pas la Programmation Orientée Objet, car cette dernière n'est pas au programme de Première, mais vous pouvez tout à fait l'utiliser de votre côté !

#### Étape 1 : Fenêtre + États de jeu

Le jeu devra être une alternance entre plusieurs états : Menu -> Jeu -> GameOver -> Menu -> ... . Il faudra donc avoir une **variable globale** pour stocker l'état du jeu actuel.

1. Ecrire la fonction pour créer la fenêtre de jeu de 128 par 128.

2. Ecrire la fonction pour afficher le menu (état Menu).

3. Ecrire la fonction pour lancer la page de jeu (état Jeu).

4. Ecrire la fonction de fin du jeu. Vous pouvez faire deux variantes, une pour une victoire et une pour une défaite (état GameOver).

👉 Ces fonctions devront être utilisé dans la fonction `draw` de la bibliothèque Pyxel.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution:</u></summary>
  <div style="margin-top: 10px;">
    <p>Afficher le jeu</p>
    <pre><code>
    LARGEUR = 128
    HAUTEUR = 128
    pyxel.init(LARGEUR, HAUTEUR, title="Dodge & Shoot")
    </code></pre>
    <p>Afficher le menu</p>
    <pre><code>
    # etat de base du jeu : "menu"
    etat = "menu"          # différents etats : "menu", "jeu", "fin"
    def afficher_menu():
        pyxel.text(32, 30, "DODGE & SHOOT", 7)
        pyxel.text(24, 50, "ENTREE : jouer", 6)
        pyxel.text(16, 62, "Fleches / ZQSD : bouger", 13)
        pyxel.text(16, 72, "ESPACE : tirer", 13)
    </code></pre>
    <p>Afficher le jeu</p>
    <pre><code>
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
    </code></pre>
    <p>Afficher la fin du jeu</p>
    <pre><code>
    def afficher_fin():
        pyxel.text(40, 36, "GAME OVER", 8)
        pyxel.text(36, 54, f"Score : {score}", 7)
        pyxel.text(30, 66, f"Meilleur : {meilleur_score}", 10)
        pyxel.text(22, 90, "R : recommencer", 6)
    </code></pre>
    <p>Fonction drawn</p>
    <pre><code>
    def draw():
        """Fonction Pyxel appelée à chaque frame (affichage)."""
        pyxel.cls(0)
        if etat == "menu":
            afficher_menu()
        elif etat == "fin":
            afficher_fin()
        else:
            afficher_jeu()
    </code></pre>
  </div>
</details>

___

#### Étape 2 : Le joueur

Ici, dans le but de faire un jeu simple, nous nous contenterons de creer un personnage pouvant se déplacer de gauche à droite de l'écran. Pour ce faire, nous allons utiliser les touches du clavier pour "bouger" le personnage. Dans la suite du jeu, nous devrons utiliser sa position et sa taille pour calculer les collisions, n'oubliez pas de les stocker dans des variables !

5. Ecrire une fonction `deplacer_joueur` qui déplace votre personnage contrôlé par les flèches. Cette fonction devra être utilisé dans la fonction `update` pour mouvoir le joueur. N'oubliez pas de "dessiner" votre joueur !

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Déplacement joueur (utilisation de variables globales):</p>
    <pre><code>
    # Joueur
    joueur_x = 0
    joueur_y = 0
    joueur_l = 6
    joueur_h = 6
    vitesse_joueur = 1.6
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
    </code></pre>
  </div>
</details>


#### Étape 3 : Affichage du score et des vies

Pour rendre votre jeu plus amusant, il peut être intéressant d'ajouter un score et des vies à votre jeu.

6. Créer les variables globales `score` et `vies`, initialisées aux valeurs de votre choix.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Gameplay</p>
    <pre><code>
    # Gameplay
    score = 0
    vies = 3
    </code></pre>
  </div>
</details>

#### Étape 4 : Tirs

Les tirs de votre personnage doivent être ajoutés et supprimés au fur et à mesure de la partie. Pour ce faire, vous allez programmer une fonction qui tir avec la barre espace, ajoute à une **liste de projectile** ce tir, et le supprime lorsque celui-ci sort de l'écran ou touche un ennemie. 

Voici un exemple de comment représenter un tir (sous la forme de liste ou de dictionnaire) :

- position (x,y)
- taille (hauteur, largeur)
- vitesse

7. Ecrire une fonction `creer_tir` qui ajoute à une liste le nouveau tir à partir de la position du joueur.

8. Ecrire une fonction `gerer_tir` qui  :

- lors de la pression de la touche espace, crée le tir
- déplace les autres tirs
- supprime les tirs en dehors de l'écran

👉 Vous pouvez ajouter un "cooldown" entre chaque tir pour éviter de remplir l'écran.

## Reponse caché code
<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Creer les tirs :</p>
    <code>
    # Objets
    tirs = []      # liste de dictionnaires {"x":..., "y":..., "vitesse":...}
    ennemis = []   # liste de dictionnaires {"x":..., "y":..., "l":..., "h":..., "vitesse":..., "mort":...}
    # Timers
    frame = 0
    cooldown_tir = 0
    timer_spawn = 0
    def creer_tir():
    """Ajoute un tir à la liste."""
    tirs.append({
        "x": joueur_x + joueur_l // 2,
        "y": joueur_y - 2,
        "vitesse": 3.2
    })
    </code>
    <p>Gerer les tirs :</p>
    <code>
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
    </code>
  </div>
</details>

#### Étape 5 : Ennemis

Tout comme votre personnage et les tirs, il faudra créer et faire apparaître des ennemies, de taille et positions différentes. 

9. Ecrire une fonction `creer_ennemi` qui fait apparaître un ennemie dans le jeu. 

Une fois créés, il faut les déplacer :

10. Ecrire une fonction `gerer_ennemis`qui :

- fais apparaître les ennemies (utiliser la fonction `creer_ennemi`) ,
- déplace les ennemies encore en vie,
- supprime les ennemis au bout de l'écran.

👉 Vous pouvez ajouter un "timer" ou une "fréquence" entre l'apparition de chaque ennemie.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Creer un ennemi</p>
    <code>
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
    </code>
    <p>Gerer les ennemis</p>
    <code>
    def gerer_ennemis():
        """Apparition + déplacement + suppression des ennemis."""
        global timer_spawn, ennemis

        # Apparition d'un ennemie au bout d'un certain temps
        timer_spawn += 1
        frequence = max(10, 40 - score // 2)  # plus le score monte, plus ça spawn vite
        if timer_spawn >= frequence:
            timer_spawn = 0
            creer_ennemi()

        # Déplace chaque ennemis
        for ennemi in ennemis:
            ennemi["y"] += ennemi["vitesse"]

        # Change la liste de tous les ennemis pour ne garder que ceux dans l'écran 
        ennemis = [e for e in ennemis if e["y"] < HAUTEUR + 8]
    </code>
  </div>
</details>

#### Étape 6 : Collisions

Il existe deux types de collisions dans le jeu :

- Le tir touche un ennemi → +1 point

- Un ennemi touche le joueur → -1 vie

11. Ecrire une fonction `collisions_tirs_ennemis` qui supprime les ennemies touchés par des tirs 

12. Ecrire une fonction `collisions_joueur_ennemis` qui supprime les ennemies qui touchent le personnage du joueur et enlève une vie à ce dernier.

👉 Vous pouvez ajouter une "frame" d'invincibilité à votre joueur pour éviter les coups consécutifs.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Fonction collision qui permet de calculer si deux entités entre en collision selon leur position et leur taille :</p>
    <code>
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
    </code>
    <p>Collisions entre nos tirs et les ennemies</p>
    <code>
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
    </code>
    <p>Collisions entre le joueur et les ennemies</p>
    <code>
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
    </code>
  </div>
</details>


#### Étape 7 : Mettre à jour le jeu

Maitenant que toute nos fonctions sont créées, il faut les utiliser dans notre boucle de jeu. 

13. Pour cela, vous allez créer une fonction `mettre_a_jour_jeu` sera utilisé dans la fonction `update` et qui s'occupera de lancer toute les fonctions de déplacement, de collisions, de tirs, etc etc pour que le jeu fonctionne. Lorsque les vies sont à zéro, on lance l'écran de fin.

👉 Attention ! Le code se lit de haut en bas, il existe donc un ordre dans les fonctions qui vont être exécuté ! 

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Mettre à jour le jeu :</p>
    <code>
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
        # Suite du code dans la prochaine partie
        ...
    </code>
  </div>
</details>

#### Étape 8 : Game Over

Enfin, lorsque les vies du joueur sont à zéro, on stoppe le jeu, et on lance l'écran de fin, qui affiche le score du joueur. N'oubliez pas de réinitialiser score et vie pour une prochaine partie !

10. Améliorer la fonction `mettre_a_jour_jeu` pour lancer la page de fin (GameOver) quand les vies du joueur arrivent à 0  !
    
👉 Amélioration possible : ajouter le score s'il est meilleur que celui précédent uniquement.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Mettre à jour le jeu :</p>
    <code>
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
    </code>
  </div>
</details>

### Dodge & Shoot

Voici le code du jeu fonctionel après toute les étapes précédentes :

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Cliquez ICI :</u></summary>
  <div style="margin-top: 10px;">
    <p>
        Le lien pour télécharger le fichier : <a href="./dodge&shoot.py" target="_blank">Dodge & Shoot</a> .
    </p>
    <pre><code class="language-python">
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
    </code></pre>
  </div>
</details>
