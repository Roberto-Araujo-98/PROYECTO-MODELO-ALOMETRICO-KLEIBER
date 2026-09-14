# Modelo alométrico kleiber 🫀⚡

> **Análisis de escalamiento alométrico en mamíferos y modelo predictivo de anomalía metabólica humana mediante Inteligencia Artificial.**

`kleiber-ia` es un proyecto de investigación y modelado computacional que evalúa las leyes de potencia biológicas que relacionan la masa corporal, la tasa metabólica, el ritmo cardíaco y la esperanza de vida en los mamíferos.

El proyecto explora las diferencias entre los modelos de escalamiento por superficie ($M^{2/3}$) y redes fractales ($M^{3/4}$ / Ley de Kleiber), identificando numéricamente la esperanza de vida "teórica" del *Homo sapiens* en comparación con el impacto de la civilización y la medicina moderna.

---

## 🎯 Objetivos del Proyecto

- [ ] **Modelado Alométrico:** Entrenar modelos de regresión no lineal / espacio logarítmico con datos fisiológicos de especies mamíferas.
- [ ] **Comparativa de Exponentes ($2/3$ vs $3/4$):** Evaluar empíricamente qué hipótesis teórica (Superficie de Rubner vs. Redes de Kleiber) ajusta mejor con los datos reales.
- [ ] **Detección de Outliers:** Cuantificar la anomalía de la longevidad humana respecto a la "cuota biológica" de ~1 000 millones de latidos.
- [ ] **Interfaz Gráfica (Tauri + Rust + Python):** Desarrollar una aplicación de escritorio liviana con gráficos interactivos de la escala logarítmica.

---

## 🧮 Fundamento Teórico

El modelo se basa en la relación de potencia alométrica estándar:

$$Y = a \cdot M^b \implies \log_{10}(Y) = \log_{10}(a) + b \cdot \log_{10}(M)$$

Donde:
* **$M$**: Masa corporal (kg).
* **$b$**: Exponente alométrico ($0.75$ para tasa metabólica, $-0.25$ para frecuencia cardíaca, $0.25$ para longevidad).
* **$Y$**: Variable biológica analizada.

---

## 🏗️ Arquitectura Planeada

```text
kleiber-ia/
├── data/              # Datasets biológicos (masa, pulso, longevidad)
├── models/            # Scripts de entrenamiento y exportación (Python / ONNX)
├── src-tauri/         # Backend en Rust (ejecución de inferencias / Tauri IPC)
└── src/               # Frontend interactivo para visualización de datos
