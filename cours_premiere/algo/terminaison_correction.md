---
title: Algorithme
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


# Preuve d'un algorithme

## Préambule

Lorsqu'on écrit un algorithme, trois questions fondamentales se posent :

• **Est-ce qu'il se termine ?** => C'est ce que l'on appelle <span style="color: rgb(165,42,42);">la terminaison</span>. 
• **Est-ce qu'il donne le résultats attendu ?** => C'est ce que l'on appelle <span style="color: rgb(165,42,42);">la correction</span>.
• **Est-ce qu'il donne le résultat en utilisant des ressources (temps, mémoire...) raisonnables ?** => C'est ce que l'on appel <span style="color: rgb(165,42,42);">la complexité</span>.

**Remarque :** Démontrer la terminaison et la correction d'un algorithme s'appelle faire la **preuve de cet algorithme.**

## Définitions

<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>Terminaison d'un algorithme</strong><br>
Vérifier la terminaison d'un algorithme est en particulier nécessaire lorsque celui-ci comporte des boucles.
<br>
Dans ce cas, cela peut se faire en déterminant un <strong>variant de boucle</strong> qui converge (ou parle également de variant convergent).
<br>
Un variant convergent de boucle est une quantité qui prend ses valeurs dans un ensemble bien déterminé et qui évolue dans le même sens strictement à chaque itération de la boucle.
</div>

<br>

<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>Correction d'un algorithme</strong><br>
Vérifier la correction d'un algorithme est en particulier nécessaire lorsque celui-ci comporte des boucles.
<br>
Dans ce cas, cela peut se faire en utilisant un invariant de boucle.
<br>
On appelle invariant de boucle une propriété qui, si elle est vraie avant l’entrée dans une boucle, reste vraie après chaque passage dans la boucle, et donc est vraie aussi à la sortie de la boucle.
</div>

## Mise en pratique

Considérons l'algorithme suivant :

```python

def fonc(n):
    '''
    param n: (int) un entier positif ou nul
    return (int)
    '''
    resultat = 1
    i = 0
    while i < n:
        i = i + 1
        resultat = resultat * 2
    return resultat

```

🖊️ 1) Que fait cet algorithme (à trouver sans essayer l'algorithme) ? Compléter la docstring et changer le nom de cette fonction.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <pre><code>
    def deux_puissance_n(n):
    '''
    Fonction qui calcule la puissance n de 2

    param n: (int) un entier positif ou nul
    return (int)
    '''
        resultat = 1
        i = 0
        while i < n:
            i = i + 1
            resultat = resultat * 2
        return resultat

    </code></pre>
  </div>
</details>

🖊️ 2) Quel est le variant convergeant de boucle pour cet algorithme.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>n - i</p>
  </div>
</details>

🖊️ 3) Trouver un invariant de boucle. On pourra écrire une relation entre les différentes variables.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>resultat = 2^i</p>
  </div>
</details>

## Application à l'algorithme de recherche dichotomique

### Rappel de l'algorithme

```python
def recherche_dicho(E,L):
    '''
    Recherche dichotomique d'un élément dans une liste d'entiers triée.
    Renvoie la position de l'élément s'il est présent dans la liste.
    Renvoie None si l'élément n'est pas présent dans la liste.
    param L : (list) une liste d'entiers triés par ordre croissant
    param E : (int) un entier
    return : (int) position de l'entier ou -1
    '''
    debut = 0
    fin = len(L)-1
    milieu = (debut + fin) // 2
    while (debut - fin) <= 0 :
        if E > L[milieu]:
            debut = milieu + 1
        elif E < L[milieu]:
            fin = milieu - 1
        else :
            return milieu
        milieu = ( debut + fin ) // 2
    return -1

E = 64
L = [3,5,9,10,14,21,30,33,34,36,47,49,50,63,65,66,68,72,75,81]
print(recherche_dicho(E,L))
```

### Terminaison de l'algorithme

🖊️ Trouver un variant convergent de boucle pour montrer la terminaison de l'algorithme.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>fin - debut</p>
  </div>
</details>

### Correction de l'algorithme

Ici, il faut trouver un invariant de boucle, c'est à dire trouver une propriété qui est vraie avant la boucle et à la fin de chaque boucle.

Voici l'invariant :

- Formulation n°1 : si E est présent dans L, alors L[debut] ≤ E ≤ L[fin].
- Formulation n°2 : si E est présent dans L à une position pos, alors debut ≤ pos ≤ fin