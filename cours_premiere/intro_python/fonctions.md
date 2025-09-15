---
title: Initialisation à Python
---

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Les Fonctions

## Quelques fonctions natives

### Application

Dans un programme en python, proposer différentes instructions de façon à compléter le tableau ci-dessous, en précisant :

- la fonction native de python,
- le type de la valeur renvoyée,
- une description de la fonction.


|Fonction native |	Type de la valeur renvoyée |	Description |
|:---:|:---:|:---:|
|`int("mot")`	|   |   |
|`chr(97)`	|   |   |		
|`len("Abracadabra")`	|   |   |		
|`abs(-15)`	|   |   |
|`max(21,6)`|   |   |
|`round(3.1416)` |   |   |
|`round(3.1416,3)`	|  |   |
|     |   |   |


## Les Modules

Un module Python est un fichier contenant du code Python, généralement avec une extension `.py`, qui regroupe des fonctions, des classes, des variables ou des instructions exécutables.  
Ce fichier peut être importé et utilisé dans d'autres scripts ou projets pour organiser, réutiliser et maintenir le code de manière plus efficace.  
Un module peut être importé dans un autre fichier à l'aide de l'instruction `import`, et ses éléments peuvent être utilisés en les préfixant par le nom du module suivi d'un point.

**Exemple :**
```python
import math

# Programme principal
rayon = 5
surface_disque = math.pi * rayon ** 2
```

Voici quelques modules disponibles sur python :
- `math` ( fournit un ensemble de fonctions mathématiques, de constantes communes et de fonctions d'utilité pour effectuer des calculs mathématiques avancés )
- `random` ( permet de générer des nombres pseudo-aléatoires et d'effectuer diverses opérations aléatoires dans les programmes )
- `time` ( permet de manipuler et de travailler avec le temps, offrant des fonctionnalités essentielles pour l'obtention de l'heure actuelle, la suspension de l'exécution du programme, le contrôle de la durée d'exécution, la gestion du temps pour les tâches planifiées, ou encore la mesure des performances )
- `turtle` ( permet de dessiner des figures géométriques et des motifs de manière simple en contrôlant une « tortue » virtuelle sur un écran )
- ...  

### Applications

**Application 1**  
Écrire un programme qui affiche la racine carrée de 2, 3, 4 et 15129.

**Application 2**  
Écrire un programme qui affiche 3 nombres aléatoires compris entre 0 et 99.

**Application 3**  
Le module time contient, entre autres, la fonction sleep qui prend en paramètre une durée en seconde et permet de faire une pause dans l'exécution du programme.

Écrire un programme qui permet d'afficher, toute les secondes, les nombres 1, puis 2, puis 3, puis 4 et enfin 5.

## Vos fonctions

Pour écrire une fonction en Python, commencez par utiliser le mot-clé `def`, suivi du nom de la fonction, des parenthèses pour les paramètres (s'ils existent), et un deux-points. Le corps de la fonction, qui contient les instructions à exécuter, doit être indenté.

### Fonction simple

```python
# Définition de la fonction
def foo():
    # Code de la fonction

# Programme principal
foo()
```

### Fonction avec paramètres

```python
# Définition de la fonction
def foo(param1, param2...):
    # Code de la fonction.
    # Ce code utilise les paramètres param1, param2...

# Programme principal
foo(arg1, arg2...)
```

Lors de l'appel (ligne 7), les différentes valeurs passées en arguments sont affectées aux paramètres (ligne 2).

### Fonction qui renvoie une donnée

L'utilisation du mot `return` permet d'indiquer la donnée que la fonction doit renvoyer.

``` python
# Définition de la fonction
def foo(param1, param2...):
    # Code de la fonction (avec utilisation des paramètres)
    return donnee_retrounee

# Programme principal
val = foo(arg1, arg2...)
```

### Quelques règles supplémentaires

🔾 Le nom de la fonction doit suivre les mêmes règles que les noms de variables, avec une convention courante d'utiliser des minuscules et des traits de soulignement pour séparer les mots.

🔾 Une règle importante concerne l'ordre des paramètres : les paramètres obligatoires doivent être placés avant les paramètres ayant une valeur par défaut dans la déclaration de la fonction.
Cela garantit que les arguments passés lors de l'appel de la fonction correspondent correctement aux paramètres attendus, car Python attribue les arguments par position avant de traiter les arguments nommés ou les valeurs par défaut.
Par ailleurs, les arguments nommés doivent être passés après les arguments positionnels lors de l'appel de la fonction.

🔾 Pour permettre une flexibilité accrue, Python permet de définir des fonctions acceptant un nombre variable d'arguments. Cela se fait en utilisant la syntaxe `*args` pour les arguments positionnels variables, qui sont regroupés dans un tuple, et `**kwargs` pour les arguments nommés variables, qui sont regroupés dans un dictionnaire.
Ces syntaxes sont particulièrement utiles pour créer des fonctions génériques comme une somme ou une concaténation où le nombre d'arguments n'est pas connu à l'avance.

## Applications

### Application : Un peu de math ... 

Pour les fonctions ci-dessous, on utilisera la valeur de `pi` et la méthode `sqrt` du module `math`.  

1) Écrire une fonction `distance(x1, y1, x2, y2)` qui calcule la distance entre deux points du plan à l’aide de la formule :


$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$


2) Écrire une fonction `aire_cercle(r)` qui calcule l’aire d’un cercle de rayon `r`. Pour rappel, la formule mathématique est la suivante : 


$$A = \pi \times r^2$$


### Application : ... et d'aléatoire !

Pour les fonctions ci-dessous, on utilisera la méthode `randint` du module `random`. 

On considère le code ci-dessous.

```python
def fct():
    m = randint(1,12)
    j = randint(1,31)
    a = randint(1900,2100)
    return str(j) + "/" + str(m) + "/" + str(a)
```

1) Expliquer en une phrase l'utilité de cette fonction. Changer le nom de la fonction en conséquence.

2) Expliquer les différents éléments de la syntaxe python de la ligne 5.




