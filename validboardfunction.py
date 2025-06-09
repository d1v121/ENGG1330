def validboardcheckerhorizontal(board):
    for y in range(len(board)):
        for x in range(len(board[y])-1): # Adjusted range to avoid index out of range error
            if board[y][x] == "A": 
                return True
            elif board[y][x].lower() == board[y][x + 1].lower():
                if y - 1 in range(len(board)) and x - 1 in range(len(board[y])) and board[y - 1][x - 1].lower() == board[y][x].lower():
                    return True
                elif y + 1 in range(len(board)) and x - 1 in range(len(board[y])) and board[y + 1][x - 1].lower() == board[y][x].lower():
                    return True
                elif y - 1 in range(len(board)) and x + 2 in range(len(board[y])) and board[y - 1][x + 2].lower() == board[y][x].lower():
                    return True
                elif y + 1 in range(len(board)) and x + 2 in range(len(board[y])) and board[y + 1][x + 2].lower() == board[y][x].lower():
                    return True
    return False


def validboardcheckervertical(board):
    for y in range(len(board)-1):  # Adjusted range to avoid index out of range error
        for x in range(len(board[y])):
            if board[y][x] == "A":
                return True
            elif y - 1 in range(len(board)) and board[y][x].lower() == board[y - 1][x].lower():
                if y + 1 in range(len(board)) and x - 1 in range(len(board[y])) and board[y + 1][x - 1].lower() == board[y][x].lower():
                    return True
                elif y + 1 in range(len(board)) and x + 1 in range(len(board[y])) and board[y + 1][x + 1].lower() == board[y][x].lower():
                    return True
                elif y - 2 in range(len(board)) and x - 1 in range(len(board[y])) and board[y - 2][x - 1].lower() == board[y][x].lower():
                    return True
                elif y - 2 in range(len(board)) and x + 1 in range(len(board[y])) and board[y - 2][x + 1].lower() == board[y][x].lower():
                    return True
    return False



