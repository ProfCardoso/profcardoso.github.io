---
title: Initialisation à Python
---

# Programmation en Python

<link rel="stylesheet" href="../../assets/style.css" />

## Affectation d'une valeur à une variable

En programmation, nous avons besoin de stocker des éléments, de les mettre en mémoire. Pour cela , on procède à l'affectation d'une variable par une donnée.  

**Propriété**
> En Python, l' affectation se réalise avec l'opérateur `=`

**Exemple**

le script :

```python
a=5
```
met en mémoire l'entier 5 dans la variable a

```python
a="easy"
```

met en mémoire la chaine de caractères "easy" dans la variable `a`

> **Exercice 1**
> Que vaut `a` à la fin de ce script :
> 
```python
a=1
b=-1
a=a*b
a=a+b
```
> 

## Affichage en python

**Propriété**

> Une chaîne de caractères correspond à un texte pouvant contenir différents symboles. En Python, une chaîne de caractères est le contenu délimité par `""`.
> 
> Pour afficher une chaine de caractères en Python on utilise la fonction `print()`

---

> **Exercice 2**
> Testez ces différents scripts :
```python
print("Vivement les vacances !")
prenom="Bob"
print("Mon prénom est :",prenom)
```
> Pourquoi ce n'est pas prenom qui est affiché dans la dernière phrase ?
> 
> **Exercice 3**
> 
> Réaliser un script qui contient trois variables : prenom, nom et age et qui doit afficher :
> 
> "Bonjour je m'appelle Alphonse Dansletas, j'ai 358 ans. "
> 
> Dans le cas où vous vous appelleriez Alphonse Dansletas et que vous seriez âgé de 358 ans.

## Dialogue avec l'utilisateur

**Propriété**

> La fonction `input` permet d'ouvrir une boite de dialogue et de récupérer une information saisie par l'utilisateur.
> 
> Attention ! L'information récupérée grâce à un `input` est une <u>chaîne de caractères</u>.

**Exemple**

```python
prenom=input("quel est ton prénom?")
print(prenom)
```

---

> **Exercice 4**
> 
> Ecrire un script en Python qui demande à l'utilisateur, son prénom, son nom et son âge et qui réalise un affichage comme dans l'exercice 2.
> 
> ( Attention il y a un piège ! )

## A connaître : les types de base

Les types d'objets avec lesquels nous travaillerons cette année sont :

🔾 `int` pour les entiers relatifs (exemple : 15, 489, -10, ...);  
🔾 `float` pour les nombres à virgules (exemple : 3.48, 9.203, ...);  
🔾 `bool` pour les booléens (exemple : True, False);  
🔾 `str` pour les chaines de caractères (exemple : "SNT", "bonjour", "ceci est une phrase", ...);   
  
Comme l'information récupérée grâce à un `input` est une `chaîne de caractères`, il va falloir changer le **type** de la variable pour permettre d'effectuer des calculs avec.

**Exemple**

1. Essayez ce script suivant :

```python
nombre=input("Combien de baguettes désirez-vous ?")
prix = nombre * 1.1
print("Vous avez à payer",prix,"euros.")
```

2. Qu'obtenez vous ?
  
  
  
  
3. Réessayez avec ce script :

```python
nombre=int(input("Combien de baguettes désirez-vous ?"))
prix = nombre * 1.1
print("Vous avez à payer",prix,"euros.")
```

4. Quelle est la différence avec le code précédent de cet exemple ?  
  
    
  
  
**Propriété**
> L'instruction `int` permet de changer certaines chaînes de caractères en un nombre entier.
> L'instruction `float` permet de changer certaines chaînes de caractères en un flottant, c'est-à-dire un "nombre à virgule".