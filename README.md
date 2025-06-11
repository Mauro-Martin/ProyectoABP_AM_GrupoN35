# 📊 Proyección del Crecimiento Poblacional en la Provincia de Córdoba

**Este repositorio contiene el desarrollo completo del proyecto final del espacio curricular _Análisis Matemático_, correspondiente a la Tecnicatura en Ciencia de Datos e Inteligencia Artificial.**

---

## 📌 Descripción general

Este trabajo tiene como objetivo modelar el crecimiento poblacional de la provincia de Córdoba (Argentina) mediante herramientas matemáticas, aplicando modelos de crecimiento **lineal**, **exponencial** y **logístico**, ajustados a datos censales oficiales desde 1970 hasta 2022.

Se realizaron proyecciones demográficas para los años **2032** y **2042**, con análisis gráfico, cálculo de tasas de crecimiento, derivadas, y evaluación crítica de cada modelo en función de su comportamiento matemático.

---


## 👥 Autores

Este proyecto fue desarrollado por el **Grupo N°35** para el espacio curricular **Análisis Matemático**, en el marco de la **Tecnicatura en Ciencia de Datos e Inteligencia Artificial**.

- **Corvalán, Marcelo** – DNI: 31.115.158  
- **López, Franco** – DNI: 47.712.128  
- **Martin, Mauro Leonel** – DNI: 43.879.835  
- **Morales, Benjamín** – DNI: 47.320.279  
- **Riquelme, Belén Marité** – DNI: 36.435.161  
- **Rovaretti, Matías** – DNI: 46.452.760

---

## 📁 Estructura del repositorio

### `data/`
Contiene el archivo de datos censales históricos (formato CSV).

### `scripts/`
Contiene los scripts de Python utilizados para:

- Ajustar modelos y generar gráficos comparativos.
- Representar proyecciones ilustrativas.
- Generar automáticamente un informe técnico en PDF.

### `images/`
Imágenes generadas por los scripts para incluir en el informe y presentaciones.

### `informes/`
Contiene el informe final en PDF generado con Python, incluyendo introducción, metodología, análisis matemático y conclusiones.

---

## 🧠 Modelos matemáticos utilizados

- **Modelo Lineal**  
  \( P(t) = a \cdot t + b \)

- **Modelo Exponencial**  
  \( P(t) = a \cdot e^{bt} \)

- **Modelo Logístico**  
  \( P(t) = \frac{L}{1 + e^{-k(t - t_0)}} \)

---

## 📈 Visualizaciones

### 📌 Gráfico ajustado con modelos matemáticos

<img src="images/grafico_modelos_ajustados.png" width="600">

### 📌 Gráfico ilustrativo con valores estimativos

<img src="images/grafico_modelos_ilustrativos.png" width="600">

---

## 🔧 Requisitos para ejecutar los scripts

- Python 3.x
- Bibliotecas:
  - `numpy`
  - `matplotlib`
  - `scipy`
  - `fpdf`

## Instalación rápida:

```
bash
pip install numpy matplotlib scipy fpdf

```

## 📚 Bibliografía

- Instituto Nacional de Estadística y Censos (INDEC). (2022). *Resultados provisionales del Censo Nacional de Población, Hogares y Viviendas*. Recuperado de [https://www.indec.gob.ar](https://www.indec.gob.ar)

- Stewart, J. (2016). *Cálculo de varias variables*. Cengage Learning.

- Larson, R., & Edwards, B. H. (2018). *Cálculo*. Cengage Learning.

- Python Software Foundation. (2023). *Python Language Reference*. Recuperado de [https://www.python.org](https://www.python.org)

- SciPy Developers. (2023). *SciPy Library Documentation*. Recuperado de [https://docs.scipy.org](https://docs.scipy.org)

- Hunter, J. D. (2007). *Matplotlib: A 2D Graphics Environment*. *Computing in Science & Engineering*, 9(3), 90–95. [https://matplotlib.org/](https://matplotlib.org/)

- Harris, C. R., et al. (2020). *Array programming with NumPy*. *Nature*, 585(7825), 357–362. [https://numpy.org/](https://numpy.org/)
