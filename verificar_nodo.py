from collections import OrderedDict

def ubicacion_nodo(matriz, fila_central, columna_central, left_dir, right_dir, up_dir, down_dir):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    
    nodos = {
        "Arriba": (fila_central - 1, columna_central),
        "Abajo": (fila_central + 1, columna_central),
        "Izquierda": (fila_central, columna_central - 1),
        "Derecha": (fila_central, columna_central + 1)
    }
    
    vecinos = OrderedDict()  
    vecinos_agregados = 0
    for direccion, (fila, columna) in nodos.items():
        if 0 <= fila < num_filas and 0 <= columna < num_columnas:
            if direccion == "Arriba" and matriz[fila][columna] in down_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
            elif direccion == "Abajo" and matriz[fila][columna] in up_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
            elif direccion == "Izquierda" and matriz[fila][columna] in right_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
            elif direccion == "Derecha" and matriz[fila][columna] in left_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
    
    return vecinos

def imprimir_vecinos(matriz, fila_central, columna_central, left_dir, right_dir, up_dir, down_dir):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    
    nodos = {
        "Arriba": (fila_central - 1, columna_central),
        "Abajo": (fila_central + 1, columna_central),
        "Izquierda": (fila_central, columna_central - 1),
        "Derecha": (fila_central, columna_central + 1)
    }
    
    vecinos = OrderedDict()  
    vecinos_agregados = 0
    for direccion, (fila, columna) in nodos.items():
        if 0 <= fila < num_filas and 0 <= columna < num_columnas:
            if direccion == "Arriba" and matriz[fila][columna] not in piezas and matriz[fila][columna] in down_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
            elif direccion == "Abajo" and matriz[fila][columna] not in piezas and matriz[fila][columna] in up_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
            elif direccion == "Izquierda" and matriz[fila][columna] not in piezas and matriz[fila][columna] in right_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
            elif direccion == "Derecha" and matriz[fila][columna] not in piezas and matriz[fila][columna] in left_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
    
    return vecinos
 
def asignar_valor(vecinos):
    if len(vecinos) == 1:
        if "Arriba" in vecinos or "Abajo" in vecinos:
            return 6
        elif "Izquierda" in vecinos or "Derecha" in vecinos:
            return 5
    elif len(vecinos) == 2:
        if "Arriba" in vecinos and "Abajo" in vecinos:
            return 6
        if "Izquierda" in vecinos and "Derecha" in vecinos:
            return 5
        if "Arriba" in vecinos and "Derecha" in vecinos:
            return 7
        elif "Derecha" in vecinos and "Abajo" in vecinos:
            return 8
        elif "Abajo" in vecinos and "Izquierda" in vecinos:
            return 9
        elif "Izquierda" in vecinos and "Arriba" in vecinos:
            return 10
    return None 

def insertarNumero11(matriz, fila, columna):
    matriz[fila][columna] = 11
    
    posiciones_vecinos = imprimir_vecinos(matriz,fila,columna,left_dir,right_dir,up_dir,down_dir)
    print("Nodos vecinos:")
    for direccion, (fila_vecino,columna_vecino) in posiciones_vecinos.items():
     print(matriz[fila_vecino][columna_vecino])
    print("Filas y columnas de vecinos:")
    for direccion, (fila_vecino, columna_vecino) in posiciones_vecinos.items():
        print(matriz[fila_vecino][columna_vecino])
        print(direccion, ":", "Fila:", fila_vecino, "Columna:", columna_vecino)
        if matriz[fila_vecino][columna_vecino]:
         vecinos_del_vecinos = ubicacion_nodo(matriz,fila_vecino,columna_vecino,left_dir,right_dir,up_dir,down_dir)
         valor = asignar_valor(vecinos_del_vecinos)
         matriz[fila_vecino][columna_vecino] = valor
         print("por ubicacion_nodo del vecino:")
         print(valor)

    nuevos_vecinos = ubicacion_nodo(matriz,fila,columna,left_dir,right_dir,up_dir,down_dir)
    valor = asignar_valor(nuevos_vecinos)
    matriz[fila][columna] = valor
    print("por ubicacion_nodo directo:")
    print(valor)
    
        
# Matriz de ejemplo
matriz = [
    [0, 8, 1, 5, 1, 0, 0, 0, 0, 0],
    [8, 10, 0, 0, 1, 0, 0, 0, 2, 0],
    [6, 0, 2, 0, 2, 0, 1, 0, 0, 0]
]

fila_central = 2
columna_central = 1

left_dir = {7,10, 5, 1, 2}  # Constantes.RIGHT_DOWN, Constantes.DOWN_LEFT, Constantes.AL_LADO
right_dir = {8,9,5, 1, 2}  # Constantes.UP_RIGHT, Constantes.LEFT_UP, Constantes.AL_LADO
up_dir = {9, 10, 6, 1, 2}  # Constantes.DOWN_LEFT, Constantes.LEFT_UP, Constantes.VERTICAL
down_dir = {7, 8, 6, 1, 2}
piezas = {0,1,2}
insertarNumero11(matriz,fila_central,columna_central)
def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))
mostrar_matriz(matriz)
