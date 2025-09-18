---
title: Projet Python
---

# Projet Python

Le but de ce projet est de créer une calculatrice qui permet de faire des opérations simples sur les entiers et les nombres à virgule. Elle permet aussi de refaire une opération en partant du résultat de la dernière opération.


## Calculatrice 

Votre programme demande à l'utilisateur de saisir un nombre de départ. Il affiche ensuite un menu proposant à l'utilisateur les opérations suivantes (en remplaçant x par le nombre saisi) :

```
x + y : addition
x - y : soustraction
x × y : multiplication
x ÷ y : division
√x : racine carrée
```

Dans le cas d'une opération qui nécessite un deuxième nombre, l'utilisateur doit saisir ce nombre. Votre programme affiche ensuite le résultat de l'opération et propose à l'utilisateur de refaire une opération en partant du résultat de la dernière opération.

Votre programme continue de proposer à l'utilisateur de refaire une opération jusqu'à ce qu'il choisisse de quitter. Pour lui permettre de quitter, ajoutez une option Quitter dans le menu de choix de l'opération.

**Attention :** votre programme doit pouvoir gérer les entiers et les nombres à virgule. Une façon simple de savoir si un nombre saisi par l'utilisateur est un nombres à virgule est de regarder s'il y a un point (.) dans la chaîne de caractères. Si c'est le cas, vous pouvez convertir la chaîne de caractères en nombre à virgule avec la fonction float().

**Exemple d'exécution**

Voici un exemple possible d'exécution de votre programme (le texte affiché par le programme est en bleu, tandis que le texte entré par l'utilisateur est en noir).

``` python
Entrez un nombre : 42
Choisissez une opération :
1) 42 + y
2) 42 - y
3) 42 × y
4) 42 ÷ y
5) √42
0) Quitter
Choix : 1
Valeur de y : 7
Résultat : 49
Choisissez une opération :
1) 49 + y
2) 49 - y
3) 49 × y
4) 49 ÷ y
5) √49
0) Quitter
Choix : 5
Résultat : 7.0
Choisissez une opération :
1) 7.0 + y
2) 7.0 - y
3) 7.0 × y
4) 7.0 ÷ y
5) √7.0
0) Quitter
Choix : 3
Valeur de y : 1.5
Résultat : 10.5
Choisissez une opération :
1) 10.5 + y
2) 10.5 - y
3) 10.5 × y
4) 10.5 ÷ y
5) √10.5
0) Quitter
Choix : 0
```