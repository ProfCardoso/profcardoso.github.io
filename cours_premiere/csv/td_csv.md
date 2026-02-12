# Traitement des données en python

Documentation officielle python : [Lecture et écriture de fichiers CSV](https://docs.python.org/fr/3.7/library/csv.html)

## Importation des données d'un fichier csv en python

Noous travaillerons par la suite avec ce document : [films.csv](./films.csv)

### Importation dans une liste de listes
Voici les étapes de l'importation

- La première étape consiste à importer le fichier texte à l'aide de la fonction `open`. Le paramètre `'r'` indique que le fichier est **ouvert en lecture seule** et le paramètre `encoding='utf-8'` fichier source est **codé en utf-8**.
- La deuxième étape consiste à transformer le texte importé en utilisant la fonction `reader` de la librairie `csv`. Cette fonction renvoie un objet qui n'est pas directement exploitable mais qui est un itérable dont **chaque élément est un tableau à une dimension correspondant à une ligne du fichier csv**.
- La troisième étape consiste donc à parcourir l'itérable **élément par élément** et à ajouter chacun de ces éléments dans une liste.
On obtient ainsi une **liste de liste**.

🠆 Exemple avec le fichier films.csv.

```python
import csv
listeFilms = []
objFichier = open('films.csv', 'r', encoding='utf-8')
objDatasCsv = csv.reader(objFichier, delimiter=';')
for ligne in objDatasCsv:
    listeFilms.append(ligne)
objFichier.close()
print(listeFilms)
```
🠆 Ce code peut être simplifié en utilisant with :

```python
import csv
listeFilms = []
with open('films.csv', 'r', encoding='utf-8') as objFichier:
    objDatasCsv = csv.reader(objFichier, delimiter=';')
    for ligne in objDatasCsv:
        listeFilms.append(ligne)
```

### Importation dans une liste de dictionnaires

La méthode est similaire.  
  
La première étape est inchangée.  
  
Dans la deuxième étape, on utilise la fonction DictReader (à la place de reader). Cette fonction renvoie un objet itérable dont chaque élément est un objet apparenté à un dictionnaire correspondant à une ligne du fichier csv, les clés étant les valeurs de la première ligne du fichier.

Dans la troisième étape, il faut, en plus convertir chaque élément en dictionnaire (avec la fonction `dict()`) avant de l'ajouter à la liste.

On obtient ainsi une **liste de dictionnaires**.

🠆 Exemple avec le fichier films.csv.

```python
import csv
listeFilms = []
with open('films.csv', 'r', encoding='utf-8') as objFichier:
    objDatasCsv = csv.DictReader(objFichier, delimiter=';')
    for ligne in objDatasCsv:
        listeFilms.append(dict(ligne))
```

## Projection de données

On appelle projection le fait d'obtenir les valeurs de certains ou tous les attributs d'une table / base de données / fichiers CSV.

**Exemple** : depuis le fichier des données ouvertes sur les villes et départements.

```python
# Exemple : Afficher le nom des villes
for ligne in villes:  # Pour chaque ligne dans la liste des villes
   print(ligne["nom_commune"])  # Affiche la valeur associée à la clé 'nom_commune'

# Afficher le nom de toutes les villes
for ligne in villes:
   print(ligne["nom_commune"])

# Afficher le département de chaque ville
for ligne in villes:
   print("La ville ", ligne["nom_commune"], " est dans le département : ", ligne["nom_departement"])
```

Cela permet donc d'obtenir dans notre exemple de villes, le nom de celle-ci, le département, etc. de toutes les villes sans aucune contrainte.

> ### Application I : Liste des titres
> 
> Écrire une fonction `extraire_titres(films)` qui retourne la liste de tous les titres de films.
> 
> Résultat attendu :
> 
```python
["La ligne verte", "La liste de Schindler", "Le voyage de Chihiro"]
```
> 
> ### Application II : Années de sortie
> 
> Écrire une fonction `extraire_annees(films)` qui retourne la liste de toutes les années de sortie (sans doublons).
> 

## Sélection de données

On appelle sélection le fait de sélectionner des valeurs suivant certains critères ou condition. Cela permet donc d'obtenir des informations ou de réaliser des traitements sur les données d'un fichier suivant divers critères (par exemple sur les villes).

**Exemple** : depuis le fichier des données ouvertes sur les villes et départements.

```python
# Afficher le nom des villes qui sont dans le département 30
for ligne in villes:
   if ligne['code_departement'] == '30':
      print(ligne["nom_commune"])

# Afficher les noms des villes commençant par la lettre N
for ligne in villes:
   if ligne["nom_commune"][0] == "N":
      print(ligne["nom_commune"])
```

> ### Application III : Films anciens
> 
> Écrire une fonction `films_avant_2000(films)` qui retourne la liste des films sortis avant l'an 2000.
> 
> ### Application IV : Films bien notés
>
> Écrire une fonction `films_note_superieure(films, seuil)` qui retourne les films ayant une note supérieure ou égale au seuil donné.
>
> Exemple : `films_note_superieure(films, 9.0)` doit retourner "Le voyage de chihiro" et "Interstellar"
>
> ### Application V : Titres des films de Nolan
>
> Écrire une fonction `titres_nolan(films)` qui retourne uniquement les titres des films réalisés par Nolan.
>
> Résultat attendu :
>
```python
["Inception", "Interstellar"]
```

## Tri d'une table sur une colonne

Une table étant représentée par une liste, on peut la trier en utilisant la fonction `sorted` ou la méthode `.sort()`, avec l’argument supplémentaire `key` qui est une fonction renvoyant la valeur utilisée pour le tri.
  
**Rappel :** la méthode `.sort()` trie la liste **en place**, c'est-à-dire modifie la liste directement sans en créer une nouvelle, alors que la fonction `sorted()` renvoie une **nouvelle liste** correspondant la liste triée, la liste initiale étant laissée intacte.  
  
Pour la suite nous utiliserons la fonction `sorted()`.

### key 

**Exemple** : Tri de liste

```python
>>>liste = sorted(['abc', 'yz']) 
>>>print(liste)
['abc', 'yz']       # le tri se fait par défaut suivant l'ordre lexicographique 
>>>liste = sorted(['abc', 'yz'], key=len) 
>>>print(liste)
['yz', 'abc']       # le tri s'est fait ici suivant la longueur des chaînes de caractères contenues.			
```
L'attribut `key` nous permet de choisir le critère de tri, ici `len` , pour trier par ordre croissant suivant la longueur de la chaîne de caractères considérée.

### lamda fonction

Une fonction `lambda` est une **fonction anonyme**, c'est en quelque sorte une fonction pouvant être écrite en une seule ligne.
  
On la note ainsi :

```
lambda entree : expression de la sortie
```

<u>Voici un exemple de lambda fonction (g) avec une autre fonction (f) :</u>

```python
def f(x):
    return x*2  

g = lambda x : x*2  
```
**Exemple** : Tri de liste de dictionnaire par lambda fonction

```python
eleves_poudlard = [
    {'Nom': 'Granger', 'Prenom': 'Hermione', 'Magie': 18, 'Potion': 16, 'Baguette': 15},
    {'Nom': 'Weasley', 'Prenom': 'Ron', 'Magie': 1, 'Potion': 3, 'Baguette': 5},
    {'Nom': 'Potter', 'Prenom': 'Harry', 'Magie': 14, 'Potion': 13, 'Baguette': 16}
]

table_triee = sorted(eleves_poudlard, key=lambda sorcier: sorcier["Magie"])

print(table_triee)	
```
> ### Application VI : Tri selon les notes
>
> Écrire une fonction `tri_des_notes(films)` qui retourne les titres des films triés de la note la plus basse à la plus grande.
>

## Activité pour allez plus loin 

<div style="display: flex; flex-direction:column;  text-align: center; ">
  <img style="margin: auto;" src="./pokemon-logo-png-1428.png" alt="Python" width="800" />
</div>

Vous êtes devenu il y a peu fan de la licence Pokémon, et pour vous renseigner sur tous les pokémons de la première génération ( il y en a 151 ), vous avez téléchargé toutes les données concernant cette génération ([le document csv est ici](./pokemon_001_151_fr.csv)).  

Les attributs de ces données sont les suivantes :
- **numero** : le numéro du pokémon;
- **nom**: le nom du pokémon;
- **type_1** : le premier type du pokémon;
- **type_2** : le second type du pokémon, si il en possède un;
- **pv** : la statistique du pokémon sur ses points de vie
- **attaque** : la statistique du pokémon sur son attaque
- **défense** : la statistique du pokémon sur sa défense
- **attaque_spé**	: la statistique du pokémon sur attaque spéciale
- **défense_spé**	: la statistique du pokémon sur sa défense spéciale
- **vitesse** : la statistique du pokémon sur sa vitesse

Vous décidez donc de manipuler ces données pour vous former la meilleure équipe de pokémon ( 6 au maximum ), devenir le meilleur dresseur et gagner les défis !

1. Dans un dossier, télécharger le document csv précédent, et créer un fichier python pour y importer la bibliothèque csv.

2. Utiliser cette bibliothèque pour créer la variable globale `POKEMON`, contenant la liste de dictionnaire de chacun des pokémon

```python
>>> print(POKEMON)
[ {"numero": 1 ,"nom": "Bulbizarre" ,"type_1": "Plante" ,"type_2": "Poison", "pv":45 ,"attaque":49 ,"défense":49 ,"attaque_spé":65 ,"défense_spé":65 ,"vitesse":45}, 
... ]
								
```

3. Écrire le programme python pour afficher la liste des 151 pokémons du document csv.

4. Écrire la fonction `type()`, qui affiche les types possibles de tous les pokémons, à partir des types présent dans le document csv.

5. Écrire la fonction `meilleur(stat)`, qui affiche le meilleur pokémon de la liste selon la statistique voulu donné en paramètre.

6. Écrire la fonction `equipe()`, qui créer une liste de pokémon composé des meilleurs pokemons de chaque statistique.
