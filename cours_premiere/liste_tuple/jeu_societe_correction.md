---
title: Initialisation à Python
---

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Jeu de société

**Objectifs** : Le but de ce tp est de vous faire manipuler les listes grâce à différentes activités.   

**Attention, sauvegarder correctement ce script python, nous le réutiliserons plus tard.** 

## Jeux de dés 🎲

On souhaite simuler plusieurs lancer de dés. Lancer cette fonction à chaque fois que vous générer cette page.

1. Créez une fonction `plusieurs_lancer(des)` qui prend en paramètre le nombre de dés et renvoie une liste de valeur de dés.   

*Aide : Il pourrait être intérressant de créer en amont une fonction `lance_dé()` sans paramètre qui utilise la fonction randint de la  bibliothèque random pour tirer aléatoirement une valeur entre 1 et 6 pour modéliser le lancer de dé*  

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      import random

      def plusieurs_lancer(des):
          liste = []
          for i in range(des):
              lance = random.randint(1,6)
              liste.append(lance)
          return liste
    </code></pre>
  </div>
</details>

2. Écrivez une fonction `minimum(liste_de)` qui prend en paramètre une liste de dés et qui renvoie la valeur minimum dans cette liste. Faite de même pour `maximum(liste_de)`.  

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      def minimum(liste_de):
      return min(liste_de)


      def minimum(liste_de):
          mini = 7
          for i in range(len(liste_de)):
              if liste_de[i] < mini:
                  mini = liste_de[i]
          return mini

      def maximum(liste_de):
          maxi = 0
          for i in range(len(liste_de)):
              if liste_de[i] > maxi:
                  maxi = liste_de[i]
          return maxi
    </code></pre>
  </div>
</details>

3. On souhaite tester si la liste de dés possède un certain nombre de dés de valeur n. Créer une fonction `test_presence_n(liste_de,n)` qui prend en paramètre une liste de dés et un entier n qui vérifie si le dé se trouve dans la liste.  

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
    
      def test_presence_n(liste_de,n):
          return n in liste_de

    </code></pre>
  </div>
</details>

## Jeu des petits chevaux 🐴

Vous allez par la suite créer une version simplifiée du jeu des petits chevaux.  

<div style="display: flex; flex-direction:column;  text-align: center; ">
  <img style="margin: auto;" src="../../images/Petit Cheveau.jpg" alt="Python" width="800" />
</div>

**Simplification des règles :** 

- Un cheval ( représenté par un `'C'` ) doit atteindre la ligne d'arrivée avant les autres.
Pour cela il avance d'un certain nombre de case que le dé indique. 
- La "piste de course" est le nombre de case avant la ligne d'arrivée, et le cheval
commence toujours à la première. Ici, une piste sera une **liste de taille 10**, avec en
premier élément ( indice 0 ) un cheval `'C'`, des cases `'_'` et une arrivée `'A'` ( à la fin de
la liste )
- Le jeu se termine quand le premier cheval arrive sur la dernière case de la piste.y

1. Créez une fonction `nouvelle_piste(t)` avec en paramètre une taille t et qui renvoie
une liste de chaîne de caractères.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      def nouvelle_piste(t):
        """
        fonction qui renvoie une liste de chaîne de caractères composé du cheval 'C',
        des cases de piste '_' et de l'arrivée 'A'
        """
        cheval = ['C']
        case = ['_']
        arrivee = ['A']
        piste = cheval + (t-2)*case + arrivee
        return piste
    </code></pre>
  </div>
</details>

2. Ecrivez une fonction `cheval_arrive(piste)` qui test si le cheval est sur la dernière case de
la piste, donc en dernière position de la liste. Elle prendra une liste ( correspondant à
la piste ) en paramètre et renverra True ou False selon la positon du cheval.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      def cheval_arrive(piste):
        """
        Fonction qui prendra une liste ( piste ) en paramètre et
        renverra True ou False selon la position du cheval :
            - True : Le cheval est arrivé
            - False : Le cheval n'est pas arrivé
        """
        if 'A' in piste:
            return False
        else:
            return True
    </code></pre>
  </div>
</details>

3. Créez une fonction `tour_de_jeu(piste)`, qui prendra la liste correspondant à la piste en
paramètre, et renverra la piste avec la nouvelle position du cheval après un lancer de
dé.  

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      def tour_de_jeu(piste):
        """
        Fonction qui prendra la liste (piste) en paramètre,
        et renverra la piste avec la nouvelle position du cheval
        après un lancer de dé.
        """
        de = random.randint(1,6)
        taille =len(piste)
        for i in range(taille):
            if piste[i] == "C":
                position = i
        if position + de <= taille-1:
            piste[position+de] = "C"
            piste[position]="_"
        return piste
    </code></pre>
  </div>
</details>

Attention : si la nouvelle position du cheval dépasse la ligne d'arrivée, le cheval ne
bougera pas et passe son tour. De plus, n'oubliez pas "d'effacer" le cheval de son
ancienne position.

