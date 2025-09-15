---
title: Projet Python
---

# Projet Python


## Logiciel d'apprentissage des tables de multiplication

Le but de ce projet est de créer un logiciel éducatif permettant de s'entraîner sur les tables de multiplication.

Votre programme demande d'abord à l'utilisateur quelle table de multiplication il veut réviser. Une fois qu'il a répondu, le programme lui pose 10 questions de la forme : "Combien font 3 x 5 ?" correspondant à la table choisie. Après chaque question, le programme indique si la réponse est fausse (et ne dit rien si elle est juste). À la fin, le programme affiche le nombre de bonnes réponses sur 10 et félicite l'utilisateur s'il a fait un sans faute. S'il n'a pas fait un sans faute, le programme fait essayer l'utilisateur à nouveau.

1) Créer une fonction `revision(table)` qui prend un entier `table` et qui lance une série de question pour l'utilisateur.

**Exemple d'exécution :**

``` shell
>>> revision(5)
Combien font 5 x 1 ? 5
Combien font 5 x 2 ? 10
Combien font 5 x 3 ? 15
Combien font 5 x 4 ? 22
Erreur : la réponse était 20
Combien font 5 x 5 ? 25
Combien font 5 x 6 ? 30
Combien font 5 x 7 ? 35
Combien font 5 x 8 ? 39
Erreur : la réponse était 40
Combien font 5 x 9 ? 45
Combien font 5 x 10 ? 50

Votre note est de 8/10

Essayons à nouveau !
Quelle table de multiplication voulez-vous réviser ? 5
Combien font 5 x 1 ? 5
Combien font 5 x 2 ? 10
Combien font 5 x 3 ? 15
Combien font 5 x 4 ? 20
Combien font 5 x 5 ? 25
Combien font 5 x 6 ? 30
Combien font 5 x 7 ? 35
Combien font 5 x 8 ? 40
Combien font 5 x 9 ? 45
Combien font 5 x 10 ? 50

Votre note est de 10/10
Bravo, vous avez fait un sans faute !
```