---
title: Initialisation à Python
---

# Opérateurs


<link rel="stylesheet" href="../assets/style.css" />


## Comprendre les opérateurs

### Les opérateurs (à connaître)

Les principaux opérateurs en Python sont : `+` `-` `*` `**` `/` `//` `%` `<` `>` `<=` `>=` `==` `!=` .

### A faire

__Sur l'ordinateur__ : Tester ces différents opérateurs sur des objets de différents types.

**Exemple :**

```python
resultat = 8 + 6
type_de_resultat = type(resultat)
```

__Compte rendu sur feuille__ : Pour chaque test (faire une vingtaine de tests), ajouter une ligne du tableau ci-dessous.

| Opérateur | Type du premier objet	| Type du deuxième objet	| Type du résultat	| Rôle	| Exemple |
|*---*|*---*|*---*|*---*|*---*|*---*|
|`+` |	int |	int	 | int	| Addition |	8 + 6 renvoie 14 |
|`+` |	str	|str	|str	|Concaténation	|"a" + "b" renvoie "ab"|
|`+` |	str	|int	|Erreur !|	---	|"A" + 310 renvoie une erreur|
|  |        |       |        |      |                            |
 	 	 	 	 	 
 	 	 	 	 	 
###  Bilan (à connaître)
Les opérateurs agissent de façon différente en fonction des types des objets avec lesquels ils sont utilisés.

## Ordre de priorité des opérateurs
### A faire
On considère les opérations suivantes :
```python
(3 + 8) * 2
3 + (8 * 2)
3 + 8 * 2
2 * 8 + 3
```
__Sur feuille__ : Proposer un résultat pour chacune d'elles.

__Sur l'ordinateur__ : Tester ces opérations, vérifier vos propositions.

__Sur feuille__ : Indiquer, du `+` ou du `*`, quel est l'opérateur prioritaire en Python.

### A faire
Sur le modèle de l'exemple 1, tester les priorités entre les opérateurs suivants :

- Priorité entre `*` et `**`
- Priorité entre `+` et `//`
