# Proyecto3Leng
# DSL_ML: Lenguaje de Dominio Específico para Machine Learning

## Descripción del Proyecto
DSL_ML es un lenguaje de dominio específico diseñado para realizar procesos de Machine Learning, manejo de datos y visualización de resultados. Este proyecto utiliza ANTLR v4 para la construcción de la gramática y Python para la ejecución del lenguaje mediante un intérprete basado en el patrón de diseño Visitor.

### Características principales:
- **Operaciones Aritméticas**: Suma, resta, multiplicación, división, módulo, exponenciación y raíces.
- **Operaciones con Matrices**: Suma, resta, multiplicación, transposición e inversa.
- **Condicionales y Bucles**: Estructuras `if`, `else`, `while` y `for`.
- **Graficado de Datos**: Funciones para graficar utilizando datos de entrada.
- **Manejo de Archivos**: Lectura y escritura de archivos de texto.
- **Operaciones de Machine Learning**:
  - Regresión lineal.
  - Clasificación utilizando un perceptrón multicapa.
  - Agrupamiento (clustering) con K-means.

---

## Instalación

### Requisitos previos
1. Python 3.9 o superior.
2. Instalación de ANTLR v4 y su runtime para Python:
   ```bash
   pip install antlr4-python3-runtime
