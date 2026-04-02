---
title: IHM et Web
---

<link rel="stylesheet" href="../../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# PHP

## Introduction


## L'éditeur de texte

Jusqu'à présent, nous avons utilisé un éditeur de texte comme par exemple Visual Studio Code, ou autre.

Dans cette activité découverte du langage php, nous n'allons pas utiliser UwAmp, mais nous allons tester les codes php en ligne sur le site :<a href="https://www.w3schools.com/php/phptryit.asp?filename=tryphp_intro" target="_blank"> w3school </a>

## Variables et affichages en php


👉 Tester : Recopier et exécuter le script ci-dessous.

- Les noms de variables commencent par un « $ »
- echo est l’instruction d’affichage.
- Le point « . » sert pour la concaténation.
- Les lignes se terminent par un « ; »
- <br> sert à passer à la ligne.

```PHP

<?php
$couleur1 = "rouge";
$couleur2 = "noir";
echo "Ma voiture est " . $couleur1 . "." ."<br>";
echo "J'aime le " . $couleur1 ." et le ". $couleur2 . "." . "<br>";
echo "A bientôt" . ".";
?>

```
👉 Tester : Recopier, puis tester le script suivant. ( Rafraichir la page plusieurs fois. )

```HTML

<html>
<head>
    <title>Nombre aléatoire </title>
</head>
<body>
    <?php
    echo rand(1,6);
    ?>
</body>
</html>

```

>
> 1) Modifier : Ecrire le script qui produit un affichage analogue à celui-ci (le nombre obtenu est un entier aléatoire entre 1 et 6) :
>
>
```
Si vous obtenez 6, vous avez gagné.
Vous avez obtenu : 6
```
>

## Les boucles while et foreach

👉 Tester while : Recopier, puis tester le script suivant.
( Rafraichir la page plusieurs fois. )

// ou # sert à écrire des commentaires

```HTML

<html>
<head>
    <title>Ma deuxième loterie </title>
</head>
<body>
    <h1>Les dés</h1>
    <p> On rejoue automatiquement, jusqu'à ce que 6 sorte. :</p>
    <?php               // Attention aux ;
    $de=rand(1, 6);      // $de désigne la variable $de
    while ($de<6)       // Observez la syntaxe du while
    {
        echo $de . "<br>";// ."<br>" permet de passer à la ligne
        $de=rand(1, 6);
    }
    echo $de . "<br>";
    ?>
</body>
</html>
```

>
> 2) Modifier ce programme pour qu’il affiche au bout de combien de lancers de dé, on a obtenu le premier « 6 ».
>
> Exécuter votre script, puis rafraichir la page.

👉 Tester foreach : Recopier, puis tester le script suivant.

```HTML

<!DOCTYPE html>
<html>
<body>

    <?php  
    $colors = array("red", "green", "blue", "yellow");  # Un tableau

    foreach ($colors as $value) {
    echo "$value <br>";
    }
    ?>  

</body>
</html>
```

👉 Tester encore foreach : Recopier, puis tester le script suivant.

```HTML

<!DOCTYPE html>
<html>
<body>

    <?php
    for ($i = 5; $i <= 15; $i++) {
        echo $i . "<br>";
    }
    ?>

</body>
</html>
```

>
> 3) Modifier ce programme pour qu’il affiche la table de multiplication de 7.
>
> Exécuter votre script, puis rafraichir la page.

## Les tableaux associatifs

Les tableaux associatifs consistent en un ensemble de couples clé=>valeur, séparés entre eux par des virgules. On peut faire l’analogie avec les dictionnaires utilisée en Python.

**Exemple**  

Ici, le tableau associatif donne le nombre de calories pour 100 g de différents aliments :

```PHP

$calories = ["Pain au chocolat" => 410,
"Miel" => 304,
"Réglisse" => 377,
"Sorbet" => 90,
"Sucre" => 396,
"Cookies" => 464];
```

Les valeurs sont retrouvées par la clé qui leur est associée. Par exemple, pour trouver le nombre de calories associées à 100 g de sorbet, vous utiliserez cette instruction :


```PHP
echo $calories["Sorbet"];
```

Pour parcourir tous les éléments du tableau, vous pouvez utiliser une boucle foreach crée pour parcourir les tableaux:  

```PHP
foreach($calories as $cle => $valeur){
echo $cle."=". $valeur.", "."<br>";}
```

Pour ajouter un couple clé=>valeur dans le tableau associatif :

```PHP
$calories["Pain blanc" ]= 265 ;
```


>
> 4) Tester les syntaxes ci-dessus, puis créer un programme qui affiche la somme de tous les nombres de calories données dans le tableau.
>

