---
title: Représentation des nombres
---

<link rel="stylesheet" href="../../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Outils : Décimal, binaire...

## Compter dans les différentes bases

| Base 10 Décimal |	Base Binaire  |	Base 3	|Base 5|	Base 8|	Base 16 Hexadécimal |
|:--:|:--:|:--:|:--:|:--:|:--:|
|1	|1	|1	|1	|1	|1|
|2	|10	|2	|2	|2	|2|
|3	|11|	10|	3|	3|	3|
|4	|100|	11|	4|	4|	4|
|5	|101|	12|	10|	5|	5|
|6	|110|	20|	11|	6|	6|
|7	|111|	21|	12|	7|	7|
|8	|1000|	22|	13|	10|	8|
|9	|1001|	100|	14|	11|	9|
|10	|1010|	101|	20|	12|	A|
|11	|1011|	102|	21|	13|	B|
|12	|1100|	110|	22|	14|	C|
|13	|1101|	111|	23|	15|	D|
|14	|1110|	112|	24|	16|	E|
|15	|1111|	120|	30|	17|	F|
|16	|10000|	121|	31|	20|	10|
|17	|10001|	122|	32|	21|	11|
|...|  |  |  |  |  		|
|25	|11001	|221	|100	|31	|19|
|26	|11010	|222	|101	|32	|1A|
|...|	|	|	|	|   |
|31	|11111|	1011|	111|	37	|1F|
|32	|100000	|1012	|112	|40	|20|

Vous pouvez le retrouver ici en [pdf](./outil_repr_entier.pdf)

## Valeur en base 10 d'un nombre écrit en base $$k$$

**Principe général**

> Nombre en base $$k$$ : $$(a_n…a_3\ a_2\ a_1\ a_0)_k$$
> 
> Calcul de la valeur en base 10 : $$a_n×k^n+…+a_3×k^3+a_2×k^2+a_1×k^1+a_0×k^0$$

**Exemples**  

> $$\begin{aligned}[t] (4301)_5 &= (4×5^3+3×5^2+0×5^1+1×5^0)_{10} &= (576)_{10} \end{aligned}$$
>
> $$\begin{aligned}[t] (493)_{10} &= (4×10^2+9×10^1+3×10^0)_{10} &= (493)_{10} \end{aligned}$$

## Écriture en base $$k$$ d'un nombre dont on connaît la valeur en base 10

### Méthode des divisions successives

On pose les divisions successives du nombre par $$k$$ jusqu'à obtenir un quotient égal à 0.

L'écriture en base $$k$$ s'obtient avec les restes, en commençant par le dernier.

**Exemple**

> Cherchons l'écriture de $$(89)_{10}$$ en base 2.
>
>
> $$(89)_{10} = (1011001)_{2}$$