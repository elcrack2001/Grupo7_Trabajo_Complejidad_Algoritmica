![enter image description here](https://www.laureate.net/wp-content/uploads/2019/03/10-UPC-Universidad-Peruana-de-Ciencias-Aplicadas.png)
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
## Pathfinding
Se denomina Pathfinding al trazado del camino más corto entre dos puntos. Este trazado es realizado por algoritmos predefinidos bajo un cierto criterio. Para el curso, se trabajan estos algoritmos para hallar el camino más contro entre dos nodos de un grafo. Algunos algoritmos son: el algoritmo de Dijkstra, BFS, A*, D*, etc. Los algoritmos de búsqueda de rutas son importantes ya que se utilizan en aplicaciones como Google Maps, sistemas de navegación por satélite y paquetes de enrutamiento a través de internet.

![pathfinding](https://en.scratch-wiki.info/w/images/Pathfinding.jpg)

## Complejidad de los Algoritmos
La complejidad algorítmica es una métrica teórica que nos ayuda a describir el comportamiento de un algoritmo en términos de tiempo de ejecución (tiempo que tarda un algoritmo en resolver un problema) y memoria requerida (cantidad de memoria necesaria para procesar las instrucciones que solucionan dicho problema). Esto nos ayuda a comprar entre la efectividad de un algoritmo y otro, y decidir cuál es el más óptimo. A la idea del tiempo de ejecución se le conoce como complejidad temporal, y a la idea de la memoria requerida para resolver el problema se le denomina complejidad espacial. Dichos valores se encuentran en función del tamaño del problema (valor o valores dictados por el número de elementos con los que un algoritmo trabaja), aunque en algunos casos no.

![complejidad](https://jorgeantilefblog.files.wordpress.com/2013/11/orden-de-complejidad2.jpg)


# Estado del Arte

## A - star (A*)
El Algoritmo A * tiene su origen en el año 1968 y fue desarrollado principalmente para aportar elementos a la determinación de rutas de costo mínimo. Este algoritmo es una mejora desarrollada a los postulados del algoritmo Dijsktra que se encarga de encontrar rutas más cortas dentro de un grafo. En esta modificación se toma como punto central la observación búsquedas informadas dentro del grafo que nos permitan tomar decisiones óptimas sobre los caminos que deben tomarse para recorrer de forma eficiente el grafo.
### Cómo funciona el algoritmo A*
Para la aplicación de este algoritmo debemos comprender como se procede a dividir el costo de la ruta. En este caso se divide en dos partes donde g (n) representa el costo de la ruta desde su origen hasta algún nodo n dentro del grafo. También tenemos que h (n) representa el costo estimado de la ruta desde el nodo n al nodo de destino, calculado por una suposición heurística. En él, se logra equilibrar g (n) y h (n) mientras itera el grafo, asegurando así que en cada iteración elija el nodo con el costo total más bajo f (n) = g (n) + h (n).

![a-star_algorithm](https://www.edureka.co/blog/wp-content/uploads/2019/12/Astar_progress_animation.gif)

### Pseudocódigo
![a-star_pseudocode](https://i.stack.imgur.com/8nAs8.png)

## Breadth First Search (BFS)
El algoritmo de búsqueda por amplitud (BFS por sus siglas en inglés) es una manera sistemática de recorrer todos los nodos de un grafo, teniendo como parámetros un nodo de inicio y un nodo de destino. Este enfoque se denomina en "amplitud" porque desde cada vértice V que se visita se busca en forma tan amplia como sea posible, visitando todos los vértices o nodos adyacentes a V. 
### Cómo funciona el algoritmo BFS
La estrategia seria partir de algún vértice U, visitar U y, después, visitar cada uno de los vértices adyacentes a U. Hay que repetir el proceso para cada nodo adyacente a U, siguiendo el orden en que fueron visitados con la característica que si estos, en caso de haber sido visitados, se les asigna una etiqueta de "visitados" para no aumentar el tiempo de búsqueda y contarlos denuevo.

![bfs_algorithm](https://koenig-media.raywenderlich.com/uploads/2017/04/bfs1-1.gif)

## Pseudocódigo
![bfs_pseudocode](http://rosalind.info/media/pseudocode_bfs.png)

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

*3
*9 (Tamaño original)
*100
*1000 

El objetivo de estas pruebas es medir el tiempo de cada algoritmo que 

a) Declaración de 3 algoritmos a usar para alcanzar el objetivo
Para nuestro proyecto emplearemos 3 algoritmos de búsqueda los cuales son: 

- Por fuerza bruta: En este caso el peón buscará todas las posibles soluciones de caminos para llegar a su objetivo sin embargo solo escogerá la primera solución que encuentre para que sea más rápido ya que en un tablero de muchos azulejos puede generar una cantidad muy grande de caminos posibles. 

- Divide y vencerás: Para esto el peón formará rectángulos alrededor suyo limitando su espacio de movimiento en caso tenga paredes cerca, esto es divide y vencerás ya que creará su propio tablero dentro del tablero para concentrarse en resolverlo primero. El backtracking entra cuando el peón busque las posibles salidas que tenga de ese rectángulo para seguir avanzando eligiendo la posición más cercana a él, en caso de que le pusiera otro muro en frente volverá por el camino que ideó originalmente y decidiendo otro camino más cercano. 

- BFS: El peón tomará toda las rutas decidiendo el camino más corto para llegar a su destino, el cual será modificado cada vez que un muro se ponga en frente. Creemos que este será el más efectivo. 

- A*: En este caso, el peón buscará la manera más corta de llegar a su extremo opuesto (destino) siguiento unas métricas heurísticas entre nodos de la matriz para evaluar sus camino elegido. Cabe resaltar, que en este entregable no se contará con las barreras que pueden elegir colocar los jugadores.

b) Así mismo, identificación del espacio de búsqueda
El espacio de búsqueda abarca toda la matriz (tablero) dado que esta se implementa para que esté unida por nodos. Visto de esta manera, los algoritmos de búsqueda de camino más corto recorren los nodos adyacentes dado un nodo de inicio. Es decir, cabe la posibilidad que en el peor de los casos se recorra todo el tablero para poder llegar al destino. Es por ello, que se define al espacio de búsqueda como todo el tablero.

c) Declaracíon de diferentes tamanos de entradas de datos para trabajar
Para la creación de nuestra tabla utilizaremos la fórmula de (2*n)+1, ya que consideraremos las líneas de una tabla normal como espacios dentro de una matriz para colocar las paredes. utilizaremos entonces para las comparaciones los tamaños de: 

- 9x9 (Tamaño original de tablero de quoridor)
- 15*15
- 25*22

No obstante, esto se implementará cuando se habilite la funcionalidad de colocar las paredes.

d) Declaracion de las ḿetricas que se usaran para evaluar la eficienciade los algoritmos a usar. 
Para las métricas, se utilizará la medición de la eficiencia de los algoritmos en base al tiempo y a su complejidad.

# Experimentos
Para los experimentos, se desea medir el tiempo de cada algoritmo descrito (Backtracking + divide y vencerás, BFS, A*) puesto en la misma situación donde se simulará un laberinto para poder comprobar la eficiencia de cada uno. Estos experimentos están basados en los realizados por el canal de youtube de Dane Perry Svendsen. Sin embargo, cabe aclarar que el tiempo de los algoritmos depende del programa que se esté utilizando tanto como el hardware que lo prueba.

## Video de demostración
[![Demo](https://j.gifs.com/q71wBG.gif)](https://www.youtube.com/watch?v=X3x7BlLgS-4&list=LLfFGr-JPbJxUU11j6xl5Cnw&index=1&ab_channel=DanePerrySvendsen)

# Resultados
- BFS:
  - Para la primera matriz, el tiempo de resolución del problema es  10.62555456161499
  - Para la primera matriz, el tiempo de resolución del problema es  17.98764456235452
- A*:
  - Para la primera matriz, el tiempo de resolución del problema oscila en el rango de <0.00262260437011719; 0.00476837158203125> siendo el ganador la ficha número 1.
  - Para la segunda matriz, el tiempo de resolución del problema oscila en el rango de <0.00286102294921875; 0.00452995300292969> siendo el ganador la ficha número 2.
- Divide y vencerás:

# Conclusiones y Recomendaciones
- El tiempo de respuesta de los algoritmos para la resolución de hallar el camino más corto depende de un factor externo el cuál es el hardware en dónde se corren las pruebas. Para poder acercarnos a una evaluación y decisión sobre qué algoritmo es más eficiente, es necesario evaluar su complejidad. Como recomendación, es necesario realizar varias pruebas para poder hallar un rango de intervalos de tiempo que presenta la solución.
