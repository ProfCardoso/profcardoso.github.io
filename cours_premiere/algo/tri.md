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

### Terminaison de l'algorithme

🖊️ Démontrer la terminaison de l'algorithme.

### Correction de l'algorithme

🖊️ Proposer un invariant pour chacune des deux boucles.

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

### Terminaison de l'algorithme

🖊️ Démontrer la terminaison de l'algorithme.

### Correction de l'algorithme

🖊️ Proposer un invariant pour chacune des deux boucles.

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

