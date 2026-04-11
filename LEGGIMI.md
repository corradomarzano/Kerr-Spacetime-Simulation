# Visualizzazione Interattiva dello Spaziotempo di Kerr 🌌
[Read in English (EN)](README.md) | [Leggi in Italiano (IT)](LEGGIMI.md)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Visualization-Plotly-orange)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Questa repository offre una visualizzazione 3D interattiva della **metrica di Kerr**, che descrive la geometria dello spaziotempo attorno a un buco nero rotante non carico.

## 🔭 Background Fisico
La geometria di Kerr è determinata dalla massa $M$ e dal momento angolare $J$. Nelle coordinate di Boyer-Lindquist, le superfici di interesse sono definite da:

### 1. Orizzonti degli Eventi ($r_\pm$)
Le coordinate radiali dove il coefficiente metrico $\Delta = r^2 - 2Mr + a^2$ si annulla:
$$r_\pm = M \pm \sqrt{M^2 - a^2}$$
dove $a = J/M$ è il parametro di spin.

### 2. Ergosfere (Limiti Statici, $r_{s\pm}$)
I confini dove la componente temporale della metrica $g_{tt}$ svanisce:
$$r_{s\pm} = M \pm \sqrt{M^2 - a^2 \cos^2 \theta}$$

La regione compresa tra $r_+$ e $r_{s+}$ è l'**ergosfera**, dove l'effetto di trascinamento dei sistemi di riferimento (*frame-dragging*) è così intenso che non possono esistere osservatori stazionari.

## 🚀 Funzionalità Principali
- **Rendering 3D Interattivo:** Esplora l'orizzonte degli eventi e l'ergosfera da qualsiasi angolazione.
- **Manipolazione dello Spin in Tempo Reale:** Include uno slider (tramite Plotly) per variare il parametro $a$ dal limite di Schwarzschild ($0$) al buco nero di Kerr estremo ($M$).