4. Réalisez un script python qui joue maximum 5 tours de jeu et qui écris un message de félicitation si le cheval est arrivé, ou un message d'encouragement si celui ci n'a pas fini la course. 

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      tour = 0
      taille = 10
      piste = nouvelle_piste(taille)

      while tour < 5 and not(cheval_arrive(piste)):
        tour +=1 
        piste = tour_de_jeu(piste)
        print(piste)

      if cheval_arrive(piste) :
        print("BRAVO")
      else:
        print("DOMMAGE")
    </code></pre>
  </div>
</details>

## Jeu de carte 🃏

Un jeu de 52 cartes standard est composé de quatre couleurs : pique, cœur, carreau et trèfle.  
Chaque couleur contient 13 valeurs :

- **1 carte spéciale** : As (peut être la plus basse ou la plus haute selon le jeu)

- **9 cartes numérotées** : 2, 3, 4, 5, 6, 7, 8, 9, 10

- **3 figures** : Valet, Dame, Roi

Les couleurs **piques** ♠️ et **trèfles** ♣️ sont **noires**, tandis que **cœurs** ♥️ et **carreaux** ♦️ sont **rouges**.

Le jeu peut être utilisé dans des jeux comme le poker, le blackjack, la bataille, le solitaire, etc.

On souhaite modéliser un jeu de carte en utilisant le langage Python, voici un exemple possible de liste pour représenter ces cartes : 

```python
# Valeurs possibles d'une carte
valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]

# Symboles (couleurs) possibles
symboles = ["♠️", "♥️", "♦️", "♣️"]
```

1) Écrire une fonction `creer_carte(valeur,symbole)` qui "crée" une carte à partir d'une valeur et d'un symbole donné en paramètre et renvoie la valeur et le symbole de la carte.

```python
>>> creer_carte("3","♠️")
3 de ♠️
```

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      def creer_carte(valeur,symbole):
        """
        Fonction qui “crée” une carte à partir d’une valeur et d’un symbole donné en paramètre
        et renvoie la valeur et le symbole de la carte.
        """
        return valeur + "de" + symbole
    </code></pre>
  </div>
</details>
  
  

2) Écrire une fonction `creer_jeu(valeurs,symboles)` qui "crée" un jeu de carte à partir des valeurs et des symboles donnés en paramètre et renvoie une liste contenant toutes les cartes.

```python
>>> valeurs = ["As", "2", "3"]

>>> symboles = ["♠️", "♥️"]

>>> creer_jeu("3","♠️")
["As de ♠️","2 de ♠️","3 de ♠️","As de ♥️","2 de ♥️","3 de ♥️"]
```

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      def creer_jeu(valeurs,symboles):
        """
        fonction qui “crée” un jeu de carte à partir des valeurs et des symboles donnés en paramètre et renvoie une liste contenant toutes les cartes.
        """
        jeu = []
        for val in valeurs :
            for symb in symboles:
                jeu.append(creer_carte(val,symb))
        return jeu
    </code></pre>
  </div>
</details>

3) Écrire une fonction `tirer_carte(jeu_de_carte)` qui "tire" aléatoirement une carte à partir d'un jeu de carte donné en paramètre. Attention ! Une fois la carte tirée du jeu, le jeu de carte ne doit plus la contenir.

```python

>>> jeu_de_carte = ["As de ♠️","2 de ♠️","3 de ♠️","As de ♥️","2 de ♥️","3 de ♥️"]

>>> tirer_carte(jeu_de_carte)
As de ♥️

>>> print(jeu_de_carte)
["As de ♠️","2 de ♠️","3 de ♠️","2 de ♥️","3 de ♥️"]

```

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      def tirer_carte(jeu_de_carte) :
        """
        Fonction qui “tire” aléatoirement une carte à partir d’un jeu de carte donné en paramètre.
        Attention ! Une fois la carte tirée du jeu, le jeu de carte ne doit plus la contenir.
        """
        numero_de_carte = random.randint(0,len(jeu_de_carte)-1) # tire un numéro de carte ( indice ) compris entre 0 et la taille de la liste - 1

        carte = jeu_de_carte.pop(numero_de_carte) # Retire de la liste et renvoie l'élément à l'indice numéro_de_carte

        return carte
    </code></pre>
  </div>
</details>

## Bonus : Puissance 4 ⭐

On vous demande de réaliser un version jouable du Puissance 4, et ceci depuis l’interpréteur de Thonny ou Edupython.  

Pour vous aider, on vous fournit le squelette de chacune des fonctions ainsi que le programme nécéssaire pour jouer au Puissance 4 : [Squelette du Puissance 4](./puissance4.py)  
On s’accordera à dire qu’une partie se finit si l’un des joueurs forme une ligne, une
colonne ou une diagonale de 4 pions d’affilés, ou que la grille soit pleine de pions sans qu’un joueur ai pu gagner ( dans ce cas ils seront égalités) .
1. Codez les fonctions dont les blocs d’instructions sont vides grâce aux spécifications de ces dernières.

2. Tester de jouer avec la [version graphique](./interface_puissance4.py)  du jeu, fonctionnant avec la bibliothèque Pygame ( vous devrez, pour pouvoir l'utiliser, ajouter le module Pygame à votre environnement de travail )