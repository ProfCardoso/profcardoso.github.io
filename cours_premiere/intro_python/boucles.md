---
title: Initialisation à Python
---

# Boucle `for`

L'instruction `for` permet de répéter un bloc de code en considérant successivement les valeurs d'une séquence (donnée itérable).

## Syntaxe

```python
#Instructions qui précèdent
for var in sequence :
    # Bloc d'instructions répété avec var qui prend successivement chaque valeur de la sequence
# Instructions qui suivent
```

## Les objets itérables

### Les objets range : séquence d'entiers

**Avec un paramètre**  

La fonction `range(n:int)`, lorsqu'elle est utilisée avec un seul paramètre `n` renvoie une séquence contenant les entiers de `0` à `n` exclu (c'est-à-dire à de `0` à `n-1` inclus).

**Exemple :** `range(8)` correspond à la séquence 0, 1, 2, 3, 4, 5, 6 et 7.

**Avec deux paramètres**  

La fonction `range(a:int, b: int)`, lorsqu'elle est utilisée avec deux paramètres `a` et `b` renvoie une séquence contenant les entiers de `a` inclus à `b` exclu.

**Exemple :** `range(3, 8)` correspond à la séquence 3, 4, 5, 6 et 7.

**Avec trois paramètres**  

La fonction `range(a:int, b: int, pas:int)`, lorsqu'elle est utilisée avec trois paramètres `a` et `b` renvoie une séquence contenant les entiers de `a` inclus à `b` exclu avec un interval égal à pas.

### Les chaines de caractères : séquence de caractères
Les chaines de caractères sont des objets itérables, c'est-à-dire qu'il sont des séquence de lettres.

### Les listes : séquences de données
Les listes sont des objets itérables, c'est-à-dire qu'il sont des séquences de leurs valeurs.

# Boucle `while`
L'instruction `while` permet de répéter un bloc de code tant qu'une condition est vérifiée.

## Syntaxe

```python
#Instructions qui précèdent
while Condition :
    # Bloc d'instructions répété tant que Condition est évalué à True
# Instructions qui suivent
```

**Remarque**  
La boucle `while` est intéressante à utiliser lorsque l'on ne connait pas le nombre de répétition que l'on souhaite.


## Applications

### Application : Les dix premiers nombres

Écrire une fonction qui affiche tous les nombres entre 1 et 10, et indique pour chacun si celui-ci est pair ou impair.

L'affichage dans la console sera :

```shell
1 est impair
2 est pair
...
10 est pair
```

On proposera deux versions : l'une avec `while`, l'autre avec `for`.

### Application : Les nombres dans l'ordre décroissant

Écrire une fonction qui prend un entier n en paramètre et affiche, ligne après ligne, les nombres de n à 1.

On proposera deux versions : l'une avec `while`, l'autre avec `for`.

### Application : Les premiers nombres dans une chaine de caractères

Écrire une fonction qui prend un entier n en paramètre et renvoie une chaine de caractères constituée de ces nombres dans l'ordre croissant, séparés par des virgules.

Par exemple, avec l'entier 6, la fonction doit renvoyer "1, 2, 3, 4, 5, 6".

### Application : Pour apprendre ses tables de multiplication

1) Écrire une fonction qui affiche la table de multiplication de 8.

Autrement dit, l'affichage dans la console doit être :

```shell
8 × 1 = 8
8 × 2 = 16
...
8 × 10 = 80
```
2) Écrire une fonction qui prend un nombre entier en paramètre et affiche la table de multiplication de ce nombre.

3) En utilisant la fonction précédente, écrire un programme qui affiche la table de multiplication d'un entier (entre 2 et 10) entré par l'utilisateur.

### Application : Les premières puissances de 2

Écrire un programme qui :

- demande un nombre à l'utilisateur
- affiche toutes les puissances de 2 inférieures à ce nombre.
Exemple : si l'utilisateur entre le nombre 18, le programme doit afficher les nombres 1, 2, 4, 8 et 16.


### Application :
1) Sans utiliser l'opérateur multiplier *, écrire une fonction qui prend un entier n en paramètre et renvoie une chaine contenant n `'◼'` à la suite.

Par exemple, avec le nombre entier 7, la fonction doit renvoyer : '◼◼◼◼◼◼◼'

2) Utiliser la fonction précédente dans une nouvelle fonction qui permet d'afficher exactement le résultats ci-dessous :

```shell
◼
◼◼
◼◼◼
◼◼◼◼
◼◼◼◼◼
◼◼◼◼◼◼
◼◼◼◼◼◼◼
```

### Application : Nombre de chiffres d'un nombre

Écrire une fonction qui prend un nombre entier positif en paramètre et renvoie le nombre de chiffres de cet entier.

Par exemples :

- avec l'entier 75, la fonction doit renvoyer 2 ;
- avec l'entier 1948, la fonction doit renvoyer 4 ;
- etc.
Plusieurs versions sont possibles... Si vous avez plusieurs idées, écrire plusieurs fonctions.

### Application : Somme d'une série de nombres

Écrire un programme qui :

- demande des nombres entiers à l'utilisateur jusqu'à ce que l'utilisateur entre 0,
- affiche la somme de tous les entiers entrés.
