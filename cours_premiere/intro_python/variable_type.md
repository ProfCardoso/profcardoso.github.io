---
title: Initialisation à Python
---

# Variables et types d'objets


<link rel="stylesheet" href="../assets/style.css" />

---

## Qu'est-ce qu'une variable ?

### Affectation d'une valeur à une variable

Dans un programme, pour les variables, on distingue :

- L'affectation d'une valeur à une variable ;
- L'utilisation de la variable.
L'affectation se fait à l'aide du signe `=` . Les étapes sont les suivantes :

1) Le code à droite du signe = est évalué.  
2) Le résultat est créé en mémoire.  
3) Le nom placé à gauche du signe = est associé à cette mémoire.  
Lors de l'affectation, si la variables n'existait pas, elle est créée.  

### Application

Sur feuille : Pour chaque programme ci-dessous, indiquer les valeurs des variables a, b et r en fin d'exécution.

🔾 Programme 1 :

```python
# Programme principal
a = 8
b = 15
r = a + b
```

🔾 Programme 2 :

```python
# Programme principal
r = 2
a = 8
b = a - 3
r = a + b
```

🔾 Programme 3 :

```python
# Programme principal
r = 10
r = r + 3
```

🔾 Programme 4 :

```python
# Programme principal
r = 20
b = -5
r = r + b
```

🔾 Programme 5 :

```python
# Programme principal
r = 1
a = 2
r = r * a
a = 4
r = r * a
```

Sur l'ordinateur, avec Thonny :

- lancer le programme en mode débogage  (Ctrl+F5),
- avancer pas à pas  (F7),
- vérifier vos résultats.

## Les types d'objets

### A faire

Le langage python dispose de la fonction `type(...)` qui permet de connaitre le type du contenu d'une variable.

Copier le code ci-dessous dans Thonny.

```python
# Programme principal
pi = 3.1416
rayon = 5
phrase = "Bonjour à tous"
prenom = "Jean"
test_lecture = True
liste_prenoms = ["Anne", "Bernard", "Carole"]
```
Faire la liste des types d'objets.

### A connaître : les types de base

Les types d'objets avec lesquels nous travaillerons cette année sont :

🔾 `int` pour les entiers relatifs ;  
🔾 `float` pour les rationnels ;  
🔾 `bool` pour les booléens ;  
🔾 `str` pour les chaines de caractères ;  
🔾 `list` pour les listes ;  
🔾 `tuple` pour les tuples ;  
🔾 `dict` pour les dictionnaires.  


## Obtenir un objet d'un type donné à partir d'un objet d'un autre type

### Les fonctions de typage

En python, pour chaque type d'objet, il existe une fonction qui permet de créer un objet de ce type à partir d'un autre objet d'un autre type.

- Pour les entiers, la fonction est `int(...)`.
- Pour les flottants, la fonction est `float(...)`.
- Pour les chaine de caractères, la fonction est `str(...)`.
- Pour les booléen, la fonction est `bool(...)`
...

Exemples
Tester le code suivant dans Thonny.

```python
# Programme principal
pi = 3.1416
a = str(pi)
b = int(pi)
c = bool(pi)
```

### Applications

Sur feuille : proposer les instructions qui permettent :

- de transformer "8" en un entier.
- de transformer 5.8 en un entier. Le résultat est-il l'entier 5 ou l'entier 6 ?
- de transformer 9 en "9".
- de transformer 3.14 en "3.14"
Sur ordinateur : Tester vos propositions.
