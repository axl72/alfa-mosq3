import sys


def boarConstructor(widget, constructor, size=5):
    if size % 2 == 0:
        sys.exit(1)
    matriz = []
    for i in range(size):
        lista = list()
        for j in range(size):
            element = constructor(widget, i, j, (i+j) % 2)
            element.grid(row=i, column=j)
            lista.append(element)
        matriz.append(lista)
    return matriz


def piecesConstructor(widget, constructor, size=5, boxList=[]):
    if boxList == []:
        sys.exit(1)
    matriz = []
    for i in range(size):
        lista = list()
        for j in range(size):
            codigo = "mosquetero" if (i == 0 and j == 4) or (
                i == 2 and j == 2) or (i == 4 and j == 0) else "guardian"

            elemento = constructor(widget, codigo, (i, j), (i+j) % 2)
            elemento.grid(row=i, column=j)
            elemento.box = (i, j)
            boxList[i][j].piece_contained = 0 if codigo == "guardian" else 1
            lista.append(elemento)
        matriz.append(lista)
    return matriz
