---
title : Algorithmique
---

<link rel="stylesheet" href="../../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Algorithmes gloutons

## Introduction

Un algorithme glouton résout un problème étape par étape. À chaque étape il fait le meilleur choix dans la situation présente. La solution trouvée n’est pas nécessairement optimale (la meilleure) mais l’algorithme permet de trouver rapidement une solution.

## Présentation du problème
Énoncé
Étant donné un système de monnaie, comment rendre une somme donnée avec le nombre minimal de pièces et de billets ?

Exemple avec le système monétaire européen
Pièces et billets
Pour rendre 6 €, les combinaisons possibles sont :

• 1 billet de 5 € et 1 pièce de 1 € ;

• 3 pièces de 2 € ;

• 6 pièces de 1 € ;

Le rendu avec le nombre minimal de pièce ou billets et le premier.