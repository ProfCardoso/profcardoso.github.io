---
title: Aide
---

#  # 🐍 Fiche de révision – Bases de Python

---

## Créer une variable

Une variable en Python est un nom qui sert à stocker une valeur en mémoire afin de pouvoir la réutiliser plus tard dans le programme.

<div style="border: 2px solid red; padding: 10px; border-radius: 8px;">
🧠 <strong>Définition simple</strong><br><br>
👉 Une variable, c’est comme une boîte avec une étiquette :<br>
• l’étiquette = le nom de la variable<br>
• la boîte = le contenu, la valeur
</div>
<br>

**Exemple** : 

```python
age = 16
```
- **age** → nom de la variable

- **=** → affectation (on donne une valeur)

- **16** → valeur stockée

## Afficher avec print()

La fonction `print()` permet d’afficher du texte ou des variables à l’écran (dans la console).

```python
print("Bonjour")
print(age)
print("Mon âge est", age)
```

## Demander une entrée utilisateur avec input()

La fonction `input()` permet de demander une valeur à l’utilisateur.

```python
nom = input("Quel est ton nom ? ")
print("Bonjour", nom)
```
⚠️ `input()` retourne toujours une chaîne de caractères (str).

### Pour récupérer un nombre :

```python
age = int(input("Quel est ton âge ? "))
```

## Structures conditionnelles (if, elif, else)

Les conditions permettent d’exécuter du code selon une situation.

```python
age = 18

if age >= 18:
    print("Tu es majeur")
elif age == 17:
    print("Presque majeur")
else:
    print("Tu es mineur")
```

### Opérateurs de comparaison

Quelques opérateurs :

- **==** : égal à

- **!=** : différent de

- **<** : inférieur à

- **>** : supérieur à

- **<=** : inférieur ou égal à

- **>=** : supérieur ou égal à

## Créer une fonction (def)

Une fonction sert à regrouper du code réutilisable.

### Fonction sans valeur de retour
```python
def dire_bonjour(nom):
    print("Bonjour", nom)

# Pour utiliser la fonction créer, il faut l'appeler !
dire_bonjour("Alice")
```

### Fonction avec valeur de retour
```python
def carre(nombre):
    return nombre * nombre

# Pour utiliser la fonction créer, il faut l'appeler !
resultat = carre(4)
print(resultat)
```

## Boucle for 

### Par index
Permet de parcourir des indices.

```python
for i in range(5):
    print(i) 

# Affiche : 0 1 2 3 4
```

**Exemple** : avec une liste :

```python
notes = [12, 15, 9]

for i in range(len(notes)):
    print(notes[i])

```
### Par élément
La méthode la plus simple pour parcourir une liste.

```python
notes = [12, 15, 9]

for note in notes:
    print(note)
```

## Boucle while
La boucle while s’exécute tant que la condition est vraie.

```python
compteur = 0

while compteur < 5:
    print(compteur)
    compteur += 1

```
⚠️ Attention aux boucles infinies : la condition doit finir par devenir fausse.