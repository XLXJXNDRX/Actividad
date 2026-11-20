    **Integrantes:**
*Alejandro Jose Reverol Ramos 0192453
**Asignatura:** Análisis de Algoritmos - Grupo B  
---

## 1. Robots que deciden hacia dónde girar

Para saber si una ruta está obstruida por una pared, se modela la pared como un segmento de recta y se verifica si el segmento de la trayectoria del robot lo interseca usando pruebas de orientación.

Dada la fórmula del determinante:

$$\det = (x_b - x_a)(y_c - y_a) - (y_b - y_a)(x_c - x_a)$$

* **$\det > 0$:** Giro a la **izquierda** (sentido antihorario).
* **$\det < 0$:** Giro a la **derecha** (sentido horario).
* **$\det = 0$:** Puntos **colineales** (el robot sigue recto).

| Caso | Puntos $(a, b, c)$ | Cálculo del determinante | Resultado | Dirección de giro |
| :--- | :--- | :--- | :---: | :--- |
| **Caso 1** | $a(1, 1)$, $b(4, 3)$, $c(5, 1)$ | $(4 - 1)(1 - 1) - (3 - 1)(5 - 1) = (3)(0) - (2)(4)$ | **$-8$** | **Derecha** (horario) |
| **Caso 2** | $a(2, 1)$, $b(4, 2)$, $c(3, 5)$ | $(4 - 2)(5 - 1) - (2 - 1)(3 - 2) = (2)(4) - (1)(1)$ | **$+7$** | **Izquierda** (antihorario) |
| **Caso 3** | $a(1, 2)$, $b(3, 4)$, $c(5, 6)$ | $(3 - 1)(6 - 2) - (4 - 2)(5 - 1) = (2)(4) - (2)(4)$ | **$0$** | **Colineal** (sigue recto) |
| **Caso 4** | $a(0, 3)$, $b(4, 3)$, $c(2, 5)$ | $(4 - 0)(5 - 3) - (3 - 3)(2 - 0) = (4)(2) - (0)(2)$ | **$+8$** | **Izquierda** (antihorario) |

### Gráficas en GeoGebra (Punto 1)

* **Caso 1:**
  ![Punto 1 - Caso 1](imagenes/grafica 1.png)
* **Caso 2:**
  ![Punto 1 - Caso 2](imagenes/grafica 1.png)
* **Caso 3:**
  ![Punto 1 - Caso 3](imagenes/grafica 2.png)
* **Caso 4:**
  ![Punto 1 - Caso 4](imagenes/grafica 2.png)

---

## 2. Verificación de rutas en autos autónomos

### a) Representación en el plano cartesiano

* **Caso 1:**
  ![Punto 2 - Caso 1](imagenes/grafica 1.png)
* **Caso 2:**
  ![Punto 2 - Caso 2](imagenes/grafica 2.png)
* **Caso 3:**
  ![Punto 2 - Caso 3](imagenes/grafica 1.png)

### b) Cálculo de las 4 orientaciones por caso
Para verificar si el segmento $ab$ interseca al segmento $cd$, calculamos las 4 orientaciones:
1. $o_1 = \text{orientación}(a, b, c)$
2. $o_2 = \text{orientación}(a, b, d)$
3. $o_3 = \text{orientación}(c, d, a)$
4. $o_4 = \text{orientación}(c, d, b)$

* **Caso 1:** $a(1, 1), b(5, 4)$ y $c(1, 4), d(5, 1)$
  * $o_1(a,b,c) = (4)(3) - (3)(0) = \mathbf{+12}$ (Izquierda)
  * $o_2(a,b,d) = (4)(0) - (3)(4) = \mathbf{-12}$ (Derecha)
  * $o_3(c,d,a) = (4)(-3) - (-3)(0) = \mathbf{-12}$ (Derecha)
  * $o_4(c,d,b) = (4)(0) - (-3)(4) = \mathbf{+12}$ (Izquierda)
  * **Conclusión:** **Sí hay intersección** ($o_1 \neq o_2$ y $o_3 \neq o_4$; los segmentos se cruzan en el punto $(3, 2.5)$).

* **Caso 2:** $a(1, 3), b(6, 3)$ y $c(4, 3), d(8, 3)$
  * $o_1(a,b,c) = (5)(0) - (0)(3) = \mathbf{0}$ (Colineal)
  * $o_2(a,b,d) = (5)(0) - (0)(7) = \mathbf{0}$ (Colineal)
  * $o_3(c,d,a) = (4)(0) - (0)(-3) = \mathbf{0}$ (Colineal)
  * $o_4(c,d,b) = (4)(0) - (0)(-2) = \mathbf{0}$ (Colineal)
  * **Conclusión:** **Sí hay intersección** (caso especial colineal con superposición en el intervalo $x \in [4, 6]$).

* **Caso 3:** $a(1, 1), b(3, 3)$ y $c(4, 1), d(7, 2)$
  * $o_1(a,b,c) = (2)(0) - (2)(3) = \mathbf{-6}$ (Derecha)
  * $o_2(a,b,d) = (2)(1) - (2)(6) = \mathbf{-10}$ (Derecha)
  * $o_3(c,d,a) = (3)(0) - (1)(-3) = \mathbf{+3}$ (Izquierda)
  * $o_4(c,d,b) = (3)(2) - (1)(-1) = \mathbf{+7}$ (Izquierda)
  * **Conclusión:** **No hay intersección** ($o_1 = o_2$ y $o_3 = o_4$).

### c) Función en Python (4 parámetros)

