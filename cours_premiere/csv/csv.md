# Les traitements de données en table: définition et enjeux

Aujourd’hui, une très grande quantité de **données** est produite en permanence. Ces données proviennent de nombreuses sources du quotidien : lorsque nous utilisons un **smartphone**, naviguons sur **Internet**, regardons des **vidéos en ligne**, utilisons une **carte bancaire**, ou encore lorsque des **capteurs** mesurent une température, une vitesse ou une position GPS. À cela s’ajoutent les données produites par les **entreprises**, les **réseaux sociaux**, les **objets connectés** ou les **expériences scientifiques**. On appelle le **Big Data** tout ce qui tourne autour de ces immenses ensembles de données.

Par exemple :

- un **lycée** produit des données sur les **notes**, les **absences** et les **emplois du temps** ;

- une **application de streaming** enregistre les **films** regardés et le **temps de visionnage** ;

- une **station météo** collecte des **températures**, des **pressions** et des **vitesses de vent**.

Cependant, ces données brutes, telles qu’elles sont collectées, ne sont souvent ni lisibles ni directement exploitables. Elles peuvent être très nombreuses, désordonnées, incomplètes ou stockées sous forme de fichiers (comme des **fichiers CSV**). C’est pourquoi on réalise des traitements de données.

Les traitements de données désignent l’**ensemble des opérations informatiques** qui permettent de organiser, transformer, analyser et exploiter des données afin d’en extraire des informations utiles. Ces traitements peuvent consister à trier des données, supprimer des erreurs, faire des calculs, rechercher des valeurs, regrouper des informations ou encore produire des statistiques.

## Les données ouvertes (open data)
Les données ouvertes (en anglais : open data) sont des données numériques dont l'accès et l'usage sont laissés libres aux usagers.

Elle peuvent être d'origine privée mais surtout publique, produites notamment par une collectivité ou un établissement public comme l'INSEE, les collectivités locales...

Elles sont diffusées de manière structurée selon une méthode et une licence ouverte garantissant leur libre accès et leur réutilisation par tous, sans restriction technique, juridique ou financière. Ces droits d'accès et de réutilisation s'inscrivent dans la pensée qui considère l'information publique comme un bien commun.

**Exemple :** [Les données ouvertes de la ville de Nîmes](https://data.nimes-metropole.fr/pages/home/)

## Qu’est-ce qu’un fichier CSV ?

Les petites quantités de données peuvent être stockées dans des fichiers texte dans le format csv.

Le sigle CSV signifie **Comma-Separated Values** et désigne un fichier texte contenant des données sous forme de tableau où:

- chaque **ligne** représente un **enregistrement**.

- chaque **colonne** représente une information, appelé **propriété** ou **attribut** (parfois aussi appelées **champ**, mais ce terme est plus large).

- les valeurs sont séparées par un **séparateur**, la virgule `,` (ou le point-virgule parfois en France )

En général, la **première ligne** explique le contenu de chaque colonne (« Nom », « Prénom » et « Date de naissance » par exemple). On appelle ces éléments des **descripteurs**. Chaque ligne est ensuite une nouvelle entrée avec différentes valeurs.

**Exemple de fichier CSV**

<div style="display:flex; gap:32px; align-items:flex-start; flex-wrap:wrap;">

  <!-- Gauche : tableau -->
  <div style="flex:1; min-width:320px;">
    <table style="border-collapse:collapse; width:100%; max-width:520px;">
      <thead>
        <tr>
          <th style="border:1px solid #444; padding:6px 10px; text-align:center;">Titre</th>
          <th style="border:1px solid #444; padding:6px 10px; text-align:center;">Année</th>
          <th style="border:1px solid #444; padding:6px 10px; text-align:center;">Réalisateur</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid #444; padding:6px 10px;">La ligne verte</td>
          <td style="border:1px solid #444; padding:6px 10px; text-align:center;">2000</td>
          <td style="border:1px solid #444; padding:6px 10px;">Frank Darabont</td>
        </tr>
        <tr>
          <td style="border:1px solid #444; padding:6px 10px;">La liste de Schindler</td>
          <td style="border:1px solid #444; padding:6px 10px; text-align:center;">1994</td>
          <td style="border:1px solid #444; padding:6px 10px;">Steven Spielberg</td>
        </tr>
        <tr>
          <td style="border:1px solid #444; padding:6px 10px;">Le voyage de Chihiro</td>
          <td style="border:1px solid #444; padding:6px 10px; text-align:center;">2002</td>
          <td style="border:1px solid #444; padding:6px 10px;">Hayao Miyazaki</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Droite : "contenu du fichier csv" -->
  <div style="flex:1; min-width:320px;">
  <pre style="margin:0; white-space:pre;">
Titre;Année;Réalisateur
La ligne verte;2000;Frank Darabont
La liste de Schindler;1994;Steven Spielberg
Le voyage de Chihiro;2002;Hayao Miyazaki
    </pre>
</div>

</div>


## Travail à faire 

🖥️ Récupérer le fichier csv "departements-france.csv" (téléchargeable [ici](https://www.data.gouv.fr/datasets/communes-de-france-base-des-codes-postaux) depuis le site des Données ouvertes de data.gouv.fr) .

🖥️ Ouvrer ce fichier avec un éditeur de texte.

🖊️ Quels sont les attributs de ces données ?

🖊️ Combien de département existe-t-il ?

🖥️ Récupérer le fichier csv "commune-departement-region.csv" (téléchargeable [ici](https://www.data.gouv.fr/datasets/communes-de-france-base-des-codes-postaux) depuis le site des Données ouvertes de data.gouv.fr) .

🖥️ Importer ce fichier dans un tableur (par exemple dans LibreOffice Calc ou des tableurs en ligne).

🖊️ Quels sont les attributs de ces données ?

🖊️ Quelles sont les informations disponibles sur la ville de Nîmes ?

🖊️ Quelle peut-être l'utilisation de ce fichier de données ?