# Visualizzazione Interattiva dello Spaziotempo di Kerr 🌌
[Read in English (EN)](README.md) | [Leggi in Italiano (IT)](LEGGIMI.md)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Visualization-Plotly-orange)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Questa repository offre una visualizzazione 3D interattiva della **metrica di Kerr**, che descrive la geometria dello spaziotempo attorno a un buco nero rotante non carico. Utilizzando Python e Plotly, questo strumento permette di esplorare le superfici matematiche e i limiti che caratterizzano gli spaziotempi rotanti, tra cui gli orizzonti degli eventi e le ergosfere.

## 🔭 Background Fisico

La geometria di Kerr è determinata dalla massa $M$ e dal momento angolare $J$. Nelle coordinate di Boyer-Lindquist, le superfici di interesse sono definite da:

### 1. Orizzonti degli Eventi ($r_\pm$)
Le coordinate radiali dove il coefficiente metrico $\Delta = r^2 - 2Mr + a^2$ si annulla:
$$r_\pm = M \pm \sqrt{M^2 - a^2}$$
dove $a = J/M$ è il parametro di spin.

### 2. Ergosfere (Limiti Statici, $r_{s\pm}$)
I confini dove la componente temporale della metrica $g_{tt}$ svanisce:
$$r_{s\pm} = M \pm \sqrt{M^2 - a^2 \cos^2 \theta}$$

La regione compresa tra $r_+$ e $r_{s+}$ è l'**ergoregione**, dove l'effetto di trascinamento dei sistemi di riferimento (*frame-dragging*) è così intenso che non possono esistere osservatori stazionari.

## 🚀 Funzionalità Principali

- **Rendering 3D Interattivo:** Esplora gli orizzonti degli eventi e le ergosfere da qualsiasi angolazione.
- **Manipolazione dello Spin in Tempo Reale:** Include uno slider (tramite Plotly) per variare il parametro di spin $a$ dal limite di Schwarzschild ($0 M$) al buco nero di Kerr estremo ($1 M$).
- **Mappatura delle Coordinate:** Accurata trasformazione dalle coordinate di Boyer-Lindquist a quelle Cartesiane $(x, y, z)$ per una rappresentazione realistica dello spaziotempo.

## 🛠️ Installazione & Uso

1. **Clonare la repository:**
   ```bash
   git clone [https://github.com/corradomarzano/Kerr-Spacetime-Simulation.git](https://github.com/corradomarzano/Kerr-Spacetime-Simulation.git)
   cd Kerr-Spacetime-Simulation

2. **Installare le librerie richieste:**
   ```bash
   pip install -r requirements.txt

3. **Eseguire il Programma:**
   - **Opzione A (Jupyter)**: Aprire Kerr_Visualizer.ipynb in JupyterLab, Google Colab o Visual Studio Code e selezionare il comando *"run all cells"*.
   - **Opzione B (Python script)**: Se si è esportato lo script, eseguire il comando:
   ```bash
   python Kerr_Visualizer.py

## 📊 Funzionalità Chiave
Il programma permette di visualizzare quattro superfici innestate:
- **Ergosfera Esterna**: Rappresenta il limite per gli osservatori statici, i quali all'interno di questa regione dello spaziotempo intorno al Buco Nero sono costretti a co-ruotare con esso, non potendo rimanere statici.
- **Orizzonte degli Eventi Esterno**: Rappresenta il cosiddetto *Punto di Non Ritorno* oltre il quale ogni cosa, persino la luce, deve dirigersi verso la singolarità posizionata al centro del Buco Nero.
- **Orizzonte degli Eventi Interno & Ergosfera Interna**: Limiti teorici situati all'interno dell'orizzonte di Cauchy, caratterizzati dalle stesse proprietà delle loro controparti esterne.

**Consiglio**: Usa lo slider posto in fondo al grafico interattivo per cambiare il parametro di spin $a$ e osserva come si deformano gli Orizzonte degli Eventi e le Ergosfere!

---
**Autore**: [Corrado Marzano](https://www.linkedin.com/in/corrado-marzano-7846353a8/)

**Contesto di Ricerca**: Sviluppato come strumento computazionale per studiare e illustrare la dinamica degli oggetti compatti e la Relatività Generale in vista del mio esame di Gravitazione Sperimentale (Analisi Dati).
