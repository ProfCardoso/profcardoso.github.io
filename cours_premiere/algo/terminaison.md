---
title: Algorithme
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


# Preuve d'un algorithme

## Préambule

Lorsqu'on écrit un algorithme, trois questions fondamentales se posent :

• **Est-ce qu'il se termine ?** => C'est ce que l'on appelle <span style="color: rgb(165,42,42);">la terminaison</span>. 
• **Est-ce qu'il donne le résultats attendu ?** => C'est ce que l'on appelle <span style="color: rgb(165,42,42);">la correction</span>.
• **Est-ce qu'il donne le résultat en utilisant des ressources (temps, mémoire...) raisonnables ?** => C'est ce que l'on appel <span style="color: rgb(165,42,42);">la complexité</span>.

**Remarque :** Démontrer la terminaison et la correction d'un algorithme s'appelle faire la **preuve de cet algorithme.**

## Définitions

<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>Terminaison d'un algorithme</strong><br>
Vérifier la terminaison d'un algorithme est en particulier nécessaire lorsque celui-ci comporte des boucles.
<br>
Dans ce cas, cela peut se faire en déterminant un variant de boucle qui converge (ou parle également de variant convergent).
<br>
Un variant convergent de boucle est une quantité qui prend ses valeurs dans un ensemble bien déterminé et qui évolue dans le même sens strictement à chaque itération de la boucle.
</div>


<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>Correction d'un algorithme</strong><br>
Vérifier la correction d'un algorithme est en particulier nécessaire lorsque celui-ci comporte des boucles.
<br>
Dans ce cas, cela peut se faire en utilisant un invariant de boucle.
<br>
On appelle invariant de boucle une propriété qui, si elle est vraie avant l’entrée dans une boucle, reste vraie après chaque passage dans la boucle, et donc est vraie aussi à la sortie de la boucle.
</div>




