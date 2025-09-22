---
title: Représentation des nombres
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Représentation des entiers naturels

## Comprendre le principe des différentes bases

### Compter dans les différentes bases

**A faire (sans ordinateur et sans calculatrice)**  
  
Écrire les 32 premiers nombres dans les différentes bases en complétant le tableau ci-dessous.  
  
| Base 10 |	Base 2 | Base 3 | Base 5 | Base 8 |	Base 16 |
|:-------:|:------:|:------:|:------:|:------:|:-------:|
|         |        |        |        |        |         |
|         |        |        |        |        |         |

Remarques :

- la base 10 est également appelée "le décimal"
- la base 16 est également appelée "l'hexadécimal"

### Valeur en base 10 d'un nombre écrit en base n

**Exemples**

- Le nombre \((4532)_{10}\) a pour valeur en base 10 :  
  \(4 \times 10^{3} + 5 \times 10^{2} + 3 \times 10^{1} + 2 \times 10^{0}\)

- Le nombre \((4301)_{5}\) a pour valeur en base 10 :  
  \(4 \times 5^{3} + 3 \times 5^{2} + 0 \times 5^{1} + 1 \times 5^{0}\)

➜ Il en est de même pour toutes les bases.

### Généralisation

> La valeur en base 10 du nombre qui s’écrit \(a_n \dots a_3 a_2 a_1 a_0\) en base \(x\) répond à l’égalité suivante :  
>
> \(a_n \dots a_3 a_2 a_1 a_0 = a_n \times x^{n} + \dots + a_3 \times x^{3} + a_2 \times x^{2} + a_1 \times x^{1} + a_0 \times x^{0}\)
>
> Cette relation permet de calculer la valeur en base dix d’un nombre écrit dans n’importe quelle base.

**À faire (sans ordinateur et sans calculatrice)**

1. Convertir \((323)_{4}\) en base 10.  

2. Donner la valeur en base 10 de \((110011)_{2}\).  

3. Convertir \((B9)_{16}\) en base 10.

<div style="display: flex; flex-direction:column;  border: 1px solid #ccc; text-align: center; border-radius: 8px;">
  <img src="../../images/conversion_en_base2.png" alt="Python" width="400" />
</div>

## Valeur en base `x` d'un nombre écrit en base 10

# I.3 – Valeur en base \(x\) d’un nombre écrit en base 10

**Exemple**

On souhaite écrire \((89)_{10}\) en base 2.

*(schéma des divisions successives à insérer ici sous forme d’image)*  

Donc \((89)_{10} = (1011001)_{2}\)

---

### Généralisation

> L’écriture en base \(x\) d’un nombre en base dix nécessite de faire des divisions successives par \(x\) et de garder les restes.

---

**À faire (sans ordinateur et sans calculatrice)**  

1. Convertir \((202)_{10}\) en base 2.  

2. Écrire \((101)_{10}\) en base 3.



## Représentation des entiers naturels

Les entiers naturels sont représenté par leur valeur en base 2.

L'écriture en base 2 conduisant à beaucoup de 0 et de 1, il est courant de remplacer l'écriture en base 2 par l'écriture en base 16 (hexadécimal).

## Applications

### Application I

Passer de la base 10 à la base 2 et inversement

**A faire (sans ordinateur et sans calculatrice)**

1) A quel entier en base dix la séquence de bits 0100 correspond-elles ?

2) Quelle est la valeur décimale de l'entier qui s'écrit 1010 en binaire ?

3) Convertir en base 2 le nombre entier qui s'écrit 37 en base 10

4) Donner la séquence de 8 bits qui correspond au nombre 10 en base 10.

### Application II 

Passer de la base 10 à la base 16 et inversement

**A faire (sans ordinateur et sans calculatrice)**

1) Quelle est l'écriture en base dix du nombre qui s'écrit AAA en base 16 ?

2) Convertir le nombre 6D de la base 16 à la base 10.

3) Quelle est l'écriture en base 16 du nombre décimale 315 ?

4) Convertir le nombre 95 de la base 10 à la base 16.

### Application III : Un peu de Python 

1) Dans la documentation officielle de Python, rechercher les fonctions bin(x), oct(x) et hex(x).

- Expliquer leur rôle.
- Comment les nombres en base 2, 8 ou 16 sont-ils représentés dans le Shell ?

2) Utiliser ces trois fonctions pour faire quelques conversions.

3) Utiliser la fonction print() sur un nombre représenté en binaire. Quel est le résultat ?