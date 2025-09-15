---
title: Projet Python
---

# Projet Python


## Nombre mystère 

Le but de ce projet est de créer le jeu du nombre mystère, dans lequel un joueur A choisit un nombre aléatoire entre 1 et 100 et un joueur B doit le retrouver. À chaque essai du joueur B, le joueur A indique si le nombre mystère est plus grand ou plus petit que le nombre proposé.

Vous devrez programmer deux modes de jeu : le mode où l'ordinateur choisit le nombre et l'utilisateur le cherche, et le mode où l'utilisateur choisit le nombre et l'ordinateur le cherche.

Votre programme demande d'abord à l'utilisateur dans quel mode il veut jouer. Selon le mode choisi, le programme se comporte différemment.

Si le mode choisi est celui où l'ordinateur choisit le nombre, le programme demande à l'utilisateur de choisir un nombre entre 1 et 100, puis lui indique si le nombre mystère est plus grand ou plus petit et recommence tant que l'utilisateur n'a pas trouvé le nombre. Quand l'utilisateur a trouvé, le programme indique en combien de tours il a trouvé le nombre.

Si le mode choisi est celui où le joueur choisit le nombre, le programme demande à l'utilisateur d'appuyer sur Entrée quand il a choisi son nombre. Ensuite, l'ordinateur fait une proposition. L'utilisateur doit indiquer si le nombre mystère est plus grand, plus petit ou égal à la proposition. L'ordinateur fait d'autres propositions jusqu'à ce que le nombre mystère soit trouvé. Quand l'ordinateur a trouvé, le programme indique en combien de tours il a trouvé le nombre. Essayez de trouver une méthode efficace pour votre intelligence artificielle !

1) Écrire une fonction `nombre_mystere()` qui lance dans le terminal le jeu du nombre mystère selon les règles décrites ci-dessus.

**Exemples d'exécution :**

Cas où l'ordinateur choisit le nombre mystère :

```shell
Dans quel mode voulez-vous jouer ?
1) L'ordinateur choisit le nombre
2) L'utilisateur choisit le nombre
Choix : 1
Entrez un nombre : 43
C'est plus grand !
Entrez un nombre : 72
C'est plus petit !
Entrez un nombre : 67
Bravo ! Vous avez trouvé en 3 coups !
```

Cas où l'utilisateur choisit le nombre mystère :

```shell
Dans quel mode voulez-vous jouer ?
1) L'ordinateur choisit le nombre
2) L'utilisateur choisit le nombre
Choix : 2
Appuyez sur Entrée quand vous avez choisi un nombre...
Je tente ma chance... 50 !
Votre réponse :
1) C'est ça !
2) Plus petit
3) Plus grand
Choix : 2
Je tente ma chance... 25 !
Votre réponse :
1) C'est ça !
2) Plus petit
3) Plus grand
Choix : 3
Je tente ma chance... 37 !
Votre réponse :
1) C'est ça !
2) Plus petit
3) Plus grand
Choix : 1
L'ordinateur a trouvé en 3 coups !
```