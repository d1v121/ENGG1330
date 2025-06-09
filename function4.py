     # other functions: (Bosco do)
#

import random

def clearAction(xclearlist, yclearlist, board): # do this before upgradeAction()
    for i in range(len(xclearlist)): # execute the clearing 
        x = xclearlist[i]
        y = yclearlist[i]
        board[y][x] = " "
    return board

def upgradeAction(upgradelist, board):
    for s in upgradelist.keys(): # execute the upgrading
        for i in upgradelist[s]:
            x = i[0]
            y = i[1]
            board[y][x] = s
    return board

def fillClear(board): # fill in any empty space after the clearAction 
    c, r = len(board), len(board[0])
    gamePieces = ["h", "d", "s", "c"]
    spacefound = True
    while spacefound:
        spacefound = False
        for x in range(r):
            for y in range(c):
                if board[y][x] == " " and y < c - 1:
                    board[y][x] = board[y + 1][x]
                    board[y + 1][x] = " "
                    spacefound == True

    for y in range(c):
        for x in range(r):
            if board[y][x] == " ":
                board[y][x] = random.choice(gamePieces)
    
    return board

def score(score, noCleared):
    if noCleared >= 10: 
        noCleared * 2 # got multiplier for move cleared 

    elif noCleared >= 5:
        noCleared * 1.5
    
    score += noCleared
    return score



