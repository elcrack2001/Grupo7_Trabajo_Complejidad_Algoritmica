![enter image description here](https://www.laureate.net/wp-content/uploads/2019/03/10-UPC-Universidad-Peruana-de-Ciencias-Aplicadas.png)
# Grupo7_Trabajo_Complejidad_Algoritmica

<center><b>Complejidad Algorítmica – CC41</b></center> <br>
<center><b>Trabajo Final</b></center> <br>
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

Este proyecto consistira en una investigacion para comparar tres algoritmos y ver cual es mas efectivo. Los 3 algoritmos que seran estudiados son de bfs, divide y vencera y A star. Ademas, incluiremos una funcion que hara que la computadora piense cuando colocar paredes para dificultarle el movimiento a sus adversarios y evitar que lleguen al objetivo. Ese algoritmo de paredes tambien colaborara en la eficiencia de nuestros algoritmos y sera estudiado.

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

### A* Time Complexity
Dependiendo de la heurística y el contexto de los grafos, es entendible que en el peor de los casos la complejidad del algoritmo sea O(V + E) donde V son los vértices y E representan las aristas habiendo recorrido todo el grafo. Sin embargo, ¿qué pasaría si el grafo resulta ser infinito? medir con estas métricas la complejidad carece de sentido. Es por ello, que se utiliza otro enfoque en donde solamente se requiere evaluar el factor de conexión entre nodos (b) y examinar cada vértice en profundidad menor o igual al vértice d (destino. Si la meta es detenerse cuando se llega al vértice de destino, se terminará obteniendo una complejidad de O(b^d) 

### Pseudocódigo
![a-star_pseudocode](https://i.stack.imgur.com/8nAs8.png)

## Breadth First Search (BFS)
El algoritmo de búsqueda por amplitud (BFS por sus siglas en inglés) es una manera sistemática de recorrer todos los nodos de un grafo, teniendo como parámetros un nodo de inicio y un nodo de destino. Este enfoque se denomina en "amplitud" porque desde cada vértice V que se visita se busca en forma tan amplia como sea posible, visitando todos los vértices o nodos adyacentes a V. 

### Cómo funciona el algoritmo BFS
La estrategia seria partir de algún vértice U, visitar U y, después, visitar cada uno de los vértices adyacentes a U. Hay que repetir el proceso para cada nodo adyacente a U, siguiendo el orden en que fueron visitados con la característica que si estos, en caso de haber sido visitados, se les asigna una etiqueta de "visitados" para no aumentar el tiempo de búsqueda y contarlos denuevo.

![bfs_algorithm](https://koenig-media.raywenderlich.com/uploads/2017/04/bfs1-1.gif)

## Pseudocódigo
![bfs_pseudocode](http://rosalind.info/media/pseudocode_bfs.png)

## Divide y venceras
El Divide y venceras es una estrategia de la programacion que busca dividir el problema en fragmentos mas pequenos los cuales pueden ser analizados de manera mas detallada y sencilla. En el caso de nuestro algoritmo lo utilizaremos para dividir el tablero en rectangulos mas pequenos que el peon pueda analizar detalladamente y tomar la decision de desplazarse hacia otra posicion, acercandose de esta manera mas a su destino final.

### Cómo funciona el algoritmo de Divide y venceras

En este caso lo que implementaremos seran rectangulos dentro del tablero que el peon analizara para lograr encontrar salidas. Los limites de dicho rectangulo sera definidos por las paredes que este alrededor de este y limiten su movilidad, principalmente si estan al frente ya que evitan que tome el camino mas sencillo que es simplemente avanzar. Una vez que este rectangulo sea definido y resuelto y el peon logre salir volver a analizar su nueva posicion para generar otro y de esta manera lograr llegar al otro extremo. 
Se generan listas de psoibilidades de hacia donde puede avanzar el peon, de estas posibilidades se escoge la menor en comparacion al resto haciendo entender al peon que si va hacia esa direccion llegara mas rapido.

## Algoritmo Maxn
Para este algoritmo de divide y venceras se utilizara el Maxn. La logica que seguira sera que el peon del turno correspondiente analizara a un rival al que su objetivo sera dificultar la movilidad. Primero le tratara de poner una pared en frente siempre, para que este tenga que moverse a un lado, sino es posible por diferentes motivos procedera a intentar hacerlo a los lados. Si el peon no puede colocar una pared porque ya existen o porque lo encierra, decidirá moverse en su lugar. 

Pseudo-código

    int MaxN(estado) {
          if(estado_final(estado)) {
               return evaluacion_heurística(estado);
           }
           max=-infinito;
           while exist movimiento_posible(estado) {
               val=-MaxN(mover(mov, estado));
               if (val>max) {
                   max=val;
               }
           }
           return(max);
       }

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
La metodología que utilizaremos para resolver este problema se divide en cuatro partes:

1. Investigación
2. Desarrollo
3. Testeo
4. Implementación

## 1. Investigación

Para iniciar nuestro proyecto nos pusimos a investigar los distintos métodos de búsqueda que existen. Luego de analizar 3 distintos métodos, analizamos su complejidad y eso mismo será lo que compararemos al finalizar el proyecto. Lo que se evaluará será el tiempo en que demoran los peones al llegar en el menor tiempo al otro extremo del tablero con estos 3 métodos y analizar por que son más efectivos unos que otros de acuerdo a los resultados obtenidos. 

## 2. Desarollo
Mientras se realizo el desarrollo de los algoritmos analizamos previamente la complejidad de estos para definir a simple vista cual aparenta ser el mas efectivo. Nuestra opcion mas certera seria el algoritmo de A* con una complejidad de O(E) siendo E el numero total de aristas. Este algoritmo utiliza grafos para encontrar la mejor opcion a donde el peon se va a desplazar. El segundo puesto en cuanto a complejidad seria para el algoritmo de divide y venceras alcanzando una complejidad de O(n^2) en la implementacion de su algoritmo de busqueda de rutas mas cortas. El ultimo puesto de complejidad se lo llevo el algoritmo de BFS siendo este el menos eficiente de los 3. 

## 3. Testeo
Luego de la complejidad se realizo un testeo para poder analizar la potencia de los 3 algoritmos. Compararemos los algoritmos de acuerdo a los diferentes tipos de entrada que le entregaremos al tablero. Este será nuestro parámetro de testeo teniendo en cuenta el tamaño del tablero y la potencia que cada algoritmo tiene. 

Los tamaños de n del tablero para nuestro testeo serán: 

Para el de fuerza bruta: 
- Matriz de 3x3 con obstaculos
- Matriz de 9x9 con obstaculos

Para el de Divide y venceras:
- Matriz de 9x9 vacia
- Matriz de 25x25 vacia
- Matriz de 9x9 con obstaculos
- Matriz de 101x101

Para el de A*:
- Matriz de 9x9 con obstaculos
- Matriz de 15*15 con obstaculos

El objetivo de estas pruebas es medir el tiempo de cada algoritmo que 

a) Declaración de 3 algoritmos a usar para alcanzar el objetivo
Para nuestro proyecto emplearemos 3 algoritmos de búsqueda los cuales son: 

- Divide y vencerás: Para esto el peón formará rectángulos alrededor suyo limitando su espacio de movimiento en caso tenga paredes cerca, esto es divide y vencerás ya que creará su propio tablero dentro del tablero para concentrarse en resolverlo primero. El backtracking entra cuando el peón busque las posibles salidas que tenga de ese rectángulo para seguir avanzando eligiendo la posición más cercana a él, en caso de que le pusiera otro muro en frente volverá por el camino que ideó originalmente y decidiendo otro camino más cercano. 

- BFS: El peón tomará toda las rutas decidiendo el camino más corto para llegar a su destino, el cual será modificado cada vez que un muro se ponga en frente. Creemos que este será el más efectivo. 

- A*: En este caso, el peón buscará la manera más corta de llegar a su extremo opuesto (destino) siguiento unas métricas heurísticas entre nodos de la matriz para evaluar sus camino elegido. Cabe resaltar, que en este entregable no se contará con las barreras que pueden elegir colocar los jugadores.

b) Así mismo, identificación del espacio de búsqueda
El espacio de búsqueda abarca toda la matriz (tablero) dado que esta se implementa para que esté unida por nodos. Visto de esta manera, los algoritmos de búsqueda de camino más corto recorren los nodos adyacentes dado un nodo de inicio. Es decir, cabe la posibilidad que en el peor de los casos se recorra todo el tablero para poder llegar al destino. Es por ello, que se define al espacio de búsqueda como todo el tablero.

c) Declaracíon de diferentes tamanos de entradas de datos para trabajar
Para la creación de nuestra tabla utilizaremos la fórmula de (2*n)+1, ya que consideraremos las líneas de una tabla normal como espacios dentro de una matriz para colocar las paredes. utilizaremos entonces para las comparaciones los tamaños de: 

- 9x9 (Tamaño original de tablero de quoridor)
- 15 x 15
- 25 x 22

No obstante, esto se implementará cuando se habilite la funcionalidad de colocar las paredes.

d) Declaracion de las ḿetricas que se usaran para evaluar la eficienciade los algoritmos a usar. 
Para las métricas, se utilizará la medición de la eficiencia de los algoritmos en base al tiempo y a su complejidad.

# Experimentos
Para los experimentos, se desea medir el tiempo de cada algoritmo descrito (Backtracking + divide y vencerás, BFS, A*) puesto en la misma situación donde se simulará un laberinto para poder comprobar la eficiencia de cada uno. Estos experimentos están basados en los realizados por el canal de youtube de Dane Perry Svendsen. Sin embargo, cabe aclarar que el tiempo de los algoritmos depende del programa que se esté utilizando tanto como el hardware que lo prueba.

## Video de demostración
[![Demo](https://j.gifs.com/q71wBG.gif)](https://www.youtube.com/watch?v=X3x7BlLgS-4&list=LLfFGr-JPbJxUU11j6xl5Cnw&index=1&ab_channel=DanePerrySvendsen)

# Resultados
- BFS:
  - Para la primera matriz, el tiempo de resolución del problema es  0.07239842414855957 segundos
  - Para la segunda matriz, el tiempo de resolución del problema es  5.24133825302124 segundos
- A*:
  - Para la primera matriz, el tiempo de resolución del problema oscila en el rango de <0.00262260437011719; 0.00476837158203125> segundos siendo el ganador la ficha número 1.
  - Para la segunda matriz, el tiempo de resolución del problema oscila en el rango de <0.00286102294921875; 0.00452995300292969> segundos siendo el ganador la ficha número 2.
- Divide y vencerás:
  - Para la primera matriz 9x9 vacia, el tiempo de resolucion del problema es de:  1.0542097091674805 segundos
  - El tiempo del tablero vacio 25x25 es:  6.013184070587158 segundos
  - El tiempo del tablero con laberinto 9x9 es:  1.416558027267456 segundos
  - El tiempo del tablero vacio 101x101 es:  111.29700016975403 segundos

## 4. Implementación

### Paredes del Quoridor
Como se mencionó previamente, la meta de un jugador es llegar al extremo opuesto de donde empezó para poder obtener la victoria. Sin embargo, su camino puede ser bloqueado por otros jugadores obstruyendo su paso con paredes. Estos bloques de paredes están ligados al tablero y constan de unos 20. Se reparten equitativamente entre los jugadores: 10 bloques para cada jugador o 5 bloques para cada jugador si el juego consta de 2 o 4 jugadores, respectivamente. En cada turno, los jugadores pueden optar por dos opciones: mover su ficha y avanzar un casillero o colocar una pared siempre y cuando este cuente con bloques para colocar. No obstante, está prohibido encerrar a un jugador con los bloques.

### Código de funcionalidad del bloqueo

    def ponerpared(self,tablero,listaAD):
        posicion = self.buscarPeon(listaAD)#busco la posicion del adversario
        #print("la posicion es ",posicion)
        posicion[0]=posicion[0]+1
        #print("la posicion actualizada ess ",posicion)
        #print(tablero)
        if self.NParedes==0:
          return self.obtenerruta(tablero,listaAD)
        #en el siguiente if estamos colocando una pared horizontal
        if tablero[posicion[0]][posicion[1]]==0:
          centinela=self.ejecutarpared(tablero,posicion,0,1,0,1,0,2,0,0,1,2)#lado derecho horizontal
          if centinela == False:
            centinela=self.ejecutarpared(tablero,posicion,0,1,0,-1,0,-2,0,0,-1,-2)#lado izquierdo horizontal
            if centinela==False:
              return self.obtenerruta(tablero,listaAD)#no se pudo me muev
        else:
          #ahora vamos a intentar colocar una pared vertical
          posicion[0] = posicion[0] -1
          posicion[1] = posicion[1] + 1 # como intento para poner una pared del lado derecho
          if tablero[posicion[0]][posicion[1]]==0:
            centinela=self.ejecutarpared(tablero,posicion,0,1,1,0,2,0,1,2,0,0)#lado derecho vertical
            if centinela == False:
              centinela=self.ejecutarpared(tablero,posicion,0,1,-1,0,-2,0,-1,-2,0,0)#lado izquierda vertical
              if centinela==False:
                return self.obtenerruta(tablero,listaAD)#no se pudo me muev
          else:
            posicion[1] = posicion[1] - 2
            if tablero[posicion[0]][posicion[1]]==0:
              centinela=self.ejecutarpared(tablero,posicion,0,1,1,0,2,0,1,2,0,0)#lado derecho vertical
              if centinela == False:
                centinela=self.ejecutarpared(tablero,posicion,0,1,-1,0,-2,0,-1,-2,0,0)#lado izquierda vertical
                if centinela==False:
                  return self.obtenerruta(tablero,listaAD)#no se pudo me mue
        self.NParedes=self.NParedes-1
        return [self.getPX(),self.getPY()]

En la siguiente imagen se puede apreciar en pleno juego, cómo los peones tienen los caminos bloqueados y para ello deberán tomar diferentes rutas con el objetivo de llegar a la meta antes que los contrincantes

![game](/functional-game.jpeg)

# Conclusiones y Recomendaciones
Conclusiones y Recomendaciones | Entregable
------------ | -------------
El tiempo de respuesta de los algoritmos para la resolución de hallar el camino más corto depende de un factor externo el cuál es el hardware en dónde se corren las pruebas. Para poder acercarnos a una evaluación y decisión sobre qué algoritmo es más eficiente, es necesario evaluar su complejidad. Como recomendación, es necesario realizar varias pruebas para poder hallar un rango de intervalos de tiempo que presenta la solución. Sin embargo, se vieron resultados muy notorios en la comparacion de los 3 algoritmos ante la prueba de la matriz 9x9 con obstaculos, siendo de estas 3 el algoritmo A* como ganador con un rango de tiempo de <0.00262260437011719; 0.00476837158203125> segundos, luego le sigue el algoritmo de divide y venceras con un tiempo de 1.0542097091674805 segundos y finalmente el de BFS, muy por detras de los otros 2, con un tiempo total de 5.24133825302124 segundos. Luego de haber analizado la complejidad de estos 3 algoritmos se podia decir cual era el mas efectivo pero al ponerlos en prueba es donde realmente se nota la diferencia y la eficiencia y superioridad que tiene uno ante otro como seria el caso del A* contra el de BFS. | Trabajo Parcial
Según vemos ahora con la implementación de las paredes, en tiempo que toma el BFS en realizar todo el proceso según el tamaño de la tabla es: (tablero de 9 x 9 => 559.112548828125 segundos
tablero de 15 x 15=> 1332.042932510376 segundos
tablero de 25 x 25=> 3522.0999717712402 segundos
tablero de 50 x 50=> 13749.105215072632 segundos
tablero de 75 x 75=> 31358.9985370636 segundos
tablero de 100 x 100 => 55145.38264274597 segundos) No obstante, como el código fue ejecutado en la herramienta de Google Collab, el tamaño del tiempo varía según variables externas como la memoria RAM otorgada por la herramienta y el procesador. | Hito 1 - TF
