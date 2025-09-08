---
title: Initialisation à Python
---

# Les chaines de caractères

Les chaines de caractères sont des séquences : elles sont ordonnées et itérables.

Les chaines de caractères sont immuables : elles ne peuvent pas être modifiées une fois créées.

Les chaines de caractères sont constituées de caractères, c'est-à-dire de points de code Unicode.

## Généralité
### Création d'une chaine

- Les chaines de caractères s'écrivent entre apostrophes (guillements simples) `'...'` ou entre guillements (guillemets doubles) `"..."`.

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
```

- Tous les caractères unicode sont utilisables.

```python
couleurs_cartes = "♠♣♥♦"
```

- Certains caractères (on parle des caractère d'échappement) s'obtiennent à l'aide du symbole \ :

`\n` : saut de ligne
`\t` : tabulation
`\'` : apostrophe (guillemet simple)
`\"` : guillement (guillemet double)
`\\` : antislash
`texte_sur_deux_lignes = "Bonjour !\nÇa va ?"`

# La fonction print

## Usage basique avec un seul paramètre

La fonction `print()` permet d'afficher des données dans la console.

```python
print("Bonjour")  #Affiche Bonjour
print(8.5)  #Affiche le nombre 8,5
```

**A noter :** Le paramètre est automatiquement convertie en chaine de caractère avec la fonction str() avant d'être affichée.

**A noter :** Par défaut, à l'affichage, un retour à la ligne est automatiquement ajouté à la fin de ligne.

**Complément :** Il est possible de concaténer des chaines de caractères en une seule chaine pour l'afficher dans la console. Dans ce cas, les variables qui ne sont pas des chaines de caractères devront être converties en chaines de caractères à l'aide de la fonction str().

```python
prenom = "Albert"
age = 26
chaine = "Voici " + prenom + ", il a " + str(age) + " ans !"
print(chaine)  #Affiche Voici Albert, il a 26 ans
```

```python
prenom = "Simone"
age = 23
print("Voici " + prenom + ", elle a " + str(age) + " ans !")  #Affiche Voici Simone, elle a 23 ans
```

## Usage avancé avec plusieurs paramètres

Il est possible d'utiliser la fonction `print()` avec plusieurs paramètres.

Dans ce cas :

- toutes les valeurs sont automatiquement converties en chaines de caractères,
- un espace est inséré entre chaque chaine correspond à un paramètre.

**Exemple 1 :**

``` python
print("La", "température", "est", "de", 20, "°C")  #Affiche La température est de 20 °C
```

**Exemple 2 :**

```python
prenom = "Albert"
age = 26
print(prenom, "a", age, "ans !")  #Affiche Albert a 26 ans !
```


### Le paramètre `sep`

Il est possible de choisir la chaine de caractère de séparation des valeurs avec le paramètre `sep`.

**Exemple :**

```python
print("a", "b", "c", "d", "e", sep="**")  #Affiche a**b**c**d**e
print("a", "b", "c", "d", "e", sep="")  #Affiche abcde
```
Si le paramètre sep n'est pas renseigné, sa valeur par défaut est un espace, c'est-à-dire `" "`.

### Le paramètre end

Il est possible de choisir la chaine de caractère de fin d'affichage avec le paramètre end.

**Exemple :**

```python
print("Bonjour", end="")
print(" et à bientôt...")  #Affiche 'Bonjour et à bientôt' sur une seule ligne.
```
Si le paramètre end n'est pas renseigné, sa valeur par défaut est un retour à la ligne, c'est-à-dire `\n`.

# La fonction input

La fonction `input()` interrompt le déroulement du programme afin de permettre à l'utilisateur d'entrer une donnée. L'information tapée au clavier par l'utilisateur est renvoyée sous la forme d'une chaine de caractères.

La fonction `input()` peut être utilisée avec ou sans paramètre.

Les deux codes ci-dessous sont équivalents :

```python
print("Entrez votre prénom : ",end="")
prenom = input()
prenom = input("Entrez votre prénom : ")
```

**Attention :** la fonction `input()` renvoie toujours une chaine de caractère. Il est parfois nécessaire de convertir cette chaine de caractère en entier (avec `int(...)`) ou en nombre à virgule (avec `float(...)`).

```python
prenom = "Albert"
chaine = prenom + " ! Combien voulez-vous de cartes ?"
nb_cartes = int(input(chaine))  
```