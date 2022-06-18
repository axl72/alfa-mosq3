import vars
import copy


def which_side_move():
    """Funcino de apoyo para computer_move_spitter"""
    return (MOVES_PLAYED + 1 + SIDE_COLOUR_VAR) % 2


def computer_move_spitter():
    global COMPUTER_PROCESSING_STATUS, CHECK_MATE_STATUS
    if CHECK_MATE_STATUS == 0 and which_side_move() == vars.COLOUR_OF_COMPUTER and vars.NUMBER_OF_HUMAN_PLAYERS == 1 or NUMBER_OF_HUMAN_PLAYERS == 0 and CHECK_MATE_STATUS == 0:
        COMPUTER_PROCESSING_STATUS = 1
        entire_board_matrix_ = deepcopy(ENTIRE_BOARD_MATRIX)
        moves_played_ = MOVES_PLAYED
        pieces_alive_ = copy.deepcopy(PIECES_ALIVE)
        number_of_rounds_to_check = 4
        colour_of_computer = which_side_move()

        def func_for_weight_killed_to_prob_conversion(piece_code_killed):
            def func_to_use(a):
                return a
            if piece_code_killed == 6969:
                return PIECE_WEIGHT_LIST[-1]
            else:
                return func_to_use(vars.piecesList[piece_code_killed].weight)

        def piece_mover_in_board_matrix_and_pieces_alive_remover(piece_code_input, final_position, board_matrix_input,
                                                                 pieces_alive_input):
            initial_position = index_2d(board_matrix_input, piece_code_input)
            board_matrix_input[initial_position[0]][initial_position[1]] = 6969
            piece_to_be_killed = board_matrix_input[final_position //
                                                    8][final_position % 8]
            if piece_to_be_killed != 6969:
                pieces_alive_input[not piecesList[piece_code_input].colour].remove(
                    piece_to_be_killed)
            board_matrix_input[final_position //
                               8][final_position % 8] = piece_code_input

        list_for_piece_code_and_final_position = []
        temp_list = []
        list_ = []

        for piece1 in vars.PIECES_ALIVE[colour_of_computer]:
            temp_board_matrix_1 = copy.deepcopy(vars.ENTIRE_BOARD_MATRIX)
            pieces_alive_1 = copy.deepcopy(vars.PIECES_ALIVE)

            if vars.piecesList[piece1].typeCode == 5:
                pawn_memory_1_original = vars.piecesList[piece1].movesPlayedByPiece
            for move1 in final_destination_giver(piece1, temp_board_matrix_1, pieces_alive_1):
                temp_board_matrix_1 = copy.deepcopy(entire_board_matrix_)
                pieces_alive_1 = copy.deepcopy(vars.PIECES_ALIVE)
                piece_killed = temp_board_matrix_1[move1 // 8][move1 % 8]

                l1r1 = func_for_weight_killed_to_prob_conversion(piece_killed)
                piece_mover_in_board_matrix_and_pieces_alive_remover(
                    piece1, move1, temp_board_matrix_1, pieces_alive_1)

                if vars.piecesList[piece1].typeCode == 5:
                    vars.piecesList[piece1].movesPlayedByPiece = pawn_memory_1_original
                    vars.piecesList[piece1].movesPlayedByPiece += 1

                checkmate_var = 1
                for piece2 in pieces_alive_1[not colour_of_computer]:
                    if piecesList[piece2].typeCode == 5:
                        pawn_memory_2_original = piecesList[piece2].movesPlayedByPiece
                    temp_board_matrix_2 = deepcopy(temp_board_matrix_1)
                    pieces_alive_2 = deepcopy(pieces_alive_1)

                    for move2 in final_destination_giver(piece2, temp_board_matrix_2, pieces_alive_2):
                        checkmate_var = 0
                        temp_board_matrix_2 = deepcopy(temp_board_matrix_1)
                        pieces_alive_2 = deepcopy(pieces_alive_1)

                        if piecesList[piece2].typeCode == 5:
                            piecesList[piece2].movesPlayedByPiece = pawn_memory_2_original
                        piece_killed2 = temp_board_matrix_2[move2 //
                                                            8][move2 % 8]
                        l2r2 = 1 / \
                            func_for_weight_killed_to_prob_conversion(
                                piece_killed2)

                        if piece_killed2 != 6969:
                            l2r2 *= 0.99

                        temp_list.append(l1r1 * l2r2)

                    if piecesList[piece2].typeCode == 5:
                        piecesList[piece2].movesPlayedByPiece = pawn_memory_2_original
                if checkmate_var == 1:

                    return [piece1, move1]
                if temp_list:
                    list_.append(min(temp_list))
                    list_for_piece_code_and_final_position.append(
                        [piece1, move1])
                    temp_list.clear()
            if piecesList[piece1].typeCode == 5:
                piecesList[piece1].movesPlayedByPiece = pawn_memory_1_original

        length = len(list_)
        final_final_list = [[list_for_piece_code_and_final_position[i], list_[i]]
                            for i in range(length)]

        shuffle(final_final_list)
        list1 = [final_final_list[i][0] for i in range(length)]
        list2 = [final_final_list[i][1] for i in range(length)]
        COMPUTER_PROCESSING_STATUS = 0
        if list2:
            return list1[list2.index(max(list2))]
        else:
            CHECK_MATE_STATUS += 2  # for stalemate
            for box in boxesList:
                box.widget.config(bg=clickBoxColourList[box.colour])
            for piece in piecesList:
                piece.widget.config(
                    bg=clickBoxColourList[(piece.row + piece.column) % 2])
            return [6969, 6969]
    else:
        return [6969, 6969]
