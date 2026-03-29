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

## Les opérateurs mathématiques
 
Ils existent plusieurs opérateurs pour effectuer des calculs dans vos scripts Python :

| Opérations    | Symboles | Exemples                                  |
|---------------|:--------:|-------------------------------------------|
| Addition      | +        | 2 + 5 donne 7                             |
| Soustraction  | -        | 8 - 2 donne 6                             |
| Multiplication| *        | 6 * 7 donne 42                            |
| Puissance     | **       | 5 ** 3 donne 125

Cependant certains opérateurs n’existent pas dans le langage Python natif, et on doit les ajouter préalablement avant de les utiliser en important des bibliothèques.
```python
# Importation de la bibliothèque math 
import math
# racine carré de 9
racine = math.sqrt(9)
```
> **Exercice 5**
>Il est possible d’utiliser ces opérateurs sur des entiers (int) et des flottants (float), mais peut on les utiliser sur des chaînes de caractères ? 🤔 
>
> Essayez cette ligne de code Python en remplaçant l’opérateur entre ces deux chaînes de caractères :
```python
print( "J’aime la" OPERATEUR "SNT" )
```
> 

## Les booléens

**Propriété**
>Un **booléen** est un type de donnée en informatique et en mathématiques qui ne peut prendre que **deux valeurs possibles** :
> 
> Vrai (`True`) ou Faux (`False`).
>
> Il sert à représenter une vérité logique ou le résultat d’une comparaison.
>
> Par exemple :
>
> - 2 > 1 est **vrai** → booléen =  `True`
> - 5 = 3 est **faux** → booléen =  `False`

> **Exercice 6**
>
> <u>Sur feuille, puis vérifier sur l'ordinateur</u>
> 1) Donner la valeur (True ou False) des expressions suivantes :
```python
15 <= 20 or 1> 150
2 < 4 and 2 < 3
"A" == "A" and "B"=="B"
"A" != "C"
not (1 < 3)
not (15 <= 20) or 1 < 150
3 < 5 and ((7 < 5) or (2 < 3))
```
>
> 2) Que font les opérateurs <= ? > ? == ? and ? or ? not ?
>
| Opérateur | Description |
|-----------|-------------|
|           |             |
|           |             |
|           |             |
|           |             |
|           |             |
>

## La structure conditionnelle "if"
**Propriété**
>En Python, voici la structure :
```python
if condition :
    instruction(s) à effectuer dans la cas où la condition est remplie
else :
    instruction(s) à effectuer dans la cas contraire
```
>
> **ATTENTION !**  Le bloc else n'est pas obligatoire !
> **Remarque :**  Le symbole   :   est très important en Python car il marque le début d'un bloc. C'est l'indentation (=décalage) qui délimite le bloc d'instructions.

> **Exercice 7**
> Écrire ce code et exécuter le :
```python
a=float(input("Entrer un nombre réel : ")) 
if a>=0 : 
print("Vous avez entré un nombre positif ou nul",a) 
else : 
print("Vous avez entré un nombre négatif",a) 
```
>
> 1) Qu'affiche le programme de l'exemple dans chacun des cas suivants :
>   1.Avec a=8 ?
>   2.Avec a=-6 ?
>   3.Avec a=0 

## Programmation en Python  
### Les boucles

---

### Introduction : pourquoi une boucle ?

En programmation, une **boucle** permet de **répéter plusieurs fois une même instruction** sans avoir à la réécrire.

#### Exemple  
Quel code utiliser pour afficher les nombres de 1 à 5 ?

Sans boucle, il faudrait écrire plusieurs instructions identiques, ce qui pose un problème de lisibilité et d’efficacité 🙋.

---

### La boucle `for`

La boucle `for` répète un bloc d’instructions **pour chaque valeur dans une séquence**.

#### Syntaxe
```python
for variable in sequence:
    instructions
```
**variable :** prend successivement chaque valeur de la séquence

**sequence :** ensemble de valeurs à parcourir

Exemple : afficher les nombres de 1 à 5
```python
for i in range(1, 6):
    print(i)
```
➡️ range(1, 6) crée la séquence suivante :
1, 2, 3, 4, 5

> ### Exercice 1 : répéter une action 10 fois 💻
>Écrire le code Python pour afficher "Bonjour" 10 fois.
>
> ### Exercice 2 : compter de 0 à 20 par pas de 2 💻
>Écrire le code Python pour compter de 2 en 2 jusqu’à 20.
>
> **Rappel :** fonction range `range(début, fin, pas)`

### La boucle while

La boucle while répète des instructions tant qu’une condition est vraie.

#### Syntaxe

```python
while condition:
    instructions
```

<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>⚠️ Attention aux boucles infinies</strong><br>
Exemple de boucle infinie
    <pre><code>
    while True:
        print("Boucle infinie !") 
    </code></pre>

</div>

➡️ Il faut toujours vérifier que la condition deviendra fausse au moins une fois durant l’exécution du programme.

> ### Exercice 3 : demander un nombre positif 💻
>
>Demander à l’utilisateur un nombre tant qu’il n’est pas positif.
>
> ### Exercice 4 : demander un mot de passe 💻
>
>Écrire le code qui demande un mot de passe à l’utilisateur et le redemande tant que celui-ci est incorrect.
>
```python
mot_de_passe = "PYTHON"
while ...
```
> ### Bonus ⭐ : Ajouter un compteur d’erreurs :
>
> - Il s’incrémente de 1 à chaque erreur
> - Au bout de 3 erreurs, afficher un message indiquant que le compte est bloqué

## Les Fonctions

### Définition

Une fonction est un bloc de code nommé qui :

- réalise une tâche précise
- peut recevoir des paramètres (informations d’entrée)
- peut renvoyer un résultat
- peut être utilisée plusieurs fois dans un programme

### Syntaxe

```python
def nom_de_la_fonction (paramètre(s)) :
     instruction(s)
return resultat   # Le return n’est pas obligatoire
```

**Exemple :**

```python
def carre(x):
    return x * x
resultat = carre(3)
print(resultat)             # 9
```

### Applications :
>
> #### Exercice 1 : Sans return et sans paramètre
>
> 1. Écrire une fonction hello() qui affiche un message pour dire bonjour. 
>
> 2. Écrire le programme pour utiliser cette fonction, qui dit bonjour 10 fois.
>
> #### Exercice 2 : Avec return et 2 paramètres
>
> 1. Écrire une fonction addition(a, b) qui retourne la somme de deux 
nombres. 
>
> 2. Écrire le programme pour utiliser cette fonction avec les nombres de votre 
choix