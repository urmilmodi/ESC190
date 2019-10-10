from multiprocessing.pool import ThreadPool
import time

limit = 100
Rook = ((8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8),
        (8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1),
        (1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8))
Bishop = ((1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 7, 1, 2, 3, 4, 5, 6, 6, 6, 1, 2, 3, 4, 5, 5, 5, 5, 1, 2, 3, 4, 4, 4, 4, 4, 1, 2, 3, 3, 3, 3, 3, 3, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1),
          (8, 7, 6, 5, 4, 3, 2, 1, 7, 7, 6, 5, 4, 3, 2, 1, 6, 6, 6, 5, 4, 3, 2, 1, 5, 5, 5, 5, 4, 3, 2, 1, 4, 4, 4, 4, 4, 3, 2, 1, 3, 3, 3, 3, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1),
          (1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 4, 4, 4, 4, 4, 1, 2, 3, 4, 5, 5, 5, 5, 1, 2, 3, 4, 5, 6, 6, 6, 1, 2, 3, 4, 5, 6, 7, 7, 1, 2, 3, 4, 5, 6, 7, 8),
          (1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 3, 3, 3, 3, 3, 3, 2, 1, 4, 4, 4, 4, 4, 3, 2, 1, 5, 5, 5, 5, 4, 3, 2, 1, 6, 6, 6, 5, 4, 3, 2, 1, 7, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1))

def isWhite(value):
    """
    Checks whether value (piece) is of the White Player
    :param value: board[position] of current position
    :return: True (if White), False (if Black)
    """
    return 9 < value and value < 16

def isBlack(value):
    """
    Checks whether value (piece) is of the Black Player
    :param value: board[position] of current position
    :return: True (if Black), False (if White)
    """
    return 19 < value and value < 26

def getplayer(value):
    """
    Returns player offset value from value (piece)
    :param value: board[position] of current position
    :return: 10 (if White), 20 (if Black)
    """
    return value - value % 10

def getpiece(value):
    if value == 10 or value == 20:
        return "Pawn"
    elif value == 11 or value == 21:
        return "Knight"
    elif value == 12 or value == 22:
        return "Bishop"
    elif value == 13 or value == 23:
        return "Rook"
    elif value == 14 or value == 24:
        return "Queen"
    elif value == 15 or value == 25:
        return "King"
    return None

def genboardLR():
    """
    Generates default initial board
    :return: board
    """
    board = [0] * 64
    
    board[0] = 13
    board[7] = board[0]
    board[1] = 11
    board[6] = board[1]
    board[2] = 12
    board[5] = board[2]
    board[3] = 14
    board[4] = 15

    for position in range(8, 16, 1):
        board[position] = 10

    board[0 + 56] = 23
    board[7 + 56] = board[0 + 56]
    board[1 + 56] = 21
    board[6 + 56] = board[1 + 56]
    board[2 + 56] = 22
    board[5 + 56] = board[2 + 56]
    board[3 + 56] = 24
    board[4 + 56] = 25
    
    for position in range(48, 56, 1):
        board[position] = 20

    return board

def renderLR(board, player=10):
    """
    Print the board on console
    :param board: current state of the board
    :param order: the order of rendering, White's order or Black's order 
    """
    #black = [0, 2, 4, 6, 9, 11, 13, 15, 16, 18, 20, 22, 25, 27, 29, 31, 32, 34, 36, 38, 41, 43, 45, 47, 48, 50, 52, 54, 57, 59, 61, 63]
    data = ["|"] * 8
    counter = 0
    for position in range(0, 64, 1):
        if isWhite(board[position]):
            data[counter] += "W"
        elif isBlack(board[position]):
            data[counter] += "B"
        else:
            data[counter] += " "
        if board[position] == 10 or board[position] == 20:
            data[counter] += "p"

        elif board[position] == 11 or board[position] == 21:
            data[counter] += "k"

        elif board[position] == 12 or board[position] == 22:
            data[counter] += "b"
        
        elif board[position] == 13 or board[position] == 23:
            data[counter] += "r"

        elif board[position] == 14 or board[position] == 24:
            data[counter] += "Q"

        elif board[position] == 15 or board[position] == 25:
            data[counter] += "K"

        else:
            data[counter] += " "

        data[counter] += "|"
        if (position + 1) % 8 == 0:
            data[counter] += "  |"
            for i in range(0, 8, 1):
                if 8*counter + i < 10:
                    data[counter] += " " + str(8*counter + i) + "|"
                else:
                    data[counter] += str(8*counter + i) + "|"
            counter += 1
    
    if player == 10:
        for i in range(7, -1, -1):
            print("-------------------------  -------------------------")
            print(data[i])
        print("-------------------------  -------------------------")
    
    else:
        for i in range(0, 8, 1):
            print("-------------------------  -------------------------")
            print(data[i])
        print("-------------------------  -------------------------")
    return True

def genboardRL():
    """
    Generates default initial board
    :return: board
    """
    board = [0] * 64
    board[0] = 13
    board[7] = 13
    board[1] = 11
    board[6] = 11
    board[2] = 12
    board[5] = 12
    board[4] = 14
    board[3] = 15

    for position in range(8, 16, 1):
        board[position] = 10

    board[0 + 56] = 23
    board[7 + 56] = 23
    board[1 + 56] = 21
    board[6 + 56] = 21
    board[2 + 56] = 22
    board[5 + 56] = 22
    board[4 + 56] = 24
    board[3 + 56] = 25

    for position in range(48, 56, 1):
        board[position] = 20

    return board

def renderRL(board, player=10):
    """
    Print the board on console
    :param board: current state of the board
    :param order: the order of rendering, White's order or Black's order 
    :return: True
    """
    #black = [0, 2, 4, 6, 9, 11, 13, 15, 16, 18, 20, 22, 25, 27, 29, 31, 32, 34, 36, 38, 41, 43, 45, 47, 48, 50, 52, 54, 57, 59, 61, 63]
    data = ["|"] * 8
    counter = 0
    for position in range(0, 64, 1):

        if board[position] == 10 or board[position] == 20:
            data[counter] += "p"

        elif board[position] == 11 or board[position] == 21:
            data[counter] += "k"

        elif board[position] == 12 or board[position] == 22:
            data[counter] += "b"

        elif board[position] == 13 or board[position] == 23:
            data[counter] += "r"

        elif board[position] == 14 or board[position] == 24:
            data[counter] += "Q"

        elif board[position] == 15 or board[position] == 25:
            data[counter] += "K"

        else:
            data[counter] += " "
        
        if isWhite(board[position]):
            data[counter] += "W"
        elif isBlack(board[position]):
            data[counter] += "B"
        else:
            data[counter] += " "

        data[counter] += "|"
        if (position + 1) % 8 == 0:
            data[counter] = data[counter][::-1]
            data[counter] += "  "
            legend = "|"
            for i in range(0, 8, 1):
                if 8*counter + i < 10:
                    legend += "" + str(8*counter + i)[::-1] + " |"
                else:
                    legend += str(8*counter + i)[::-1] + "|"
            data[counter] += legend[::-1]
            counter += 1

    if player == 10:
        for i in range(7, -1, -1):
            print("-------------------------  -------------------------")
            print(data[i])
        print("-------------------------  -------------------------")

    else:
        for i in range(0, 8, 1):
            print("-------------------------  -------------------------")
            print(data[i])
        print("-------------------------  -------------------------")
    return True

def setmove(board, oldposition, newposition):
    """
    Set the move on the board, if the positions are valid
    :param board: the current state of the board
    :param oldposition: the current index of the piece on the board
    :param newposition: the new (desired) index of the piece on the board
    """
    board[newposition] = board[oldposition]
    board[oldposition] = 0

    # Pawn Promotion to Queen
    if newposition < 8 and board[newposition] == 20:
        board[newposition] = 24

    elif 55 < newposition and board[newposition] == 10:
        board[newposition] = 14

    return True

