
# Definicion clase grafo, indicando: inicio, meta, cada nodo asociado con su heuristica,
# cada nodo con sus conexiones asociadas y el costo de estas y cada nodo con su cantidad
# de veces que se ha expandido
class Grafo:
    def __init__(self, inicio, meta, heuristicas, conexiones_costo):
        self.inicio = inicio
        self.meta = meta
        self.heuristicas = heuristicas
        self.conexiones_costo = conexiones_costo

    # Algoritmo búsqueda en profundidad

    def B_profundidad(self, nodos_expandidos):
        self.nodos_expandidos = nodos_expandidos

        for key in nodos_expandidos:
            nodos_expandidos[key] = 0
        # Definicion de variables
        pila = []
        pila_aux = []
        nodos_visitados = set()
        costo_camino = 0
        exp_totales = 0
        flag = 1

        # Pila tendrá el nodod actual, con el camino asociado
        pila.append((inicio, [inicio], [costo_camino]))

        # Mientras la pila asociada tenga elementos
        while len(pila) > 0:

            # Se almacenara el nodo actual, la lista camino y el costo del camino
            (nodo_actual, camino, costo_camino) = pila.pop()

            # Se irá almacenando el numero de veces que se expande cada nodo en el
            # diccionario nodos_expandidos
            if nodo_actual != camino[0]:
                indice_nodo_actual = camino.index(nodo_actual)
                cantidad_expansion = nodos_expandidos[camino[indice_nodo_actual - 1]]
                nodos_expandidos[camino[indice_nodo_actual - 1]
                                 ] = cantidad_expansion + 1

            # Si el nodo actual no ha sido visitado
            if nodo_actual not in nodos_visitados:
                nodos_visitados.add(nodo_actual)

                # Si el nodo actual es igual a la meta, se detiene el algoritmo, indicando
                # camino encontrado, costo del camino, numero de veces que se expande y total
                # de expansiones
                if nodo_actual == meta:
                    print("-------Algoritmo Búsqueda en Profundidad-------")
                    print("Camino encontrado: ")
                    for elem in camino:
                        print(elem, end=" ")

                    costo_total = 0

                    print("\nCosto total: ")
                    for elemento in costo_camino:
                        costo_total += elemento
                        print(elemento, end=" ")
                    print(f" = {costo_total}")

                    print("Expansiones de nodos: ")
                    for key in nodos_expandidos:
                        print(f"{key} : {nodos_expandidos[key]}")

                    for key in nodos_expandidos:
                        valor = nodos_expandidos[key]
                        exp_totales += valor
                    print(f"Total de Expansiones de nodos:\n{exp_totales}")
                    flag = 0
                    break

                # Se irá almacenando en la pila los nodos destinos de cada nodo junto con su
                # costo asociado
                for nodo_destino, costo in conexiones_costo[nodo_actual]:
                    pila_aux.append(
                        (nodo_destino, camino + [nodo_destino], costo_camino + [int(costo)]))

                # Se ocupa una pila axuliar para ir visitando los nodos por orden alfabetico
                while len(pila_aux) > 0:
                    pila.append(pila_aux.pop())

        # Indica que no se ha encontrado un camino
        if flag:
            print("-------Algoritmo Búsqueda en Profundidad-------")
            print("Camino encontrado:\nNo se ha encontrado un camino")
            print("Expansiones de nodos: ")
            for key in nodos_expandidos:
                print(f"{key} : {nodos_expandidos[key]}")
            for key in nodos_expandidos:
                valor = nodos_expandidos[key]
                exp_totales += valor
            print(f"Total de Expansiones de nodos:\n{exp_totales}")

    def B_costo_uniforme(self, nodos_expandidos):

        # Se inicializa en 0 la cantidad de veces que se han expandido los nodos
        self.nodos_expandidos = nodos_expandidos
        for key in nodos_expandidos:
            nodos_expandidos[key] = 0

        # Lista que almacena los nodos que se van a visitar
        # Lista que almacena los nodos visitados,
        nodos_visitados = []
        nodos_por_visitar = []
        nodos_por_visitar.append((inicio, [inicio], 0))
        exp_totales = 0
        flag = 1

        while len(nodos_por_visitar) > 0:

            # Se escoge el camino con menor costo de la lista de los nodos por visitar
            nodo_costo_minimo = nodos_por_visitar[0]
            for nodo in nodos_por_visitar:
                if nodo[2] < nodo_costo_minimo[2]:
                    nodo_costo_minimo = nodo
            nodo_actual, camino, costo = nodo_costo_minimo
            nodos_por_visitar.remove((nodo_actual, camino, costo))

            # Se irá almacenando el numero de veces que se expande cada nodo en el
            # diccionario nodos_expandidos
            if nodo_actual != camino[0]:
                indice_nodo_actual = camino.index(nodo_actual)
                cantidad_expansion = nodos_expandidos[camino[indice_nodo_actual - 1]]
                nodos_expandidos[camino[indice_nodo_actual - 1]
                                 ] = cantidad_expansion + 1

            # Si el nodo actual no ha sido visitado
            if nodo_actual not in nodos_visitados:
                nodos_visitados.append(nodo_actual)

                # Si el nodo actual es igual a la meta, se detiene el algoritmo, indicando
                # camino encontrado, costo del camino, numero de veces que se expande y total
                # de expansiones
                if nodo_actual == meta:
                    print("-------Algoritmo Búsqueda Costo Uniforme-------")
                    print("Camino encontrado: ")
                    for elem in camino:
                        print(elem, end=" ")

                    costo_total = 0

                    print(f"\nCosto total:\n {costo}")

                    print("Expansiones de nodos: ")
                    for key in nodos_expandidos:
                        print(f"{key} : {nodos_expandidos[key]}")

                    for key in nodos_expandidos:
                        valor = nodos_expandidos[key]
                        exp_totales += valor
                    print(f"Total de Expansiones de nodos:\n{exp_totales}")
                    flag = 0
                    break

                # Se irá almacenando en los nodos por visitar los posibles caminos a seguir con
                # sus costos
                for nodo_destino, costo_destino in conexiones_costo[nodo_actual]:
                    if nodo_destino not in nodos_visitados:
                        nodos_por_visitar.append(
                            (nodo_destino, camino + [nodo_destino], costo + costo_destino))

        # Indica que no se ha encontrado un camino
        if flag:
            print("-------Algoritmo Búsqueda Costo Uniforme-------")
            print("Camino encontrado:\nNo se ha encontrado un camino")
            print("Expansiones de nodos: ")
            for key in nodos_expandidos:
                print(f"{key} : {nodos_expandidos[key]}")
            for key in nodos_expandidos:
                valor = nodos_expandidos[key]
                exp_totales += valor
            print(f"Total de Expansiones de nodos:\n{exp_totales}")

    def B_greedy(self, nodos_expandidos, heuristicas):
        # Se inicializa en 0 la cantidad de veces que se han expandido los nodos
        self.nodos_expandidos = nodos_expandidos
        for key in nodos_expandidos:
            nodos_expandidos[key] = 0

        # Lista que almacena los nodos que se van a visitar
        # Lista que almacena los nodos visitados,
        nodos_visitados = []
        nodos_por_visitar = []
        nodos_por_visitar.append((inicio, [inicio], heuristicas[inicio]))
        exp_totales = 0
        flag = 1

        while len(nodos_por_visitar) > 0:

            # Se escoge el camino con menor costo de la lista de los nodos por visitar
            nodo_costo_minimo = nodos_por_visitar[0]
            for nodo in nodos_por_visitar:
                if nodo[2] < nodo_costo_minimo[2]:
                    nodo_costo_minimo = nodo
            nodo_actual, camino, costo = nodo_costo_minimo
            nodos_por_visitar.remove((nodo_actual, camino, costo))

            # Se irá almacenando el numero de veces que se expande cada nodo en el
            # diccionario nodos_expandidos
            if nodo_actual != camino[0]:
                indice_nodo_actual = camino.index(nodo_actual)
                cantidad_expansion = nodos_expandidos[camino[indice_nodo_actual - 1]]
                nodos_expandidos[camino[indice_nodo_actual - 1]
                                 ] = cantidad_expansion + 1

            # Si el nodo actual no ha sido visitado
            if nodo_actual not in nodos_visitados:
                nodos_visitados.append(nodo_actual)

                # Si el nodo actual es igual a la meta, se detiene el algoritmo, indicando
                # camino encontrado, costo del camino, numero de veces que se expande y total
                # de expansiones
                if nodo_actual == meta:
                    print("-------Algoritmo Búsqueda Greedy-------")
                    print("Camino encontrado: ")
                    for elem in camino:
                        print(elem, end=" ")

                    costo_total = 0
                    exp_totales = 0

                    print(f"\nCosto total:\n {costo}")

                    print("Expansiones de nodos: ")
                    for key in nodos_expandidos:
                        print(f"{key} : {nodos_expandidos[key]}")

                    for key in nodos_expandidos:
                        valor = nodos_expandidos[key]
                        exp_totales += valor
                    print(f"Total de Expansiones de nodos:\n{exp_totales}")
                    flag = 0
                    break

                # Se irá almacenando en los nodos por visitar los posibles caminos a seguir con
                # sus costos
                for nodo_destino, costo_destino in conexiones_costo[nodo_actual]:
                    if nodo_destino not in nodos_visitados:
                        nodos_por_visitar.append(
                            (nodo_destino, camino + [nodo_destino], costo + heuristicas[nodo_destino]))

        # Indica que no se ha encontrado un camino
        if flag:
            print("-------Algoritmo Búsqueda Greedy-------")
            print("Camino encontrado:\nNo se ha encontrado un camino")
            print("Expansiones de nodos: ")
            for key in nodos_expandidos:
                print(f"{key} : {nodos_expandidos[key]}")
            for key in nodos_expandidos:
                valor = nodos_expandidos[key]
                exp_totales += valor
            print(f"Total de Expansiones de nodos:\n{exp_totales}")

    def B_A_estrella(self, nodos_expandidos, heuristicas):

        # Se inicializa en 0 la cantidad de veces que se han expandido los nodos
        self.nodos_expandidos = nodos_expandidos
        for key in nodos_expandidos:
            nodos_expandidos[key] = 0
        flag = 1

        # Lista que almacena los nodos que se van a visitar
        # Lista que almacena los nodos visitados,
        nodos_visitados = []
        nodos_por_visitar = []
        nodos_por_visitar.append((inicio, [inicio], heuristicas[inicio]))
        exp_totales = 0

        while len(nodos_por_visitar) > 0:

            # Se escoge el camino con menor costo de la lista de los nodos por visitar
            nodo_costo_minimo = nodos_por_visitar[0]
            for nodo in nodos_por_visitar:
                if nodo[2] < nodo_costo_minimo[2]:
                    nodo_costo_minimo = nodo
            nodo_actual, camino, costo = nodo_costo_minimo
            nodos_por_visitar.remove((nodo_actual, camino, costo))

            # Se irá almacenando el numero de veces que se expande cada nodo en el
            # diccionario nodos_expandidos
            if nodo_actual != camino[0]:
                indice_nodo_actual = camino.index(nodo_actual)
                cantidad_expansion = nodos_expandidos[camino[indice_nodo_actual - 1]]
                nodos_expandidos[camino[indice_nodo_actual - 1]
                                 ] = cantidad_expansion + 1

            # Si el nodo actual es igual a la meta, se detiene el algoritmo, indicando
            # camino encontrado, costo del camino, numero de veces que se expande y total
            # de expansiones
            if nodo_actual == meta:
                print("-------Algoritmo Búsqueda A*-------")
                print("Camino encontrado: ")
                for elem in camino:
                    print(elem, end=" ")
                print(f"\nCosto total:\n {costo}")
                print("Expansiones de nodos: ")
                for key in nodos_expandidos:
                    print(f"{key} : {nodos_expandidos[key]}")
                for key in nodos_expandidos:
                    valor = nodos_expandidos[key]
                    exp_totales += valor
                print(f"Total de Expansiones de nodos:\n{exp_totales}")
                flag = 0
                break
            # Se irá almacenando en los nodos por visitar los posibles caminos a seguir con
            # sus costos asociados
            for nodo_destino, costo_destino in conexiones_costo[nodo_actual]:
                nodos_por_visitar.append(
                    (nodo_destino, camino + [nodo_destino], costo + costo_destino + heuristica_nodo[nodo_destino] - heuristica_nodo[nodo_actual]))

        # Indica que no se ha encontrado un camino
        if flag:
            print("-------Algoritmo Búsqueda A*-------")
            print("Camino encontrado:\nNo se ha encontrado un camino")
            print("Expansiones de nodos: ")
            for key in nodos_expandidos:
                print(f"{key} : {nodos_expandidos[key]}")
            for key in nodos_expandidos:
                valor = nodos_expandidos[key]
                exp_totales += valor
            print(f"Total de Expansiones de nodos:\n{exp_totales}")


