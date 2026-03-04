# Interactive Kerr Spacetime Visualization 🌌

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Visualization-Plotly-orange)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository provides an interactive 3D visualization of the **Kerr metric** geometry, representing a rotating, uncharged black hole. Using Python and Plotly, this tool allows users to explore the mathematical boundaries of rotating spacetimes, including event horizons and ergoregions.

## 🔭 Physics Background

The Kerr geometry is determined by two parameters: the mass $M$ and the angular momentum $J$. In Boyer-Lindquist coordinates, the surfaces of interest are defined by:

### 1. Event Horizons ($r_\pm$)
The radial coordinates where the metric coefficient $\Delta = r^2 - 2Mr + a^2$ vanishes:
$$r_\pm = M \pm \sqrt{M^2 - a^2}$$
where $a = J/M$ is the spin parameter.

### 2. Ergoregions (Static Limits, $r_{s\pm}$)
The boundaries where the temporal component of the metric $g_{tt}$ vanishes:
$$r_{s\pm} = M \pm \sqrt{M^2 - a^2 \cos^2 \theta}$$

The region between $r_+$ and $r_{s+}$ is the **ergosphere**, where frame-dragging is so intense that stationary observers cannot exist.

## 🚀 Key Features

- **Interactive 3D Rendering:** Explore the event horizons and ergoregions from any angle.
- **Real-time Spin Manipulation:** Includes a Plotly-based slider to vary the spin parameter $a$ from $0$ (Schwarzschild limit) to $M$ (Extremal Kerr black hole).
- **Coordinate Mapping:** Accurate transformation from Boyer-Lindquist coordinates to Cartesian $(x, y, z)$ for realistic spatial representation.

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/corradomarzano/Kerr-Interactive-Viz.git](https://github.com/corradomarzano/Kerr-Interactive-Viz.git)
   cd Kerr-Interactive-Viz

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the visualizer:**
   - **Option A (Jupyter)**: Open Kerr_Visualizer.ipynb in JupyterLab or VS Code and run all cells.
   - **Option B (Python script)**: If you exported the script, run:
   ```bash
   python Kerr_Visualizer.py

## 📊 Key Features
The tool visualizes four nested surfaces:
- **Outer Ergosphere**: The limit for static observers, that inside this region must co-rotate with the Black Hole and cannot remain static.
- **Outer Event Horizon**: The point of no return where everything, even light, must go towards the singularity located at the center of the Black Hole.
- **Inner Event Horizon & Inner Ergosphere**: Theoretical boundaries within the Cauchy horizon, with same properties as their outer counterparts.

**Tip**: Use the slider at the bottom of the interactive plot to change the spin parameter $a$ and watch the Event Horizons and Ergospheres deform!

---
**Author**: [Corrado Marzano](https://www.linkedin.com/in/corrado-marzano-7846353a8/)

**Research Context**: Developed as a computational tool to study and illustrate the dynamics of compact objects and General Relativity for my Experimental Gravitation (Data Analysis) exam.

---

### File `requirements.txt`

```text
numpy
plotly
matplotlib