def undomove(board, oldposition, newposition, oldvalue, newvalue):
    
    board[newposition] = newvalue
    board[oldposition] = oldvalue
    return True

def GetPlayerPositions(board, player):
    return [position for position, value in enumerate(board) if player <= value and value < player + 6]

def GetPieceLegalMoves(board, position):
    
    moves = set()

    # Pawn
    # White \|/
    if board[position] == 10:

        # Straight
        if board[position + 8] == 0:
            moves.add(position + 8)

        # Attack Black Left
        if position % 8 != 0 and isBlack(board[position + 7]):
            moves.add(position + 7)

        # Attack Black Right
        if (position + 1) % 8 != 0 and isBlack(board[position + 9]):
            moves.add(position + 9)

    # Black /|\
    elif board[position] == 20:

        # Straight
        if board[position - 8] == 0:
            moves.add(position - 8)

        # Attack White Right
        if (position + 1) % 8 != 0 and isWhite(board[position - 7]):
            moves.add(position - 7)

        # Attack White Right
        if position % 8 != 0 and isWhite(board[position - 9]):
            moves.add(position - 9)

    # Knight
    elif board[position] == 11:
        
        # 15   17    6    -10  10   -6   -17  -15
        # 3U1L 3U1R  3L1U 3L1D 3R1U 3R1D 3D1L 3D1R
        # void position in [16, 17, 24, 25, 32, 33, 40, 41, 22, 23, 30, 31, 38, 39, 46, 47]
        if position % 8 == 0:
            if position > 15:
                if board[position - 15] == 0 or isBlack(board[position - 15]):
                    moves.add(position - 15)
                
                if board[position - 6] == 0 or isBlack(board[position - 6]):
                    moves.add(position - 6)

            elif position > 7:
                if board[position - 6] == 0 or isBlack(board[position - 6]):
                    moves.add(position - 6)
            
            if position < 48:
                if board[position + 17] == 0 or isBlack(board[position + 17]):
                    moves.add(position + 17)

                if board[position + 10] == 0 or isBlack(board[position + 10]):
                    moves.add(position + 10)
            
            elif position < 56:
                if board[position + 10] == 0 or isBlack(board[position + 10]):
                    moves.add(position + 10)
            
        elif position % 8 == 7:
            if position > 15:
                if board[position - 17] == 0 or isBlack(board[position - 17]):
                    moves.add(position - 17)

                if board[position - 10] == 0 or isBlack(board[position - 10]):
                    moves.add(position - 10)

            elif position > 7:
                if board[position - 10] == 0 or isBlack(board[position - 10]):
                    moves.add(position - 10)
            
            if position < 48:
                if board[position + 15] == 0 or isBlack(board[position + 15]):
                    moves.add(position + 15)
                    
                if board[position + 6] == 0 or isBlack(board[position + 6]):
                    moves.add(position + 6)
            
            elif position < 56:
                if board[position + 6] == 0 or isBlack(board[position + 6]):
                    moves.add(position + 6)

        elif position % 8 == 1:
            if position > 15:
                if board[position - 17] == 0 or isBlack(board[position - 17]):
                    moves.add(position - 17)
                
                if board[position - 15] == 0 or isBlack(board[position - 15]):
                    moves.add(position - 15)
                
                if board[position - 6] == 0 or isBlack(board[position - 6]):
                    moves.add(position - 6)

            elif position > 7:
                if board[position - 6] == 0 or isBlack(board[position - 6]):
                    moves.add(position - 6)
            
            if position < 48:
                if board[position + 15] == 0 or isBlack(board[position + 15]):
                    moves.add(position + 15)

                if board[position + 17] == 0 or isBlack(board[position + 17]):
                    moves.add(position + 17)

                if board[position + 10] == 0 or isBlack(board[position + 10]):
                    moves.add(position + 10)
            
            elif position < 56:
                if board[position + 10] == 0 or isBlack(board[position + 10]):
                    moves.add(position + 10)

        elif position % 8 == 6:
            if position > 15:
                if board[position - 15] == 0 or isBlack(board[position - 15]):
                    moves.add(position - 15)

                if board[position - 17] == 0 or isBlack(board[position - 17]):
                    moves.add(position - 17)
                
                if board[position - 10] == 0 or isBlack(board[position - 10]):
                    moves.add(position - 10)

            elif position > 7:
                if board[position - 10] == 0 or isBlack(board[position - 10]):
                    moves.add(position - 10)
            
            if position < 48:
                if board[position + 15] == 0 or isBlack(board[position + 15]):
                    moves.add(position + 15)

                if board[position + 17] == 0 or isBlack(board[position + 17]):
                    moves.add(position + 17)
                
                if board[position + 6] == 0 or isBlack(board[position + 6]):
                    moves.add(position + 6)
            
            elif position < 56:
                if board[position + 6] == 0 or isBlack(board[position + 6]):
                    moves.add(position + 6)

        elif position > 55:
            if board[position - 17] == 0 or isBlack(board[position - 17]):
                moves.add(position - 17)

            if board[position - 15] == 0 or isBlack(board[position - 15]):
                moves.add(position - 15)

            if board[position - 10] == 0 or isBlack(board[position - 10]):
                moves.add(position - 10)

            if board[position - 6] == 0 or isBlack(board[position - 6]):
                moves.add(position - 6)

        elif position > 47:
            if board[position - 17] == 0 or isBlack(board[position - 17]):
                moves.add(position - 17)

            if board[position - 15] == 0 or isBlack(board[position - 15]):
                moves.add(position - 15)

            if board[position - 10] == 0 or isBlack(board[position - 10]):
                moves.add(position - 10)

            if board[position - 6] == 0 or isBlack(board[position - 6]):
                moves.add(position - 6)
            
            if board[position + 6] == 0 or isBlack(board[position + 6]):
                moves.add(position + 6)

            if board[position + 10] == 0 or isBlack(board[position + 10]):
                moves.add(position + 10)

        elif position < 8:
            if board[position + 6] == 0 or isBlack(board[position + 6]):
                moves.add(position + 6)

            if board[position + 10] == 0 or isBlack(board[position + 10]):
                moves.add(position + 10)

            if board[position + 15] == 0 or isBlack(board[position + 15]):
                moves.add(position + 15)

            if board[position + 17] == 0 or isBlack(board[position + 17]):
                moves.add(position + 17)

        elif position < 16:
            if board[position + 6] == 0 or isBlack(board[position + 6]):
                moves.add(position + 6)

            if board[position + 10] == 0 or isBlack(board[position + 10]):
                moves.add(position + 10)

            if board[position + 15] == 0 or isBlack(board[position + 15]):
                moves.add(position + 15)

            if board[position + 17] == 0 or isBlack(board[position + 17]):
                moves.add(position + 17)

            if board[position - 10] == 0 or isBlack(board[position - 10]):
                moves.add(position - 10)

            if board[position - 6] == 0 or isBlack(board[position - 6]):
                moves.add(position - 6)

        else:
            if board[position - 17] == 0 or isBlack(board[position - 17]):
                moves.add(position - 17)

            if board[position - 15] == 0 or isBlack(board[position - 15]):
                moves.add(position - 15)

            if board[position - 10] == 0 or isBlack(board[position - 10]):
                moves.add(position - 10)

            if board[position - 6] == 0 or isBlack(board[position - 6]):
                moves.add(position - 6)

            if board[position + 6] == 0 or isBlack(board[position + 6]):
                moves.add(position + 6)

            if board[position + 10] == 0 or isBlack(board[position + 10]):
                moves.add(position + 10)

            if board[position + 15] == 0 or isBlack(board[position + 15]):
                moves.add(position + 15)

            if board[position + 17] == 0 or isBlack(board[position + 17]):
                moves.add(position + 17)

    elif board[position] == 21:

        if position % 8 == 0:
            if position > 15:
                if board[position - 15] == 0 or isWhite(board[position - 15]):
                    moves.add(position - 15)
                
                if board[position - 6] == 0 or isWhite(board[position - 6]):
                    moves.add(position - 6)

            elif position > 7:
                if board[position - 6] == 0 or isWhite(board[position - 6]):
                    moves.add(position - 6)
            
            if position < 48:
                if board[position + 17] == 0 or isWhite(board[position + 17]):
                    moves.add(position + 17)

                if board[position + 10] == 0 or isWhite(board[position + 10]):
                    moves.add(position + 10)
            
            elif position < 56:
                if board[position + 10] == 0 or isWhite(board[position + 10]):
                    moves.add(position + 10)
            
        elif position % 8 == 7:
            if position > 15:
                if board[position - 17] == 0 or isWhite(board[position - 17]):
                    moves.add(position - 17)

                if board[position - 10] == 0 or isWhite(board[position - 10]):
                    moves.add(position - 10)

            elif position > 7:
                if board[position - 10] == 0 or isWhite(board[position - 10]):
                    moves.add(position - 10)
            
            if position < 48:
                if board[position + 15] == 0 or isWhite(board[position + 15]):
                    moves.add(position + 15)
                    
                if board[position + 6] == 0 or isWhite(board[position + 6]):
                    moves.add(position + 6)
            
            elif position < 56:
                if board[position + 6] == 0 or isWhite(board[position + 6]):
                    moves.add(position + 6)

        elif position % 8 == 1:
            if position > 15:
                if board[position - 17] == 0 or isWhite(board[position - 17]):
                    moves.add(position - 17)
                
                if board[position - 15] == 0 or isWhite(board[position - 15]):
                    moves.add(position - 15)
                
                if board[position - 6] == 0 or isWhite(board[position - 6]):
                    moves.add(position - 6)

            elif position > 7:
                if board[position - 6] == 0 or isWhite(board[position - 6]):
                    moves.add(position - 6)
            
            if position < 48:
                if board[position + 15] == 0 or isWhite(board[position + 15]):
                    moves.add(position + 15)

                if board[position + 17] == 0 or isWhite(board[position + 17]):
                    moves.add(position + 17)

                if board[position + 10] == 0 or isWhite(board[position + 10]):
                    moves.add(position + 10)
            
            elif position < 56:
                if board[position + 10] == 0 or isWhite(board[position + 10]):
                    moves.add(position + 10)

        elif position % 8 == 6:
            if position > 15:
                if board[position - 15] == 0 or isWhite(board[position - 15]):
                    moves.add(position - 15)

                if board[position - 17] == 0 or isWhite(board[position - 17]):
                    moves.add(position - 17)
                
                if board[position - 10] == 0 or isWhite(board[position - 10]):
                    moves.add(position - 10)

            elif position > 7:
                if board[position - 10] == 0 or isWhite(board[position - 10]):
                    moves.add(position - 10)
            
            if position < 48:
                if board[position + 15] == 0 or isWhite(board[position + 15]):
                    moves.add(position + 15)

                if board[position + 17] == 0 or isWhite(board[position + 17]):
                    moves.add(position + 17)
                
                if board[position + 6] == 0 or isWhite(board[position + 6]):
                    moves.add(position + 6)
            
            elif position < 56:
                if board[position + 6] == 0 or isWhite(board[position + 6]):
                    moves.add(position + 6)

        elif position > 55:
            if board[position - 17] == 0 or isWhite(board[position - 17]):
                moves.add(position - 17)

            if board[position - 15] == 0 or isWhite(board[position - 15]):
                moves.add(position - 15)

            if board[position - 10] == 0 or isWhite(board[position - 10]):
                moves.add(position - 10)

            if board[position - 6] == 0 or isWhite(board[position - 6]):
                moves.add(position - 6)

        elif position > 47:
            if board[position - 17] == 0 or isWhite(board[position - 17]):
                moves.add(position - 17)

            if board[position - 15] == 0 or isWhite(board[position - 15]):
                moves.add(position - 15)

            if board[position - 10] == 0 or isWhite(board[position - 10]):
                moves.add(position - 10)

            if board[position - 6] == 0 or isWhite(board[position - 6]):
                moves.add(position - 6)
            
            if board[position + 6] == 0 or isWhite(board[position + 6]):
                moves.add(position + 6)

            if board[position + 10] == 0 or isWhite(board[position + 10]):
                moves.add(position + 10)

        elif position < 8:
            if board[position + 6] == 0 or isWhite(board[position + 6]):
                moves.add(position + 6)

            if board[position + 10] == 0 or isWhite(board[position + 10]):
                moves.add(position + 10)

            if board[position + 15] == 0 or isWhite(board[position + 15]):
                moves.add(position + 15)

            if board[position + 17] == 0 or isWhite(board[position + 17]):
                moves.add(position + 17)

        elif position < 16:
            if board[position + 6] == 0 or isWhite(board[position + 6]):
                moves.add(position + 6)

            if board[position + 10] == 0 or isWhite(board[position + 10]):
                moves.add(position + 10)

            if board[position + 15] == 0 or isWhite(board[position + 15]):
                moves.add(position + 15)

            if board[position + 17] == 0 or isWhite(board[position + 17]):
                moves.add(position + 17)

            if board[position - 10] == 0 or isWhite(board[position - 10]):
                moves.add(position - 10)

            if board[position - 6] == 0 or isWhite(board[position - 6]):
                moves.add(position - 6)

        else:
            if board[position - 17] == 0 or isWhite(board[position - 17]):
                moves.add(position - 17)

            if board[position - 15] == 0 or isWhite(board[position - 15]):
                moves.add(position - 15)

            if board[position - 10] == 0 or isWhite(board[position - 10]):
                moves.add(position - 10)

            if board[position - 6] == 0 or isWhite(board[position - 6]):
                moves.add(position - 6)

            if board[position + 6] == 0 or isWhite(board[position + 6]):
                moves.add(position + 6)

            if board[position + 10] == 0 or isWhite(board[position + 10]):
                moves.add(position + 10)

            if board[position + 15] == 0 or isWhite(board[position + 15]):
                moves.add(position + 15)

            if board[position + 17] == 0 or isWhite(board[position + 17]):
                moves.add(position + 17)

    # Bishop & Queen
    elif board[position] == 12 or board[position] == 14:

        # / RightUp
        for i in range(1, Bishop[0][position], 1):

            # General
            if board[position + 7*i] == 0:
                moves.add(position + 7*i)

            # White
            elif isBlack(board[position + 7*i]):
                moves.add(position + 7*i)
                break

            else:
                break

        # \ LeftUp
        for i in range(1, Bishop[1][position], 1):

            # General
            if board[position + 9*i] == 0:
                moves.add(position + 9*i)

            # White
            elif isBlack(board[position + 9*i]):
                moves.add(position + 9*i)
                break

            else:
                break

        # \ RightDown
        for i in range(1, Bishop[2][position], 1):

            # General
            if board[position - 9*i] == 0:
                moves.add(position - 9*i)

            # White
            elif isBlack(board[position - 9*i]):
                moves.add(position - 9*i)
                break

            else:
                break

        # / LeftDown
        for i in range(1, Bishop[3][position], 1):

            # General
            if board[position - 7*i] == 0:
                moves.add(position - 7*i)

            # White
            elif isBlack(board[position - 7*i]):
                moves.add(position - 7*i)
                break

            else:
                break

    elif board[position] == 22 or board[position] == 24:

        # / RightUp
        for i in range(1, Bishop[0][position], 1):

            # General
            if board[position + 7*i] == 0:
                moves.add(position + 7*i)

            # Black
            elif isWhite(board[position + 7*i]):
                moves.add(position + 7*i)
                break

            else:
                break

        # \ LeftUp
        for i in range(1, Bishop[1][position], 1):

            # General
            if board[position + 9*i] == 0:
                moves.add(position + 9*i)

            # Black
            elif isWhite(board[position + 9*i]):
                moves.add(position + 9*i)
                break

            else:
                break

        # \ RightDown
        for i in range(1, Bishop[2][position], 1):

            # General
            if board[position - 9*i] == 0:
                moves.add(position - 9*i)

            # Black
            elif isWhite(board[position - 9*i]):
                moves.add(position - 9*i)
                break

            else:
                break

        # / LeftDown
        for i in range(1, Bishop[3][position], 1):

            # General
            if board[position - 7*i] == 0:
                moves.add(position - 7*i)

            # Black
            elif isWhite(board[position - 7*i]):
                moves.add(position - 7*i)
                break

            else:
                break

    # Rook & Queen
    if board[position] == 13 or board[position] == 14:

        # Forward
        for i in range(1, Rook[0][position], 1):

            # General
            if board[position + 8*i] == 0:
                moves.add(position + 8*i)

            # White
            elif isBlack(board[position + 8*i]):
                moves.add(position + 8*i)
                break

            else:
                break

        # Backward
        for i in range(1, Rook[1][position], 1):

            # General
            if board[position - 8*i] == 0:
                moves.add(position - 8*i)

            # White
            elif isBlack(board[position - 8*i]):
                moves.add(position - 8*i)
                break

            else:
                break

        # <- Left
        for i in range(1, Rook[2][position], 1):

            # General
            if board[position + i] == 0:
                moves.add(position + i)

            # White
            elif isBlack(board[position + i]):
                moves.add(position + i)
                break

            else:
                break

        # -> Right
        for i in range(1, Rook[3][position], 1):
            # General
            if board[position - i] == 0:
                moves.add(position - i)

            # White
            elif isBlack(board[position - i]):
                moves.add(position - i)
                break

            else:
                break
        
    elif board[position] == 23 or board[position] == 24:

        # Forward
        for i in range(1, Rook[0][position], 1):

            # General
            if board[position + 8*i] == 0:
                moves.add(position + 8*i)

            # Black
            elif isWhite(board[position + 8*i]):
                moves.add(position + 8*i)
                break

            else:
                break

        # Backward
        for i in range(1, Rook[1][position], 1):

            # General
            if board[position - 8*i] == 0:
                moves.add(position - 8*i)

            # Black
            elif isWhite(board[position - 8*i]):
                moves.add(position - 8*i)
                break

            else:
                break

        # <- Left
        for i in range(1, Rook[2][position], 1):

            # General
            if board[position + i] == 0:
                moves.add(position + i)

            # Black
            elif isWhite(board[position + i]):
                moves.add(position + i)
                break

            else:
                break

        # -> Right
        for i in range(1, Rook[3][position], 1):
            # General
            if board[position - i] == 0:
                moves.add(position - i)

            # Black
            elif isWhite(board[position - i]):
                moves.add(position - i)
                break

            else:
                break

    # Queen
    # Included Within Bishop & Rook

    # King
    elif board[position] == 15:

        if position % 8 == 0:
            if board[position + 1] == 0 or isBlack(board[position + 1]):
                moves.add(position + 1)

            if not (position > -1 and position < 8):
                if board[position - 8] == 0 or isBlack(board[position - 8]):
                    moves.add(position - 8)

                if board[position - 7] == 0 or isBlack(board[position - 7]):
                    moves.add(position - 7)

            if not (position > 55 and position < 64):
                if board[position + 8] == 0 or isBlack(board[position + 8]):
                    moves.add(position + 8)

                if board[position + 9] == 0 or isBlack(board[position + 9]):
                    moves.add(position + 9)

        elif (position + 1) % 8 == 0:
            if board[position - 1] == 0 or isBlack(board[position - 1]):
                moves.add(position - 1)

            if not (position > -1 and position < 8):
                if board[position - 8] == 0 or isBlack(board[position - 8]):
                    moves.add(position - 8)

                if board[position - 9] == 0 or isBlack(board[position - 9]):
                    moves.add(position - 9)

            if not (position > 55 and position < 64):
                if board[position + 8] == 0 or isBlack(board[position + 8]):
                    moves.add(position + 8)

                if board[position + 7] == 0 or isBlack(board[position + 7]):
                    moves.add(position + 7)

        elif position > -1 and position < 8:
            if board[position - 1] == 0 or isBlack(board[position - 1]):
                moves.add(position - 1)

            if board[position + 8] == 0 or isBlack(board[position + 8]):
                moves.add(position + 8)

            if board[position + 7] == 0 or isBlack(board[position + 7]):
                moves.add(position + 7)

            if board[position + 9] == 0 or isBlack(board[position + 9]):
                moves.add(position + 9)

            if board[position + 1] == 0 or isBlack(board[position + 1]):
                moves.add(position + 1)

        elif position > 55 and position < 64:
            if board[position - 1] == 0 or isBlack(board[position - 1]):
                moves.add(position - 1)

            if board[position - 8] == 0 or isBlack(board[position - 8]):
                moves.add(position - 8)

            if board[position - 7] == 0 or isBlack(board[position - 7]):
                moves.add(position - 7)

            if board[position - 9] == 0 or isBlack(board[position - 9]):
                moves.add(position - 9)

            if board[position + 1] == 0 or isBlack(board[position + 1]):
                moves.add(position + 1)

        else:
            if board[position - 1] == 0 or isBlack(board[position - 1]):
                moves.add(position - 1)

            if board[position - 8] == 0 or isBlack(board[position - 8]):
                moves.add(position - 8)

            if board[position - 7] == 0 or isBlack(board[position - 7]):
                moves.add(position - 7)

            if board[position - 9] == 0 or isBlack(board[position - 9]):
                moves.add(position - 9)

            if board[position + 1] == 0 or isBlack(board[position + 1]):
                moves.add(position + 1)

            if board[position + 8] == 0 or isBlack(board[position + 8]):
                moves.add(position + 8)

            if board[position + 7] == 0 or isBlack(board[position + 7]):
                moves.add(position + 7)

            if board[position + 9] == 0 or isBlack(board[position + 9]):
                moves.add(position + 9)

    elif board[position] == 25:

        if position % 8 == 0:
            if board[position + 1] == 0 or isWhite(board[position + 1]):
                moves.add(position + 1)

            if not (position > -1 and position < 8):
                if board[position - 8] == 0 or isWhite(board[position - 8]):
                    moves.add(position - 8)

                if board[position - 7] == 0 or isWhite(board[position - 7]):
                    moves.add(position - 7)

            if not (position > 55 and position < 64):
                if board[position + 8] == 0 or isWhite(board[position + 8]):
                    moves.add(position + 8)

                if board[position + 9] == 0 or isWhite(board[position + 9]):
                    moves.add(position + 9)

        elif (position + 1) % 8 == 0:
            if board[position - 1] == 0 or isWhite(board[position - 1]):
                moves.add(position - 1)

            if not (position > -1 and position < 8):
                if board[position - 8] == 0 or isWhite(board[position - 8]):
                    moves.add(position - 8)

                if board[position - 9] == 0 or isWhite(board[position - 9]):
                    moves.add(position - 9)

            if not (position > 55 and position < 64):
                if board[position + 8] == 0 or isWhite(board[position + 8]):
                    moves.add(position + 8)

                if board[position + 7] == 0 or isWhite(board[position + 7]):
                    moves.add(position + 7)

        elif position > -1 and position < 8:
            if board[position - 1] == 0 or isWhite(board[position - 1]):
                moves.add(position - 1)

            if board[position + 8] == 0 or isWhite(board[position + 8]):
                moves.add(position + 8)

            if board[position + 7] == 0 or isWhite(board[position + 7]):
                moves.add(position + 7)

            if board[position + 9] == 0 or isWhite(board[position + 9]):
                moves.add(position + 9)

            if board[position + 1] == 0 or isWhite(board[position + 1]):
                moves.add(position + 1)

        elif position > 55 and position < 64:
            if board[position - 1] == 0 or isWhite(board[position - 1]):
                moves.add(position - 1)

            if board[position - 8] == 0 or isWhite(board[position - 8]):
                moves.add(position - 8)

            if board[position - 7] == 0 or isWhite(board[position - 7]):
                moves.add(position - 7)

            if board[position - 9] == 0 or isWhite(board[position - 9]):
                moves.add(position - 9)

            if board[position + 1] == 0 or isWhite(board[position + 1]):
                moves.add(position + 1)

        else:
            if board[position - 1] == 0 or isWhite(board[position - 1]):
                moves.add(position - 1)

            if board[position - 8] == 0 or isWhite(board[position - 8]):
                moves.add(position - 8)

            if board[position - 7] == 0 or isWhite(board[position - 7]):
                moves.add(position - 7)

            if board[position - 9] == 0 or isWhite(board[position - 9]):
                moves.add(position - 9)

            if board[position + 1] == 0 or isWhite(board[position + 1]):
                moves.add(position + 1)

            if board[position + 8] == 0 or isWhite(board[position + 8]):
                moves.add(position + 8)

            if board[position + 7] == 0 or isWhite(board[position + 7]):
                moves.add(position + 7)

            if board[position + 9] == 0 or isWhite(board[position + 9]):
                moves.add(position + 9)
    
    Blacklist = set()
    if isBlack(board[position]):
        if 25 in board:
            for newpos in moves:
                oldvalue = board[position]
                newvalue = board[newpos]
                setmove(board, position, newpos)

                if 25 in board:
                    if IsPositionUnderThreat(board, board.index(25), 20):
                        Blacklist.add(newpos)
                else:
                    Blacklist.add(newpos)

                undomove(board, position, newpos, oldvalue, newvalue)
        else:
            return []

    else:
        if 15 in board:
            for newpos in moves:
                oldvalue = board[position]
                newvalue = board[newpos]
                setmove(board, position, newpos)
                
                if 15 in board:
                    if IsPositionUnderThreat(board, board.index(15), 10):
                        Blacklist.add(newpos)
                else:
                    Blacklist.add(newpos)
                
                undomove(board, position, newpos, oldvalue, newvalue)
        else:
            return []

    return list(moves^Blacklist)

