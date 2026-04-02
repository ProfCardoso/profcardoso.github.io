---
title: IHM et Web
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Formulaires

## Introduction

Les formulaires permettent à l’utilisateur de saisir simplement des données et de les envoyer à une page.

Voici une petite vidéo introductive à regarder chez vous pour les plus rapide : <a href="https://www.youtube.com/watch?v=XZ_sarpdgOE&t=3s" target="_blank">1ère NSI - Le Web Dynamique #1 - Mise au point de formulaire HTML - Web statique VS Web dynamique</a>

## Premier formulaire

Pour utiliser un formulaire, il faut deux fichiers. Un fichier qui contient le formulaire et un autre qui va traiter les données envoyées. Ce deuxième fichier ne peut donc pas être statique, nous utiliserons donc PHP encore une fois.

👉  Créez ou remplacez le fichier `page_web.html` dans votre dossier avec votre nom et placez-y le code suivant :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Un formulaire</title>
        <meta charset="utf-8">
    </head>

    <body>
        <h1>Un formulaire</h1>
        <form method="get" action="traitement.php">
            <label for="nom">Nom</label>
            <input type="text" name="nom" value="" id="nom">
            <label for="prenom">Prénom</label>
            <input type="text" name="prenom" value="" id="prenom">
            <input type="submit" value="Envoyer">
        </form>
    </body>
</html>
```

👉 Dans le même dossier, créez un fichier `traitement.php` et placez-y le code suivant :

```html
<h1>Traitement du formulaire</h1>
<p>Bonjour <?php echo $_GET['prenom']; ?> <?php echo $_GET['nom']; ?>, votre formulaire a bien été traité.</p>
```

👉 Allez maintenant sur "Navigateur www", ouvrez `page_web.html` et complétez le formulaire. Cliquez sur « Envoyer », si tout a bien fonctionné vous devriez voir vos nom et prénom sur la page.

## Comment cela fonctionne ?

L’élément html `<form>` permet d’envoyer des formulaires. Pour cela, il faut lui spécifier une méthode (ici GET) et un fichier cible (ici `traitement.php`). Lors d’un clic sur le **bouton submit**, l’ensemble des champs à l’intérieur du formulaire sont envoyés au fichier cible par la méthode choisie.

Il existe plusieurs types de champs, mais nous n’avons utilisé que des **champs de type text**. On associe à **ses champs un nom (name)** qui correspond à la variable qui contiendra le contenu du champ. Enfin on associe un **label à un champ input** en utilisant l’attribut **for** pour pointer vers l’**id du champ**.

Lorsque vous cliquez sur le bouton « envoyer » vous êtes envoyé sur la page `traitement.php` avec les **variables ajoutées au bout de l’URL**. C’est **la méthode GET**.

>
> 1) Modifiez le nom et le prénom dans l’URL. Que constatez-vous ?
>

## Formulaire plus discret

La méthode GET est efficace mais il n’est pas forcément désirable d’avoir toutes les variables dans l’URL. Surtout si on envoie des textes dans un formulaire. Pour cela il existe une deuxième méthode, la **méthode POST**.

Nous allons cette fois utiliser ce fichier `index.html` :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Un formulaire</title>
        <meta charset="utf-8">
    </head>

    <body>
        <h1>Un formulaire</h1>
        <form method="post" action="traitement.php">
            <label for="nom">Nom</label>
            <input type="text" name="nom" value="" id="nom">
            <label for="prenom">Prénom</label>
            <input type="text" name="prenom" value="" id="prenom">
            <input type="submit" value="Envoyer">
        </form>
    </body>
</html>
```

On a juste changé la méthode en post.

Et comme ficher `traitement.php` :

```html
<h1>Traitement du formulaire</h1>
<p>Bonjour <?php echo $_POST['prenom']; ?> <?php echo $_POST['nom']; ?>, votre formulaire a bien été traité.</p>
```

Ici, on a juste changé le nom de la variable `$_GET` en `$_POST`.

👉 Allez à nouveau sur "Navigateur www", ouvrez `index.html` et complétez le formulaire, avant de cliquez sur « Envoyer ». 


>
> 2) Que remarquez-vous dans la barre d’adresse ?
>

Attention la méthode POST ne fait que cacher les variables à l’utilisateur lambda, mais elles restent visibles très facilement.

👉 Ouvrez le moniteur réseau (`F12`) et rechargez la page de traitement du formulaire. Cliquez sur la requête POST et allez dans l’onglet « Requête ». 


>
> 3) Que voyez-vous ?
>


## Bilan

Deux méthodes permettent d’envoyer des formulaires : **GET et POST**. On utilise en général la méthode POST car elle cache les variables et permet d’avoir des URLs plus « propres ». Mais la méthode POST n’est pas « sécurisé » pour autant, il ne faut pas faire confiance aux données qui arrivent d’un formulaire, quelque soit la méthode.


## Pour les plus rapides 

>
> 8) Après avoir cherché le champ qui permet de saisir du texte et le champ qui n’est pas affiché, modifiez le formulaire pour pouvoir saisir votre expression favorite et passer le code « turing » à la page `traitement.php` sans que l’utilisateur le voit. La page traitement.php devra alors afficher vos nom, prénom, l'expression et le code « turing ».
>
