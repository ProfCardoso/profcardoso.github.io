---
title: Représentation des nombres
---

<link rel="stylesheet" href="../../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<!-- ecrire du code python avec balise -->
<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> <script defer src="https://pyscript.net/alpha/pyscript.js"></script> 



# Programmation Python

Voici quelques exercices supplémentaires pour vous tester et vous entraîner. Vous proposerez un script différent par exercice que vous enregistrez dans un dossier **exercice_python**.

## Exercices

> ### Exercice 1 : Parc d'attraction
> 
> Vous êtes chargé.e de mettre en place une borne automatique pour régler les droits d’entrée à un parc d’attraction.
> Chaque adulte doit payer 21€ pour rentrer et chaque enfant doit payer 13€. Pour cette borne, vous devez programmer sur Python un algorithme qui renvoie le prix à payer en fonction du nombre d’adultes et d’enfants du groupe.
> Sachant que la variable `A` stocke le nombre d’adultes, `E` le nombre d’enfants et `P` le prix à payer, proposez un tel algorithme qui demande à l'utilisateur le nombre de personnes dans chacune des catégories et qui affiche le prix total à payer.
> 

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <py-script>
        A = int(input("Nombre d'adultes ?"))
        E = int(input("Nombre d'enfants ?"))

        P = A * 21 + E * 13

        print("Le prix du total est de ", P, "€")
    </py-script>
  </div>
</details>

> 
> ### Exercice 2 : IMC
> 
> L'Indice de Masse Corporelle (IMC) est un indicateur chiffré utilisé en médecine. L'IMC d'une personne est donné par la formule $$ IMC = \frac{\text{masse}}{\text{taille}^{2}} $$ où la masse est en kilos et la taille en mètres.
> 
> Proposez un algorithme qui demande à l'utilisateur sa taille et sa masse puis qui affiche l'IMC de la personne.
> 
> (Pensez à écrire un texte clair à destination de l'utilisateur pour qu'il sache quoi saisir.)
>

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <py-script>
        taille = int(input("Donnez votre taille (en m) :"))
        masse = int(input("Donnez votre masse (en kg) :"))

        imc = masse / ( taille ** 2 )

        print("Votre IMC est de : " , imc)
    </py-script>
  </div>
</details>

> 
> ### Exercice 3 : Pair ou Impair 
> 
> Ecrire un programme qui demande un nombre à l'utilisateur et test dans la console si celui-ci est pair ou impair. Attention, si ce n'est pas un entier ou un flottant, un message d'erreur devra être affiché pour prevenir l'utilisateur de son erreur.
>

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <py-script>
        nombre = int(input("Ecrire un nombre :"))

        if nombre % 2 == 0 :
            print(nombre, " est PAIR" )
        else:
            print(nombre, " est IMPAIR" )
    </py-script>
  </div>
</details>

>
> ### Exercice 4 : Calculatrice simple
>
> Ecrire un programme qui demande deux nombres a et b et une opération (+, -, *, /) à l’utilisateur.
> Le programme doit afficher le résultat correspondant.
>
> Exemple d’utilisation :
>
```shell
Entrer un premier nombre : 4
Entrer un deuxième nombre : 2
Choisis une opération (+, -, *, /) : *
Résultat : 8
```
>
>

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Réponse :</u></summary>
  <div style="margin-top: 10px;">
    <py-script>
        a = int(input("Entrer un premier nombre :"))
        b = int(input("Entrer un deuxieme nombre :"))
        operation = input("Choisis une opération (+, -, *, /) :")

        if operation == "+":
            print("Resultat : " , a + b)
        if operation == "-":
            print("Resultat : " , a - b)
        if operation == "*":
            print("Resultat : " , a * b)
        if operation == "/":
            print("Resultat : " , a / b)
    </py-script>
  </div>
</details>
  
---
  
