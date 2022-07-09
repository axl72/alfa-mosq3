def suma_cartesiana(tupla1, tupla2):
    "Esta funcion nos permite obtener la suma cartesiana dada dos tuplas"
    a, b = tupla1
    x, y = tupla2
    return (a+x, b+y)


def obtenerCordenadasFrontales(cordenadas_origen):
    "Esta fucion nos permite obtener las cordenadas frontales y laterales dada una cordenada"
    frontales = []
    for i in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        frontales.append(suma_cartesiana(cordenadas_origen, i))

    resultado = []

    for x, y in frontales:
        if x <= 4 and y <= 4 and x >= 0 and y >= 0:
            resultado.append((x, y))
    return resultado


def obtenerCordenadasPosibles(tablero, cordenadas, maxmin):
    """Esta función recibe la cordenada de la casilla del tablero seleccionada para iniciar una jugada, retorna una lista de cordenadas posibles a donde moverse en base al tipo de ficha"""
    cordenadas_resultantes = []
    for x, y in obtenerCordenadasFrontales(cordenadas):
        if maxmin:
            if 'M' != tablero[x][y] and tablero[x][y] != ' ':
                cordenadas_resultantes.append((x, y))
        else:
            if tablero[x][y] == ' ':
                cordenadas_resultantes.append((x, y))
    return cordenadas_resultantes