def IsPositionUnderThreat(board, position, player):
    
    if player == 10:
        
        # Knight
        if position % 8 == 0:
            if position > 15:
                if board[position - 15] == 21 or board[position - 6] == 21:
                    return True

            elif position > 7:
                if board[position - 6] == 21:
                    return True
            
            if position < 48:
                if board[position + 17] == 21 or board[position + 10] == 21:
                    return True
            
            elif position < 56:
                if board[position + 10] == 21:
                    return True
            
        elif position % 8 == 7:
            if position > 15:
                if board[position - 17] == 21 or board[position - 10] == 21:
                    return True

            elif position > 7:
                if board[position - 10] == 21:
                    return True
            
            if position < 48:
                if board[position + 15] == 21 or board[position + 6] == 21:
                    return True
            
            elif position < 56:
                if board[position + 6] == 21:
                    return True
        
        elif position % 8 == 1:
            if position > 15:
                if board[position - 17] == 21 or board[position - 15] == 21 or board[position - 6] == 21:
                    return True
                    
            elif position > 7:
                if board[position - 6] == 21:
                    return True
            
            if position < 48:
                if board[position + 15] == 21 or board[position + 17] == 21 or board[position + 10] == 21:
                    return True
            
            elif position < 56:
                if board[position + 10] == 21:
                    return True

        elif position % 8 == 6:
            if position > 15:
                if board[position - 15] == 21 or board[position - 17] == 21 or board[position - 10] == 21:
                    return True

            elif position > 7:
                if board[position - 10] == 21:
                    return True
            
            if position < 48:
                if board[position + 15] == 21 or board[position + 17] == 21 or board[position + 6] == 21:
                    return True
            
            elif position < 56:
                if board[position + 6] == 21:
                    return True

        elif position > 55:
            if board[position - 17] == 21 or board[position - 15] == 21 or board[position - 10] == 21 or board[position - 6] == 21:
                return True

        elif position > 47:
            if board[position - 17] == 21 or board[position - 15] == 21 or board[position - 10] == 21 or board[position - 6] == 21 or board[position + 10] == 21 or board[position + 10] == 21:
                return True

        elif position < 8:
            if board[position + 17] == 21 or board[position + 15] == 21 or board[position + 10] == 21 or board[position + 6] == 21:
                return True
        
        elif position < 16:
            if board[position + 17] == 21 or board[position + 15] == 21 or board[position + 10] == 21 or board[position + 6] == 21 or board[position - 10] == 21 or board[position - 6] == 21:
                return True

        elif board[position - 17] == 21 or board[position - 15] == 21 or board[position - 10] == 21 or board[position - 6] == 21 or board[position + 6] == 21 or board[position + 10] == 21 or board[position + 15] == 21 or board[position + 17] == 21:
                return True

        # Bishop
        # \ LeftUp
        for i in range(1, Bishop[0][position], 1):

            # White
            if isBlack(board[position + 7*i]):
                if (i == 1 and (board[position + 7*i] == 20 or board[position + 7*i] == 25)) or (board[position + 7*i] == 22 or board[position + 7*i] == 24):
                    return True
                break

            elif isWhite(board[position + 7*i]):
                break

        # / RightUp
        for i in range(1, Bishop[1][position], 1):

            # White
            if isBlack(board[position + 9*i]):
                if (i == 1 and (board[position + 9*i] == 20 or board[position + 9*i] == 25)) or (board[position + 9*i] == 22 or board[position + 9*i] == 24):
                    return True
                break

            elif isWhite(board[position + 9*i]):
                break

        # / LeftDown
        for i in range(1, Bishop[2][position], 1):

            # White
            if isBlack(board[position - 9*i]):
                if (i == 1 and board[position - 9*i] == 25) or (board[position - 9*i] == 22 or board[position - 9*i] == 24):
                    return True
                break

            elif isWhite(board[position - 9*i]):
                break

        # \ RightDown
        for i in range(1, Bishop[3][position], 1):

            # White
            if isBlack(board[position - 7*i]):
                if (i == 1 and board[position - 7*i] == 25) or (board[position - 7*i] == 22 or board[position - 7*i] == 24):
                    return True
                break
            
            elif isWhite(board[position - 7*i]):
                break

        # Rook
        # Forward
        for i in range(1, Rook[0][position], 1):

            # White
            if isBlack(board[position + 8*i]):
                if (i == 1 and board[position + 8*i] == 25) or (board[position + 8*i] == 23 or board[position + 8*i] == 24):
                    return True
                break

            elif isWhite(board[position + 8*i]):
                break

        # Backward
        for i in range(1, Rook[1][position], 1):

            # White
            if isBlack(board[position - 8*i]):
                if (i == 1 and board[position - 8*i] == 25) or (board[position - 8*i] == 23 or board[position - 8*i] == 24):
                    return True
                break

            elif isWhite(board[position - 8*i]):
                break

        # Right
        for i in range(1, Rook[2][position], 1):

            # White
            if isBlack(board[position + i]):
                if (i == 1 and board[position + i] == 25) or (board[position + i] == 23 or board[position + i] == 24):
                    return True
                break
            
            elif isWhite(board[position + i]):
                break

        # Left
        for i in range(1, Rook[3][position], 1):

            # White
            if isBlack(board[position - i]):
                if (i == 1 and board[position - i] == 25) or (board[position - i] == 23 or board[position - i] == 24):
                    return True
                break

            elif isWhite(board[position - i]):
                break

    else:

        if position % 8 == 0:
            if position > 15:
                if board[position - 15] == 11 or board[position - 6] == 11:
                    return True

            elif position > 7:
                if board[position - 6] == 11:
                    return True
            
            if position < 48:
                if board[position + 17] == 11 or board[position + 10] == 11:
                    return True
            
            elif position < 56:
                if board[position + 10] == 11:
                    return True
            
        elif position % 8 == 7:
            if position > 15:
                if board[position - 17] == 11 or board[position - 10] == 11:
                    return True

            elif position > 7:
                if board[position - 10] == 11:
                    return True
            
            if position < 48:
                if board[position + 15] == 11 or board[position + 6] == 11:
                    return True
            
            elif position < 56:
                if board[position + 6] == 11:
                    return True
        
        elif position % 8 == 1:
            if position > 15:
                if board[position - 17] == 11 or board[position - 15] == 11 or board[position - 6] == 11:
                    return True
                    
            elif position > 7:
                if board[position - 6] == 11:
                    return True
            
            if position < 48:
                if board[position + 15] == 11 or board[position + 17] == 11 or board[position + 10] == 11:
                    return True
            
            elif position < 56:
                if board[position + 10] == 11:
                    return True

        elif position % 8 == 6:
            if position > 15:
                if board[position - 15] == 11 or board[position - 17] == 11 or board[position - 10] == 11:
                    return True

            elif position > 7:
                if board[position - 10] == 11:
                    return True
            
            if position < 48:
                if board[position + 15] == 11 or board[position + 17] == 11 or board[position + 6] == 11:
                    return True
            
            elif position < 56:
                if board[position + 6] == 11:
                    return True

        elif position > 55:
            if board[position - 17] == 11 or board[position - 15] == 11 or board[position - 10] == 11 or board[position - 6] == 11:
                return True

        elif position > 47:
            if board[position - 17] == 11 or board[position - 15] == 11 or board[position - 10] == 11 or board[position - 6] == 11 or board[position + 10] == 11 or board[position + 10] == 11:
                return True

        elif position < 8:
            if board[position + 17] == 11 or board[position + 15] == 11 or board[position + 10] == 11 or board[position + 6] == 11:
                return True
        
        elif position < 16:
            if board[position + 17] == 11 or board[position + 15] == 11 or board[position + 10] == 11 or board[position + 6] == 11 or board[position - 10] == 11 or board[position - 6] == 11:
                return True

        elif board[position - 17] == 11 or board[position - 15] == 11 or board[position - 10] == 11 or board[position - 6] == 11 or board[position + 6] == 11 or board[position + 10] == 11 or board[position + 15] == 11 or board[position + 17] == 11:
                return True
    
        # Bishop
        # \ LeftUp
        for i in range(1, Bishop[0][position], 1):

            # Black
            if isWhite(board[position + 7*i]):
                if (i == 1 and board[position + 7*i] == 15) or (board[position + 7*i] == 12 or board[position + 7*i] == 14):
                    return True
                break

            elif isBlack(board[position + 7*i]):
                break

        # / RightUp
        for i in range(1, Bishop[1][position], 1):

            # Black
            if isWhite(board[position + 9*i]):
                if (i == 1 and board[position + 9*i] == 15) or (board[position + 9*i] == 12 or board[position + 9*i] == 14):
                    return True
                break

            elif isBlack(board[position + 9*i]):
                break

        # / LeftDown
        for i in range(1, Bishop[2][position], 1):

            # Black
            if isWhite(board[position - 9*i]):
                if (i == 1 and (board[position - 9*i] == 10 or board[position - 9*i] == 15)) or (board[position - 9*i] == 12 or board[position - 9*i] == 14):
                    return True
                break

            elif isBlack(board[position - 9*i]):
                break

        # \ RightDown
        for i in range(1, Bishop[3][position], 1):

            # Black
            if isWhite(board[position - 7*i]):
                if (i == 1 and (board[position - 7*i] == 10 or board[position - 7*i] == 15)) or (board[position - 7*i] == 12 or board[position - 7*i] == 14):
                    return True
                break

            elif isBlack(board[position - 7*i]):
                break

        # Rook
        # Forward
        for i in range(1, Rook[0][position], 1):

            # Black
            if isWhite(board[position + 8*i]):
                if (i == 1 and board[position + 8*i] == 15) or (board[position + 8*i] == 13 or board[position + 8*i] == 14):
                    return True
                break

            elif isBlack(board[position + 8*i]):
                break

        # Backward
        for i in range(1, Rook[1][position], 1):

            # Black
            if isWhite(board[position - 8*i]):
                if (i == 1 and board[position - 8*i] == 15) or (board[position - 8*i] == 13 or board[position - 8*i] == 14):
                    return True
                break

            elif isBlack(board[position - 8*i]):
                break

        # Right
        for i in range(1, Rook[2][position], 1):

            # Black
            if isWhite(board[position + i]):
                if (i == 1 and board[position + i] == 15) or (board[position + i] == 13 or board[position + i] == 14):
                    return True
                break

            elif isBlack(board[position + i]):
                break

        # Left
        for i in range(1, Rook[3][position], 1):

            # Black
            if isWhite(board[position - i]):
                if (i == 1 and board[position - i] == 15) or (board[position - i] == 13 or board[position - i] == 14):
                    return True
                break

            elif isBlack(board[position - i]):
                break

    return False