with open("archivo.txt", "r") as archivo:

    lineas = archivo.readlines()

    # Se almacena el nodo inicial y final
    inicio = lineas[0].strip().split(' ')[1]
    meta = lineas[1].strip().split(' ')[1]

    heuristica_nodo = {}
    costo_arista = []
    conexiones_costo = {}
    nodos_expandidos = {}

    # Se almacena cada nodo con su heuristica en la lista heuristica_nodo
    # Se crea el diccionario conexiones_costo, en donde la llave representará
    # el nodo y sus valores asociados indicarán hacia donde pueden expandirse
    # Se crea el diccionario nodos expandidos, en donde la llave representará
    # el nodo y su valor asociado el numero de veces que se expandirá
    for linea in lineas[2:10]:
        nodo, heuristica = linea.strip().split(' ')
        conexiones_costo[nodo] = []
        nodos_expandidos[nodo] = 0
        heuristica_nodo[nodo] = int(heuristica)

    # En el diccionario conexiones_costo se almacena por cada nodo hacia donde
    # se puede expandir, indicando eel destino y el costo para llegar a ese
    # destino
    for key in conexiones_costo:
        for linea in lineas[10:]:
            origen, destino, costo = linea.strip().split(', ')
            if key == origen:
                conexiones_costo[key].append((destino, int(costo)))

    mi_grafo = Grafo(inicio, meta, heuristica_nodo, conexiones_costo)
    mi_grafo.B_profundidad(nodos_expandidos)
    mi_grafo.B_costo_uniforme(nodos_expandidos)
    mi_grafo.B_greedy(nodos_expandidos, heuristica_nodo)
    mi_grafo.B_A_estrella(nodos_expandidos, heuristica_nodo)
