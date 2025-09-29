---
title: Représentation des nombres
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Représentation des entiers relatifs

## Méthode naïve: utilisation d’un bit de signe

La façon la plus simple de procéder serait de réserver le bit de poids fort pour le signe(0 pour positif et 1 pour négatif), et de garder le rester pour la représentation de la valeur absolue du nombre.

Avec un codage utilisant des mots de n bits, on pourrait représenter des nombres entre 
$$-2^{n-1} + 1 \text{ et } 2^{n-1} - 1$$.

Par exemple, avec un codage sur 3 bits, des nombres entre -3 et 3:

| Représentation binaire | Valeur décimale |
|------------------------|-----------------|
| 000                    | +0              |
| 001                    | +1              |
| 010                    | +2              |
| 011                    | +3              |
| 100                    | -0              |
| 101                    | -1              |
| 110                    | -2              |
| 111                    | -3              |

<details>
  <summary style="cursor: pointer; font-weight: bold;">Mais alors ? Pourquoi pas cette méthode ? 🤔</summary>
  <div style="margin-top: 10px;">
    <p>
    Malheureusement cette représentation possède deux inconvénients. Le premier (mineur) est que le nombre zéro (0) possède deux représentations. L’autre inconvénient (majeur) est que cette représentation impose de modifier l’algorithme d’addition ; si un des nombres est négatif, l’addition binaire usuelle donne un résultat incorrect.
    </p>
  </div>
</details>

## Seconde méthode: Complément à 2