<div id="quiz" style="border: 2px solid #007acc; padding: 20px; border-radius: 12px; background: #f8faff; font-family: sans-serif;">
  <h2>Programmation Python</h2>
  <p>Réponds aux questions ci-dessous puis clique sur <strong>Vérifier mes réponses</strong>.</p>

  <!-- Question 1 -->
  <div style="margin-top: 15px;">
    <h4>Quel est le type de la variable <strong>a</strong> quand <code> a = 3.14 </code></h4>
    <input type="text" id="q1" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f1" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p><strong>Flottant (ou float)</strong></p>
    </details>
  </div>

  <!-- Question 2 -->
  <div style="margin-top: 20px;">
    <h4> Code à trou : <code>print(_______)</code> que mettre dans le print pour écrire bonjour dans la console ? </h4>
    <label><input type="radio" name="q2" value="1"> "bonjour"</label><br>
    <label><input type="radio" name="q2" value="2"> bonjour</label><br>
    <label><input type="radio" name="q2" value="3"> [bonjour]</label><br>
    <p id="f2" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p><code>print("bonjour")</code></p>
    </details>
  </div>

  <!-- Question 3 -->
  <div style="margin-top: 15px;">
    <h4> Quelle fonction permet de demander une information à l'utilisateur ? </code></h4>
    <input type="text" id="q3" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f3" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p><strong>input()</strong></p>
    </details>
  </div>

  <!-- Question 4 -->
  <div style="margin-top: 20px;">
    <h4> Qu'est ce qu'une indentation </h4>
    <label><input type="radio" name="q4" value="1"> le bouton pour exécuter le programme</label><br>
    <label><input type="radio" name="q4" value="2"> 4 espaces ou une tabulation</label><br>
    <label><input type="radio" name="q4" value="3"> un moyen de coder </label><br>
    <p id="f4" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>4 espaces ou une tabulation</p>
    </details>
  </div>

  <!-- Bouton de validation -->
  <button onclick="verifierQuiz()" 
          style="margin-top: 25px; background-color: #007acc; color: white; border: none; border-radius: 6px; padding: 8px 15px; cursor: pointer;">
    Vérifier mes réponses
  </button>

  <h3 id="score" style="margin-top: 20px;"></h3>
</div>

<script>
function verifierQuiz() {
  let score = 0;

  // Question A remplir
  const q1 = document.getElementById("q1").value.trim();
  const f1 = document.getElementById("f1");
  if (q1 === "floattant" or q1 === "float" or q1 === "Floattant" or q1 === "Float") {
    f1.textContent = "✅ Bonne réponse !";
    f1.style.color = "green";
    score++;
  } else {
    f1.textContent = "❌ Mauvaise réponse.";
    f1.style.color = "red";
  }

  // Question QCM
  const q2 = document.querySelector('input[name="q2"]:checked');
  const f2 = document.getElementById("f2");
  if (q2 && q2.value === "1") {
    f2.textContent = "✅ Bonne réponse !";
    f2.style.color = "green";
    score++;
  } else {
    f2.textContent = "❌ Mauvaise réponse.";
    f2.style.color = "red";
  }

    // Question A remplir
  const q3 = document.getElementById("q3").value.trim();
  const f3 = document.getElementById("f3");
  if (q3 === "input()" or q3 === "input") {
    f3.textContent = "✅ Bonne réponse !";
    f3.style.color = "green";
    score++;
  } else {
    f3.textContent = "❌ Mauvaise réponse.";
    f3.style.color = "red";
  }

  // Question QCM
  const q4 = document.querySelector('input[name="q4"]:checked');
  const f4 = document.getElementById("f4");
  if (q4 && q4.value === "2") {
    f4.textContent = "✅ Bonne réponse !";
    f4.style.color = "green";
    score++;
  } else {
    f4.textContent = "❌ Mauvaise réponse.";
    f4.style.color = "red";
  }

  // Score final
  const scoreText = document.getElementById("score");
  scoreText.innerHTML = `🎯 Ton score : <strong>${score}/3</strong>`;
}
</script>
