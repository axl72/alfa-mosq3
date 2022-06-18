from model.box import Box


def boardConstructor(gameWindow):
    """Funcion que nos permite constuir un tablero en la ventana de juego"""
    size = 5
    for r in range(size):
        for c in range(size):

            # Se instancia el cuadrado. nota: Box recibe el componente padre, fila, columna, y un valor de 0(dorado) y 1(rojo oscuro)
            box = Box(gameWindow, r, c, (r + c) % 2)
            vars.boxesList.append(box)
            box.grid(row=r, column=c)

# if vars.BOX_NUMBERER_VAR == 0:
#     print("Entramos")
#     vars.boxesList[-1].widget.config(image=tk.PhotoImage(file=vars.blank_box_widget_list[0]),
#                                      bg=vars.boxColourList[0])
# else:
#     print("Entramos")
#     vars.boxesList[-1].widget.config(
#         height=4, width=10, text=f"{len(vars.boxesList) - 1}", bg=vars.boxColourList[0])


# vars.boxesList[size * r + c].widget.grid(column=r, row=c)
# vars.boxesList[size * r + c].widget.bind("<Button-1>",
#  vars.boxesList[size * r + c].pieceTeleporter_or_box_click_func)
