---
title: Introduction à l’algorithmique

---

# Introduction à l’algorithmique

## Introduction

L’algorithmique est une vaste discipline étudiant les moyens de trouver une suite d’opérations permettant de résoudre un problème ou de répondre à une question. On appelle ces suites d’instructions des algorithmes. Il existe de nombreux algorithmes comme une recette de cuisine ou des instructions pour construire un modèle en Lego. Nous nous intéresserons ici aux algorithmes du monde informatique qui peuvent néanmoins avoir des répercutions dans d’autres disciplines.  
  
Nous verrons qu’il existe plusieurs familles de problèmes et donc d’algorithmes.  
  
## Recherche d’occurrence

Nous allons étudier notre premier algorithme sur le problème de recherche d’occurrence, c’est à dire trouver si un élément est dans une liste (ou un tableau). Nous voulons donc savoir si un élément x est dans le tableau t. Voici donc un algorithme permettant de répondre à cette question :

```
VARIABLES
t : tableau d'entiers
x : nombre entier
present : booléen (VRAI ou FAUX)
i : nombre entier

DEBUT
present ← FAUX
i ← 1
tant que i<=longueur(t) et que present==FAUX:
	si t[i]==x:
	    present ← VRAI
	fin si
	i ← i+1
fin tant que
renvoyer la valeur de present
FIN

```
Deux remarques :

- un algorithme s’écrit en langage naturel avec quelques notations informatiques. Mais il doit pouvoir être implémenté dans n’importe quel langage.
- on fait commencer la numérotation des tableaux à 1 (vraisemblablement car l’algorithmique est née avant l’informatique).
Pour comprendre un algorithme, il faut le faire tourner à la main sur un exemple simple.

1) Prenons par exemple t=[2,4,8,12,45] et x=8 et faisons tourner l'algorithme.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Déroulé de l'algorithme</p>
    <table>
      <tr>
        <td>boucle</td>
        <td>present</td>
        <td>i</td>
      </tr>
      <tr>
        <td>init.</td>
        <td>FAUX</td>
        <td>1</td>
      </tr>
      <tr>
        <td>1</td>
        <td>FAUX</td>
        <td>2</td>
      </tr>
      <tr>
        <td>2</td>
        <td>FAUX</td>
        <td>3</td>
      </tr>
      <tr>
        <td>3</td>
        <td>VRAI</td>
        <td>4</td>
      </tr>
    </table>
    <p> On sort de la boucle car present = VRAI et l'algorithme renvoie donc VRAI</p>
  </div>
</details>
<br>

2) Faites tourner l’algorithme à la main avec t=[4,9,12] et x=23

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Déroulé de l'algorithme</p>
    <table>
      <tr>
        <td>boucle</td>
        <td>present</td>
        <td>i</td>
      </tr>
      <tr>
        <td>init.</td>
        <td>FAUX</td>
        <td>1</td>
      </tr>
      <tr>
        <td>1</td>
        <td>FAUX</td>
        <td>2</td>
      </tr>
      <tr>
        <td>2</td>
        <td>FAUX</td>
        <td>3</td>
      </tr>
      <tr>
        <td>3</td>
        <td>FAUX</td>
        <td>4</td>
      </tr>
    </table>
    <p> On sort de la boucle car 4 > 3 et l'algorithme renvoie donc FAUX</p>
  </div>
</details>
<br>

## Complexité

### Nombre d'opérations

La complexité d’un algorithme permet de mesurer son efficacité et ainsi de le comparer aux autres algorithmes. Nous nous intéresserons au temps d’exécution pour mesurer la complexité (il est possible d’utiliser la mémoire utilisée). Pour estimer le temps d’exécution on comptera les opérations dans l’algorithme dans le pire des cas, c’est à dire dans le cas qui prend le plus de temps.  
  
Par exemple pour l’algorithme précédent, le pire des cas est lorsqu’il ne trouve pas l’élément à chercher.  
  
