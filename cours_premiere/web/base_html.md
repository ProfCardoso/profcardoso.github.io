---
title: IHM et Web
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# HTML et CSS

## Avant de commencer !

### Application 

Pour la suite du cours sur HTML et CSS, nous allons devoir utiliser une application pour écrire et voir le résultat en direct des pages webs.

Cette application, c'est Visual Studio, avec quelques extensions à ajouter :

- **HTML Preview**
- **HTML CSS Support**
- et d'autre encore si vous souhaitez des améliorations ou d'autre chose encore sur votre application.

### Dossier de travail

Vous pouvez, dans votre dossier NSI, créer un dossier `page_web`, où se situera votre site web. 

### Si problème quelconque

Nous allons construire des page simples pour comprendre le HTML. Pour cela, vous pouvez utilisez le site <a href="https://jsfiddle.net/" target="_blank">suivant</a> pour réaliser et tester la création de page web.

## HTML

Le **HTML (HyperText Langage Markup)** est un langage de description qui permet de construire une page web.

### Bases

1) Saisissez ou copiez le code suivant dans la fenêtre HTML puis appuyez sur run pour voir le résultat :

```html
<h1>Mon titre</h1>

<p>
    Ceci est un paragraphe. Et un élément <strong>important</strong>.
</p>
```

Vous venez de créer une page web ! Essayons de voir comment cela fonctionne :

- `<h1>`, `<p>` et `<strong>` sont des **balises ouvrantes** et `</h1>`, `</p>` et `</strong>` sont des **balises fermantes**. Ce qu’il y a entre une balise ouvrante et une fermante est **son contenu** ;

- la balise `<h1>` est le titre le plus important. Il existe des balises `<h1>` jusqu’à `<h6>` pour les titres moins importants ;
- la balise `<p>` représente un paragraphe ;
- la balise `<strong>` sert à mettre en valeur un texte important.

2) Reprenez la page précédente et ajoutez deux titres `<h2>` ainsi qu’un paragraphe.


### Liens

Pour faire un lien hypertexte il faut utiliser la balise `<a>`. Son contenu est le texte cliquable et on lui ajoute un attribut href pour indiquer la cible du lien.

3) Ajoutez le lien suivant à votre page :

```html
<a href="https://www.google.fr">Lien vers Google</a>
```

4) Ajoutez un autre lien et faite qu’il pointe vers Bing.

### Listes

Les listes se font grâce aux balises `<ul>` ou `<ol>`. Les éléments d’une liste sont défini par la balise `<li>`.  
  
Saisissez le code suivant dans votre page :

```html
<ul>
    <li>un élément</li>
    <li>un deuxième élément</li>
    <li>un autre élément</li>
</ul>

<ol>
    <li>un élément</li>
    <li>un deuxième élément</li>
    <li>un autre élément</li>
</ol>
```
5) Quelle est la différence entre <ul> et <ol> ?

### Images

Pour ajouter une image, on utilisera la balise `<img>` **sans balise fermante**. Un attribut **src** permettra d’indiquer l’url de l’image, qu’elle soit locale ou sur internet.

6) Après avoir cherché une image sur internet et copié son url, ajouter le code ci-dessous à votre page :

```html
<img src="url_de_l_image">
```

### Balises neutres

Il existe deux balises qui n’ont aucune signification. Cela permet d’organiser la page, de regrouper des éléments dans une même entité.

La première est la balise `<div>`. Elle permet de créer un bloc qui va prendre toute la largeur de l’écran. Elle peut contenir n’importe quels éléments. Elle est très utilisée.

La deuxième est la balise `<span>` qui permet de regrouper un groupe de mot ou tout élément « en ligne » comme un lien par exemple.

7) Ajoutez les balises `<span>` et `</span>` autour du mot « **deuxième** » dans vos deux listes. Que se passe-t-il ?

## CSS

Le **CSS (Cascading Style Sheet)** permet d’apporter un peu de style à une page HTML. C’est à dire changer la mise en page ou les couleurs par exemple.

### Bases

Pour appliquer un style à un élément il faut écrire des instructions dans la fenêtre CSS à droite.

8) Ajoutez le code suivant dans la fenêtre CSS et décrire ce qu’il se passe :

```css
h1 {
    text-align: center;
    color: red;
}

strong {
    background-color: green;
}
```

### Classes

Il est aussi possible de cibler des éléments HTML en CSS en leur ajoutant un attribut class.

9) Remplacez une balise `<p>` par `<p class="texte">` dans votre page puis ajoutez le code suivant dans la fenêtre CSS, que se passe-t-il ?  

```css
.texte {
    color: yellow;
}
```

### Identifiant unique

Si on veut cibler un seul élément, on peut utiliser l’attribut id.

10) Remplacez l'autre balise `<p>` par `<p id="toto">` dans votre page puis ajoutez le code suivant dans la fenêtre CSS :

```css
#toto {
    color: pink;
}
```

11) Pour terminer créez une page web qui décrit vos trois sites web préférés. Elle doit avoir : un titre, des sous-titres, des liens vers les sites, des paragraphes et des couleurs différentes pour chaque paragraphe. Vous ajouterez également une liste avec des liens vers vos pages préférées d’un de ces sites.
