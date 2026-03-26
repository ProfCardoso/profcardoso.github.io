---
title: Langage Html
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# LES PRINCIPALES BALISES HTML

Les balises HTML sont organisées en différentes catégories selon leur fonction.

## BALISES DE STRUCTURE

- `<!DOCTYPE html>` : Déclare le type de document (HTML5).
- `<html>` : Élément racine du document.
- `<head>` : Contient les métadonnées (titre, encodage, liens CSS).
- `<body>` : Contient le contenu visible de la page.
- `<header>`, `<main>`, `<footer>` : Balises sémantiques définissant les grandes zones de la page.
- `<section>`, `<article>`, `<nav>` : Balises pour structurer le contenu.

## BALISES DE TEXTE

- `<h1>` à `<h6>` : Titres de différents niveaux (h1 étant le plus important).
- `<p>` : Paragraphe.
- `<strong>` : Texte important (généralement affiché en gras).
- `<em>` : Texte mis en emphase (généralement affiché en italique).

## BALISES DE LIEN ET MÉDIA

- `<a href="url">` : Lien hypertexte.
- `<img src="image.jpg" alt="description">` : Image.
- `<video>`, `<audio>` : Éléments multimédias.

## BALISES DE LISTE

- `<ul>` : Liste non ordonnée (à puces).
- `<ol>` : Liste ordonnée (numérotée).
- `<li>` : Élément de liste.

## BALISES DE TABLEAU

- `<table>` : Définit un tableau.
- `<tr>` : Ligne de tableau (Table Row).
- `<th>` : Cellule d'en-tête (Table Header).
- `<td>` : Cellule de données (Table Data).

## BALISES NEUTRES DE MISE EN FORME

- `<div>` : Créer un bloc pour contenir des éléments librement customisable.
- `<span>` : Créer une zone de texte pour y customiser du texte.

## FORMULAIRES ET TRANSMISSION DE DONNÉES

Les formulaires HTML permettent aux utilisateurs d'envoyer des données au serveur. Ils sont définis par la balise `<form>` et contiennent divers éléments interactifs.

### STRUCTURE D'UN FORMULAIRE

```html
<form action="/traitement.php" method="post">
  <label for="nom">Nom :</label>
  <input type="text" id="nom" name="nom" required>

  <label for="email">Email :</label>
  <input type="email" id="email" name="email" required>

  <label for="message">Message :</label>
  <textarea id="message" name="message"></textarea>

  <button type="submit">Envoyer</button>
</form>
```

### ATTRIBUTS IMPORTANTS DE LA BALISE `<form>`

- `action` : URL où les données du formulaire seront envoyées pour être traitées.
- `method` : Méthode HTTP utilisée pour envoyer les données.
- `GET` : Les données sont ajoutées à l’URL (visible, limité en taille).
- `POST` : Les données sont envoyées dans le corps de la requête (invisible, pas de limite de taille).