3) Reprenons donc l’algorithme précédent et comptons le nombre d’opérations pour qu’il se termine. Nous supposerons que le tableau en entrée contient **n éléments.**

```
VARIABLES
t : tableau d'entiers
x : nombre entier
present : booléen (VRAI ou FAUX)
i : nombre entier

DEBUT
present ← FAUX
i ← 1
tant que i<=longueur(t) et que present==FAUX:
	si t[i]==x:
	    present ← VRAI
	fin si
	i ← i+1
fin tant que
renvoyer la valeur de present
FIN
```

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Voici le contenu qui s’affiche quand on clique sur la ligne ci-dessus.</p>
    <pre><code>
    DEBUT
    present ← FAUX									[1 fois]
    i ← 1											[1 fois]
    tant que i<=longueur(t) et que present==FAUX:	[n+1 fois]
      si t[i]==x:									[n fois]
          present ← VRAI							[0 fois]
      fin si
      i ← i+1										[n fois]
    fin tant que
    renvoyer la valeur de present					[1 fois]
    FIN
    </code></pre>
    <p>Il y a donc 3n+4 opérations.</p>
  </div>
</details>
<br>


## Ordre de grandeur asymptotique

Pour comparer les algorithmes il faut exprimer la complexité de manière plus simple qu’avec le nombre exact d’opérations. Pour cela, on ne va garder que *l’ordre de grandeur asymptotique*. C’est à dire qu’on s’intéresse uniquement à la plus **grande puissance de n** dans l’expression de la complexité. Et on notera le résultat avec un **O majuscule (on dira « grand O »)**.  
  
Par exemple 6n² + 5n + 45 = O(n²), on dira que la complexité est en **« grand O de n² »**.  

4) Quelle est alors la complexité de notre algorithme ?

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>La complexité est en O(n).</p>
  </div>
</details>
<br>

5) Écrire un algorithme (en pseudo-code) qui permet de déterminer **le maximum dans un tableau d’entiers**. Faire tourner l’algorithme sur le tableau [2,6,4,1,9] puis déterminer la complexité de l’algorithme.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Déroulé de l'algorithme</p>
    <pre><code>
    VARIABLES
    t : tableau d'entiers
    max : nombre entier
    i : nombre entier
    DEBUT
    max ← t[1]
    i ← 2
    tant que i<=longueur(t):
      si t[i] > max:
          max ← t[i]
      fin si
      i ← i+1
    fin tant que
    renvoyer la valeur de max
    FIN
    </code></pre>
    <p>Déroulé de l'algorithme</p>
    <table>
      <tr>
        <td>boucle</td>
        <td>max</td>
        <td>i</td>
      </tr>
      <tr>
        <td>init.</td>
        <td>2</td>
        <td>2</td>
      </tr>
      <tr>
        <td>1</td>
        <td>6</td>
        <td>3</td>
      </tr>
      <tr>
        <td>2</td>
        <td>6</td>
        <td>4</td>
      </tr>
      <tr>
        <td>3</td>
        <td>6</td>
        <td>5</td>
      </tr>
      <tr>
        <td>4</td>
        <td>9</td>
        <td>6</td>
      </tr>
    </table>
    <p>On sort de la boucle car 6 > 5 et l'algorithme renvoie donc 9</p>
    <pre><code>
    DEBUT
    max ← t[1]										[1 fois]
    i ← 2											[1 fois]
    tant que i<=longueur(t):						[n fois]
      si t[i] > max:								[n-1 fois]
          max ← t[i]								[n-1 fois]
      fin si
      i ← i+1										[n-1 fois]
    fin tant que
    renvoyer la valeur de max						[1 fois]
    FIN
    </code></pre>
    <p>Il y a donc 4n opérations.</p>
    <p>La complexité est en O(n).</p>
  </div>
</details>
<br>




