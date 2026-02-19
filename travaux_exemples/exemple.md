---
title: Exemple d'élèments pour le site web
---


<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

___

# Quelques exemples

## Bouton 

<a href="./seconde/lecon1.md" style="display: inline-block; padding: 10px 15px; background-color: #4CAF50; color: white; border-radius: 5px; text-decoration: none;">📘 Leçon 1 : Les entiers</a>


## ✅ Info box

<div style="border: 1px solid #007ACC; padding: 10px; border-radius: 5px; background-color: #E6F2FF;">
  <strong>ℹ️ Info :</strong> Cette leçon est importante pour comprendre les bases du calcul.
</div>

___

## Boite

<div class="cours-section">
  <div class="boites-lecons">

    <a href>
    <h3>Bit</h3>
    </a>
  </div>
</div>


___

## Photo

<div style="display: flex; flex-direction:column;  border: 1px solid #ccc; text-align: center; border-radius: 8px;">
  <img src="../../images/Portrait_of_George_Boole.png" alt="Python" width="400" />
  <span style="font-style: italic; color: gray;">George BOOLE (1815-1864)</span>
</div>

<div style="display: flex; flex-direction:column;  text-align: center; ">
  <img style="margin: auto;" src="../../images/Portrait_of_George_Boole.png" alt="Python" width="400" />
</div>


___


## Exercice
>
>### 🐍 Exercice 
>
>
>
>### 💻 Exercice 
>
>
>### 🖋️ Exercice 
>
>
>

___
## Reponse caché

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Mais alors ? Pourquoi pas cette méthode ? 🤔</u></summary>
  <div style="margin-top: 10px;">
    <p>Voici le contenu qui s’affiche quand on clique sur la ligne ci-dessus.</p>
    <ul>
      <li>Point 1</li>
      <li>Exemple : <code>print("Hello")</code></li>
    </ul>
  </div>
</details>

## Reponse caché code
<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Solution</u></summary>
  <div style="margin-top: 10px;">
    <p>Voici le contenu qui s’affiche quand on clique sur la ligne ci-dessus.</p>
    <code>
    </code>
  </div>
</details>

___
## Texte en couleur

<span style="color: rgb(165,42,42);">brown</span>


___
## Ligne sur le coté d'un texte

<div style="border-left: 5px solid green; padding-left: 12px;">
  <p> texte </p>
</div>

___

## Exemple questionnaire 

<div id="quiz" style="border: 2px solid #007acc; padding: 20px; border-radius: 12px; background: #f8faff; font-family: sans-serif;">
  <h2>Conversion de bases</h2>
  <p>Réponds aux questions ci-dessous puis clique sur <strong>Vérifier mes réponses</strong>.</p>

  <!-- Question 1 -->
  <div style="margin-top: 15px;">
    <h4>1️⃣ Convertis <strong>(1011)<sub>2</sub></strong> en base 10 :</h4>
    <input type="text" id="q1" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f1" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>(1011)<sub>2</sub> = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = <strong>11</strong></p>
    </details>
  </div>

  <!-- Question 2 -->
  <div style="margin-top: 20px;">
    <h4>2️⃣ Quelle est la base du système binaire ?</h4>
    <label><input type="radio" name="q2" value="8"> 8</label><br>
    <label><input type="radio" name="q2" value="10"> 10</label><br>
    <label><input type="radio" name="q2" value="2"> 2</label><br>
    <p id="f2" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>Le système binaire est basé sur la base <strong>2</strong> (chiffres possibles : 0 et 1).</p>
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
  if (q1 === "11") {
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
  if (q2 && q2.value === "2") {
    f2.textContent = "✅ Bonne réponse !";
    f2.style.color = "green";
    score++;
  } else {
    f2.textContent = "❌ Mauvaise réponse.";
    f2.style.color = "red";
  }

  // Score final
  const scoreText = document.getElementById("score");
  scoreText.innerHTML = `🎯 Ton score : <strong>${score}/3</strong>`;
}
</script>


---
# Troll

La suite du cours après les vacances ! En attendant : [ici](https://www.youtube.com/watch?v=xvFZjo5PgG0)

<div style="display: flex; flex-direction:column;  text-align: center; ">
  <img style="margin: auto;" src="../../images/to_be_continued.jpg" alt="Python" width="400" />
</div>

---

# Bouton caché

<a href="./liste_questions.html" class="secret-btn">.</a>

<style>
.secret-btn {
  font-size: 8px;
  color: rgba(0,0,0,0.05); /* presque invisible */
  text-decoration: none;
}
.secret-btn:hover {
  color: rgba(0,0,0,0.4); /* visible au survol */
}
</style>

---

# Definition

<div style="border:2px solid #af4c4cff; padding:10px; border-radius:8px">
<strong>Définition — Assertion</strong><br>
Une assertion est une instruction qui permet de vérifier qu’une condition est vraie.
</div>
