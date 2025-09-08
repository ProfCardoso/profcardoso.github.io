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