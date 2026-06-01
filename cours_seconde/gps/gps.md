---
title : GPS
---

<link rel="stylesheet" href="../../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Localisation, cartographie et mobilité

## Comment fonctionne un GPS ?

Regarder la vidéo <a href="https://www.youtube.com/watch?v=WoqpQbWdacQ" target="_blank"> « Kezako : Comment fonctionne un GPS ? »</a>

Les satellites de la constellation GPS : <a href="https://geoxc-apps.bd.esri.com/space/satellite-explorer/" target="_blank">Satellite Map</a>

## Protocole NMEA 0183

Une **trame NMEA** est une suite de caractères (max.  82 caractères) générée par un récepteur GPS pour transmettre des données de géolocalisation via **un protocole normalisé, la NMEA 0183,** définie par la **National Marine Electronics Association**.   

Cette phrase texte, structurée en **champs séparés par des virgules**, contient des informations essentielles telles que :

- L'heure UTC du relevé.
- La latitude et la longitude (généralement en degrés et minutes décimales). 
- Le Fix Quality : 1 = GPS.
- Le nombre de satellites utilisés pour le calcul. 
- HDOP : Horizontal Dilution of Precision, qualité géométrique des satellites, plus c’est faible, meilleure est la précision.
- Altitude au dessus du niveau moyen de la mer.
- Unité altitude : M, Mètres. 

La trame **débute toujours par le signe $**, suivi de l'**identifiant du récepteur** (ex: GP pour GPS) et **du type de message**, se terminant par un **caractère de contrôle**. 

Exemple de trame :

```
$GPGGA,123000.000,4349.8946,N,00423.0898,E,1,08,1.0,50.0,M
```