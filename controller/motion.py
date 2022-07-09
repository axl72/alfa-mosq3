from controller.util import *

clickBoxColourList = {'gold': 'khaki', 'darkred': 'darkmagenta'}
boxColourList = ('gold', 'darkred')
PIECE_CLICKED = (-1, -1)


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


def siguienteTurno(tablero, boxesMatrix, piecesMatrix, juega_mosquetero, cordenadas, preseleccion):
    # Si ya hemos elegido la ficha a mover y luego elegimos un movimiento valido
    global PIECE_CLICKED
    if cordenadas in preseleccion:
        x, y = PIECE_CLICKED
        cordenadas
        if juega_mosquetero[0]:
            piecesMatrix[x][y].comerPieza(cordenadas)
            tablero.mover_pieza(PIECE_CLICKED, cordenadas, juega_mosquetero[0])
        else:
            piecesMatrix[x][y].moverPieza(cordenadas)
            tablero.mover_pieza(PIECE_CLICKED, cordenadas, juega_mosquetero[0])
        pintarTablero(boxesMatrix, piecesMatrix, preseleccion)

        # Esto se puede optimizar
        while preseleccion != []:
            preseleccion.pop()

        # Dado el error 'referenced before assignment' la linea queda así
        # Debería ser de esta forma 'return not juega_mosquetero'
        juega_mosquetero[0] = not juega_mosquetero[0]

        return

    cordenadas_posibles = obtenerCordenadasPosibles(
        tablero.estado, cordenadas, juega_mosquetero[0])
    if cordenadas_posibles == []:
        print("No hay jugadas posibles para esta ficha")
        return

    for z in cordenadas_posibles.copy():
        preseleccion.append(z)

    if preseleccion != []:
        pintarTablero(boxesMatrix, piecesMatrix, preseleccion)

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
