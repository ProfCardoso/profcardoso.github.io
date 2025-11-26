---
title: Représentation des nombres
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Exercice Bonus

>
> ## Exercice 1 – Comprendre l’indexation
>
> On considère la liste suivante :
>
```python
L = [3, 8, 2, 7, 4, 10]
```
>
> 1. Que vaut L[3] ?
>
> 2. Que vaut L[-1] ?
> 
> 3. Écrire l’instruction qui remplace l’élément d'indice 4 par 12.
>
>
<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <p>1. L[3] vaut 7 </p>
    <p>2. L[-1] vaut 10 → dernier élément (indices négatifs) </p>
    <pre><code class="language-python">
      L[4] = 12
    </code></pre>
  </div>
</details>

>
> ## Exercice 2 – Méthodes de liste
>
> On utilise :
>
```python
noms = ["Alice", "Bob", "Charles"]
```
>
> 1. Ajouter "David" à la fin de la liste.
>
> 2. "Zack" en position 1.
>
> 3. Supprimer "Bob" de la liste.
>
>
<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      # Exercice 1
      noms.append("David") # → ajoute à la fin.
    </code></pre>
    <pre><code class="language-python">
      # Exercice 2
      noms.insert(1, "Zack") # → insère à l’indice 1.
    </code></pre>
    <pre><code class="language-python">
      # Exercice 3
      noms.remove("Bob") # → retire la première occurrence de "Bob".
    </code></pre>
  </div>
</details>

>
> ## 🎮 Exercice 3 – Gestion d’inventaire d’un jeu vidéo (sous la forme de listes)
>
> Contexte :
>
> Tu développes un petit jeu vidéo d’aventure. Le joueur possède un inventaire sous la forme d’une liste Python, qui contient des objets.
>
> Au début, l’inventaire contient :
>
```python
inventaire = ["épée", "potion", "bouclier", "potion"]
```
>
> Tu dois écrire des fonctions Python permettant de gérer cet inventaire au fur et à mesure du jeu.
>
> 1. Créer une fonction objet(nom, inventaire) avec en paramètre le nom de l'objet à ajouter à l'inventaire, lui aussi donné en paramètre.
>
> 2. Créer une fonction utiliser(nom, inventaire) avec en paramètre le nom de l'objet à supprimer de l'inventaire, lui aussi donné en paramètre.
>
> 3. Créer une fonction comptage(nom, inventaire) avec en paramètre le nom de l'objet à compter dans l'inventaire, lui aussi donné en paramètre.
>
> Certaines parties du code ont ajouté des objets inutiles "vide". 
> On veut créer un nouvel inventaire où les "vide" sont retirés.
>
> On te donne une version salie :
```python
inventaire = ["épée", "vide", "potion", "vide", "bouclier"]
```
>
> 4. Construis une nouvelle liste "propre" sans modifier celle d’origine.
>
<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <pre><code class="language-python">
      # Exercice 1
      def objet(nom, inventaire):
        inventaire.append(nom)
        return inventaire
    </code></pre>
    <pre><code class="language-python">
      # Exercice 2
      def utiliser(nom, inventaire):
        inventaire.remove("potion")
        return inventaire
    </code></pre>
    <pre><code class="language-python">
      # Exercice 3
      def comptage(nom, inventaire):
        compte = 0
        for objet in inventaire:
            if objet == nom:
                compte += 1
        return compte
    </code></pre>
    <pre><code class="language-python">
      # Exercice 4
      inventaire_propre = []
      for x in inventaire:
          if x != "vide":
              inventaire_propre.append(x)
    </code></pre>
  </div>
</details>