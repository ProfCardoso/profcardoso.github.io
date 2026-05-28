---
title : Algorithmique
---

<link rel="stylesheet" href="../../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Les tris

## Tri par sélection

L'algorithme de tri par sélection est un algorithme classique qui permettent de trier une liste.

### Principe

Lien : <a href="./tri_selection.html" target="_blank" >Visualisation du principe du tri par selection</a>

### Algorithme

🖊️ Repérer les actions qui sont répétées.

🖥️ Proposer une fonction qui prend une liste en paramètre et modifie cette liste pour qu'à la fin de l'exécution de la fonction la liste soit triée par ordre croissant.

🖥️ Compléter avec le programme principal qui permet de tester la fonction avec une liste de 20 nombres entiers choisis aléatoirement entre 0 et 99.


<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <pre><code>
      from random import randint
      def tri_selection(tab):
        n = len(tab)

        for i in range(n):
            indice_min = i

            for j in range(i + 1, n):
                if tab[j] < tab[indice_min]:
                    indice_min = j

            tab[i], tab[indice_min] = tab[indice_min], tab[i]

        return tab
      # ==== Programme principal ====
      L = [randint(0,99) for _ in range(20)]
      print(L)
      tri_selection(L)
      print(L)
    </code></pre>
  </div>
</details>



### Terminaison de l'algorithme

🖊️ Démontrer la terminaison de l'algorithme.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution </u></summary>
  <div style="margin-top: 10px;">
    <p>Les boucles for parcourent un nombre fini d’indices. Elles s’arrêtent donc forcément. Le tri par sélection termine toujours.</p>
  </div>
</details>

### Correction de l'algorithme

🖊️ Proposer un invariant pour chacune des deux boucles.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution </u></summary>
  <div style="margin-top: 10px;">
    <p>Invariant de boucle : au début de chaque tour de boucle for i, les éléments avant l’indice i sont déjà triés et sont les plus petits éléments du tableau.
    Au départ, avant i = 0, il n’y a aucun élément avant i, donc c’est vrai.
    À chaque tour, on cherche le plus petit élément dans la partie non triée, puis on l’échange avec l’élément à la position i. Donc la partie triée gagne un élément bien placé.
    À la fin, quand i a parcouru tout le tableau, tous les éléments sont triés.
    </p>
  </div>
</details>

### Coût

🖊️ Pour quelle configuration de liste l'algorithme fait-il le moins de comparaison ? Dans ce cas combien en fait-il ?

🖊️ Pour quelle configuration de liste l'algorithme fait-il le plus de comparaison ? Dans ce cas, combien en fait-il ?

## Tri par insertion

L'algorithme de tri par sélection est un algorithme classique qui permettent de trier une liste.

### Principe

Lien : <a href="./tri_insertion.html" target="_blank" >Visualisation du principe du tri par insertion</a>

### Algorithme

🖊️ Repérer les actions qui sont répétées.

🖥️ Proposer une fonction qui prend une liste en paramètre et modifie cette liste pour qu'à la fin de l'exécution de la fonction la liste soit triée par ordre croissant.

🖥️ Compléter avec le programme principal qui permet de tester la fonction avec une liste de 20 nombres entiers choisis aléatoirement entre 0 et 99.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <pre><code>
      from random import randint
      def tri_insertion(tab):
        n = len(tab)

        for i in range(1, n):
            valeur = tab[i]
            j = i - 1

            while j >= 0 and tab[j] > valeur:
                tab[j + 1] = tab[j]
                j = j - 1

            tab[j + 1] = valeur

        return tab
      # ==== Programme principal ====
      L = [randint(0,99) for _ in range(20)]
      print(L)
      tri_selection(L)
      print(L)
    </code></pre>
  </div>
</details>

### Terminaison de l'algorithme

