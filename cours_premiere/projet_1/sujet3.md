---
title: Projet Python
---

# Projet Python


## Analyseur de mots de passe

Le but de ce projet est de créer un assistant qui analyse la robustesse d'un mot de passe.

Votre programme demande d'abord à l'utilisateur de saisir un mot de passe. Si le mot de passe ne suit pas les règles, le programme indique pourquoi à l'utilisateur et l'invite à en saisir un nouveau. Un mot de passe ne suit pas les règles dans les cas suivants :

- il est trop court (4 caractères ou moins) ;
- il est trop long (plus de 20 caractères) ;
- il ne contient pas de majuscule ;
- il ne contient pas de minuscule ;
- il ne contient pas de chiffres.

Si le mot de passe suit les règles, le programme affiche un message indiquant que le mot de passe est valide et demande à l'utilisateur de l'entrer à nouveau. Si les deux mots de passe sont identiques, le programme affiche un message de confirmation. Sinon, le programme recommence depuis le début.

1) Ecrire une fonction `mot_de_passe()` qui test la robustesse d'un mot de passe donné par l'utilisateur. Une fois le mot de passe validé, l'utilisateur devra le retaper pour valider ce dernier.

**Exemple d'exécution :**

```python
>>> mot_de_passe()
Saisissez votre mot de passe : Top NSI
Ce mot de passe n est pas sécurisé : il ne contient pas de chiffres.
Saisissez votre mot de passe : T0p NS1
Ce mot de passe est sécurisé.
Saisissez à nouveau votre mot de passe : Tob NS1
Erreur : les mots de passe ne sont pas identiques. Merci de recommencer.

Saisissez votre mot de passe : t0p ns1
Ce mot de passe n est pas sécurisé : il ne contient pas de majuscule.
Saisissez votre mot de passe : T0p NS1
Ce mot de passe est sécurisé.
Saisissez à nouveau votre mot de passe : T0p NS1
Le mot de passe est correct !
```