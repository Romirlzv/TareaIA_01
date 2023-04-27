# TareaIA_01
Tarea1 Inteligencia Artificial Romina Zurita Vidal

El siguiente programa resulve los algoritmos de busqueda en profundidad,
costo uniforme, greedy y A*

Para utilizarlo se debe tener el archivo.txt en la misma carpeta que el 
programa.

Para ejecutarlo solo se debe crear un objeto de la clase Grafo, con los argumentos
que corresponden a la lectura del archivo.txt.
mi_grafo = Grafo(inicio, meta, heuristica_nodo, conexiones_costo)

Para realizar los algoritmos solo se deben llamar como funciones del objeto, y estas
imprimiran los resultados
mi_grafo.B_profundidad(nodos_expandidos)
mi_grafo.B_costo_uniforme(nodos_expandidos)
mi_grafo.B_greedy(nodos_expandidos, heuristica_nodo)
mi_grafo.B_A_estrella(nodos_expandidos, heuristica_nodo)

Si se quiere realizar una modificacion de valores solo se debe modificar el archivo.txt
