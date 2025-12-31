---
title: Projet Python
---

# Projet Python : jeu de société

<link rel="stylesheet" href="../../assets/style.css" />


## Consignes

Par groupe de 3 ou 4, vous devrez réaliser un jeu de société ou jeu de carte de votre choix (autre que ceux faits en classe). Ce dernier sera une version jouable dans la console grâce au lancement d'une seule fonction, nommée `jouer()`. 

Exemple : 

```
>>> jouer()
Lancement de la partie de solitaire
...
```

Voici quelques consignes :

- Créez un dossier `Projet_2`, dans votre dossier `NSI`, et y ajouter un document texte avec le **nom**, le **prénom** et le **sujet** choisi par votre groupe.
- Commentez les parties du code qui ne seraient pas immédiatement compréhensibles à la lecture.
- Ecrivez un document consignant vos recherches sur le sujet, la répartition des tâches et une explication du fonctionnement de votre code.
- Pour chacune de vos fonctions, vous écrirez une documentation sous forme de docstring.
- A la du projet, celui-ci sera à rendre complet (fichier(s) python + document de réflexion) sur Pearltrees.

<span style="color:red">Attention ! L'IA peut être utilisé pour vous aider à chercher des idées ou vous aidez à écrire votre code, pas le faire à votre place !</span>

## 1ere étape : Contexte du projet (1 heure)

Vous allez créer un programme Python qui manipule des listes, selon le jeu de société de votre choix (jeu sur grille, jeu de carte, etc.).  

Avant de coder, vous devez produire un document de réflexion qui répond aux consignes suivantes.

### 📝 Consigne 1 — Décrire le projet 

Expliquez (en 4–6 lignes) :

- Quel est le but du programme ?

- Que doit-il permettre de faire ?

- Quels sont les éléments manipulés ?

- Quel sera le rôle des listes dans ce programme ?

👉 But : vérifier que vous comprenez l’objectif avant de coder.

### 📝 Consigne 2 — Identifier les données 

Listez précisément toutes les données que vous devrez stocker, par exemple :

- objets, scores, positions, valeurs, etc.

- une grille ? une liste simple ? plusieurs listes ? une liste de listes ?

- quels types d’éléments contiennent ces listes ?

Pour chaque donnée, indiquez :

- pourquoi ce choix est pertinent

- un exemple concret de ce que contiendra la liste

👉 Exemple attendu : “Le plateau sera une liste de listes, car il représente une grille 6x7. Chaque case contient `.` si elle est vide ou `X`/`O` si elle est occupée.” 

### 📝 Consigne 3 — Lister les opérations à effectuer 

Pour chaque liste, écrivez quelles opérations votre programme devra réaliser :

- ajout d’élément ? (`append`)

- suppression ? (`remove`, `pop`)

- insertion ? (`insert`)

- parcours ? (`for`)

- filtrage ? (liste en compréhension)

### 📝 Consigne 4 — Concevoir les fonctions

Listez les fonctions dont vous aurez besoin.
Pour chaque fonction, indiquez :

- son nom

- ses paramètres

- ce qu’elle doit retourner

- un exemple d’appel

👉 Exemple attendu :

```
Nom : jouer_coup
Paramètres : plateau (liste de listes), colonne (int), pion (str)
Rôle : placer le pion dans la bonne case
Retour : True/False
Exemple : jouer_coup(plateau, 3, "X")
```



### 📝 Consigne 5 — Difficultés anticipées 

Écrivez ce qui risque de poser problème :

- indices ?

- listes modifiées pendant le parcours ?

- compréhension de la grille ?

- boucle infinie ?

Et comment vous comptez les résoudre !

## 2eme étape : Écriture du code (4 heures)

Vous allez maintenant passer de la réflexion à la programmation.
L’objectif est de transformer votre document préparatoire en programme Python fonctionnel, lisible et structuré.

Vous devez respecter les consignes ci-dessous.

###  Organisation du code
#### ✔️ Créer un fichier projet.py

Tout votre programme doit tenir dans ce fichier (ou plusieurs si vous êtes à l’aise).

#### ✔️ Commentez votre code

Chaque fonction doit commencer par un docstring :

```
def nom_fonction(x, y):
    """
    Description courte.
    Paramètres :
    - x : ...
    - y : ...
    Retour : ...
    """
```

#### ✔️ Respecter le plan conçu lors de la réflexion

Votre code doit suivre les décisions prises lors de la première séance :

- structure des listes

- choix des fonctions

- méthode pour générer la liste ou la grille

- modalités d’ajout/suppression

💡 Si vous changez quelque chose, vous devez justifier brièvement en commentaire.


### 🎁 Bonus (facultatif mais valorisé)

Vous pouvez ajouter :

- un menu interactif

- une sauvegarde dans un fichier texte

- des statistiques

- un score

- une IA simple

## 3ème étape : Passage à l'oral

1. Une présentation de 5 à 10 min où vous présenterez votre projet avec en point important :

- le but du jeu (règles),
- une démonstration (rapide),
- où sont les listes et pourquoi les avoir utilisées ici,
- les points qui vous ont causé des difficultés.

2. Ensuite une phase de plusieurs questions de ma part et/ou du public.  
  
3. Et pour finir, chaque élève sera interrogé individuellement sur une fonction tirée aléatoirement du projet pour m'expliquer en détails

## Barème



<table>
  <thead>
    <tr>
      <th>Partie</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Projet</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Document réflexif</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Oral</td>
      <td>8</td>
    </tr>
    
  </tbody>
</table>

