---
title: Algorithmique
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Recherche dans une liste

## Problème de position

L'algorithme vu dans la leçon précédente à pour mérite de tester la présence d'un nombre entier dans une liste d'entier non trié. Après analyse de sa complexité, nous avons conclu que dans le pire des cas, cette algorithme pouvez être en **« grand O de n » ( O(n) )**.  

Poussons la réflexion un peu plus loin : on souhaite, cette fois ci, programmer une fonction qui permet de connaitre la **position** du nombre dans la liste s'il y est.

Toutes les fonctions pourront être testées avec le programme principal suivant :

```python

L1 = [2, 8, 12, 15]
assert (recherche_seq(1, L1) == -1), "Erreur"
assert (recherche_seq(2, L1) == 0) , "Erreur"
assert (recherche_seq(7, L1) == -1) , "Erreur"
assert (recherche_seq(8, L1) == 1) , "Erreur"
assert (recherche_seq(15, L1) == 3) , "Erreur"
assert (recherche_seq(20, L1) == -1) , "Erreur"

```

## Recherche séquentielle dans une liste non triée

> **A faire :** Compléter la fonction du programme ci-dessous :

```python
def recherche_seq(E, L):
    '''
    Recherche un élément dans une liste d'entiers.
    Renvoie la position de la première occurrence l'élément s'il est présent dans la liste.
    Renvoie -1 si l'élément n'est pas présent dans la liste.
    param L : (list) une liste d'entiers
    param E : (int) un entier
    return : (int) position de l'entier ou -1
    '''
    # partie à compléter

# ----- programme principal -----
L1 = [2, 8, 12, 15]
assert (recherche_seq(1, L1) == -1), "Erreur"
assert (recherche_seq(2, L1) == 0) , "Erreur"
assert (recherche_seq(7, L1) == -1) , "Erreur"
assert (recherche_seq(8, L1) == 1) , "Erreur"
assert (recherche_seq(15, L1) == 3) , "Erreur"
assert (recherche_seq(20, L1) == -1) , "Erreur"

```

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Voici le contenu qui s’affiche quand on clique sur la ligne ci-dessus.</p>
    <pre><code>
        def recherche_seq(E, L):
        '''
        Recherche un élément dans une liste d'entiers.
        Renvoie la position de la première occurrence l'élément s'il est présent dans la liste.
        Renvoie -1 si l'élément n'est pas présent dans la liste.
        param L : (list) une liste d'entiers
        param E : (int) un entier
        return : (int) position de l'entier ou -1
        '''
        for indice in range(len(L)):
            if E == L[indice] :
                return indice
        return -1
        # ----- programme principal -----
        L1 = [2, 8, 12, 15]
        assert (recherche_seq(1, L1) == -1), "Erreur"
        assert (recherche_seq(2, L1) == 0) , "Erreur"
        assert (recherche_seq(7, L1) == -1) , "Erreur"
        assert (recherche_seq(8, L1) == 1) , "Erreur"
        assert (recherche_seq(15, L1) == 3) , "Erreur"
        assert (recherche_seq(20, L1) == -1) , "Erreur"
    </code></pre>
  </div>
</details>
<br>

## Recherche séquentielle dans une liste triée
On souhaite optimiser la fonction précédente lorsque la liste est triée.

> **A faire :** Compléter la fonction du programme ci-dessous :

```python
def recherche_seq_triee(E, L):
    '''
    Recherche un élément dans une liste d'entiers triée.
    Renvoie la position de l'élément s'il est présent dans la liste.
    Renvoie None si l'élément n'est pas présent dans la liste.
    param L : (list) une liste d'entiers triés par ordre croissant
    param E : (int) un entier
    return : (int) position de l'entier ou -1
    '''
    # partie à compléter
```

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Voici le contenu qui s’affiche quand on clique sur la ligne ci-dessus.</p>
    <pre><code>
    def recherche_seq_triee(E, L):
    '''
    Recherche un élément dans une liste d'entiers triée.
    Renvoie la position de l'élément s'il est présent dans la liste.
    Renvoie None si l'élément n'est pas présent dans la liste.
    param L : (list) une liste d'entiers triés par ordre croissant
    param E : (int) un entier
    return : (int) position de l'entier ou -1
    '''
    for indice in range(len(L)):
        if E == L[indice]:
            return indice
    return -1
    </code></pre>
  </div>
</details>


## Recherche dichotomique

Dans cette partie, on s'intéresse encore à la recherche dans une liste triée, et on souhaite encore optimiser le programme précédent.

### Préambule

🖊️ Quelle est la meilleure stratégie pour trouver la bonne réponse au <a href="./jeu_plus_ou_moins.html" target="_blank">Jeu du plus/moins</a> ?

### Principe

Lorsque la liste dans laquelle la recherche se fait est triée, il est possible d'appliquer la même méthode que pour le jeu du Plus/Moins : la recherche dichotomique.

Un exemple possible expliqué ici : <a href="./exemple_application_algo_recherche_dichotomique.pdf" target="_blank">Exemple algorithme recherche dichotomique</a>

### Écriture d'un algorithme

🖊️ Écrire la fonction basée sur la recherche par dichotomie.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Voici le contenu qui s’affiche quand on clique sur la ligne ci-dessus.</p>
    <pre><code>
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
    </code></pre>
  </div>
</details>

### Pour allez plus loin

<a href="https://professeurb.github.io/articles/dichoto/"> Lire ceci</a>