```python
def orientacion(p, q, r):
    val = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    if round(val, 9) == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def en_segmento(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def interseccion(a, b, c, d):
    o1 = orientacion(a, b, c)
    o2 = orientacion(a, b, d)
    o3 = orientacion(c, d, a)
    o4 = orientacion(c, d, b)

    if o1 != o2 and o3 != o4:
        return True

    # Casos colineales
    if o1 == 0 and en_segmento(a, c, b):
        return True
    if o2 == 0 and en_segmento(a, d, b):
        return True
    if o3 == 0 and en_segmento(c, a, d):
        return True
    if o4 == 0 and en_segmento(c, b, d):
        return True

    return False
```

### Complejidad $O(1)$ de la intersección entre dos segmentos
La función `interseccion(a, b, c, d)` tiene complejidad temporal **$O(1)$** (tiempo constante) porque siempre ejecuta un número fijo y acotado de operaciones aritméticas y comparaciones (exactamente 4 determinantes y como máximo 4 verificaciones de rango), independientemente de la longitud de los segmentos o de la magnitud de sus coordenadas.

---

## 3. Empresa de acueducto e intersección de tuberías

El algoritmo de **fuerza bruta** toma cada tubería $i$ (desde $1$ hasta $n-1$) y la compara contra todas las tuberías posteriores $j$ (desde $i+1$ hasta $n$) para evitar repetir pares o comparar una tubería consigo misma.

El número total de pares comparados es:

$$
\binom{n}{2} = \frac{n(n - 1)}{2} = \frac{n^2 - n}{2}
$$

Como cada verificación individual entre dos segmentos cuesta $O(1)$, el tiempo total es proporcional a $\frac{1}{2}n^2 - \frac{1}{2}n$. Al descartar constantes multiplicativas y términos de menor grado, la complejidad asintótica resulta **$O(n^2)$**.

---

## 4. Análisis de iteraciones y llamadas de función

### a) Tabla de iteraciones para $n = 4$ y $n = 6$

| Iteración externa ($i$) | Comparaciones internas ($j$) para $n = 4$ | Nº pares ($n=4$) | Comparaciones internas ($j$) para $n = 6$ | Nº pares ($n=6$) |
| :---: | :--- | :---: | :--- | :---: |
| $i = 1$ | $j \in \{2, 3, 4\}$ | $3$ | $j \in \{2, 3, 4, 5, 6\}$ | $5$ |
| $i = 2$ | $j \in \{3, 4\}$ | $2$ | $j \in \{3, 4, 5, 6\}$ | $4$ |
| $i = 3$ | $j \in \{4\}$ | $1$ | $j \in \{4, 5, 6\}$ | $3$ |
| $i = 4$ | — | — | $j \in \{5, 6\}$ | $2$ |
| $i = 5$ | — | — | $j \in \{6\}$ | $1$ |
| **Total** | **Pares evaluados** | **$6$** | **Pares evaluados** | **$15$** |

### b) Expresión exacta de llamadas
* **Llamadas a `interseccion(a, b, c, d)` (pares de segmentos):**

$$
\text{Llamadas}_{\text{inter}} = \sum_{i=1}^{n-1} (n - i) = \frac{n(n - 1)}{2}
$$

* **Llamadas a determinantes (`orientacion` — 4 por cada llamada a `interseccion`):**

$$
\text{Llamadas}_{\text{det}} = 4 \cdot \frac{n(n - 1)}{2} = 2n(n - 1) = 2n^2 - 2n
$$

### c) Como función matemática
* Función de llamadas a `interseccion`: $f(n) = \frac{1}{2}n^2 - \frac{1}{2}n$
* Función de evaluaciones de determinantes: $g(n) = 2n^2 - 2n$

### d) Desarrollo y simplificación de la sumatoria de constantes
Si denotamos como $c$ el costo constante de cada comprobación (por ejemplo, $c = 4$ determinantes o $c = 1$ llamada a `interseccion`):

$$
T(n) = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} c = c \sum_{i=1}^{n-1} (n - i) = c \left[ (n-1) + (n-2) + \dots + 1 \right] = c \cdot \frac{n(n - 1)}{2} = \frac{c}{2}n^2 - \frac{c}{2}n
$$

### e) Complejidad temporal
Al eliminar las constantes y conservar el término dominante de mayor crecimiento:

$$
T(n) \in O(n^2)
$$

### f) Comprobaciones para $n = 50$, $500$ y $20.000$ tuberías

| Número de tuberías ($n$) | Llamadas a `interseccion(a,b,c,d)` $\frac{n(n-1)}{2}$ | Evaluaciones de determinantes $2n(n-1)$ |
| :---: | :---: | :---: |
| **$50$** | $1.225$ | $4.900$ |
| **$500$** | $124.750$ | $499.000$ |
| **$20.000$** | $199.990.000$ | $799.960.000$ |

---

## 5. Comparación de implementaciones

Conviene utilizar el **Algoritmo B**, ya que tiene un crecimiento cuadrático ($O(n^2)$) frente al cúbico ($O(n^3)$) del Algoritmo A y evita hacer comparaciones innecesarias. A medida que aumenta el tamaño de la entrada $n$, la diferencia de rendimiento se vuelve mucho más notoria, haciendo que el Algoritmo A sea $n$ veces más lento.

| Tamaño de entrada ($n$) | $T_A(n) = n^3$ | $T_B(n) = n^2$ | Razón $\frac{T_A(n)}{T_B(n)} = \frac{n^3}{n^2} = n$ | Complejidad Big O |
| :---: | :---: | :---: | :---: | :--- |
| **$20$** | $8.000$ | $400$ | **$20$** | Algoritmo A: $O(n^3)$ |
| **$200$** | $8.000.000$ | $40.000$ | **$200$** | Algoritmo B: $O(n^2)$ |
| **$2.000$** | $8.000.000.000$ | $4.000.000$ | **$2.000$** | **Más eficiente: Algoritmo B** |
