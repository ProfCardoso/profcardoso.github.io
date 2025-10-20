---
title: Représentation des nombres
---

<link rel="stylesheet" href="../assets/style.css" />
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Exercice Bonus

<div id="quiz" style="border: 2px solid #007acc; padding: 20px; border-radius: 12px; background: #f8faff; font-family: sans-serif;">
  <h2>Conversion de bases</h2>
  <p>Réponds aux questions ci-dessous puis clique sur <strong>Vérifier mes réponses</strong>.</p>

  <!-- Question 1 -->
  <div style="margin-top: 15px;">
    <h4>1/ Convertis <strong>(1011)<sub>2</sub></strong> en base 10 :</h4>
    <input type="text" id="q1" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f1" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>(1011)<sub>2</sub> = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = <strong>11</strong></p>
    </details>
  </div>

  <!-- Question 2 -->
  <div style="margin-top: 20px;">
    <h4>2/ Quelle est la base du système binaire ?</h4>
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
    <h4>3/ Convertis <strong>(23)<sub>10</sub></strong> en base 2 :</h4>
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


---
>
> 🔎 **Rappel :**  
> En base 16, chaque chiffre correspond à **4 bits**.  
> Exemple :  
> 
> $$(1010)_2 = (A)_{16}, \quad (1111)_2 = (F)_{16}, (1010 1111)_2 = (AF)_{16}$$
> 


<div id="quiz" style="border: 2px solid #7e3ff2; padding: 20px; border-radius: 12px; background: #faf8ff; font-family: sans-serif;">
  <h2> Conversion base 2 ↔ base 16</h2>
  <p>Réponds aux questions ci-dessous puis clique sur <strong>Vérifier mes réponses</strong>.</p>

  <!-- Question 1 -->
  <div style="margin-top: 15px;">
    <h4>1/ Convertis <strong>(11011100)<sub>2</sub></strong> en base 16 :</h4>
    <input type="text" id="q1" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f1" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>
        (1101 1100)<sub>2</sub> = D C en base 16.  
        En regroupant 4 bits : 1101 = D et 1100 = C → <strong>(DC)<sub>16</sub></strong>
      </p>
    </details>
  </div>

  <!-- Question 2 -->
  <div style="margin-top: 20px;">
    <h4>2/ Convertis <strong>(A9)<sub>16</sub></strong> en base 2 :</h4>
    <input type="text" id="q2" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f2" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>
        A = 10 → 1010, 9 = 1001  
        Donc (A9)<sub>16</sub> = <strong>10101001<sub>2</sub></strong>
      </p>
    </details>
  </div>

  <!-- Question 3 -->
  <div style="margin-top: 20px;">
    <h4>3/ Convertis <strong>(1111 0001)<sub>2</sub></strong> en base 16 :</h4>
    <input type="text" id="q3" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f3" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>
        (1111)(0001) → F 1  
        Donc (1111 0001)<sub>2</sub> = <strong>(F1)<sub>16</sub></strong>
      </p>
    </details>
  </div>

  <!-- Question 4 -->
  <div style="margin-top: 20px;">
    <h4>4/ Convertis <strong>(3E)<sub>16</sub></strong> en base 2 :</h4>
    <input type="text" id="q4" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f4" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>
        3 = 0011 et E = 1110  
        Donc (3E)<sub>16</sub> = <strong>00111110<sub>2</sub></strong>
      </p>
    </details>
  </div>

  <!-- Validation -->
  <button onclick="verifierQuiz()" 
          style="margin-top: 25px; background-color: #7e3ff2; color: white; border: none; border-radius: 6px; padding: 8px 15px; cursor: pointer;">
    Vérifier mes réponses
  </button>

  <h3 id="score" style="margin-top: 20px;"></h3>
</div>

<script>
function verifierQuiz() {
  let score = 0;

  // Question 1
  const q1 = document.getElementById("q1").value.trim().toUpperCase();
  const f1 = document.getElementById("f1");
  if (q1 === "DC") {
    f1.textContent = "✅ Bonne réponse !";
    f1.style.color = "green";
    score++;
  } else {
    f1.textContent = "❌ Mauvaise réponse (attendu : DC).";
    f1.style.color = "red";
  }

  // Question 2
  const q2 = document.getElementById("q2").value.trim();
  const f2 = document.getElementById("f2");
  if (q2 === "10101001") {
    f2.textContent = "✅ Bonne réponse !";
    f2.style.color = "green";
    score++;
  } else {
    f2.textContent = "❌ Mauvaise réponse (attendu : 10101001).";
    f2.style.color = "red";
  }

  // Question 3
  const q3 = document.getElementById("q3").value.trim().toUpperCase();
  const f3 = document.getElementById("f3");
  if (q3 === "F1") {
    f3.textContent = "✅ Bonne réponse !";
    f3.style.color = "green";
    score++;
  } else {
    f3.textContent = "❌ Mauvaise réponse (attendu : F1).";
    f3.style.color = "red";
  }

  // Question 4
  const q4 = document.getElementById("q4").value.trim();
  const f4 = document.getElementById("f4");
  if (q4 === "00111110") {
    f4.textContent = "✅ Bonne réponse !";
    f4.style.color = "green";
    score++;
  } else {
    f4.textContent = "❌ Mauvaise réponse (attendu : 00111110).";
    f4.style.color = "red";
  }

  // Score final
  const scoreText = document.getElementById("score");
  scoreText.innerHTML = `🎯 Ton score : <strong>${score}/4</strong>`;
}
</script>