6) Écrire un algorithme qui permet de calculer la moyenne des entiers d’un tableau. Faire tourner l’algorithme sur le tableau [2,6,4,1,9] puis déterminer la complexité de l’algorithme.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Déroulé de l'algorithme</p>
    <pre><code>
    VARIABLES
    t : tableau d'entiers
    somme : nombre entier
    moyene : nombre flottant
    i : nombre entier
    DEBUT
    somme ← 0
    i ← 1
    tant que i<=longueur(t):
      somme ← somme + t[i]
      i ← i+1
    fin tant que
    moyenne = somme / longueur(t)
    renvoyer moyenne
    FIN
    </code></pre>
    <p>Déroulé de l'algorithme</p>
    <table>
      <tr>
        <td>boucle</td>
        <td>somme</td>
        <td>i</td>
      </tr>
      <tr>
        <td>init.</td>
        <td>0</td>
        <td>1</td>
      </tr>
      <tr>
        <td>1</td>
        <td>2</td>
        <td>2</td>
      </tr>
      <tr>
        <td>2</td>
        <td>8</td>
        <td>3</td>
      </tr>
      <tr>
        <td>3</td>
        <td>12</td>
        <td>4</td>
      </tr>
      <tr>
        <td>4</td>
        <td>13</td>
        <td>5</td>
      </tr>
      <tr>
        <td>5</td>
        <td>22</td>
        <td>6</td>
      </tr>
    </table>
    <p>On sort de la boucle car 6 > 5 et l'algorithme renvoie donc 22/5 = 4.4</p>
    <pre><code>
    DEBUT
    somme ← 0										[1 fois]
    i ← 1											[1 fois]
    tant que i<=longueur(t):						[n+1 fois]
      somme ← somme + t[i]						[n fois]
      i ← i+1										[n fois]
    fin tant que
    moyenne = somme / longueur(t)					[1 fois]
    renvoyer moyenne								[1 fois]
    FIN
    </code></pre>
    <p>Il y a donc 3n+5 opérations.</p>
    <p>La complexité est en O(n).</p>
  </div>
</details>
<br>

## Pour les plus rapides

7) Écrire un programme en Python qui va permettre de mesurer le temps d’exécution de l'algorithme de recherche d’occurrence (On appelle cela un benchmark). Le programme doit faire les choses suivantes :

- implémenter l'algorithme de recherche dans une fonction recherche(t, k) ;  
- générer un tableau de longueur n rempli avec des entiers aléatoires ;  
- enregistrer l’heure de début (voir le module time et la méthode time()) ;  
- exécuter l’algorithme de recherche avec un nombre qui n’est pas dans le tableau ;   
- avec l’heure de fin, afficher le temps d’exécution.  

Essayer avec n = 10, 100, 1000… et voir si le temps d’exécution correspond bien à la complexité.


<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Voici le contenu qui s’affiche quand on clique sur la ligne ci-dessus.</p>
    <pre><code>
    import random
    import time
    n = 10
    t = []
    # On remplit le tableau avec des nombres aléatoires entre 0 et n
    print("Création du tableau…")
    for i in range(n):
        t.append(random.randint(0,n))
    # Algorithme de recherche
    def recherche(t,k):
        """
            Cherche k dans le tableau t
        """
        i = 0
        present = False
        while i < len(t):
            if t[i] == k:
                present = True
            i = i + 1
        return present
    # Heure de début
    t1 = time.time()
    # On cherche un nombre qui n'est pas dans le tableau
    recherche(t,n+1)
    # Heure de fin
    t2 = time.time()
    print("n =",n,"| temps :",t2-t1)
    </code></pre>
    <pre><code>
    n = 10 | temps : 2.86102294921875e-06
    n = 100 | temps : 1.33514404296875e-05
    n = 1000 | temps : 0.00015878677368164062
    n = 10000 | temps : 0.0015091896057128906
    n = 100000 | temps : 0.01606440544128418
    n = 1000000 | temps : 0.15948057174682617
    n = 10000000 | temps : 1.6848335266113281
    </code></pre>
    <p>La complexité est bien en O(n) car le temps augmente linéairement avec n (il est multiplié par 10 quand n est multiplié par 10).</p>
  </div>
</details>
<br>




