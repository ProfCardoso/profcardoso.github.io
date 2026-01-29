# Les dictionnaires


<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>Définition — Dictionnaire</strong><br>
Les dictionnaires sont des ensembles de paires clé-valeur.

Les clés permettent d'accéder à leurs valeurs respectives.

Les clés doivent être toutes différentes et toutes immuables : int, str, tuple...

Les valeurs peuvent être de tous les types.

Les paires d'un dictionnaire n'ont pas d'ordre.

</div>

## Généralités

### Création d'un dictionnaire
Les dictionnaires s'écrivent avec des accolades **{}**, les paires (clé,valeur) sont séparées par des **virgules** et chaque clé est séparée de sa valeur par un **double point :**.  
  
**Exemple :** création directe
```python
dico1 = {'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}
```

#### Récupération de la longueur d'un dictionnaire
La longueur d'un dictionnaire, c'est-à-dire le nombre de paires qu'il contient, peut être récupérée à l'aide de la fonction `len(dico)`.

```python
dico2 = {0: 0, 1: 'texte', 2: True}
print(len(dico2))  #3

```

## Ajout et suppression d'éléments

### Ajout d'une paire à un dictionnaire

**Exemple**:Le programme ci-dessous ajoute successivement de paires clé-valeur à la variable dico2

```python
dico2 = {}
dico2['one'] = 1
dico2['two'] = 2
dico2['three'] = 3
```

- Ligne 1 : affectation d'un dictionnaire vide à la variable dico2.

- Lignes 2 : ajout au dictionnaire dico2 la clef `'one'` et la valeur `1`

- Lignes 3 : ajout au dictionnaire dico2 la clef `'two'` et la valeur `2`

- Lignes 4 : ajout au dictionnaire dico2 la clef `'three'` et la valeur `3`

A l'issue de l'exécution du programme, dico2 référence le dictionnaire `{'one': 1, 'two': 2, 'three': 3}`

### Suppression d'un élément dans un dictionnaire

**Exemple**

```python
dico1 = {'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}
del dico1['rouge']   # Supprime la paire 'rouge':'red'
```

### Lecture d'un dictionnaire
#### Lecture d'une valeur à partir d'une clé
Il est possible d'accéder à chacune des valeurs à partir des clés correspondantes.

**Exemple**
```python
dico1 = {'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}
mot_anglais = dico1['bleu']
```

- Ligne 1 : affectation d'un dictionnaire `{'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}` à la variable dico1.

- Ligne 2 : mot_anglais contient la valeur `'blue'`.

#### Récupération de l'ensemble des clés
La méthode `keys()` renvoie une séquence contenant les clés de la liste à laquelle elle est appliquée.

Cette séquence peut être :

- transformée en liste avec `list()`

- transformée en tuple avec `tuple()`

**Exemple**
```python
dico1 = {'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}
liste_cles = list(dico1.keys())
```
- Ligne 1 : affectation d'un dictionnaire `{'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}` à la variable dico1.

- Ligne 2 : liste_cles contient `['bleu', 'rouge', 'vert']`

#### Récupération de l'ensemble des valeurs
La méthode `values()` renvoie une séquence contenant les valeurs de la liste à laquelle elle est appliquée.

Cette séquence peut être :

- utilisée dans une boucle for

- transformée en liste avec `list()`

- transformée en tuple avec `tuple()`


**Exemple**
```python
dico1 = {'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}
liste_valeurs = list(dico1.values())
```

- Ligne 1 : affectation d'un dictionnaire `{'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}` à la variable dico1.

- Ligne 2 : liste_valeurs contient `['blue', 'red', 'green']`

#### Récupération des paires sous forme de tuples
La méthode `items()` renvoie une séquence contenant les paires clé-valeur sous forme de tuples.

Cette séquence peut être :

- utilisée dans une boucle for

- transformée en liste de tuples avec `list()`

- transformée en tuple de tuples avec `tuple()`


**Exemple**
```python
dico = {'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}
liste_paires = list(dico.items())
```

- Ligne 1 : affectation d'un dictionnaire `{'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}` à la variable dico1.

- Ligne 2 : liste_paire contient `[('bleu', 'blue'), ('rouge', 'red'), ('vert', 'green)]`

## Condition d'appartenance
La condition d'appartenance `in` ou de non appartenance `not in` ne s'applique qu'aux clés.

**Exemple**

```python
dico = {'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}
test_cle = 'bleu' in dico   # test_cle contient True
test_valeur = 'blue' in dico   # test_valeur contient False
```


## Parcours d'un dictionnaire
### Parcours par les clés
**Exemple**
Le programme ci-dessous affichage des clés du dictionnaire dico1.

```python
dico1 = {'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}
for c in dico1:
    print(c)
```
### Parcours par les paires clé-valeur
Pour parcourir un dictionnaire et utiliser les clés comme les valeurs, il faut utiliser la méthode `items()` vue ci-dessus.

**Exemple**
Le programme ci-dessous affichage des paires clé-valeur du dictionnaire dico1.

```python
dico1 = {'bleu': 'blue', 'rouge': 'red', 'vert': 'green'}
for c, v in dico1.items():
    print(c + ' se traduit, en anglais, par ' + v)
```

> ## Applications
>
> ### Application I : Les voyelles de l'alphabet 🖋️
>
> Créer un dictionnaire contenant les voyelles comme clés et leurs positions dans l'alphabet comme valeurs.

Application II_app2 : Les lettres de l'alphabet
Écrire les instructions qui permettent de créer le dictionnaire contenant les lettres de l'alphabet comme clé et leurs positions comme valeurs.

Rappels :

- la fonction chr permet d'obtenir un caractère à partir de son point de code unicode.
- le point de code de la lettre 'A' est 65.
Application II_app3 : Des dictionnaires pour sa musicothèque
On souhaite stocker les albums de chanteurs en créant un dictionnaire par chanteur.

Les clés de chaque dictionnaire seront les suivantes : 'nom', 'album1', 'album2'...

Créer les dictionnaires de deux ou trois chanteurs.

Application (incontournable) II_app4 : Affichage lisible d'un dictionnaire
Écrire une fonction qui affiche proprement un dictionnaire, c'est à dire que les paires clé-valeur sont affichées ligne par ligne.

Application, pour approfondir
Application III_app1 : Echange clé <=> valeur
Écrire une fonction qui prend un dictionnaire en paramètre et renvoie un nouveau dictionnaire dans lequel les clés et les valeurs sont interverties.

On pourra tester sa fonction sur le dictionnaire contenant les lettres de l'alphabet et leur positions.

Application (incontournable) III_app2 : Nombre d’occurrences des lettres d'un texte
Écrire une fonction qui prend un texte en argument et renvoie un dictionnaire dont les clés sont les lettres présentes dans le texte et les valeurs le nombre de fois que les lettres apparaissent.