# Grupo7_Trabajo_Complejidad_Algoritmica

<center><b>Complejidad Algorítmica – CC41</b></center> <br>
<center><b>Trabajo Parcial</b></center> <br>
<center><b> Carrera de Ingeniería de Software y Ciencias de la computación </b></center> <br>
<center><b>Sección: CC41 </b></center> 

# Profesor
  Ricardo Eugenio Gonzalez Valenzuela
# Alumnos
 - U201811410 Moscol Suarez, Adrian Gabriel 
 - U201810723 Schmidt Avila, Mark Albert 
 - U20171B251 Molero Caceda, Rodrigo Alonso 

# Introducción
Motivación:  Como grupo de trabajo nos enfocamos en la capacidad de reconocer responsabilidades éticas y profesionales en situaciones de ingeniería y hacer juicios informados, que deben considerar el impacto de las soluciones de ingeniería en contextos globales, económicos, ambientales y sociales. 

Problema: Para este trabajo nos dedicaremos a realizar un juego llamado Quoridor donde el objetivo de cada participante es llegar hasta la base del rival, en cada turno se debe escoger entre colocar dificultades como muros o avanzar.

# Marco Teórico 
Para el presente proyecto utilizaremos 3 algoritmos los cuales compararemos para encontrar el más eficiente. Los problemas pueden tener diferentes soluciones pero siempre existe una que en comparación al resto es la más efectiva muchas veces por su complejidad. La complejidad de un algoritmo nos ayuda a determinar el tiempo de ejecución y la memoria que requiere como parámetros para definir su eficiencia. 

# Estado del Arte
## Depth - first Search (DFS)
En la búsqueda de profundidad, la idea es recorrer lo más profundo posible siempre que sea posible. La búsqueda de profundidad explora las aristas del vértice descubierto más recientemente que todavía tiene aristas sin explorar. Una vez que todas las aristas han sido exploradas, la búsqueda regresa para revisar el resto de aristas. Este proceso continúa hasta que se haya descubierto o todos los vértices que son accesibles desde el vértice original. Si quedan vértices sin descubrir, la búsqueda en profundidad selecciona uno de ellos como nueva fuente y repite la búsqueda desde dicha fuente. El algoritmo repite este proceso hasta que se hayan descubierto todos los vértices.
### Cómo funciona el algoritmo DFS
En la búsqueda de profundidad primeros descubre un vértice durante un escaneo de la lista de adyacencia de un vértice u ya descubierto, registra este evento estableciendo al atributo predecesor v.father a u. El grafo predecesor producido por una búsqueda en profundidad primero debe estar compuesto por varios árboles, porque la búsqueda puede repetirse desde múltiples fuentes. Por lo tanto, se define el subgrafo predecesor de una búsqueda en profundidad.

Gfather = (V, Efather), donde

Efather = {(v.father, v): v ∈ V y v.father ≠ NIL}

El subgrafo predecesor de una búsqueda de profundidad primero forma un bosque de profundidad que comprende varios árboles. Las aristas en E son aristas de árboles. Cada vértice es inicialmente blanco, aparece en gris cuando se descubre en la búsqueda y ennegrecido cuando finaliza, es decir, cuando se ha examinado completamente su lista de adyacencia. Esta técnica garantiza que cada vértice termine exactamente en un árbol de profundidad, de modo que estos árboles estén separados. Además de crear un bosque en profundidad, la búsqueda en profundidad también marca el tiempo de cada vértice. Cada vértice v tiene dos marcas de tiempo: la primera marca v.d registra cuándo se descubre por primera vez y la segunda marca v.f registra cuándo la búsqueda termina de examinar la lista de adyacencia. Estas marcas de tiempo proporcionan información importante sobre la estructura del gráfico y generalmente son útiles para razonar sobre el comportamiento de la búsqueda en profundidad.

