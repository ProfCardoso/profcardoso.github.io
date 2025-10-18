---
title: Représentation des nombres
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Exercice Bonus

<div style="border: 2px solid #007acc; padding: 15px; border-radius: 10px; margin: 20px 0;">
  <h3>💡 Exercice bonus</h3>
  <p>Convertis le nombre <strong>(1011)<sub>2</sub></strong> en base 10 :</p>

  <input type="text" id="reponse1" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
  <button onclick="verifier1()" style="margin-left: 10px; background-color: #007acc; color: white; border: none; border-radius: 5px; padding: 5px 10px; cursor: pointer;">Vérifier</button>

  <p id="feedback1" style="margin-top: 10px;"></p>

  <details style="margin-top: 10px;">
    <summary><strong>Voir la correction</strong></summary>
    <p>(1011)<sub>2</sub> = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = <strong>11</strong></p>
  </details>
</div>

<script>
function verifier1() {
  const rep = document.getElementById('reponse1').value.trim();
  const feedback = document.getElementById('feedback1');
  if (rep === "11") {
    feedback.innerHTML = "✅ Bravo ! Bonne réponse 🎉";
    feedback.style.color = "green";
  } else {
    feedback.innerHTML = "❌ Ce n’est pas la bonne réponse. Essaie encore !";
    feedback.style.color = "red";
  }
}
</script>


---

<div id="quiz" style="border: 2px solid #007acc; padding: 20px; border-radius: 12px; background: #f8faff; font-family: sans-serif;">
  <h2>🧩 Exercices bonus – Conversion de bases</h2>
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

  <!-- Question 3 -->
  <div style="margin-top: 20px;">
    <h4>3️⃣ Convertis <strong>(23)<sub>10</sub></strong> en base 2 :</h4>
    <input type="text" id="q3" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f3" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>(23)<sub>10</sub> = <strong>10111</strong><sub>2</sub></p>
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

  // Question 1
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

  // Question 2
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

  // Question 3
  const q3 = document.getElementById("q3").value.trim();
  const f3 = document.getElementById("f3");
  if (q3 === "10111") {
    f3.textContent = "✅ Bonne réponse !";
    f3.style.color = "green";
    score++;
  } else {
    f3.textContent = "❌ Mauvaise réponse.";
    f3.style.color = "red";
  }

  // Score final
  const scoreText = document.getElementById("score");
  scoreText.innerHTML = `🎯 Ton score : <strong>${score}/3</strong>`;
}
</script>
