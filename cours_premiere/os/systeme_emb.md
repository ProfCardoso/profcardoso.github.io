---
title: Système embarqué et objet connecté

---

# Système embarqué et objet connecté

## Impacts sur les pratiques humaines

L’impact de l’informatisation des objets devient considérable, surtout depuis que leurs interfaces s’unifient. Le but est de fabriquer des machines d’utilisation facile permettant des fonctionnalités améliorées, voire complètement nouvelles comme la voiture autonome. Celle-ci utilise à la fois des techniques de systèmes embarqués pour son fonctionnement et sa navigation et de l’intelligence artificielle pour l’analyse en temps-réel de l’environnement à l’aide de capteurs variés (caméras, radars, lidars, etc.).  

Comme l’informatique embarquée interagit avec le monde physique en exposant quelquefois des vies humaines ou des équipements critiques (réseaux électriques par exemple), elle est soumise à de fortes contraintes de sûreté (absence d’erreurs) et de sécurité (résistance aux attaques). En avionique, ferroviaire ou autres applications critiques, des processus lourds de certification externe sont utilisés. Cependant, dans beaucoup de systèmes embarqués moins critiques, la sécurité reste souvent un point faible, et les objets connectés sont de plus en plus utilisés comme robots pour lancer des attaques sur internet.

## Définitions

<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>Définition — Systèmes informatiques embarqués</strong><br>
Un système informatique embarqué est un système autonome intégré dans un objet pour contrôler son comportement, sans écran ou clavier classiques.  Il comprend un microprocesseur, de la mémoire, des capteurs (ex : accéléromètre, température) et des actionneurs (ex : moteur, LED).  
</div>
<br>

**Exemples :** Ces systèmes sont utilisés dans les voitures (aides à la conduite), les appareils ménagers (machine à laver), les robots (Thymio) ou les objets connectés. 

<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>Définition — Objets connectés</strong><br>
Un objet connecté est un système embarqué relié à un réseau (WiFi, Bluetooth, 5G).  Il peut échanger des données avec d'autres objets ou un serveur distant, souvent via une application mobile ou une page web.  
</div>
<br>

**Exemples :** Comme la montre connectée, l'enceinte intelligente, le thermostat intelligent...

## Activité Découverte 

Pour cette première activité, nous allons utiliser 2 choses :

- le site web : <a href="https://python.microbit.org/v/3" target="_blank">python.microbit.org</a>
- une carte microbit qui vous sera distribué ( vous pouvez tout de même faire ce tp sans )

<span style="color: rgb(165,42,42);">Attention, vous n'utiliserez pas le navigateur Firefox pour la totalité des activité !</span>

### Première utilisation

Avant de vous lancer dans le code, quelques étapes sont nécessaires :

- brancher le câble à la  carte microbit;
- brancher la carte microbit à une prise USB de votre ordinateur;
- sur la page web de python.microbit, cliquer sur les 3 petits points verticaux à droite de *Send to micro:bit* pour connecter votre carte microbit;
- sans modifier le programme à l'écran, cliquer sur *Send to micro:bit*.

-> **Si le travail est fait correctement, vous devrez voir apparaître sur votre carte microbit l'image d'un coeur et le message "Hello" successivement.**

### Jouer avec l'affichage

Pour chacun des prochains exercices, écrire le code une fois validé par votre professeur sur votre feuille.

<div style="border:2px solid rgb(193, 142, 25); padding:10px; border-radius:8px">
<strong>Afficher du texte</strong><br>
L'affichage du texte se fait à l'aide de la fonction <code>display.show()</code> du module microbit.
</div>
<br>

> **Travail à faire :** Afficher votre prénom sur la carte

<div style="border:2px solid rgb(193, 142, 25); padding:10px; border-radius:8px">
<strong>Afficher un nombre</strong><br>
L'affichage d'un nombre se fait également à l'aide de la fonction <code>display.show()</code> du module microbit.
</div>
<br>

> **Travail à faire :** Afficher votre âge sur la carte.

<div style="border:2px solid rgb(193, 142, 25); padding:10px; border-radius:8px">
<strong>Afficher une image prédéfinie</strong><br>
Le module microbit propose une vingtaine d'images prédéfinies ( ex : Image.HEART, Image.ARROW_E, Image.CLOCK6, Image.YES, ... ).
<br>
L'affichage d'une image prédéfinie se fait à l'aide de la fonction <code>display.show()</code> du module microbit.
</div>
<br>

**Exemple :** Voici quelques noms d'images (à écrire en majuscules) : ANGRY, HOUSE, SAD, ASLEEP...

> **Travail à faire :** Afficher une image prédéfinie sur la carte.

### Choisir les leds que l'on allume


<div style="border:2px solid rgb(193, 142, 25); padding:10px; border-radius:8px">
<strong>Éteindre toutes les leds</strong><br>
<code>display.clear()</code>
</div>
<br>

<div style="border:2px solid rgb(193, 142, 25); padding:10px; border-radius:8px">
<strong>Allumer une led</strong><br>
Le controle de l'allumage de l'une des leds se fait à l'aide de la fonction <code>display.set_pixel(x, y, val)</code> où x est la colonne (de 0 à 4), y la ligne (de 0 à 4) et val l'intensité (de 0 à 9).
</div>
<br>

> **Travail à faire :** Afficher une image de votre création sur la carte.

### Jouer avec le temps


<div style="border:2px solid rgb(193, 142, 25); padding:10px; border-radius:8px">
<strong>Faire faire une pause au programme</strong><br>
Pour faire faire une pause au programme, il faut utiliser la fonction sleep en indiquant la durée de la pause souhaitée en millisecondes.
<code>sleep(nombre_millisecondes)</code>
</div>
<br>

> **Travail à faire :** Afficher **votre nom**, puis faite une **pause d'une seconde**, afficher **votre prénom**, une nouvelle **pause d'une seconde**, et enfin afficher une **image de votre choix**.


### Jouer avec les boutons

La carte microbit dispose de deux boutons notés A et B. Voici comment les programmer.

<div style="border:2px solid rgb(193, 142, 25); padding:10px; border-radius:8px">
<strong>Tester si l'un des boutons est appuyé</strong><br>
Pour tester si l'un des boutons est appuyé, il faut utiliser la méthode is_pressed() du bouton. Cette méthode renvoie True (vrai) ou False (faux), on peut donc l'utiliser dans une instruction conditionnelle.
<br>
Exemple avec le bouton A :
<pre><code>
while True:
    if button_a.is_pressed():
        # block des instructions qui s'exécuteront si le bouton est appuyé
    else:
        # block des instructions qui s'exécuteront si le bouton n'est pas appuyé 
</code></pre>
</div>
<br>

> **Travail à faire :** Faire en sorte que l'image HAPPY soit affichée quand le bouton est appuyé et que l'image SAD le soit quand le bouton n'est pas appuyé.

## Activité 2ème heure

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>À regarder uniquement à la deuxième heure !</u></summary>
  <div style="margin-top: 10px;">
    <p>Tp noté ! À faire sur la feuille distribué</p>
    <p>Si vous avez regardé avant : - 1 points 😈 </p>
  </div>
</details>




