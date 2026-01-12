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
## Collisions (principe simple)

Collision entre deux rectangles :

```python
def collision(x1, y1, w1, h1, x2, y2, w2, h2):
    return (
        x1 < x2 + w2 and
        x1 + w1 > x2 and
        y1 < y2 + h2 and
        y1 + h1 > y2
    )
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

#### Étape 1 : Fenêtre + joueur

1. Ecrire la fonction pour créer la fenêtre de jeu de 128 par 128.


2. Ecrire une fonction `joueur` qui affiche un carré contrôlé par les flèches. Cette fonction devra être utilisé dans la fonction `update` pour afficher le joueur. N'oubliez pas de "dessiner" votre joueur !

#### Étape 2 : États de jeu

Le jeu devra être une alternance entre plusieurs états : Menu -> Jeu -> GameOver -> Menu -> ... . Il faudra donc avoir une **variable globale** pour stocker l'état du jeu actuel.

3. Ecrire la fonction pour afficher le menu (état Menu).

4. Ecrire la fonction pour lancer la page de jeu (état Jeu).

5. Ecrire la fonction de fin du jeu. Vous pouvez faire deux variantes, une pour une victoire et une pour une défaite (état GameOver).

#### Étape 3 : Affichage du score et des vies
score

vies

#### Étape 4 : Tirs
Liste de projectiles

Tir avec la barre espace

#### Étape 5 : Ennemis
Apparition régulière

Déplacement automatique

#### Étape 6 : Collisions
Tir → ennemi → +1 point

Ennemi → joueur → -1 vie

#### Étape 7 : Game Over
Affichage du score final

Possibilité de recommencer
