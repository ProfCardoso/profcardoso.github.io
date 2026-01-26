---
title: Internet
---

# MODÈLE CLIENT-SERVEUR

## Définition

Sur un réseau, les machines échangent des données à l’aide de requêtes formulées par les programmes.

- Les clients sont les machines (ou programmes) qui émettent les requêtes.

- Les serveurs sont les machines (ou programmes) qui répondent aux requêtes.


## Schéma du modèle client-serveur

<div style="display: flex; flex-direction:column;  text-align: center; ">
  <img style="margin: auto;" src="../../images/transmission_mail.png" alt="Python" width="1000" />
</div>

Explication :

- 1 : Le client de l'émetteur communique avec le serveur de messagerie de l'émetteur et lui envoie le mail.

- 2 : Le serveur de messagerie de l'émetteur envoie le mail au serveur de messagerie du récepteur.

- 3a : Le client du envoie une requête à son serveur de messagerie pour savoir si un courriel est arrivé.

- 3b : Le serveur de messagerie du client répond en envoyant le courriel.

## Exemple de la consultation d'un site web

<div style="display: flex; flex-direction:column;  text-align: center; ">
  <img style="margin: auto;" src="../../images/clien_serveur_site_web.png" alt="Python" width="800" />
</div>

Le serveur DNS dispose d'un fichier qui lui permet de faire la correspondance entre le nom de domaine et l'adresse IP du serveur qui héberge le site.

Quand l'utilisateur, depuis son navigateur, demande l'affichage d'une page web à partir d'une adresse :

- 1a : le client envoie une requête au serveur DNS afin de connaitre l'adresse IP du serveur web.

- 1b : le serveur DNS répond à la requête avec l'adresse IP du serveur web.

- 2a : le client envoie une requête au serveur web.

- 2b : le serveur web répond à la requête en envoyant la page demandée.

> ## ✏️ Exercices – Client-Serveur
>
> ### Exercice 1
>
>Identifie le client et le serveur :
>
>1. Un élève consulte Pronote
>
>2. Un smartphone envoie un message sur Snapchat
>
> ### Exercice 2
>Complète :
>
```
Le client envoie une _______ et le serveur envoie une _______.
```
>
> ### Exercice 3
>
> Donne un exemple de service utilisant le modèle client-serveur.