def CheckMate(board, player):

    if player == 10:
        if 15 in board:
            if not IsPositionUnderThreat(board, board.index(15), 10):
                return False
            if GetPieceLegalMoves(board, board.index(15)) != []:
                return False
            for oldpos in GetPlayerPositions(board, player):
                if GetPieceLegalMoves(board, oldpos) != []:
                    return False
        else:
            return True

    else:
        if 25 in board:
            if not IsPositionUnderThreat(board, board.index(25), 20):
                return False
            if GetPieceLegalMoves(board, board.index(25)) != []:
                return False
            for oldpos in GetPlayerPositions(board, player):
                if GetPieceLegalMoves(board, oldpos) != []:
                    return False
        else:
            return True

    return True

def rate(board):
    
    if CheckMate(board, 10):
        return -limit
    elif CheckMate(board, 20):
        return limit
    
    score = 0
    basevalues = (1, 3.2, 3.3, 5, 9, 0)
    adjustmentvalues = ((0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.1, 0.1, -0.2, -0.2, 0.1, 0.1, 0.05, 0.05, -0.05, -0.1, 0.0, 0.0, -0.1, -0.05, 0.05, 0.0, 0.0, 0.0, 0.2, 0.2, 0.0, 0.0, 0.0, 0.05, 0.05, 0.1, 0.25, 0.25, 0.1, 0.05, 0.05, 0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 7.8, 7.9, 7.9, 7.95, 7.95, 7.9, 7.9, 7.8),
                        (-0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5, -0.4, -0.2, 0.0, 0.05, 0.05, 0.0, -0.2, -0.4, -0.3, 0.05, 0.1, 0.15, 0.15, 0.1, 0.05, -0.3, -0.3, 0.0, 0.15, 0.2, 0.2, 0.15, 0.0, -0.3, -0.3, 0.05, 0.15, 0.2, 0.2, 0.15, 0.05, -0.3, -0.3, 0.0, 0.1, 0.15, 0.15, 0.1, 0.0, -0.3, -0.4, -0.2, 0.0, 0.0, 0.0, 0.0, -0.2, -0.4, -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5),
                        (-0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.05, -0.1, -0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1, -0.1, 0.0, 0.1, 0.1, 0.1, 0.1, 0.0, -0.1, -0.1, 0.05, 0.05, 0.1, 0.1, 0.05, 0.05, -0.1, -0.1, 0.0, 0.05, 0.1, 0.1, 0.05, 0.0, -0.1, -0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1, -0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2),
                        (0.0, 0.0, 0.0, 0.05, 0.05, 0.0, 0.0, 0.0, -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05, -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05, -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05, -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05, -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                        (-0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2, -0.1, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0, -0.1, -0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1, 0.0, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05, -0.05, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05, -0.1, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1, -0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1, -0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2),
                        (0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.2, 0.2, -0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.1, -0.2, -0.3, -0.3, -0.4, -0.4, -0.3, -0.3, -0.2, -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3, -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3, -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3, -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3))
    void = False
    voidK = False
    for position in range(0, 64, 1):

        if isWhite(board[position]):
            score += basevalues[board[position] - 10] + adjustmentvalues[board[position] - 10][position]

            if board[position] == 10 and not void:
                try:
                    if 64 > position + 1 and board[position + 1] != 10 and not position in (7, 15, 23, 31, 39, 47, 55, 63):
                        score -= 0.05
                    
                    if 64 > position + 8 and board[position + 8] != 0:
                        score -= 0.05
                    
                    if -1 < position - 9 and not position in (16, 24, 32, 40, 48, 56):
                        if not board[position - 9] in (10, 12, 14, 15):
                            score -= 0.05
                        
                        if not board[position - 7] in (10, 12, 14, 15) and not position in (15, 23, 31, 39, 47, 55, 63):
                            score -= 0.05

                    elif -1 < position - 7 and not position in (15, 23, 31, 39, 47, 55, 63):
                        if not board[position - 7] in (10, 12, 14, 15):
                            score -= 0.05
                    
                    if 64 > position + 9:
                        if board[position + 9] in (20, 22, 24, 25) and not position in (15, 23, 31, 39, 47, 55):
                            score -= 0.05

                        if board[position + 7] in (20, 22, 24, 25) and not position in (8, 16, 24, 32, 40, 48):
                            score -= 0.05

                    elif 64 > position + 7:
                        if board[position + 7] in (20, 22, 24, 25) and not position in (8, 16, 24, 32, 40, 48):
                            score -= 0.05
                except:
                    void = True

            elif board[position] == 15 and not voidK:
                try:
                    if 64 > position + 1 and not position in (7, 15, 23, 31, 39, 47, 55, 63) and isWhite(board[position + 1]):
                        score += 0.05
                    if not position in (0, 8, 16, 24, 32, 40, 48, 56) and isWhite(board[position - 1]):
                        score += 0.05
                    if position > 7 and isWhite(board[position - 8]):
                        score += 0.05
                    if position < 56 and isWhite(board[position + 8]):
                        score += 0.05
                    if not position in (0, 8, 16, 24, 32, 40, 48, 56):
                        if position > 7 and isWhite(board[position - 9]):
                            score += 0.05
                        if position < 56 and isWhite(board[position + 9]):
                            score += 0.05

                    if not position in (7, 15, 23, 31, 39, 47, 55, 63):
                        if position > 7 and isWhite(board[position - 7]):
                            score += 0.05
                        if position < 56 and isWhite(board[position + 9]):
                            score += 0.05
                except:
                    voidK = True
        
        elif isBlack(board[position]):
            score -= basevalues[board[position] - 20] + adjustmentvalues[board[position] - 20][63 - position]
        
            if board[position] == 20 and not void:
                try:
                    if 64 > position + 1 and board[position + 1] != 20 and not position in (15, 23, 31, 39, 47, 55):
                        score += 0.05
                    
                    if board[position - 8] != 0:
                        score += 0.05
                    
                    if 64 > position + 9 and not position in (15, 23, 31, 39, 47, 55):
                        if not board[position + 9] in (20, 22, 24, 25):
                            score += 0.05
                        
                        if not board[position + 7] in (20, 22, 24, 25) and not position in (8, 16, 24, 32, 40, 48):
                            score += 0.05

                    elif 64 > position + 7 and not position in (8, 16, 24, 32, 40, 48):
                        if not board[position + 7] in (20, 22, 24, 25):
                            score += 0.05
                    
                    if 64 > position - 9:
                        if board[position - 9] in (10, 12, 14, 15) and not position in (15, 23, 31, 39, 47, 55):
                            score += 0.05

                        if board[position - 7] in (10, 12, 14, 15) and not position in (8, 16, 24, 32, 40, 48):
                            score += 0.05

                    elif 64 > position - 7:
                        if board[position - 7] in (10, 12, 14, 15) and not position in (8, 16, 24, 32, 40, 48):
                            score += 0.05
                except:
                    void = True

            elif board[position] == 25 and not voidK:
                try:
                    if 64 > position + 1 and not position in (7, 15, 23, 31, 39, 47, 55, 63) and isBlack(board[position + 1]):
                        score -= 0.05
                    if not position in (0, 8, 16, 24, 32, 40, 48, 56) and isBlack(board[position - 1]):
                        score -= 0.05
                    if position > 7 and isBlack(board[position - 8]):
                        score -= 0.05
                    if position < 56 and isBlack(board[position + 8]):
                        score -= 0.05
                    if not position in (0, 8, 16, 24, 32, 40, 48, 56):
                        if position > 7 and isBlack(board[position - 9]):
                            score -= 0.05
                        if position < 56 and isBlack(board[position + 9]):
                            score -= 0.05

                    if not position in (7, 15, 23, 31, 39, 47, 55, 63):
                        if position > 7 and isBlack(board[position - 7]):
                            score -= 0.05
                        if position < 56 and isBlack(board[position + 9]):
                            score -= 0.05
                except:
                    voidK = True
                

    #score += 0.05*(len([0 for oldpos in GetPlayerPositions(board, 10) for newpos in GetPieceLegalMoves(board, oldpos)]) - len([0 for oldpos in GetPlayerPositions(board, 20) for newpos in GetPieceLegalMoves(board, oldpos)]))
    score -= 0.1*(len([0 for oldpos in GetPlayerPositions(board, 10) if IsPositionUnderThreat(board, oldpos, 10)]) - len([0 for oldpos in GetPlayerPositions(board, 20) if IsPositionUnderThreat(board, oldpos, 20)]))
    return round(score, 2)

# Interative Deepening
def chessPlayer(board, player):
    try:
        countdown = 8.0/10
        start = time.time()

        tempboard = list(board)
        candidateMoves = []
        for oldpos in GetPlayerPositions(tempboard, player):
            for newpos in GetPieceLegalMoves(tempboard, oldpos):
                oldvalue = tempboard[oldpos]
                newvalue = tempboard[newpos]
                setmove(tempboard, oldpos, newpos)
                candidateMoves += [[[oldpos, newpos], rate(tempboard)]]
                undomove(tempboard, oldpos, newpos, oldvalue, newvalue)

        if len(candidateMoves) == 0:
            if CheckMate(tempboard, player):
                return [False, [], [], []]
            return [True, [], [], []]
        
        timetaken = time.time() - start
        countdown = countdown - timetaken
        active = None
        passive = None
        depth = 1
        while countdown >= 2*timetaken:
            with ThreadPool(processes=1) as threadpool:
                try:
                    start = time.time()
                    active = threadpool.apply_async(AlphaBeta, (tempboard, player, depth)).get(timeout=countdown)
                    if active[1] == []:
                        break
                    passive = active[1]
                    depth += 1
                    timetaken = time.time() - start
                    countdown = countdown - timetaken - 0.3
                    #print("Depth -", depth - 1, "Time Left -", countdown, "Time Taken -", timetaken, "Move -", passive)
                    if active[0] == limit or active[0] == -limit:
                        break
                except:
                    break
        
        if passive == None or passive == []:
            if player == 10:
                return [True, sorted(candidateMoves, key=lambda x: x[1])[-1][0], candidateMoves, candidateMoves]
            return [True, sorted(candidateMoves, key=lambda x: x[1])[0][0], candidateMoves, candidateMoves]
        
        #print("Depth:", depth - 1)
        return [True, passive, candidateMoves, candidateMoves]
    except:
        return [False, [], [], []]

def AlphaBeta(board, player, depth, alpha = -limit, beta = limit):
    
    if depth == 0 or CheckMate(board, 10) or CheckMate(board, 20):
        
        return [rate(board), []]

    else:
        move = []
        for oldpos in GetPlayerPositions(board, player):
            moves = GetPieceLegalMoves(board, oldpos)
            if player == 10:
                moves.reverse()
            for newpos in moves:
                oldvalue = board[oldpos]
                newvalue = board[newpos]
                setmove(board, oldpos, newpos)

                if player == 10:
                    currentscore = AlphaBeta(board, 20, depth - 1, alpha, beta)[0]
                    if currentscore > alpha:
                        alpha = currentscore
                        move = [oldpos, newpos]
                        
                else:
                    currentscore = AlphaBeta(board, 10, depth - 1, alpha, beta)[0]
                    if currentscore < beta:
                        beta = currentscore
                        move = [oldpos, newpos]

                undomove(board, oldpos, newpos, oldvalue, newvalue)
                
                if alpha >= beta:
                    if player == 10:
                        return [alpha, move]
                    else:
                        return [beta, move]

        if player == 10:
            return [alpha, move]
        else:
            return [beta, move]

def MiniMax(board, player, depth):

    if (depth == 0 or CheckMate(board, player)):
        return [rate(board), []]

    else:
        bestscore = limit
        if player == 10:
            bestscore = -limit
        move = []
        for oldpos in GetPlayerPositions(board, player):
            moves = GetPieceLegalMoves(board, oldpos)
            moves.sort()
            if player == 10:
                moves.reverse()
            for newpos in moves:
                oldvalue = board[oldpos]
                newvalue = board[newpos]
                setmove(board, oldpos, newpos)
                
                if player == 10:
                    currentscore = MiniMax(board, 20, depth - 1)[0]
                    if currentscore > bestscore:
                        bestscore = currentscore
                        move = [oldpos, newpos]

                else:
                    currentscore = MiniMax(board, 10, depth - 1)[0]
                    if currentscore < bestscore:
                        bestscore = currentscore
                        move = [oldpos, newpos]
                
                undomove(board, oldpos, newpos, oldvalue, newvalue)

                if player == 10 and bestscore == limit or player == 20 and bestscore == -limit:
                    return [bestscore, move]
                

        return [bestscore, move]

def Game():

    AI = input("AI or Human: ")
    while not (AI.upper() in "AI" or AI.upper() in "HUMAN"):
        AI = input("AI or Human: ")

    if AI.upper() in "AI":
        AI = True
    else:
        AI = False

    Turn = 0
    if AI:
        while not (Turn == 10 or Turn == 20 or Turn == -1):
            try:
                Turn = int(input("Black or White, 20 for Black, 10 for White, -1 for AI vs itself: "))
            except:
                print("", end='')
    i = 1
    OTurn = Turn
    TurnCnt = 10
    board = genboardRL()
    info = []
    StaleMate = False
    if not AI:
        print()
        print("Guidelines")
        print("-2 will allow you to choose another starting position")
        print("ERR at the new position, will let you choose another starting position")
        print("-3 at the starting position or new position will make the AI play as you against itself")
        print("-4 at the starting position or new position will let you resign")
        print("Available Starting Positions along with their New Positions have been shown to you underneath the board, these are the only legal moves available to you")
        print()
    while not (CheckMate(board, 10) or CheckMate(board, 20) or StaleMate) and i < 21:
        if Turn == TurnCnt or Turn == 0:
            renderRL(board, TurnCnt)
            if info != []:
                print("AI Move:", info[0], "to", info[1])
            for piece in GetPlayerPositions(board, TurnCnt):
                moves = GetPieceLegalMoves(board, piece)
                moves.sort()
                if moves != []:
                    print(str(piece) + ":", moves)
            data = []
            oldpos = -1
            while (not oldpos in GetPlayerPositions(board, TurnCnt) or GetPieceLegalMoves(board, oldpos) == []) and not (oldpos == -3 or oldpos == -4):
                try:
                    oldpos = int(input("Old Position: "))
                    if oldpos == -2:
                        data = chessPlayer(board, TurnCnt)
                        print("Old Position:", data[1][0])
                        try:
                            if int(input("")) == -2:
                                print("New Position:", data[1][1])
                        except:
                            oldpos = data[1][0]
                except:
                    print("", end='')
            if oldpos != -3:
                print("Available Moves:", GetPieceLegalMoves(board, oldpos))
                newpos = -1
                while not newpos in GetPieceLegalMoves(board, oldpos):
                    if not newpos in GetPieceLegalMoves(board, oldpos):
                        try:
                            newpos = input("New Position: ")
                            if newpos.upper() == "ERR":
                                oldpos = -1
                                while (not oldpos in GetPlayerPositions(board, TurnCnt) or GetPieceLegalMoves(board, oldpos) == []) and oldpos != -4:
                                    try:
                                        oldpos = int(input("Old Position: "))
                                        if oldpos == -2:
                                            data = chessPlayer(board, TurnCnt)
                                            print("Old Position:", data[1][0])
                                            try:
                                                if int(input("")) == -2:
                                                    print("New Position:", data[1][1])
                                            except:
                                                oldpos = data[1][0]
                                    except:
                                        print("", end='')
                                    if oldpos == -4:
                                        break
                            else:
                                newpos = int(newpos)
                                if newpos == -2:
                                    print("New Position:", data[1][1])
                                    input("")
                                    newpos = data[1][1]
                        except:
                            print("", end='')

                if TurnCnt == 10 and isBlack(board[newpos]):
                    if AI:
                        print("Player Takes:", getpiece(board[newpos]))
                    else:
                        print("White Takes:", getpiece(board[newpos]))

                elif TurnCnt == 20 and isWhite(board[newpos]):
                    if AI:
                        print("Player Takes:", getpiece(board[newpos]))
                    else:
                        print("Black Takes:", getpiece(board[newpos]))

                setmove(board, oldpos, newpos)
            elif oldpos == -4:
                break
            else:
                Turn = -1
                # Undo the move change, and let the AI play from your old position
                if TurnCnt == 20:
                    TurnCnt = 10
                else:
                    TurnCnt = 20
        else:
            print("Move #:", i)
            i += 1
            print("Rating:", rate(board))
            start = time.time()
            data = chessPlayer(board, TurnCnt)
            #print(MiniMax(board, TurnCnt, 4))

            if data[1] == []:
                StaleMate = True
                break

            if TurnCnt == 10 and isBlack(board[data[1][1]]):
                print("White Takes:", getpiece(board[data[1][1]]))

            elif TurnCnt == 20 and isWhite(board[data[1][1]]):
                print("Black Takes:", getpiece(board[data[1][1]]))

            setmove(board, data[1][0], data[1][1])
            if AI and OTurn != -1:
                renderRL(board, OTurn)
            else:
                renderRL(board)
            
            info = (data[1][0], data[1][1])
            print("AI Move:", info[0], "to", info[1])
            print("Duration:", time.time() - start)
            print()

        if TurnCnt == 20:
            TurnCnt = 10
        else:
            TurnCnt = 20

    if StaleMate:
        print("Stalemate")

    elif CheckMate(board, 10) and Turn == 10:
        print("AI Won")

    elif CheckMate(board, 10) and Turn == 20:
        print("Human Won")

    elif CheckMate(board, 20) and Turn == 20:
        print("AI Won")

    elif CheckMate(board, 20) and Turn == 10:
        print("Human Won")

    elif CheckMate(board, 10):
        print("Black Won")

    elif CheckMate(board, 20):
        print("White Won")

    Net = [0, 0, 0, 0, 0, 0]
    for position in range(0, 64, 1):

        if board[position] in (10, 11, 12, 13, 14, 15):
            Net[board[position] - 10] += 1
        
        elif board[position] in (20, 21, 22, 23, 24, 25):
            Net[board[position] - 20] -= 1
    
    print()
    print("Results:")
    for piece in range(6):
        print(getpiece(piece + 10) + ":", Net[piece])

