clickBoxColourList = ['khaki', 'darkmagenta']
boxColourList = ['gold', 'darkred']


def suma_cartesiana(tupla1, tupla2):
    "Esta funcion nos permite obtener la suma cartesiana dada dos tuplas"
    return tuple([a + b for a, b in zip(tupla1, tupla2)])


def obtenerCordenadasFrontales(cordendas):
    "Esta fucion nos permite obtener las cordenadas frontales y laterales dada una cordenada"
    movimientos = {"izquierda": (-1, 0), "arriba": (0, -1),
                   "derecha": (1, 0), "abajo": (0, 1)}

    resultado = list()
    for i in movimientos.values():
        resultado.append(suma_cartesiana(cordendas, i))
    return resultado


def obtenerCordenadasPosibles(boxesMatrix, piecesMatrix, juega_mosquetero, cordenadas):
    """Esta funcion recibe la cordenada del tablero seleccionada para iniciar una jugada, retornar una lista de cordenadas posibles a donde moverse"""

    size = len(boxesMatrix) - 1

    if size <= 0:
        raise Exception

    cordenadasPosibles = obtenerCordenadasFrontales(cordenadas)
    cordenadasFrontales = list()

    # Con este bucle se eliminan las cordenadas negativas o absurdas
    for index, z in enumerate(cordenadasPosibles):
        x, y = z
        if not((x > size or y > size) or (x < 0 or y < 0)):
            cordenadasFrontales.append(z)

    # Con este bucle se eliminan las jugadas que carecen de lógica como que un mosquetero inte comer a otro
    cordenadasValidadas = list()
    for z in cordenadasFrontales:
        x, y = z
        codigo_pieza = boxesMatrix[x][y].piece_contained
        # Si la casilla donde queremos movernos contiene una ficha, es decir si el codigo de pieza contenida es diferente de -1
        if codigo_pieza != -1:
            # Si las cordenadas posibles de movimiento son diferentes a la clase de jugador que esta jugando es un movimiento valido
            # Es decir, si juega mosquetero y nos queremos mover a la casilla de un guardian, es correctoa != -1:
            if codigo_pieza != juega_mosquetero:
                cordenadasValidadas.append(z)
    return cordenadasValidadas


def pintarTablero(boxesMatrix, piecesMatrix, cordenadas, color=None):
    """Esta funcion recibe una lista de cordenadas y pinta las casillas en tablero, recibe como parametros el tablero y la piezas, las cordenadas a pintar y la lista de colores a pintar"""
    if color != None:
        for z in cordenadas:
            x, y = z
            piecesMatrix[x][y].config(bg=color)
            boxesMatrix[x][y].config(bg=color)

    else:
        for z in cordenadas:
            x, y = z
            color = boxesMatrix[x][y].colour
            piecesMatrix[x][y].config(bg=color)
            boxesMatrix[x][y].config(bg=color)


def siguienteTurno(boxesMatrix, piecesMatrix, juega_mosquetero, cordenadas, preseleccion):
    cordenadas_posibles = obtenerCordenadasPosibles(
        boxesMatrix, piecesMatrix, juega_mosquetero, cordenadas)
    print(preseleccion != [])

    for z in cordenadas_posibles.copy():
        preseleccion.append(z)

    if preseleccion != []:
        pintarTablero(boxesMatrix, piecesMatrix, preseleccion)
    # else:
    color = clickBoxColourList[1] if juega_mosquetero else clickBoxColourList[0]
    pintarTablero(boxesMatrix, piecesMatrix,
                  cordenadas_posibles, color)

    # Dado el error 'referenced before assignment' la linea queda así
    # Debería ser de esta forma 'return not juega_mosquetero'
    #juega_mosquetero[0] = not juega_mosquetero[0]


def pieces_movement(matrix):
    for row in matrix:
        for piece in row:
            piece.bind(
                "<Button-1>", piece.clickFunc)


if __name__ == "__main__":
    print(obtenerCordenadasFrontales((0, 0)))
