---
title: Projet Python
---

# Projet Python


## Fonction et conditionnelles

1) Écrire une fonction `bac(moyenne)` qui prend en argument une moyenne de type float entre 0 et 20, vérifie si la moyenne est entre 0 et 20 et renvoie :

• True si moyenne >= 10
• False si moyenne < 10

2) Écrire une fonction `mention(moyenne)` qui prend en argument une moyenne de type float entre 0 et 20 et qui renvoie une chaîne de caractère :

• "recalé" si 0 ⩽ note < 8
• "second groupe" si 8 ⩽ note < 10
• "reçu" si 10 ⩽ note < 12
• "assez bien" si 12 ⩽ note < 14
• "bien" si 14 ⩽ note < 16
• "très bien" si 16 ⩽ note ⩽ 20
• "valeur incohérente" sinon

3) Écrire une fonction `eleves(nombre)` qui prend un entier en argument correspondant au nombre d'élèves, qui demande à l'utilisateur un nom ainsi qu'une note pour chaque élève, et qui calcule si l'élève a le bac ainsi que sa mention avant de l'écrire dans le terminal.

**Exemple d'exécution :**

```python
>>> bac(15)
True

>>> mention(15)
"bien"

>>> eleves(1)
Nom de l'élève : Paul
Note de l'élève : 12
Paul a eu le bac mention "reçu"
```


