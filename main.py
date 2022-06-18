import tkinter as tk
from model.box import Box

boxesList = list()


def boardConstructor(gameWindow):
    """Funcion que nos permite constuir un tablero en la ventana de juego"""
    for r in range(5):
        for c in range(5):

            # Se instancia el cuadrado. nota: Box recibe el componente padre, fila, columna, y un valor de 0(dorado) y 1(rojo oscuro)
            box = Box(gameWindow, r, c, (r + c) % 2)
            boxesList.append(box)
            box.grid(row=r, column=c)


if __name__ == "__main__":
    # Definicion de la ventana
    gameWindow = tk.Tk()
    gameWindow.resizable(0, 0)
    lista = boardConstructor(gameWindow)
    gameWindow.mainloop()