🖊️ Démontrer la terminaison de l'algorithme.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution </u></summary>
  <div style="margin-top: 10px;">
    <p>La boucle for parcourt un nombre fini d’indices.
      Dans la boucle while, la variable j diminue de 1 à chaque tour. Elle finit donc par devenir négative, ou bien on trouve un élément plus petit ou égal à valeur. La boucle while s’arrête donc toujours.
      Le tri par insertion termine toujours.
    </p>
  </div>
</details>

### Correction de l'algorithme

🖊️ Proposer un invariant pour chacune des deux boucles.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution </u></summary>
  <div style="margin-top: 10px;">
    <p>Invariant de boucle : au début de chaque tour de boucle for i, la partie du tableau entre les indices 0 et i - 1 est déjà triée.
      Au départ, pour i = 1, la partie [tab[0]] contient un seul élément, donc elle est forcément triée.
      À chaque tour, on prend tab[i], puis on décale vers la droite les éléments plus grands que lui. Ensuite, on insère la valeur à la bonne position. La partie allant de 0 à i devient donc triée.
      À la fin, quand tous les éléments ont été insérés, tout le tableau est trié.
    </p>
  </div>
</details>

### Coût

🖊️ Pour quelle configuration de liste l'algorithme fait-il le moins de comparaison ? Dans ce cas combien en fait-il ?

🖊️ Pour quelle configuration de liste l'algorithme fait-il le plus de comparaison ? Dans ce cas, combien en fait-il ?

## D'autre tris 

### Tri à bulles (du plus grand au plus petit)

Fonctionnement :

- L’algorithme parcourt la liste et compare les éléments consécutifs. Lorsque deux éléments consécutifs ne sont pas dans l’ordre, ils sont échangés.

- Après un premier parcours complet de la liste, le plus petit élément est forcément en fin de la liste, à sa position définitive.

- On parcourt la liste à nouveau, en s’arrêtant à l’avant-dernier élément.

- Après ce deuxième parcours, les deux plus petits éléments sont à leur positions définitives.

- ...

Il faut donc répéter les parcours de la liste, jusqu’à ce que tous les éléments soient à leurs positions définitives.

🖥️ Travail à faire : Proposer un programme qui trie une liste suivant la méthode du tri à bulles.


<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <pre><code>
      from random import randint
      def tri_bulle(liste):
          """
          Trie la liste dans l'ordre décroissant
          """
          a_trouve_echange = True
          i_max = len(liste)-1
          while a_trouve_echange and i_max > 1 :
              a_trouve_echange = False
              for j in range(0, i_max):
                  if liste[j] < liste[j+1]:
                      liste[j], liste[j+1] = liste[j+1], liste[j]
                      a_trouve_echange = True
              i_max = i_max - 1
      # ==== Programme principal ====
      L = [randint(0,50) for _ in range(20)]
      print(L)
      tri_bulle(L)
      print(L)
    </code></pre>
  </div>
</details>

### Compétitions de tri ! Les participants sont triés sur le volet !

#### Déroulement de l’activité

Les élèves travaillent par groupes de 2 ou 3.

Chaque groupe doit :

- implémenter plusieurs tris ;
- générer des listes aléatoires ;
- comparer les performances ;
- présenter les résultats.

#### Étape 1 — Les algorithmes

A vous de choisir votre tri :

- tri par sélection ;
- tri par insertion.
- le tri à bulles ;
- le tri fusion (bonus difficile).

#### Étape 2 — Générer des listes aléatoires

```python
import random

def liste_aleatoire(n):
    tab = []

    for i in range(n):
        tab.append(random.randint(0, 1000))

    return tab
```

Test :

```python
print(liste_aleatoire(10))

```

#### Étape 3 — Mesurer le temps d’exécution

```python
import time

tab = liste_aleatoire(1000)

debut = time.time()

tri_selection(tab)

fin = time.time()

print("Temps :", fin - debut)
```

#### Étape 4 — Faire un vrai comparatif

Remplissez ce tableau :

|Taille |	Sélection |	Insertion |	Bulles |
|:-----:|:---------:|:---------:|:------:|
|100		| | | |
|500		|	| | |
|1000	| | | |

