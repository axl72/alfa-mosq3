clickBoxColourList = {'gold': 'khaki', 'darkred': 'darkmagenta'}
boxColourList = ('gold', 'darkred')
PIECE_CLICKED = (-1, -1)


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
    """Esta funcion recibe la cordenada del tablero seleccionada para iniciar una jugada, retornar una lista de cordenadas posibles a donde moverse en base al tipo de ficha"""

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
        if juega_mosquetero[0]:
            if codigo_pieza == 0:
                cordenadasValidadas.append(z)
        else:
            if codigo_pieza == -1:
                cordenadasValidadas.append(z)
    return cordenadasValidadas


def pintarTablero(boxesMatrix, piecesMatrix, cordenadas, color=None):
    """Esta funcion recibe una lista de cordenadas y pinta las casillas en tablero, recibe como parametros el tablero y la piezas, las cordenadas a pintar y la lista de colores a pintar"""
    if color != None:
        for z in cordenadas:
            x, y = z
            if piecesMatrix[x][y] != None:
                piecesMatrix[x][y].config(bg=color)
            boxesMatrix[x][y].config(bg=color)

    else:
        for z in cordenadas:
            x, y = z
            color = boxesMatrix[x][y].colour
            if piecesMatrix[x][y] != None:
                piecesMatrix[x][y].config(bg=color)
            boxesMatrix[x][y].config(bg=color)


def siguienteTurno(boxesMatrix, piecesMatrix, juega_mosquetero, cordenadas, preseleccion):
    # Si ya hemos elegido la ficha a mover y luego elegimos un movimiento valido
    global PIECE_CLICKED
    if cordenadas in preseleccion:
        x, y = PIECE_CLICKED
        cordenadas
        if juega_mosquetero[0]:
            piecesMatrix[x][y].comerPieza(cordenadas)
        else:
            piecesMatrix[x][y].moverPieza(cordenadas)
        pintarTablero(boxesMatrix, piecesMatrix, preseleccion)

        # Esto se puede optimizar
        while preseleccion != []:
            preseleccion.pop()

        # Dado el error 'referenced before assignment' la linea queda así
        # Debería ser de esta forma 'return not juega_mosquetero'
        juega_mosquetero[0] = not juega_mosquetero[0]
        return

    cordenadas_posibles = obtenerCordenadasPosibles(
        boxesMatrix, piecesMatrix, juega_mosquetero, cordenadas)

    if cordenadas_posibles == []:
        print("No hay jugadas posibles para esta ficha")
        return

    for z in cordenadas_posibles.copy():
        preseleccion.append(z)

    if preseleccion != []:
        pintarTablero(boxesMatrix, piecesMatrix, preseleccion)
    # else:

    x, y = cordenadas_posibles[0]
    color = clickBoxColourList[boxesMatrix[x][y].colour]
    pintarTablero(boxesMatrix, piecesMatrix,
                  cordenadas_posibles, color)

    PIECE_CLICKED = cordenadas


def pieces_movement(matrix):
    for row in matrix:
        for piece in row:
            piece.bind(
                "<Button-1>", piece.clickFunc)


if __name__ == "__main__":
    print(obtenerCordenadasFrontales((0, 0)))
