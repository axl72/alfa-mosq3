from model.vars import *


class Pieces:
    def __init__(self, widget, typeCode, pieceCode, colour, coordinate1=6969, coordinate2=6969, lifeState=None, movesPlayedByPiece=None,
                 clickState=bool(0),
                 art=None, weight=0):
        self.art = art
        self.widget = widget
        self.typeCode = int(typeCode)
        self.colour = colour
        '''
        SIDE_OF_WHITE   "colour" of white pieces
        0               1
        1               1
        2               0
        3               0
        '''

        if HORIZONTAL_VERTICAL_ARRANGEMENT_VAR == 0:
            self.column = int(coordinate1)
            self.row = int(coordinate2)
        else:
            self.row = int(coordinate1)
            self.column = int(coordinate2)
        self.lifeState = lifeState
        self.movesPlayedByPiece = movesPlayedByPiece
        self.pieceCode = pieceCode
        self.clickState = clickState
        self.weight = PIECE_WEIGHT_LIST[typeCode]

    def cursorHighlighter(self, event=None):
        if (
                MOVES_PLAYED + 1 + SIDE_COLOUR_VAR) % 2 == self.colour and PIECE_CLICK_VAR == 6969 and CHECK_MATE_STATUS == 0 and COMPUTER_PROCESSING_STATUS == 0:
            widget_highlighter(self)
            widget_highlighter(boxesList[pieceCodeToPositionConverterMainBoard(
                self.pieceCode)])

    def cursorHighlightRemover(self, event=None):
        if (
                MOVES_PLAYED + 1 + SIDE_COLOUR_VAR) % 2 == self.colour and PIECE_CLICK_VAR == 6969 and CHECK_MATE_STATUS == 0 and COMPUTER_PROCESSING_STATUS == 0:
            widget_highlight_remover(self)
            widget_highlight_remover(boxesList[pieceCodeToPositionConverterMainBoard(
                self.pieceCode)])

    def clickFunc(self, event):
        global PIECE_CLICK_VAR, MOVES_PLAYED
        if CHECK_MATE_STATUS == 0 and COMPUTER_PROCESSING_STATUS == 0 or CHECK_MATE_STATUS == 0 and NUMBER_OF_HUMAN_PLAYERS == 0:
            if which_side_move() == self.colour:
                if PIECE_CLICK_VAR == 6969:
                    PIECE_CLICK_VAR = self.pieceCode
                    widget_highlighter(self)
                    final_destination_giver(PIECE_CLICK_VAR)
                    for i in final_destination_giver(PIECE_CLICK_VAR):
                        widget_highlighter(boxesList[i])

                elif PIECE_CLICK_VAR == self.pieceCode:
                    widget_colourer_and_bg_colour_attribute_setter(
                        self, boxesList[pieceCodeToPositionConverterMainBoard(self.pieceCode)].bg_colour)
                    boxesList[8 * self.column + self.row].widget.config(
                        bg=boxesList[pieceCodeToPositionConverterMainBoard(self.pieceCode)].bg_colour)
                    for i in final_destination_giver(PIECE_CLICK_VAR):
                        widget_highlight_remover(boxesList[i])
                    PIECE_CLICK_VAR = 6969
                else:
                    piecesList[PIECE_CLICK_VAR].widget.config(
                        bg=boxColourList[boxesList[pieceCodeToPositionConverterMainBoard(PIECE_CLICK_VAR)].colour])
                    widget_colourer_and_bg_colour_attribute_setter(boxesList[pieceCodeToPositionConverterMainBoard(
                        PIECE_CLICK_VAR)], boxColourList[(piecesList[PIECE_CLICK_VAR].column + piecesList[PIECE_CLICK_VAR].row) % 2])
                    for i in final_destination_giver(PIECE_CLICK_VAR):
                        widget_highlight_remover(boxesList[i])
                    PIECE_CLICK_VAR = self.pieceCode
                    widget_colourer_and_bg_colour_attribute_setter(self, clickBoxColourList[
                        (piecesList[PIECE_CLICK_VAR].column + piecesList[PIECE_CLICK_VAR].row) % 2])
                    widget_colourer_and_bg_colour_attribute_setter(
                        boxesList[8 * self.column + self.row], clickBoxColourList[
                            (piecesList[PIECE_CLICK_VAR].column + piecesList[PIECE_CLICK_VAR].row) % 2])
                    final_destination_giver(PIECE_CLICK_VAR)
                    for i in final_destination_giver(PIECE_CLICK_VAR):
                        widget_highlighter(boxesList[i])
            elif PIECE_CLICK_VAR != 6969 and pieceCodeToPositionConverterMainBoard(
                    self.pieceCode) in final_destination_giver(PIECE_CLICK_VAR):
                self.widget.grid_remove()
                SIDE_POINTS[int(self.colour)] -= self.weight
                PIECES_ALIVE[int(self.colour)].remove(self.pieceCode)
                boxesList[pieceCodeToPositionConverterMainBoard(
                    self.pieceCode)].pieceTeleporter_or_box_click_func(event, self.pieceCode)