### Pseudocódigo
![dfs_pseudocode](https://i.stack.imgur.com/MIlwU.png)

## Backtracking
El Backtracking es una estrategia para encontrar soluciones a problemas que satisfacen restricciones.
Estos problemas consisten en un conjunto (o lista) de variables a la que a cada una se le debe asignar un valor sujeto a las restricciones del problema. La técnica va creando todas las posibles combinaciones de elementos para obtener una solución. Su principal virtud es que en la mayoría de las implementaciones se puede evitar combinaciones, estableciendo funciones de acotación (o poda) reduciendo el tiempo de ejecución. 

### Cómo funciona el algoritmo de Backtracking

Esencialmente, la idea es encontrar la mejor combinación posible en un momento determinado. Durante la búsqueda, si se encuentra una alternativa incorrecta, la búsqueda retrocede hasta el paso anterior y toma la siguiente alternativa. Cuando se han terminado las posibilidades, se vuelve a la elección anterior y se toma la siguiente opción (hijo, si nos referimos a un árbol). Si no hay más alternativas la búsqueda falla. De esta manera, se crea un árbol implícito, en el que cada nodo es un estado de solución (solución parcial en el caso de nodos interiores o solución total en el caso de los nodos hoja).
Normalmente, se suele implementar este tipo de algoritmos como un procedimiento recursivo. Así, en cada llamada al procedimiento se toma una variable y se le asignan todos los valores posibles, llamando a su vez al procedimiento para cada uno de los nuevos estados. De esta forma se ahorra espacio en memoria y tiempo de ejecución.

## Fuerza Bruta
La fuerza bruta, es una técnica trivial pero a menudo usada, que consiste en enumerar sistemáticamente todos los posibles candidatos para la solución de un problema, con el fin de chequear si dicho candidato satisface la solución al mismo.
La búsqueda por fuerza bruta es sencilla de implementar y, siempre que exista, encuentra una solución. Sin embargo, su coste de ejecución es proporcional al número de soluciones candidatas, el cual es exponencialmente proporcional al tamaño del problema. Por el contrario, la búsqueda por fuerza bruta se usa habitualmente cuando el número de soluciones candidatas no es elevado, o bien cuando éste puede reducirse previamente usando algún otro método heurístico.
Es un método utilizado también cuando es más importante una implementación sencilla que una mayor rapidez. Este puede ser el caso en aplicaciones críticas donde cualquier error en el algoritmo puede acarrear serias consecuencias; también es útil como método "base" cuando se desea comparar el desempeño de otros algoritmos metaheurísticos. La búsqueda de fuerza bruta puede ser vista como el método metaheurístico más simple.

### Cómo funciona la Fuerza Bruta
Para poder utilizar la búsqueda por fuerza bruta a un tipo específico de problema, se deben implementar las funciones primero, siguiente, válido, y mostrar. Todas recogerán el parámetro P indicando una instancia en particular del problema:
primero (P): genera la primera solución candidata para P.
siguiente (P, c): genera la siguiente solución candidata para P después de una solución candidata c.
válido (P, c): chequea si una solución candidata c es una solución correcta de P.
mostrar (P, c): informa que la solución c es una solución correcta de P.
La función siguiente debe indicar de alguna forma cuándo no existen más soluciones candidatas para el problema P después de la última. Una forma de realizar esto consiste en devolver un valor "nulo". De esta misma forma, la función primero devolverá un valor "nulo" cuando no exista ninguna solución candidata al problema P.
Usando tales funciones, la búsqueda por fuerza bruta se expresa mediante el siguiente algoritmo:

c <- primero (P)
mientras c != null
si válido (P, c) entonces mostrar (P, c)
c <- siguiente (P, c)
# Metodología
La metodología que utilizaremos para resolver este problema se divide en tres partes:

1. Investigación
2. Desarrollo
3. Testeo

## 1. Investigación

Para iniciar nuestro proyecto nos pusimos a investigar los distintos métodos de búsqueda que existen. Luego de analizar 3 distintos métodos, analizamos su complejidad y eso mismo será lo que compararemos al finalizar el proyecto. Lo que se evaluará será el tiempo en que demoran los peones al llegar en el menor tiempo al otro extremo del tablero con estos 3 métodos y analizar por que son más efectivos unos que otros de acuerdo a los resultados obtenidos. 

## 2. Desarollo
Esta parte la escribiremos a lo largo de nuestro proyecto pero principalmente será la implementación de los códigos para ver la complejidad de estos.

## 3. Testeo
Compararemos los algoritmos de acuerdo a los diferentes tipos de entrada que le entregaremos al tablero. Este será nuestro parámetro de testeo teniendo en cuenta el tamaño del tablero de (2*n)+1. 

Los tamaños de n del tablero para nuestro testeo serán: 

3
9 (Tamaño original)
100
1000 

a) Declaración de 3 algoritmos a usar para alcanzar el objetivo
Para nuestro proyecto emplearemos 3 algoritmos de búsqueda los cuales son: 

- Por fuerza bruta: En este caso el peón buscará todas las posibles soluciones de caminos para llegar a su objetivo sin embargo solo escogerá la primera solución que encuentre para que sea más rápido ya que en un tablero de muchos azulejos puede generar una cantidad muy grande de caminos posibles. 

- Backtracking con divide y vencerás: Para esto el peón formará rectángulos alrededor suyo limitando su espacio de movimiento en caso tenga paredes cerca, esto es divide y vencerás ya que creará su propio tablero dentro del tablero para concentrarse en resolverlo primero. El backtracking entra cuando el peón busque las posibles salidas que tenga de ese rectángulo para seguir avanzando eligiendo la posición más cercana a él, en caso de que le pusiera otro muro en frente volverá por el camino que ideó originalmente y decidiendo otro camino más cercano. 

- Grafos DFS: En grafos, el peón tomará toda las rutas decidiendo el camino más corto para llegar a su destino, el cual será modificado cada vez que un muro se ponga en frente. Creemos que este será el más efectivo. 

b) Ası mismo, identificación del espacio de búsqueda;

c) Declaracíon de diferentes tamanos de entradas de datos para trabajar
Para la creación de nuestra tabla utilizaremos la fórmula de (2*n)+1, ya que consideraremos las líneas de una tabla normal como espacios dentro de una matriz para colocar las paredes. utilizaremos entonces para las comparaciones los tamaños de: 

- 3
- 9 (Tamaño original de tablero de quoridor)
- 100
- 1000 


d) Declaracion de las ḿetricas que se usaran para evaluar la eficienciade los algoritmos a usar. 
Para las métricas, se utilizará la medición de la eficiencia de los algoritmos en base al tiempo y a su complejidad

# Experimentos
# Resultados
# Conclusiones
