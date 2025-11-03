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

##  Parcours d'une liste avec for ... in ...

### Utilisation de for pour parcourir les éléments

*Exemple : affichage des 10 premiers nombres entiers*

```python
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elt in liste:   #elt est une variable qui prend successivement les valeurs de la liste
    print(elt, "^2"," = ", elt**2, sep="")
```

### Utilisation de for pour parcourir les indices

*Exemple : affichage d'une lettre sur deux de l'alphabet*

```python
liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's']
for i in range(len(liste)):   #i est une variable qui prend successivement les valeurs des positions
    if i % 2 == 0:
        print(liste[i], end='')
```

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
>

## Modification d'une liste

### Remplacement d'une valeur par une nouvelle valeur

`liste[i] = x` avec i≥0 : Modifie `liste` en remplaçant l'élément d'indice i par x, le premier élément ayant l'indice 0.
`liste[i] = x` avec i<0 : Modifie `liste` en remplaçant l'élément d'indice i par x en partant de la fin de la liste, le dernier élément ayant l'indice -1.

*Exemple :*

```python
liste = [12, 8, -9, 9.5, 3]
liste[1] = 'a'  #La variable liste est maintenant égale à [12, 'a', -9, 9.5, 3]
```

### Ajout d'un élément à une liste

**• Ajout d'un élément à l'aide de la méthode `append(...)`**  

`liste.append(x)` :  Modifie `liste` en ajoutant l’élément x après le dernier élément.

**• Remarque : ajout d'un élément par concaténation**

Il est possible d'utiliser l'opérateur + entre deux listes :

` l1 + l2 ` : Renvoie une **nouvelle** liste qui contient les éléments de l1 avec à la suite ceux de l2.

Avec cet opérateur, on ajoute un élément à la liste avec le code suivant :

`liste = liste + [x]` : Modifie liste en ajoutant l’élément x après le dernier élément.

### Suppression d'un élément d'une liste

**• Suppression d'un élément à l'aide de la méthode pop(...)**

`liste.pop()` :	Modifie liste en supprimant le dernier élément et renvoie cet élément.
`liste.pop(i)` : Modifie liste en supprimant le ième élément et renvoie cet élément.

**• Suppression à l'aide l'instruction del**

*Exemple :*

``` python
liste = ['a', 'b', 'c', 'd', 'e', 'f']
del liste[1] #La variable liste est maintenant égale à ['a', 'c', 'd', 'e', 'f']
```

**• Suppression d'un élément d'une liste**

`liste.remove(elt)` : Modifie liste en supprimant l'élément elt.  

Attention, si l'élément x n'est pas dans liste, cette fonction lève une erreur.  

> #### Application III : Faire soi même
>
> 1) Créer une fonction modification_liste(liste,ele,pos) avec 3 paramètres : une liste liste , qui va être modifiée par l'élément ele à une position pos. Si la position pos est plus grande que la taille de la liste, l'élément sera ajouté à la fin de la liste, et si elle est plus petite ou égale que 0, il sera ajouté au début. 
>
> Exemple :
>
``` 
>>> modification_liste([1,2,3,5,5],4,3)
[1,2,3,4,5]
>>> modification_liste([1,2,3,5,6],10,9)
[1,2,3,5,10]
>>> modification_liste([1,2,3,5,6],8,-2)
[8,2,3,5,6]
```
>
> 2) Créer une fonction ajout_element_liste(liste,ele) avec 2 paramètres : une liste liste , à qui on va ajouter l'élément ele à la fin de la liste. 
>
> Exemple :
>
``` 
>>> ajout_element_liste([1,2,3,4],5)
[1,2,3,4,5]
```
>
> Pour les plus rapides, vous pouvez modifier la fonction pour ajouter un élément à la position voulu en paramètre
>
> Exemple :
>
``` 
>>> ajout_element_liste([1,2,3,5],4,3)
[1,2,3,4,5]
```
>
> 3) Créer une fonction supprimer_element_liste(liste,pos) avec 2 paramètres : une liste liste , à qui on va supprimer un élément à la position pos. Si la position pos est plus grande que la taille de la liste, l'élément sera supprimé à la fin de la liste, et si elle est plus petite ou égale que 0, il sera supprimé au début. 
>
> Exemple :
>
``` 
>>> supprimer_element_liste([1,2,3,4],2)
[1,2,4]
>>> supprimer_element_liste([1,2,3,5,6],-3)
[2,3,5,6]
```
>