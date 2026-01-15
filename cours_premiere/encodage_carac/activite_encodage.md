---
title: Représentation des nombres
---

<link rel="stylesheet" href="../../assets/style.css" />

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Activité préparatoire

## Découverte : “Comment la machine comprend-elle un mot ?”  🖋️

Durant les différents conflits, la communication a toujours été un point crucial dans la victoire. Que ce soit des messages ou des informations importantes, les Hommes ont  toujours été inventifs pour cacher à l'ennemi leurs intentions.

Vous interceptez une suite de nombres censée représenter un message texte.
Votre mission : retrouver le message et expliquer comment la machine a fait pour passer du nombre au caractère.

Voici la suite de numéro : 

```
01000001 01010100 01010100 01000101 01001110 01010100 01001001 01001111 01001110 01001110 01001111 01010101 01010011 01000001 01010100 01010100 01000001 01010001 01010101 01001111 01001110 01010011

```

1. Essayez de décrypter ce message.

2. Quels sont les avantages de ce genre de représentation pour l'ordinateur ? 

3. Écrire une fonction `decode(texte)` qui prend en paramètre une liste d'entier pour la retranscrire en texte sous la forme d'une chaîne de caractère.