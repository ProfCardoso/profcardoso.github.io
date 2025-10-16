---
title: Initialisation à Python
---

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Les listes

Dans nos révisions du langage Python, nous avions vu certains types de variables simples: `int` (entiers), `float` (nombres à virgule flottante), `bool` (booléen) et `str` (chaîne de caractères). Nous allons maintenant voir des **types construits** qui sont des collections d’objets de type simple assemblés dans ce que l’on appelle une structure de données.  

Le premier exemple de type construit s'appelle le tableau. En Python, le terme “liste” est souvent utilisé pour désigner un tableau, d'ailleurs ce dernier a comme type `list`.  
Un tableau est une structure de données qui permet de stocker plusieurs valeurs (nombres, chaînes, booléens, etc.) dans une seule variable, et d’y accéder grâce à leur position (indice).

Les listes sont des **séquences** : elles sont ordonnées et itérables.  

Les listes sont **mutables** : elles peuvent être modifiées après leur création.  

Les listes sont **hétérogènes** : elles peuvent contenir tous les types d'objets.  

## Généralités
### Création d'une liste
Les listes s'écrivent avec des crochets [ ]. Les éléments sont séparés par des virgules.

*Exemple :*

```python
liste1 = [12, 8, -9, 9.5, 3]
liste2 = ['a', 'b', 'c', 'd']
liste3 = []  #Une liste peut être vide
```

### Longueur d'une liste

`len(liste)` :	Renvoie le nombre d'élément dans la liste, c'est-à-dire la longueur de la liste.  

### Récupération d'un élément d'une liste

`liste[i]` avec i ≥ 0 :	Renvoie le ième élément de liste en partant du début, le premier élément ayant l'indice 0.  
`liste[i]` avec i < 0 :	Renvoie le ième élément de liste en partant de la fin, le dernier élément ayant l'indice -1.

*Exemple :*

```python
liste = ['a', 'b', 'c', 'd']
elt_A = liste[1]  #La variable elt_A contient maintenant 'b'
elt_B = liste[-2]  #La variable elt_B contient 'c'
```

> #### 🐍 Application I 
>
> Écrire la ligne de code qui permet de créer la liste jours_semaine contenant les jours de la semaine sans le dimanche.
>
>Compléter avec la ligne de code qui permet de récupérer et stocker le premier élément de cette liste dans la variable premier_jour. Ajouter la ligne de code qui permet d'afficher le contenu de la variable premier_jour.
>
>Compléter avec la ligne de code qui permet d'ajouter "dimanche" à la liste jours_semaine.
>
>Compléter avec la ligne de code qui permet de remplacer l'élément "mardi" par "tuesday".
>
>Compléter avec la ligne de code qui affiche le nombre d'élément de la liste jours_semaine.
>
>Compléter avec la ligne de code qui permet d'afficher le 3ème jour de la semaine, c'est-à-dire mercredi.
>

### Analyse de code : Parcourir une liste

> #### Application II 
>
> A l'aide d'un tableau, expliciter le déroulement pas à pas du code suivant :
>
```python
liste = [1, 2, 3, 4, 5]
for i in range(len(liste)):
    elt = liste[i]
    print(str(elt) + "² = " + str(elt**2))
```
>
>A l'aide d'un tableau, expliciter le déroulement pas à pas du code suivant :
>
```python
liste = [1, 2, 3, 4, 5]
for elt in liste:
    print(str(elt) + "² = " + str(elt**2))
```
>
>On considère le code suivant :
>
```python
liste = ['a', 'b', 'c', 'd', 'e']
for i in range(len(liste)):
    print("Indice " + str(i) + " : " + str(liste[i]))
```
>
>a) A l'aide d'un tableau, expliciter le déroulement pas à pas du code suivant :
>
>b) Justifier que ce programme ne peut pas être codé avec un parcours de la liste en valeurs.


<!-- 

> ### 🐍 Application II : 

## Modification d'une liste

### Remplacement d'une valeur par une nouvelle valeur

`liste[i] = x` avec i≥0 : Modifie liste en remplaçant l'élément d'indice i par x, le premier élément ayant l'indice 0.
`liste[i] = x` avec i<0 : Modifie liste en remplaçant l'élément d'indice i par x en partant de la fin de la liste, le dernier élément ayant l'indice -1.

*Exemple :*

```python
liste = [12, 8, -9, 9.5, 3]
liste[1] = 'a'  #La variable liste est maintenant égale à [12, 'a', -9, 9.5, 3]
```


-->
