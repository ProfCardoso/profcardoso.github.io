---
title: Représentation des nombres
---

<link rel="stylesheet" href="../../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Les erreurs Python

## Erreurs (de syntaxe) vs exceptions : c’est quoi la différence ?

Les erreurs de syntaxe, qui sont des erreurs d'analyse du code, sont peut-être celles que vous allez rencontrer le plus souvent lorsque vous êtes encore en phase d'apprentissage de Python. Ces erreurs apparaissent lors de la compilation du code, lorsqu'une syntaxe incorrecte ou incompréhensible par Python est détectée. 

**Exemple**

```
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

Ici il manque les `:` après le `True`.  
  
Même si une instruction ou une expression est syntaxiquement correcte, elle peut générer une erreur lors de son exécution. Les erreurs détectées durant l'exécution sont appelées des exceptions et ne sont pas toujours fatales : nous apprendrons bientôt comment les traiter dans vos programmes.  
  
Quand une exception se produit, Python arrête le programme et affiche un message d’erreur : **le Traceback**.  

**Exemple**
```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "exemple.py", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
```
La dernière ligne donne le type d’erreur : ici `ZeroDivisionError`.

## Les erreurs de syntaxe
### SyntaxError

Quand le code n’est pas du Python correct (comme une faute de grammaire en français).

```python
if x < 5
    print("coucou")
```
→ Il manque les `:` après la condition.  

Python répond : `SyntaxError: invalid syntax`

### IndentationError

En Python, l’indentation (les espaces en début de ligne) est obligatoire pour les blocs (if, for, while, def, etc.), les oublier provoque une exception :

```python
if x < 5:
print("coucou")
```
→ La ligne print devrait être indentée.  

Python répond : `IndentationError: expected an indented block`

## Erreurs liées aux noms et aux variables
### NameError

Attention au nommage des fonctions et variables, il est impossible pour python de les connaître si elles sont pas crées avant leurs appels

```python
print(score)   # mais score n'a jamais été défini avant
```

Python répond :`NameError: name 'score' is not defined`

👉 Typique : faute de frappe (socre au lieu de score), ou variable définie dans un autre bloc, comme une fonction.

**Exemple**  
```python
def fonct():
    var = 0
    print(var)

fonct()
print(var)
```
La variable `var` est crée dans la fonction `fonct`, mais pas dans le programme. Pour résoudre le problème on peut créer des **variables globales**.  
  

## Erreurs de type et de valeur
### TypeError

Certaines opérations ne fonctionne pas entre elle, c'est le cas de l'addition entre une chaine de caractère et un entier.

```python
"5" + 3      # chaîne + entier → impossible
len(10)      # len attend un objet "de longueur"
```

Python répond : `TypeError: can only concatenate str (not "int") to str, etc.`

### ValueError

Parfois le type peut être correct, mais pas la valeur associée. C'est le cas notamment lors des changements de type avec les fonction de typage `int()`,`str()` ou encore `float()`.

```python
int("abc")      # on essaye de convertir "abc" en entier
```

Ici le type ne pose pas de problème, on essaye bien de changer une chaîne de caractère en entier, mais "abc" ne peut pas être transformé en entier (str → int), cela renvoie donc une erreur.

Python répond : `ValueError: invalid literal for int()`

**Autre exemple possible:**

```python
import math
math.sqrt(-1)   # racine carrée d'un nombre négatif
```

Python répond : `ValueError: math domain error`

## Erreurs sur les listes, chaînes, dictionnaires…
### IndexError

Lors de la manipulation de liste, de chaîne de caractère ou de dictionnaire, les tailles de ces derniers sont très importante, et la tentative d'utilisation d'indice supérieur provoquera systématiquement une erreur :

```python
L = [10, 20, 30]
print(L[3])   # indices possibles : 0,1,2
```

Python répond : `IndexError: list index out of range`

### KeyError

On demande une clé qui n’existe pas dans un dictionnaire.

d = {"nom": "Alice", "age": 15}
print(d["adresse"])


Python répond : `KeyError: 'adresse'`

### AttributeError

On demande un attribut ou une méthode qui n’existe pas pour cet objet.

texte = "bonjour"
texte.append(" !")   # les str n'ont pas de méthode append


Python répond : `AttributeError: 'str' object has no attribute 'append'`

## Erreurs arithmétiques
### ZeroDivisionError

Division par zéro.

x = 5 / 0


Python répond : `ZeroDivisionError: division by zero`

## Erreurs d’import et de modules
### ImportError / ModuleNotFoundError

Tu importes un module ou un objet qui n’existe pas.

import pythn   # faute d’orthographe


Python répond : `ModuleNotFoundError: No module named 'pythn'`

Ou :

from math import tutu


Python répond : `ImportError: cannot import name 'tutu' from 'math'`

## Lecture rapide d’un message d’erreur

“Méthode” possible:

- Regarder la dernière ligne → type d’erreur (TypeError, NameError, etc.).

- Lire la ligne de code concernée (Python l’indique : File ..., line ...).

- Relier l’erreur au contexte :

    - NameError → variable pas définie ? faute de frappe ?

    - IndexError → indice trop grand ? longueur de la liste ?

    - TypeError → mélange str / int ? mauvais type passé à une fonction ?

## Mention rapide de try / except (optionnel)

Pour résoudre certaine de vos exception, il est possible d'utiliser le try/except, en voici un exemple :

```python
try:
    x = int(input("Entrez un nombre : "))
except ValueError:
    print("Ce n'est pas un nombre valide.")
```

Ici, pour éviter une valeur autre qu'un entier, on `try` quelque chose ( ici le input() pour récupérer la valeur auprès de l'utilisateur ). Si la valeur voulu par l'utilisateur n'est pas un entier, le code n'arretera pas son execution, car l'erreur sera evité par le `except`.

### Résumé des exceptions typiques

|Exception |	Quand ?|
|:---:|:---:|
|SyntaxError|	Code mal écrit (grammaire Python)|
|IndentationError|	Mauvaise indentation|
|NameError|	Variable / nom inconnu|
|TypeError|	Mauvais type (ex : "5" + 3)|
|ValueError	|Mauvaise valeur (ex : int("abc"))|
|IndexError	|Indice hors de la liste|
|KeyError|	Clé absente du dictionnaire|
|AttributeError|	Méthode/attribut n’existe pas|
|ZeroDivisionError|	Division par zéro|
|ImportError|	Problème d’import|