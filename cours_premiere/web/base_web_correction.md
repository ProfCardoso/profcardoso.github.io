---
title: IHM et Web
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Base du Web

## Introduction

Dans ce TP nous allons revoir tout ce vous avez dû voir en seconde.

## Qu’est-ce qu’un ordinateur ?


<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>Un ordinateur est une machine électronique programmable.</strong><br>
<ul>
<li>Hardware : c’est la partie matérielle (machine) de l’ordinateur (carte mère, processeur, mémoire…).</li>
<li>Software : c’est la partie logicielle (programmable) de l’ordinateur (LibreOffice, Firefox…).</li>
<li>Système d’exploitation : est un logiciel qui fait le lien entre le software et l’hardware (Windows, MacOS, Linux…).</li>
</ul>
</div>
<br>

1) Pour chacun des éléments suivants indiquer s’il s’agit d’hardware, de software ou d’un système d’exploitation :

- disque dur ;
- Twitter ;
- souris ;
- Microsoft Windows 10 ;
- Chrome ;
- Ubuntu.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <ul>
      <li>disque dur : hardware</li>
      <li>Twitter : software</li>
      <li>souris : hardware</li>
      <li>Microsoft Windows 10 : système d'exploitation</li>
      <li>Chrome : software</li>
      <li>Ubuntu : système d'exploitation</li>
    </ul>
  </div>
</details>

## Navigateurs

Un **navigateur** est un logiciel qui permet d’aller sur le web en affichant le contenu de la page web dont l’adresse est dans la barre d’adresse. Il existe de nombreux navigateurs même s’il y en a trois qui dominent le marché.

3) Donner le nom des navigateurs appartenant aux sociétés suivantes :

- Google ;
- Mozilla ;
- Apple ;
- Microsoft.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <ul>
      <li>Google : Chrome</li>
      <li>Mozilla : Firefox</li>
      <li>Apple : Safari</li>
      <li>Microsoft : Edge</li>
    </ul>
  </div>
</details>


4) Trouver au moins deux autres navigateurs.


<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Opera et Vivaldi</p>
  </div>
</details>


## URL

URL signifie **Uniform Ressource Locator**. On assimile souvent URL avec adresse web alors qu’il peut exister des URL pour des ressources qui ne sont pas sur le web (FTP, mail…).  
  
Une adresse web a une URL qui commence par ` http:// ` pour **HyperText Transfer Protocol** ou par ` https:// ` pour le même protocole sécurisé. C’est la base du **world wide web** inventé par **Tim Berners-Lee en 1989**.  
  
Prenons pour exemple une URL pour en comprendre toutes les parties :  

https://www.debian.org/intro/about

6) Sur l’URL ci-dessus indiquer la partie qui concerne :

- le protocole ;
- le nom de domaine ;
- le sous-domaine ;
- le chemin vers la ressource.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <ul>
      <li>le protocole : https</li>
      <li>le nom de domaine : debian.org</li>
      <li>le sous-domaine : www</li>
      <li>le chemin vers la ressource : /intro/about</li>
    </ul>
  </div>
</details>


7) Sur l’URL ci-dessous, déterminer le protocole, le domaine et le chemin vers la ressource.

https://www.gnu.org/philosophy/philosophy.fr.html

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <ul>
      <li>le protocole : https</li>
      <li>le nom de domaine : gnu.org</li>
      <li>le sous-domaine : www</li>
      <li>le chemin vers la ressource : /philosophy/philosophy.fr.html</li>
    </ul>
  </div>
</details>

8) Donner l’URL de la page Wikipedia sur le world wide web.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>https://fr.wikipedia.org/wiki/World_Wide_Web</p>
  </div>
</details>

Le chemin vers la ressource suit l’arborescence du serveur. « / » est la racine du serveur et « /intro/ » correspond au dossier « intro » sur le serveur.

9) Donner l’URL du dossier « devel » sur le serveur www.debian.org.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>https://www.debian.org/devel/</p>
  </div>
</details>

## Modèle client / serveur

Pour obtenir le contenu d’une URL, un navigateur (le client) envoie une requête à un serveur et il attend sa réponse. Le serveur répond en envoyant certaines informations (ce qu'on appelle les « en-têtes ») et le contenu de l’URL demandée.

Pour voir les requêtes dans Firefox, il faut d'abord appuyer sur `F12` et cliquer sur l'onglet **Network**. Il sera nécessaire de rafraîchir la page et de choisir la requête que l'on veut observer. On s'intéressera particulièrement aux entêtes (headers) des requêtes. Les requêtes sont affichées sur la droite.

10) En restant sur cette page, observer la requête envoyée et la réponse puis compléter les informations ci-dessous :

- méthode de la requête ;
- code d’état renvoyé par le serveur ;
- version HTTP ;
- type de contenu (content-type) de la réponse ;
- logiciel du serveur (Server) ;
- taille de la réponse (Content-Length) ;
- navigateur du client (dans le User-Agent) ;
- système d’exploitation du client (dans le User-Agent).

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <ul>
      <li>méthode de la requête : GET</li>
      <li>code d’état renvoyé par le serveur : 200 OK</li>
      <li>version HTTP : HTTP/2</li>
      <li>type de contenu (content-type) de la réponse : text/html</li>
      <li>logiciel du serveur (Server) : Apache</li>
      <li>taille de la réponse (Content-Length) : 8624</li>
      <li>navigateur du client (dans le User-Agent) : Mozilla/5.0 Gecko/20100101 Firefox/88.0</li>
      <li>système d’exploitation du client (dans le User-Agent) : Ubuntu</li>
    </ul>
  </div>
</details>