---
>
> 🔎 **Rappel :**  
> En base 16, chaque chiffre correspond à **4 bits**.  
> Exemple :  
> 
> $$(1010)_2 = (A)_{16}, \quad (1111)_2 = (F)_{16}, (1010 1111)_2 = (AF)_{16}$$
> 


<div id="quiz" style="border: 2px solid #ff7a00; padding: 20px; border-radius: 12px; background: #fff9f3; font-family: sans-serif;">
  <h2>Conversion base 10 ↔ base 16</h2>
  <p>Réponds aux questions ci-dessous puis clique sur <strong>Vérifier mes réponses</strong>.</p>

  <!-- Question 1 -->
  <div style="margin-top: 15px;">
    <h4>1/ Convertis <strong>(255)<sub>10</sub></strong> en base 16 :</h4>
    <input type="text" id="q1" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f1" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>
        255 // 16 = 15 et il reste 15. 15 x 16<sup>1</sup> + 15 x 16<sup>0</sup>
      </p>
      <p>
        Donc (255)<sub>10</sub> = <strong>(FF)<sub>16</sub></strong>
      </p>
    </details>
  </div>

  <!-- Question 2 -->
  <div style="margin-top: 20px;">
    <h4>2/ Convertis <strong>(4095)<sub>10</sub></strong> en base 16 :</h4>
    <input type="text" id="q2" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f2" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>
        4095 ÷ 16 = 255 reste 15 → F  
        255 ÷ 16 = 15 reste 15 → F  
        Donc (4095)<sub>10</sub> = <strong>(FFF)<sub>16</sub></strong>
      </p>
    </details>
  </div>

  <!-- Question 3 -->
  <div style="margin-top: 20px;">
    <h4>3/ Convertis <strong>(2A)<sub>16</sub></strong> en base 10 :</h4>
    <input type="text" id="q3" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f3" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>
        (2A)<sub>16</sub> = 2×16¹ + 10×16⁰ = 32 + 10 = <strong>42</strong><sub>10</sub>
      </p>
    </details>
  </div>

  <!-- Question 4 -->
  <div style="margin-top: 20px;">
    <h4>4/ Convertis <strong>(7F)<sub>16</sub></strong> en base 10 :</h4>
    <input type="text" id="q4" placeholder="Ta réponse ici..." style="padding: 5px; border-radius: 5px;">
    <p id="f4" style="margin-top: 5px;"></p>
    <details style="margin-top: 5px;">
      <summary>💡 Voir la correction</summary>
      <p>
        (7F)<sub>16</sub> = 7×16¹ + 15×16⁰ = 112 + 15 = <strong>127</strong><sub>10</sub>
      </p>
    </details>
  </div>

  <!-- Validation -->
  <button onclick="verifierQuiz()" 
          style="margin-top: 25px; background-color: #ff7a00; color: white; border: none; border-radius: 6px; padding: 8px 15px; cursor: pointer;">
    Vérifier mes réponses
  </button>

  <h3 id="score" style="margin-top: 20px;"></h3>
</div>

<script>
function verifierQuiz() {
  let score = 0;

  // Question 1
  const q1 = document.getElementById("q1").value.trim().toUpperCase();
  const f1 = document.getElementById("f1");
  if (q1 === "FF") {
    f1.textContent = "✅ Bonne réponse !";
    f1.style.color = "green";
    score++;
  } else {
    f1.textContent = "❌ Mauvaise réponse (attendu : FF).";
    f1.style.color = "red";
  }

  // Question 2
  const q2 = document.getElementById("q2").value.trim().toUpperCase();
  const f2 = document.getElementById("f2");
  if (q2 === "FFF") {
    f2.textContent = "✅ Bonne réponse !";
    f2.style.color = "green";
    score++;
  } else {
    f2.textContent = "❌ Mauvaise réponse (attendu : FFF).";
    f2.style.color = "red";
  }

  // Question 3
  const q3 = document.getElementById("q3").value.trim();
  const f3 = document.getElementById("f3");
  if (q3 === "42") {
    f3.textContent = "✅ Bonne réponse !";
    f3.style.color = "green";
    score++;
  } else {
    f3.textContent = "❌ Mauvaise réponse (attendu : 42).";
    f3.style.color = "red";
  }

  // Question 4
  const q4 = document.getElementById("q4").value.trim();
  const f4 = document.getElementById("f4");
  if (q4 === "127") {
    f4.textContent = "✅ Bonne réponse !";
    f4.style.color = "green";
    score++;
  } else {
    f4.textContent = "❌ Mauvaise réponse (attendu : 127).";
    f4.style.color = "red";
  }

  // Score final
  const scoreText = document.getElementById("score");
  scoreText.innerHTML = `🎯 Ton score : <strong>${score}/4</strong>`;
}
</script>
