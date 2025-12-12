---
title: Initialisation à Python
---

# Les bons usages du numérique

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<link rel="stylesheet" href="../../assets/plateau.css" />

<body>
    <main>
        <div id="grille">
            <div id="themes">
                <fieldset>
                    <legend>
                        <h2>Thèmes</h2>
                    </legend>
                    <table>
                        <tr>
                            <th class="c1">☺</th>
                            <td>Droit à l'image</td>
                        </tr>
                        <tr>
                            <th class="c2">△</th>
                            <td>Liberté d'expression<br>Respect de la vie privée</td>
                        </tr>
                        <tr>
                            <th class="c3">✷</th>
                            <td>Cyberviolence et<br> cyberharcèlement</td>
                        </tr>
                        <tr>
                            <th class="c4">❖</th>
                            <td>Identité numérique</td>
                        </tr>
                        <tr>
                            <th class="c5">◯</th>
                            <td>Big data</td>
                        </tr>
                        <tr>
                            <th class="c6">◼</th>
                            <td>Droit d'auteur</td>
                        </tr>
                        <tr>
                            <th class="c7">©</th>
                            <td>Licences<br>Conditions d'utilisation</td>
                        </tr>
                    </table>
                </fieldset>
            </div>
            <div id="de">
                <fieldset>
                    <legend> <button id="de_btn">Lancer</button> </legend>
                    <div id="de_visuel">⚅</div>
                </fieldset>
            </div>
            <div id="plateau">
                <table>
                    <tr>
                        <td class="cel c6">◼</td>
                        <td class="cel c5">◯</td>
                        <td class="cel c3">✷</td>
                        <td class="cel c1">☺</td>
                        <td class="cel c4">❖</td>
                        <td class="cel c5">◯</td>
                        <td class="cel c1">☺</td>
                        <td class="cel c2">△</td>
                        <td class="cel c3">✷</td>
                    </tr>
                    <tr>
                        <td class="cel c4">❖</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="cel c7">©</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="cel c7">©</td>
                    </tr>
                    <tr>
                        <td class="cel c7">©</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="cel c6">◼</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="cel c1">☺</td>
                    </tr>
                    <tr>
                        <td class="cel c2">△</td>
                        <td></td>
                        <td></td>
                        <td class="cel centre" colspan="3" rowspan="3"></td>
                        <td></td>
                        <td></td>
                        <td class="cel c4">❖</td>
                    </tr>
                    <tr>
                        <td class="cel c5">◯</td>
                        <td class="cel c3">✷</td>
                        <td class="cel c4">❖</td>
                        <td class="cel c5">◯</td>
                        <td class="cel c2">△</td>
                        <td class="cel c6">◼</td>
                    </tr>
                    <tr>
                        <td class="cel c1">☺</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="cel c7">©</td>
                    </tr>
                    <tr>
                        <td class="cel c6">◼</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="cel c2">△</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="cel c3">✷</td>
                    </tr>
                    <tr>
                        <td class="cel c3">✷</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="cel c1">☺</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="cel c1">☺</td>
                    </tr>
                    <tr>
                        <td class="cel c4">❖</td>
                        <td class="cel c2">△</td>
                        <td class="cel c5">◯</td>
                        <td class="cel c6">◼</td>
                        <td class="cel c7">©</td>
                        <td class="cel c3">✷</td>
                        <td class="cel c2">△</td>
                        <td class="cel c4">❖</td>
                        <td class="cel c5">◯</td>
                    </tr>
                </table>
            </div>
        </div>
    </main>
    <script>
        /* ==== dé ==== */
        let de_valeurs = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"];
        function reactive_de() {
            document.querySelector('#de_btn').disabled = false;
        }
        function change_de(nb) {
            if (nb == 0) {
                val = Math.floor(Math.random() * de_valeurs.length);
            } else {
                val = nb % de_valeurs.length;
                setTimeout(change_de, 100, nb - 1);
            }
            document.querySelector('#de_visuel').innerHTML = de_valeurs[val];
        }
        document.querySelector('#de_btn').addEventListener('click', function () {
            de_valeurs.sort(() => Math.random() - 0.5);
            document.querySelector('#de_btn').disabled = true;
            setTimeout(reactive_de, 5000);
            change_de(15);
        });
    </script>
</body>