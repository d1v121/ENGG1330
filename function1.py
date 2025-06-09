# board generation
import time
import random

def gameDifficulty():
    difficulty = input("Please choose a game difficulty (easy (7*7), medium (10*10), hard (13*13)): ")
    if difficulty == "easy":
        size = 7
        moves_remaining = 10 #to be tested later 
    elif difficulty == "medium":
        size = 10
        moves_remaining = 30 
    elif difficulty == "hard":
        size = 13
        moves_remaining = 35 
    
    return size, moves_remaining 

def createBoard(size):
    gamePieces = ["h", "d", "s", "c"]
    return [random.choices(gamePieces, k=size) for i in range(size)]

def printBoard(board):  
    size = len(board[0])
    out = ""
    space = "  "
    for y in range(size - 1,-1, -1):
        out += str(y+1).zfill(2) + " "
        for i in range(size):
            out += (convert(board[y][i]) + space)
            if i == size - 1:  # next row for last one
                out += "\n"
        
        out += "  "
        for n in range(size):
            out += str(n+1).zfill(2) + " "
        out += "\r"
    print(out)
    time.sleep(0.3)

def printBoardwScore(board, moves_remaining, score):  
    size = len(board[0])
    out = ""
    space = "  "
    for y in range(size - 1,-1, -1):
        out += str(y+1).zfill(2) + " "
        for i in range(size):
            out += (convert(board[y][i]) + space)
            if i == size - 1:  # next row for last one
                if y == 0:
                    out += ("Moves remaining: " + str(moves_remaining))
                out += "\n"
        
        out += "  "
        for n in range(size):
            out += " "
        out += "\r"
    out += "   "
    for n in range(size):
        out += str(n+1).zfill(2) + " "
    out += ("Score: " + str(score))
    print(out)
    time.sleep(0.3)

def convert(letter):  # convert letter into symbol
    if letter.lower() == "h":
        if letter == "H":
            return "♥"
        else:
            return "♡"
    elif letter.lower() == "d":
        if letter == "D":
            return "♦"
        else:
            return "♢"
    elif letter.lower() == "s":
        if letter == "S":
            return "♠"
        else:
            return "♤"
    elif letter.lower() == "c":
        if letter == "C":
            return "♣"
        else:
            return "♧"
    elif letter == "A":
        return "✮"
    else: return letter

def f1main():
    size, moves_remaining  = gameDifficulty()
    board = createBoard(size)
    return size, board, moves_remaining 





