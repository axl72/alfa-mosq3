# alfa-mosq3

alfa-mosq3 es un software que recrea gráficamente el tradicional juego de los tres mosqueteros. Implementa el algoritmo Minimax para determinar las jugadas de la IA.

## Tabla de contenido

[1. Tres mosqueteros](#1-tres-mosqueteros)\
[2. Objetivo del juego](#2-objetivo-del-juego)\
[3. Referencias](#3-referencias)
### 1. Tres mosqueteros
El tradicional juego de los tres mosqueteros consiste en un tablero 5x5 donde existirán 3 piezas que se situaran en la diagonal derecha intercaladamente. El resto de fichas son guardianes.

![Posicionamiento Inicial del tablero](http://www.dma.fi.upm.es/recursos/aplicaciones/matematicas_recreativas/web/los_tres_mosqueteros/images/tableroinicial.jpg)

### 2. Objetivo del juego
Los guardiante intentarán forzar a que los Tres mosqueteros esten sobre la misma fila o columna (donde es asumido que ellos ya no pueden capturar a un guardián para deshacer el posicionamiento), ganando tan pronto como estos se posicionen.

Los mosqueteros ganan si en su turno no existe un movimiento valido a jugar; es decir, no existe guardianes adyacentes a ser capturados, por supuesto, siempre y cuando no se encuentren forzados sobre la misma fila o columna.

![Final del tablero (Ganan Guardianes)](http://www.dma.fi.upm.es/recursos/aplicaciones/matematicas_recreativas/web/los_tres_mosqueteros/images/enem-ganan.jpg)

### 3. Referencias
**Sackson, S. (1992).** ***Cap. 2 A Gamut Of Games 1 edición (pp. 56-59)*** **. New York: Dover Publications, Inc**