import tkinter as tk
from view.board import boarConstructor

if __name__ == "__name__":
    # Definicion de la ventana
    gameWindow = tk.Tk()
    gameWindow.resizable(0, 0)
    lista = boardConstructor(gameWindow)
    gameWindow.mainloop()
