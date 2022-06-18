from email.mime import image
import tkinter as tk
import os
import copy
import vars
import computer_move


def piececode_to_board_matrix_position_converter(pieceCodeInput, BOARD_MATRIX_INPUT=vars.ENTIRE_BOARD_MATRIX):
    """Funcion de apoyo para piececode_to_board_matrix_position_converter"""
    if pieceCodeInput != 6969:
        return int(
            8 * index_2d(BOARD_MATRIX_INPUT, pieceCodeInput)[0] + index_2d(BOARD_MATRIX_INPUT, pieceCodeInput)[1])


def box_index_to_board_matrix_element_converter(index_in_box, ENTIRE_BOARD_MATRIX_INPUT=vars.ENTIRE_BOARD_MATRIX):
    """Funcion de apoyo para simple_possible_destination_giver"""
    return ENTIRE_BOARD_MATRIX_INPUT[index_in_box // 8][index_in_box % 8]


def like_coloured_piececode_list_spitter(pieceCode):
    """Funcion de apoyo para simple_possible_destination_giver"""
    if vars.piecesList[pieceCode].colour == vars.piecesList[8].colour:
        return list(range(16))
    else:
        return list(range(16, 32))


def king_code(colour):
    """Funciones de apyp para check_checker"""
    global SIDE_COLOUR_VAR
    return [[7, 23], [23, 7]][SIDE_COLOUR_VAR][colour]


def index_2d(myList, v):
    """Funciones de apoyo para check_checker"""
    for x in myList:
        if v in x:
            return [myList.index(x), x.index(v)]
    return [6969, 6969]


def pieceCodeToPositionConverterMainBoard(pieceCodeInput):
    # use piececode_to_board_matrix_position_converter from now on
    """Funcion de apoyo para check_or_checkmate_checker_box_colourer"""
    if pieceCodeInput != 6969:
        return int(8 * vars.piecesList[pieceCodeInput].column + vars.piecesList[pieceCodeInput].row)


def widget_colourer_and_bg_colour_attribute_setter(class_instance, colour):
    """Funcion de apoyo para check_or_checkmate_checker_box_colourer"""
    if class_instance in vars.piecesList:
        class_instance.widget.config(bg=colour)
        vars.boxesList[pieceCodeToPositionConverterMainBoard(
            vars.piecesList.index(class_instance))].widget.config(bg=colour)
        vars.boxesList[pieceCodeToPositionConverterMainBoard(
            vars.piecesList.index(class_instance))].bg_colour = colour
    else:
        class_instance.widget.config(bg=colour)
        class_instance.bg_colour = colour
        if class_instance.piece_contained < 6969:
            vars.piecesList[class_instance.piece_contained].widget.config(
                bg=colour)


def check_checker(king_colour_input, INPUT_BOARD_MATRIX=vars.ENTIRE_BOARD_MATRIX):
    TEMP_BOARD_MATRIX = copy.deepcopy(INPUT_BOARD_MATRIX)
    king_piece_code = king_code(king_colour_input)
    king_position = index_2d(TEMP_BOARD_MATRIX, king_piece_code)
    for type_looper, piece_looper in enumerate(list(i + [0, 6][king_colour_input] for i in range(32, 38))):
        TEMP_BOARD_MATRIX[king_position[0]][king_position[1]] = piece_looper
        if type_looper in [vars.piecesList[TEMP_BOARD_MATRIX[i // 8][i % 8]].typeCode for i in simple_possible_destination_giver(piece_looper, TEMP_BOARD_MATRIX, 1) if TEMP_BOARD_MATRIX[i // 8][i % 8] != 6969]:

            return 1
    return 0


def check_or_checkmate_checker_box_colourer(piece_moved_input):
    for i in range(2):
        truth_value = bool(0)
        for opp_piece in PIECES_ALIVE[not i]:
            if pieceCodeToPositionConverterMainBoard(king_code(i)) in simple_possible_destination_giver(opp_piece):
                widget_colourer_and_bg_colour_attribute_setter(vars.piecesList[king_code(i)], vars.check_colour[
                    vars.boxesList[pieceCodeToPositionConverterMainBoard(king_code(i))].colour])
                vars.piecesList[king_code(i)].checkState = 1
                truth_value = 1
                check_mate_checker = 1
                for piece in PIECES_ALIVE[i]:
                    if final_destination_giver(piece):
                        check_mate_checker -= 1
                        break
                if check_mate_checker == 1:
                    global CHECK_MATE_STATUS
                    CHECK_MATE_STATUS = 1
                    widget_colourer_and_bg_colour_attribute_setter(
                        vars.piecesList[king_code(i)], vars.CHECK_MATE_COLOUR[i])
                    break
                break
        if truth_value == 0:
            if piece_moved_input != king_code(i):
                widget_colourer_and_bg_colour_attribute_setter(vars.piecesList[king_code(i)], vars.boxColourList[
                    vars.boxesList[pieceCodeToPositionConverterMainBoard(king_code(i))].colour])
            else:
                widget_colourer_and_bg_colour_attribute_setter(vars.boxesList[LAST_MOVE[-1][1]],
                                                               vars.clickBoxColourList[vars.boxesList[LAST_MOVE[-1][1]].colour])
                widget_colourer_and_bg_colour_attribute_setter(vars.piecesList[king_code(i)], vars.clickBoxColourList[
                    vars.boxesList[pieceCodeToPositionConverterMainBoard(king_code(i))].colour])
            vars.piecesList[king_code(i)].checkState = 0


def simple_possible_destination_giver(pieceCodeInput, ENTIRE_BOARD_MATRIX_INPUT=vars.ENTIRE_BOARD_MATRIX, killer_pawn_move_input=0):
    if pieceCodeInput < 6969:
        possibleDestinations = []
        rookBishopQueenTypeCodeList = [0, 2, 3]
        if vars.piecesList[pieceCodeInput].typeCode in rookBishopQueenTypeCodeList:
            # rook, bishop, queen
            unitVectorList = [[[0, 1], [0, -1], [1, 0], [-1, 0]], [[1, 1], [1, -1], [-1, 1], [-1, -1]],
                              [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]]
            for v in unitVectorList[rookBishopQueenTypeCodeList.index(vars.piecesList[pieceCodeInput].typeCode)]:
                for i in range(7):
                    # change this into a while loop
                    position = 8 * (index_2d(
                        ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[0] + (
                        1 + i) * v[0]) + index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[1] + (1 + i) * v[1]
                    if index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[0] + (1 + i) * v[0] in range(
                            8) and index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[1] + (
                            1 + i) * v[1] in range(8) and box_index_to_board_matrix_element_converter(position,
                                                                                                      ENTIRE_BOARD_MATRIX_INPUT) == 6969:
                        possibleDestinations.append(position)
                    elif index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[0] + (1 + i) * v[0] in range(
                        8) and index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[1] + (1 + i) * v[1] in range(
                            8) and box_index_to_board_matrix_element_converter(position,
                                                                               ENTIRE_BOARD_MATRIX_INPUT) not in like_coloured_piececode_list_spitter(
                            pieceCodeInput):
                        possibleDestinations.append(position)
                        break
                    else:
                        break
        elif vars.piecesList[pieceCodeInput].typeCode == 1:
            # knight
            positionCheckerIndexList = [[1, -1], [2, -2]]
            for a in positionCheckerIndexList[0]:
                for b in positionCheckerIndexList[1]:
                    positionList = [[index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[0] + a,
                                     index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[1] + b],
                                    [index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[0] + b,
                                    index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[1] + a]]
                    for position in positionList:
                        if position[0] in range(8) and position[1] in range(
                            8) and box_index_to_board_matrix_element_converter(8 * position[0] + position[1],
                                                                               ENTIRE_BOARD_MATRIX_INPUT) not in like_coloured_piececode_list_spitter(
                                pieceCodeInput):
                            possibleDestinations.append(
                                8 * position[0] + position[1])
        elif vars.piecesList[pieceCodeInput].typeCode == 4:
            # king
            unitVectorList = [[0, 1], [0, -1], [1, 0],
                              [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            for v in unitVectorList:
                position = 8 * (index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[0] + v[0]) + \
                    index_2d(ENTIRE_BOARD_MATRIX_INPUT,
                             pieceCodeInput)[1] + v[1]
                if index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[0] + v[0] in range(8) and \
                    index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[1] + v[1] in range(
                        8) and box_index_to_board_matrix_element_converter(position,
                                                                           ENTIRE_BOARD_MATRIX_INPUT) not in like_coloured_piececode_list_spitter(
                        pieceCodeInput):
                    possibleDestinations.append(position)
        elif vars.piecesList[pieceCodeInput].typeCode == 5:
            # pawn
            pawnDirectionList = [1, -1]
            pawnDirection = pawnDirectionList[vars.piecesList[pieceCodeInput].colour]
            pawnLongitudnalCoordinate = [index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[1],
                                         index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[0]][
                vars.HORIZONTAL_VERTICAL_ARRANGEMENT_VAR]
            pawnLateralCoordinate = [index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[0],
                                     index_2d(ENTIRE_BOARD_MATRIX_INPUT, pieceCodeInput)[1]][
                vars.HORIZONTAL_VERTICAL_ARRANGEMENT_VAR]
            if killer_pawn_move_input == 0:
                position = piececode_to_board_matrix_position_converter(pieceCodeInput,
                                                                        ENTIRE_BOARD_MATRIX_INPUT) + pawnDirection * [1, 8][
                    vars.HORIZONTAL_VERTICAL_ARRANGEMENT_VAR]
                if pawnLongitudnalCoordinate + pawnDirection * 1 in range(
                        8) and box_index_to_board_matrix_element_converter(position,
                                                                           ENTIRE_BOARD_MATRIX_INPUT) == 6969:
                    possibleDestinations.append(position)

                    if vars.piecesList[pieceCodeInput].movesPlayedByPiece == 0 and box_index_to_board_matrix_element_converter(position + pawnDirection * [1, 8][vars.HORIZONTAL_VERTICAL_ARRANGEMENT_VAR], ENTIRE_BOARD_MATRIX_INPUT) == 6969:
                        possibleDestinations.append(
                            position + pawnDirection * [1, 8][vars.HORIZONTAL_VERTICAL_ARRANGEMENT_VAR])

            pawnColumnMovementList = [1, -1]
            for n in pawnColumnMovementList:
                position = [8, 1][vars.HORIZONTAL_VERTICAL_ARRANGEMENT_VAR] * (pawnLateralCoordinate + n) + [1, 8][
                    vars.HORIZONTAL_VERTICAL_ARRANGEMENT_VAR] * (pawnLongitudnalCoordinate + pawnDirection)
                if pawnLongitudnalCoordinate + pawnDirection in range(8) and pawnLateralCoordinate + n in range(
                        8) and box_index_to_board_matrix_element_converter(position, ENTIRE_BOARD_MATRIX_INPUT) != 6969 and piecesList[box_index_to_board_matrix_element_converter(position, ENTIRE_BOARD_MATRIX_INPUT)].colour != piecesList[pieceCodeInput].colour:
                    possibleDestinations.append(position)

        return set(possibleDestinations)


def final_destination_giver(piece_code_input, INPUT_BOARD_MATRIX=vars.ENTIRE_BOARD_MATRIX, INPUT_PIECES_ALIVE=vars.PIECES_ALIVE):
    TEMP_BOARD_MATRIX = copy.deepcopy(INPUT_BOARD_MATRIX)

    initially_allowed_boxes = simple_possible_destination_giver(
        piece_code_input, TEMP_BOARD_MATRIX).copy()

    output = initially_allowed_boxes.copy()

    piece_code_input_postion = index_2d(
        TEMP_BOARD_MATRIX, piece_code_input)

    king_colour_to_check = vars.PiecesList[piece_code_input].colour

    for destination in initially_allowed_boxes:
        piece_at_destination = TEMP_BOARD_MATRIX[destination //
                                                 8][destination % 8]

        TEMP_BOARD_MATRIX[piece_code_input_postion[0]
                          ][piece_code_input_postion[1]] = 6969
        TEMP_BOARD_MATRIX[destination // 8][destination % 8] = piece_code_input

        if check_checker(king_colour_to_check, TEMP_BOARD_MATRIX) == 1:
            output.remove(destination)

        TEMP_BOARD_MATRIX[destination // 8][destination %
                                            8] = piece_at_destination
        TEMP_BOARD_MATRIX[piece_code_input_postion[0]
                          ][piece_code_input_postion[1]] = piece_code_input

    return set(output)


def widget_highlight_remover(class_instance):
    """Funcion de apoyo para Boxes.pieceTeleporter_or_box_click_func"""
    if class_instance in vars.piecesList:
        class_instance.widget.config(
            bg=vars.boxesList[pieceCodeToPositionConverterMainBoard(class_instance.pieceCode)].bg_colour)
        vars.boxesList[pieceCodeToPositionConverterMainBoard(
            class_instance.pieceCode)].widget.config(
            bg=vars.boxesList[pieceCodeToPositionConverterMainBoard(class_instance.pieceCode)].bg_colour)
    elif class_instance.piece_contained == 6969:
        class_instance.widget.config(bg=class_instance.bg_colour)
    else:
        vars.piecesList[class_instance.piece_contained].widget.config(
            bg=class_instance.bg_colour)
        class_instance.widget.config(bg=class_instance.bg_colour)


def which_side_move():
    """Funcino de apoyo para Boxes.piceTeleporter_or_box_click_func"""
    return (MOVES_PLAYED + 1 + SIDE_COLOUR_VAR) % 2


def computer_piece_mover(list_w_piece_code_and_final_position):
    """Funcion de apoyo para Boxes.pieceTeleporter_or_box_click_func"""
    if list_w_piece_code_and_final_position[0] != 6969:
        computer_move_piece_code = list_w_piece_code_and_final_position[0]
        final_position = list_w_piece_code_and_final_position[1]
        global PIECE_CLICK_VAR
        PIECE_CLICK_VAR = computer_move_piece_code

        if vars.boxesList[final_position].colour_occupied == 3:
            vars.boxesList[final_position].pieceTeleporter_or_box_click_func(
                '<Key>')
        else:
            vars.piecesList[vars.boxesList[final_position].piece_contained].clickFunc(
                '<Key>')

# La clase Box hereda de Label


class Box (tk.Label):
    '''Clase que nos permite representar un cuadrado en el tablero'''

    def __init__(self, widget, column, row, colour, colour_occupied=3, piece_contained=6969):
        # Resctamos la variables
        colour = vars.boxColourList[colour]
        image = tk.PhotoImage(file=vars.blank_box_widget_list[0])

        # Configuramos el objeto padre
        super().__init__(widget, bg=colour, image=image)

        # Guardamos la ventana de juego
        self.gameWindow = widget
        # Filas y columnas
        self.column = int(column)
        self.row = int(row)

        # No se que es esto
        self.colour_occupied = colour_occupied
        self.piece_contained = piece_contained

        # Se agrega al widget principal (ventana)

    def pieceTeleporter_or_box_click_func(self, event, victimCode=6969):
        '''Funcion que permite mover'''
        global PIECE_CLICK_VAR, MOVES_PLAYED, LAST_MOVE, PIECES_ALIVE
        if PIECE_CLICK_VAR < 6969 and vars.boxesList.index(self) in final_destination_giver(PIECE_CLICK_VAR) and victimCode == 6969 or PIECE_CLICK_VAR < 6969 and pieceCodeToPositionConverterMainBoard(victimCode) in final_destination_giver(PIECE_CLICK_VAR):
            for i in final_destination_giver(PIECE_CLICK_VAR):
                if i != vars.boxesList.index(self):
                    widget_highlight_remover(vars.boxesList[i])
            if MOVES_PLAYED > 0:
                widget_colourer_and_bg_colour_attribute_setter(vars.boxesList[LAST_MOVE[-1][1]],
                                                               vars.boxColourList[vars.boxesList[LAST_MOVE[-1][1]].colour])
                widget_colourer_and_bg_colour_attribute_setter(vars.PiecesList[LAST_MOVE[-1][0]],
                                                               vars.boxColourList[vars.boxesList[LAST_MOVE[-1][2]].colour])

            vars.boxesList[pieceCodeToPositionConverterMainBoard(
                PIECE_CLICK_VAR)].colour_occupied = 3
            vars.ENTIRE_BOARD_MATRIX[vars.boxesList[pieceCodeToPositionConverterMainBoard(PIECE_CLICK_VAR)].column][
                vars.boxesList[pieceCodeToPositionConverterMainBoard(PIECE_CLICK_VAR)].row] = 6969
            vars.boxesList[pieceCodeToPositionConverterMainBoard(
                PIECE_CLICK_VAR)].piece_contained = 6969
            self.piece_contained = PIECE_CLICK_VAR
            vars.boxesList[pieceCodeToPositionConverterMainBoard(PIECE_CLICK_VAR)].widget.config(
                bg=vars.clickBoxColourList[(vars.boxesList[pieceCodeToPositionConverterMainBoard(PIECE_CLICK_VAR)].colour)])
            LAST_MOVE.append([PIECE_CLICK_VAR, pieceCodeToPositionConverterMainBoard(PIECE_CLICK_VAR),
                              8 * self.column + self.row])
            vars.PiecesList[PIECE_CLICK_VAR].column = self.column
            vars.PiecesList[PIECE_CLICK_VAR].row = self.row

            widget_colourer_and_bg_colour_attribute_setter(vars.PiecesList[PIECE_CLICK_VAR], vars.clickBoxColourList[
                vars.boxesList[pieceCodeToPositionConverterMainBoard(PIECE_CLICK_VAR)].colour])

            vars.PiecesList[PIECE_CLICK_VAR].widget.grid(
                row=self.row, column=self.column)
            vars.PiecesList[PIECE_CLICK_VAR].movesPlayedByPiece += 1
            self.colour_occupied = int(vars.PiecesList[PIECE_CLICK_VAR].colour)
            vars.ENTIRE_BOARD_MATRIX[self.column][self.row] = vars.PiecesList[PIECE_CLICK_VAR].pieceCode
            MOVES_PLAYED += 1

            check_or_checkmate_checker_box_colourer(PIECE_CLICK_VAR)
            PIECE_CLICK_VAR = 6969
            if which_side_move() == vars.COLOUR_OF_COMPUTER and vars.NUMBER_OF_HUMAN_PLAYERS == 1 or vars.NUMBER_OF_HUMAN_PLAYERS == 0 and CHECK_MATE_STATUS == 0:
                global COMPUTER_PROCESSING_STATUS
                COMPUTER_PROCESSING_STATUS = 1
                os.sleep(0.005)
                self.gameWindow.after(vars.MOVE_TIME_INTERVAL,
                                 lambda: computer_piece_mover(computer_move.computer_move_spitter()))

        elif self.piece_contained != 6969:
            vars.piecesList[self.piece_contained].clickFunc(event)

    def cursorHighlighter(self, event=None):
        if self.piece_contained != 6969:
            vars.piecesList[self.piece_contained].cursorHighlighter(event)

    def cursorHighlightRemover(self, event=None):
        if self.piece_contained != 6969:
            vars.piecesList[self.piece_contained].cursorHighlightRemover(event)


if __name__ == "__main__":
    # gameWindow = tk.Tk()
    # gameWindow.resizable(0, 0)
    # lista = boardConstructor(gameWindow)
    # gameWindow.mainloop()
    pass
