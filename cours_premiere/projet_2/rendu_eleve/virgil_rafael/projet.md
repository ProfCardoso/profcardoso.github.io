
# Projet Bataille Navale - Rafael/Virgil

<script src="https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"></script>

<button onclick="runPython()">Exécuter Python</button>
<pre id="output"></pre>

<script>
async function runPython() {
    const pyodide = await loadPyodide();
    const code = await fetch("script.py").then(r => r.text());
    pyodide.runPython(code);
    const result = pyodide.runPython("jeu(plateauJ1, plateauJ2, mapping, J1cooBateau1, J1cooBateau2, J1cooBateau3, J1cooBateau4, J1cooBateau5, J2cooBateau1, J2cooBateau2, J2cooBateau3, J2cooBateau4, J2cooBateau5)");
    document.getElementById("output").textContent = result;
}
</script>

