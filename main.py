# import tkinter as tk
import tkinter as tk
from controller.motion import pieces_movement, siguienteTurno
from view.constructors import boarConstructor, piecesConstructor


BOX_NUMBERER_VAR = 0
global piecesMatrix
global boxesMatrix

# Ventana de juego
gameWindow = tk.Tk()

# Imagenes precargadas de las fichas
img = {"mosquetero": tk.PhotoImage(file="img/musketeer.png"),
       "guardian": tk.PhotoImage(file="img/guardian.png")}

# Tamaño del tablero
BOARD_SIZE = 5

# Controla los colores de los cuadrados
boxColourList = ['gold', 'darkred']

# Lista de posibles movimientos, se llena cuando se selecciona una pieza
POSIBLES_MOVIMIENTOS = []

# Numero de jugadores
NUMBER_OF_HUMAN_PLAYERS = 1

# Cuando marca 1 juegan los mosqueteros, en caso contrario juegan los guardianes
# Esta variable debería ser un boleano pero en dado caso arroja la siguiente excepcion 'referenced before assignment'
ID_JUGADOR_JUGANDO = [True]

if NUMBER_OF_HUMAN_PLAYERS == 1:
    MOVE_TIME_INTERVAL = 1000
else:
    MOVE_TIME_INTERVAL = 10

# Imagen con la dimension para las casillas
blank_box_widget_list = 'img/blankBox__Yo.png'


class Box (tk.Label):
    '''Clase que nos permite representar un cuadrado en el tablero'''

    def __init__(self, widget, row, column, colour, colour_occupied=3, piece_contained=-1):
        # Resctamos la variables
        self.colour = boxColourList[colour]
        self.image = tk.PhotoImage(file=blank_box_widget_list)

        # Configuramos el objeto padre
        super().__init__(widget, bg=self.colour, image=self.image)
        self.cordenadas = (row, column)

        # Guardamos la ventana de juego
        self.gameWindow = widget
        # Filas y columnas
        self.column = int(column)
        self.row = int(row)

        # No se que es esto
        self.colour_occupied = colour_occupied
        self.piece_contained = piece_contained

        # Se agrega al widget principal (ventana)

    def clickFunc(self, event):
        global PIECE_CLICKED
        PIECE_CLICKED = self.cordenadas
        if self.piece_contained == -1 and not ID_JUGADOR_JUGANDO[0]:
            siguienteTurno(boxesMatrix, piecesMatrix,
                           ID_JUGADOR_JUGANDO, PIECE_CLICKED, POSIBLES_MOVIMIENTOS)
        else:
            print("No hay ficha para hola comer")


class Piece(tk.Label):
    def __init__(self, widget, tipo, cordenadas=(-1, -1), colour=None, box=(-1, -1)):
        self.cordenandas = cordenadas
        # El atributo tipo es dato un binario que represeta 1 (True) cuando es un mosquetero o 0 (False) cuando es un guardian
        self.tipo = True if tipo == "mosquetero" else False
        self.box = box
        super().__init__(widget, image=img[tipo], bg=boxColourList[colour])

    def clickFunc(self, event):
        global PIECE_CLICKED

        PIECE_CLICKED = self.cordenandas
        if self.tipo == ID_JUGADOR_JUGANDO[0] or self.cordenandas in POSIBLES_MOVIMIENTOS:
            siguienteTurno(boxesMatrix, piecesMatrix, ID_JUGADOR_JUGANDO,
                           PIECE_CLICKED, POSIBLES_MOVIMIENTOS)

    def comerPieza(self, cordenada):
        x, y = cordenada
        x0, y0 = self.cordenandas
        piecesMatrix[x][y].grid_forget()
        piecesMatrix[x][y] = piecesMatrix[x0][y0]
        piecesMatrix[x0][y0] = None
        self.cordenandas = cordenada
        self.grid_forget()
        self.grid(row=x, column=y)
        self.config(bg=boxesMatrix[x][y].colour)
        boxesMatrix[x][y].piece_contained = 1
        boxesMatrix[x0][y0].piece_contained = -1

    def moverPieza(self, cordenada):
        x, y = cordenada
        x0, y0 = self.cordenandas
        self.grid_forget()
        piecesMatrix[x][y] = piecesMatrix[x0][y0]
        piecesMatrix[x0][y0] = None
        self.config(bg=boxesMatrix[x][y].colour)
        self.grid(row=x, column=y)
        self.cordenandas = cordenada
        boxesMatrix[x][y].piece_contained = 0
        boxesMatrix[x0][y0].piece_contained = -1


if __name__ == "__main__":
    boxesMatrix = boarConstructor(gameWindow, Box)
    piecesMatrix = piecesConstructor(gameWindow, Piece, boxList=boxesMatrix)
    pieces_movement(piecesMatrix)
    pieces_movement(boxesMatrix)
    gameWindow.mainloop()
