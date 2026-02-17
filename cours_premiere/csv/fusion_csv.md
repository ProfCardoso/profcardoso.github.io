# Traitement des données en python

## Rappel de l'importation de document CSV en liste de dictionnaire

```python
import csv
listeFilms = []
with open('films.csv', 'r', encoding='utf-8') as objFichier:
    objDatasCsv = csv.DictReader(objFichier, delimiter=';')
    for ligne in objDatasCsv:
        listeFilms.append(dict(ligne))
```

## Fusion de données : Jointure de table

### Jointure de deux tables selon un champ

La **jointure de DEUX tables selon un champ** revient à fusionner ces tables à partir d'un attribut commun pour former **UNE seule table** contenant les enregistrements des valeurs correspondant au champ de deux tables.

**Exemple**

<div style="display:flex; gap:32px; align-items:flex-start; flex-wrap:wrap;">

  <!-- Gauche : tableau -->
  <div style="flex:1; min-width:320px;">
  <pre style="margin:0; white-space:pre;">
    id,nom,classe
    1,Martin,1A
    2,Dupont,1A
    3,Bernard,1B
    4,Durand,1B
    </pre>
</div>

  <!-- Droite : "contenu du fichier csv" -->
  <div style="flex:1; min-width:320px;">
  <pre style="margin:0; white-space:pre;">
    id,NSI,Math
    1,15,13
    2,12,17
    4,18,9
    5,10,11
    </pre>
</div>

</div>

### Activité I : Fusion à la main 🖋️

*Voire le document imprimé.* ( en [.odt](./fusion.odt) ou [.pdf](./fusion.pdf) )

**Consigne :**

- Soulignez la colonne clé.

- Construisez la table fusionnée.

- Que faire si un élève n’a pas de note ?

- Que faire si une note ne correspond à aucun élève ?

- Est il possible de rajouter cette enregistrement pour l'élève avec l'id 3 dans le Note.csv ?

```
3,douze,treize
```

### Activité II : Fusion sur python 🐍

A partir d' [eleve.csv](eleve.csv) et [note.csv](./note.csv), réaliser une fonction python pour fusionner ces 2 tables en une.
  
**1er étape**: Afficher tous les enregistrements des élèves, puis des notes. Vous pouvez écrire une fonction pour vous aider.

**Exemple**
```python
>>> print(eleve)
[
    [1,"Martin","1A"],
    [2,"Dupont","1A"],
    ...
]
```

**2eme étape**: Ecrire une fonction `projection(table, champ)` qui effectue l'affichage complet d'une table à partir d'un attribut, tout deux donnés en paramètre.

**Exemple**
```python
>>> projection(eleve,"id")
[
    [1],
    [2],
    ...
]
```

**3eme étape**: Ecrire une fonction `fusionne(table1, table2, champ)` qui affiche la fusion des 2 tables selon le champ donné en paramètre

**Exemple**
```python
>>> fusionne(eleve,note,"id")
[
    [1,"Martin","1A",15,13],
    [2,"Dupont","1A",12,17],
    ...
]
```


<span style="color: rgb(255,0,0);">ATTENTION !</span> Si le champ ne fait pas partie des 2 tables, une erreur doit être envoyée (assert) !

**4eme étape**: Pour les plus rapides, créer un dossier eleve_note.csv, et modifier le avec Python pour ajouter la fusion des 2 tables obtenu précédemment.

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Un indice ? 🤔</u></summary>
  <div style="margin-top: 10px;">
    <p>Vous pouvez réutiliser la fonction <code>with open</code> en changeant le paramètre <strong>'r' en 'w'</strong> pour écrire dans le document (write).</p>
    <p>Exemple :</p>
    <pre><code>
    with open("mon_fichier.txt", "w") as fichier:
        fichier.write("Bonjour tout le monde !")
    </code></pre>
  </div>
</details>