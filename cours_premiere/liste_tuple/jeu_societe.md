---
title: Initialisation à Python
---

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Jeu de société

**Objectifs** : Le but de ce tp est de vous faire manipuler les listes grâce à différentes activités.   

**Attention, sauvegarder correctement ce script python, nous le réutiliserons plus tard.** 

## Jeux de dés 🎲

On souhaite simuler plusieurs lancer de dés. Lancer cette fonction à chaque fois que vous générer cette page.

1. Créez une fonction `plusieurs_lancer(des)` qui prend en paramètre le nombre de dés et renvoie une liste de valeur de dés.   

*Aide : Il pourrait être intérressant de créer en amont une fonction `lance_dé()` sans paramètre qui utilise la fonction randint de la  bibliothèque random pour tirer aléatoirement une valeur entre 1 et 6 pour modéliser le lancer de dé*  

2. Écrivez une fonction `minimum(liste_de)` qui prend en paramètre une liste de dés et qui renvoie la valeur minimum dans cette liste. Faite de même pour `maximum(liste_de)`.  

3. On souhaite tester si la liste de dés possède un certain nombre de dés de valeur n. Créer une fonction `test_presence_n(liste_de,n)` qui prend en paramètre une liste de dés et un entier n qui vérifie si le dé se trouve dans la liste.  

## Jeu des petits chevaux 🐴

Vous allez par la suite créer une version simplifiée du jeu des petits chevaux.  

<div style="display: flex; flex-direction:column;  text-align: center; ">
  <img style="margin: auto;" src="../../images/Petit Cheveau.jpg" alt="Python" width="800" />
</div>

**Simplification des règles :** 

- Un cheval ( représenté par un `'C'` ) doit atteindre la ligne d'arrivée avant les autres.
Pour cela il avance d'un certain nombre de case que le dé indique. 
- La "piste de course" est le nombre de case avant la ligne d'arrivée, et le cheval
commence toujours à la première. Ici, une piste sera une **liste de taille 10**, avec en
premier élément ( indice 0 ) un cheval `'C'`, des cases `'_'` et une arrivée `'A'` ( à la fin de
la liste )
- Le jeu se termine quand le premier cheval arrive sur la dernière case de la piste.

1. Créez une fonction `nouvelle_piste(t)` avec en paramètre une taille t et qui renvoie
une liste de chaîne de caractères.
2. Ecrivez une fonction `cheval_arrive(piste)` qui test si le cheval est sur la dernière case de
la piste, donc en dernière position de la liste. Elle prendra une liste ( correspondant à
la piste ) en paramètre et renverra True ou False selon la positon du cheval.
3. Créez une fonction `tour_de_jeu(piste)`, qui prendra la liste correspondant à la piste en
paramètre, et renverra la piste avec la nouvelle position du cheval après un lancer de
dé.  

Attention : si la nouvelle position du cheval dépasse la ligne d'arrivée, le cheval ne
bougera pas et passe son tour. De plus, n'oubliez pas "d'effacer" le cheval de son
ancienne position.

4. Réalisez un script python qui joue maximum 5 tours de jeu et qui écris un message de félicitation si le cheval est arrivé, ou un message d'encouragement si celui ci n'a pas fini la course. 

## Jeu de carte

Un jeu de 52 cartes standard est composé de quatre couleurs : pique, cœur, carreau et trèfle.  
Chaque couleur contient 13 valeurs :

- **1 carte spéciale** : As (peut être la plus basse ou la plus haute selon le jeu)

- **9 cartes numérotées** : 2, 3, 4, 5, 6, 7, 8, 9, 10

- **3 figures** : Valet, Dame, Roi

Les couleurs **piques** ♠️ et **trèfles** ♣️ sont **noires**, tandis que **cœurs** ♥️ et **carreaux** ♦️ sont **rouges**.

Le jeu peut être utilisé dans des jeux comme le poker, le blackjack, la bataille, le solitaire, etc.

On souhaite modéliser un jeu de carte en utilisant le langage Python, voici un exemple possible de liste pour représenter ces cartes : 

```python
# Valeurs possibles d'une carte
valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]

# Symboles (couleurs) possibles
symboles = ["♠️", "♥️", "♦️", "♣️"]
```

1) Écrire une fonction `creer_carte(valeur,symbole)` qui "crée" une carte à partir d'une valeur et d'un symbole donné en paramètre et renvoie la valeur et le symbole de la carte.

```python
>>> creer_carte("3","♠️")
3 de ♠️
```

2) Écrire une fonction `creer_jeu(valeurs,symboles)` qui "crée" un jeu de carte à partir des valeurs et des symboles donnés en paramètre et renvoie une liste contenant toutes les cartes.

```python
>>> valeurs = ["As", "2", "3"]

>>> symboles = ["♠️", "♥️"]

>>> creer_jeu("3","♠️")
["As de ♠️","2 de ♠️","3 de ♠️","As de ♥️","2 de ♥️","3 de ♥️"]
```

3) Écrire une fonction `tirer_carte(jeu_de_carte)` qui "tire" aléatoirement une carte à partir d'un jeu de carte donné en paramètre. Attention ! Une fois la carte tirée du jeu, le jeu de carte ne doit plus la contenir.

```python

>>> jeu_de_carte = ["As de ♠️","2 de ♠️","3 de ♠️","As de ♥️","2 de ♥️","3 de ♥️"]

>>> tirer_carte(jeu_de_carte)
As de ♥️

>>> print(jeu_de_carte)
["As de ♠️","2 de ♠️","3 de ♠️","2 de ♥️","3 de ♥️"]

```