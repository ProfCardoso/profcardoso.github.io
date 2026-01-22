# L'encodage des caractères

<link rel="stylesheet" href="../../assets/style.css" />

# Python et l'encodage des caractères
## Généralités
L'encodage des fichiers texte en python
Python utilise l'UTF-8 comme encodage.

## Prendre connaissance : quelques éléments du Python

• Il est possible d'utiliser les points de code Unicode en Python en utilisant le caractère d'échappement \u.
```python
chaine = '\u00D7'
```

• La fonction `ord()` renvoie le code Unicode d'un caractère en base 10.

```python
val_unicode = ord('×')
```

• La fonction `chr()` renvoie le caractère correspondant à la valeur passée en paramètre (cette valeur peut être en base 10, en binaire, en hexadécimal...).

```python
caract = chr(0xD7)
caract = chr(65)
```

> ## Applications
> ### Application 1 : Code ISO-8859-1 d'une chaine de caractères
>
>1) Écrire une fonction :
>
>- qui prend un caractère en paramètre ;
>- qui renvoie le code ISO-8859-1 (en hexadécimal) de ce caractère.
>2) Écrire le programme principal qui permet à l'utilisateur de saisir un caractère afin de connaitre son code ISO-8859-1.
>
>Vérifier l'exactitude du résultat à l'aide de l'éditeur hexadécimal.
>
> ### Application 2 : Un prénom qui commence par B
>Écrire un script qui :
>
>- demande un prénom qui commence par B à l'utilisateur ;
>- vérifie que le prénom commence effectivement par B (ou b) en renvoyant un message adapté.
> ### Application 3 : ASCII ou pas ASCII
>Écrire une fonction qui :
>
>- prend un caractère en paramètre,
>- renvoie True si le caractère est un caractère du code ASCII ou False dans le cas contraire.
> ### Application 4 : Mise en majuscule
>Dans cette application, on n'utilisera pas les caractères accentués.
>
> Écrire une fonction qui prend une lettre en minuscule et la renvoie en majuscule, sans utiliser la méthode upper().