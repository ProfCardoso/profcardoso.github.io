# Jeu de tests d'une fonction

## De quoi parle-t-on ?

**Exemple**

Supposons qu'on dispose d'une fonction `prod(a:int, b:int) -> int` qui prend deux entiers en paramètres et renvoie le produit de ces deux entiers.


<!--

AVANT COURS
-->

**Question :** Quelles valeurs de a et de b serait-il judicieux de tester pour s'assurer que la fonction prod a été bien programmée ? 🤔

<!-- 

APRES COURS

<details>
  <summary style="cursor: pointer; font-weight: bold;"><strong> Question :</strong> Quelles valeurs de a et de b serait-il judicieux de tester pour s'assurer que la fonction prod a été bien programmée ?🤔</summary>
  <div style="margin-top: 10px;">
    <p>Toutes les valeurs qui pourrait poser problèmes et un exemple classique d'utilisation, dans les respect de la documentation et des pré/post-condition, ici par exemple :</p>
    <ul>
      <li>a = 3, b = 5</li>
      <li>a = 0, b = 5 (test avec zéro)</li>
      <li>a = -3, b = 5 (test avec valeur négative)</li>
    </ul>
  </div>
</details>

-->

### A connaitre

<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong style="color: #af4c4cff">Vocabulaire</strong><br>
L'ensemble des valeurs que l'on utilise pour tester une fonction s'appelle un <strong>"jeu de tests"</strong>.
</div>



## Les qualités d'un bon jeu de tests
Un bon jeu de tests doit couvrir au mieux toutes les situations possibles d'exécution de la fonction.

On pensera en particulier aux situations suivantes :

- pour les entiers : le zero, les entiers positifs et négatifs...
- pour les listes : la liste vide, des listes de tailles différentes...
- ...

> ## Application 🖋️
> On considère une fonction qui prend une liste d'entiers en paramètres et renvoie le nombre de 0 que contient la liste.
>
> 1. Proposer un jeu de tests pour cette fonction.
>

## Utilisation de doctests

**Exemple :**  A faire sur ordinateur 💻

1) Tester le code ci-dessous et analyser l'affichage de la ligne de commande :

``` python
def produit(a:int, b:int) -> int:
    """
    Renvoie le produit de deux nombres
    Paramètres :
        a : (int) un entier
        b : (int) un entier
    Valeur renvoyée :
        (int) le produit de a et b.

    Exemples :
        >>> prod(3,2)
        6
        >>> prod(-2,5)
        -10
    """
    return a * b

# Programme principal
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)

```
2) Compléter le jeu de tests.

> ## Applications
> ### Application I
>
>Proposer une fonction `prod(a:int, b:int) -> int` (avec un jeu de test pertinent) qui prend deux nombres entiers en paramètres et renvoie le produit de ces deux nombres. <strong>Le code proposé ne devra pas utiliser l'opérateur *</strong>.
>
> ### Application II
>
>On souhaite disposer d'une fonction mini3(a, b, c) qui prend trois nombres en paramètre et renvoie le plus petit des trois.
>
>1) Proposer un jeu de tests pertinent pour cette fonction.
>
>2) Écrire le code d'une telle fonction, avec une docstring et des doctests. Le code proposé ne devra utiliser ni la fonction min, ni la méthode sort.
>
> ### Application III
>
>Écrire le code d'une fonction (avec une docstring et des doctests) qui prend une liste d'entiers en paramètre et renvoie la somme des nombres de cette liste. La liste passée en paramètre pourra être vide, dans ce cas la fonction renverra 0.
>

## Utilisation des assertions

Une **assertion** est une **instruction** en Python qui sert à vérifier qu’une condition est vraie pendant l’exécution d’un programme.

Les assertions servent surtout à :

- vérifier que le programme fonctionne correctement

- repérer des erreurs plus facilement

- s’assurer qu’une fonction fait bien ce qu’on attend

**Exemple** : sur papier 🖋️

```python
def prod(a, b):
    return a*b

assert prod(3,5) == 15, "..."
assert prod(-3,5) == -15, "..."
assert prod(3,-5) == -15, "..."
assert prod(-3,-5) == 15, "..."
```
1. Expliquer le rôle des lignes 4 à 7.

2. Compléter le jeu de tests.

> ## Application 
>
>1. Écrire une fonction qui prend une liste d'entiers en paramètres et renvoie une liste contenant les mêmes éléments, dans le même ordre, en ne gardant que les entiers strictement positifs. La liste pourra être vide.
>
>2. Écrire, dans le code du programme principal, un jeu de tests sous forme d'assertions de façon à tester cette fonction.