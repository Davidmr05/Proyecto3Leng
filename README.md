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
1. **Python**: Asegúrate de tener instalado Python 3.9 o superior.
2. **ANTLR v4**: Descarga ANTLR desde su [sitio oficial](https://www.antlr.org/) y configúralo en tu sistema.
3. **Bibliotecas Python**:
   Instala las siguientes bibliotecas necesarias:
   ```bash
   pip install antlr4-python3-runtime numpy matplotlib scikit-learn




python3 -m venv venv

source venv/bin/activate

pip install antlr4-python3-runtime numpy matplotlib scikit-learn

antlr4 -Dlanguage=Python3 -visitor DSL_ML.g4

python interpreter.py mi_script.dsl



PRUEBAS DE ENTRADAS PARA IR VIENDO QUE FALTA Y QUE ESTA QUEDANDO MAL PARA NO HACER TODO AL TIEMPO SI NO IR IMPLEMENTANDOM POCO A POCO LO QUE NOS PIDE EL PROYECTO: 

El proyecto nos pide lo siguiente: 

Basándose en Python, el lenguaje de programación deberá ser capaz de:

• Hacer operaciones aritméticas: suma, resta, multiplicación, 
división, modulo, calculo de raíces de la forma x^y, operaciones 
trigonométricas, etc.

• Hacer operaciones de matrices: suma, resta, multiplicación, Inversa, 
transpuesta

• Realizar las operaciones de condicionales y ciclos for y/o While

• Realizar graficas de datos.

• Manejar archivos, lectura y escritura de archivos de texto.

• Crear funciones para hacer regresión lineal.

• Crear un clasificador usando un percepton multicapa

• Crear algoritmos que puedan hacer agrupamiento

LA IDEA ES QUE POCO A POCO VAYAN PROBANDO CADA ENTRADA DE ESTAS: 

Prueba 1: Declaración de Variables y Operaciones Aritméticas

// Declaración de variables y operaciones aritméticas
var x = 10;
var y = 5;
var suma = x + y;
var resta = x - y;
var multiplicacion = x * y;
var division = x / y;
var modulo = x % y;
print("Suma:", suma);
print("Resta:", resta);
print("Multiplicación:", multiplicacion);
print("División:", division);
print("Módulo:", modulo);

Prueba 2: Potencias y Funciones Matemáticas

// Operaciones con potencias y funciones matemáticas
var base = 2;
var exponente = 3;
var potencia = base ^ exponente;
var raiz = sqrt(16);
var seno = sin(3.14); // Aproximación de pi
var coseno = cos(3.14); // Aproximación de pi
print("Potencia:", potencia);
print("Raíz cuadrada:", raiz);
print("Seno:", seno);
print("Coseno:", coseno);

Prueba 3: Condicionales

// Prueba de condicionales
var x = 10;
var y = 5;

if (x > y) then {
    print("x es mayor que y");
} else {
    print("x no es mayor que y");
}

if (x == 10) then {
    print("x es igual a 10");
} else {
    print("x no es igual a 10");
}

Prueba 4: Bucles

// Prueba de bucles
for (i in 1..5) {
    var cuadrado = i ^ 2;
    print("i^2:", cuadrado);
}

Prueba 5: Manejo de Archivos

// Prueba de manejo de archivos
writeFile("output.txt", "Hola, este es un archivo de prueba.");
var contenido = readFile("output.txt");
print("Contenido del archivo:", contenido);

Prueba 6: Graficado

// Prueba de graficado
plot([1, 2, 3, 4], [10, 20, 30, 40]);

Prueba 7: Operaciones con Matrices

// Prueba de operaciones con matrices
var A = [[1, 2], [3, 4]];
var B = [[5, 6], [7, 8]];
var C = A + B;
var D = transpose(A);
print("Matriz C:", C);
print("Matriz transpuesta D:", D);



