# function to be made/made already: (Bosco do)
#
# checkPlayerMoveUpgrade for checking player movement caused board changes (done, not debugged)
# checkBoardClearUpgrade for checking board clear caused board changes (done, not debugged)
# checkPositionMoveUpgrade is a internal function of checkBoardClearUpgrade and checkPlayerMoveUpgrade that check given positions to determine which positions to be cleared and upgraded(done, not debugged)
# findSymbolInBoard is an internal function of checkPlayerMoveUpgrade for finding the positon of a certain symbol and it's upgrade in the board so they can be cleared(done, not debugged)
# symbolUpgradeClearlistPrint is an internal function of checkPositionMoveUpgrade to print out the positions that is cleared by a upgraded symbol(done, not debugged)


####IMPORTANT: DO CLEARLIST BEFORE UPGRADELIST

def checkPlayerMoveUpgrade(x, y, direction, board): # move should be already proven valid, only call after player input, not when board clear
    surrounding = {"w": [x, y + 1], "a": [x - 1, y], "s": [x, y - 1], "d": [x + 1, y]}
    swapped = surrounding[direction] # position of the swapped symbol
    positionSymbols = [board[y][x], board[swapped[1]][swapped[0]]]

    if "A" not in positionSymbols: # check if either of them is super
        xclearlist, yclearlist, upgradedict = checkBoardClearUpgrade(board)
    elif positionSymbols[0] == "A": # clear the same type of symbol that's not super
        upgradedict = {"H": [], "D": [], "S": [], "C": [], "A": []}
        xclearlist, yclearlist = findSymbolInBoard(board, positionSymbols[1])
        xclearlist.append(swapped[0])
        yclearlist.append(swapped[1])
        xclearlist.append(x)
        yclearlist.append(y)
    elif positionSymbols[1] == "A":
        upgradedict = {"H": [], "D": [], "S": [], "C": [], "A": []}
        xclearlist, yclearlist = findSymbolInBoard(board, positionSymbols[0])
        xclearlist.append(x)
        yclearlist.append(y)
        xclearlist.append(swapped[0])
        yclearlist.append(swapped[1])
    
    return xclearlist, yclearlist, upgradedict

def checkBoardClearUpgrade(board): #main function of checking board
    c, r = len(board), len(board[0])
    checkposition = []
    for y in range(c):
        for x in range(r):
            checkposition.append([x, y]) # give very position of the board to check
    xclearlist, yclearlist, upgradedict = checkPositionMoveUpgrade(board, checkposition)

    return xclearlist, yclearlist, upgradedict 


def findSymbolInBoard(board, symbol): # check every position of the board to find the position of a type of symbols
    c, r = len(board), len(board[0])
    xfoundList = []
    yfoundList = []
    for y in range(c):
        for x in range(r):
            if board[y][x].lower() == symbol: # if is the type add to clearlist
                    xfoundList.append(x)
                    yfoundList.append(y)
    return xfoundList, yfoundList

def checkPositionMoveUpgrade(board, checkPosition):
    c, r = len(board), len(board[0])
    xclearlist = []
    yclearlist = []
    upgradedict = {"H": [], "D": [], "S": [], "C": [], "A": []}
    xcooldown = 0 # for making sure that each combination is only counted one for effiency and upgraded symbol are added appropiatly
    ycooldown = 0
    tempy = -0 # for getting ycooldown withour double counting
    for position in checkPosition: # check for the positions
        px = position[0]
        py = position[1]
        xcount = 1 # check number of same symbol for row
        ycount = 1 # for column
        xupgradeCount = 0 # count number of upgraded symbol in the row
        yupgradeCount = 0 # count number of upgraded symbol in the column
        lx = px # left of inputted position
        rx = px # right of inputted position
        uy = py # up of the inputted position
        dy = py # down of the inputted position
        symbol = board[py][px].lower() # get the type of the symbol
        
        if lx - 1 >= 0: # check if the current checking symbol is at the side
            while True:
                lx -= 1 #check next checking symbol
                if board[py][lx].lower() != symbol: # if not the same sybol reverse action and stop
                    lx += 1
                    break
                if board[py][lx].isupper():
                    xupgradeCount += 1 # if the current checking symbol is upgraded, + 1
                xcount += 1 # count the number of the same symbols in a row
                if lx - 1 < 0:
                    break
        if rx + 1 <= r - 1: # ^
            while True:
                rx += 1
                if board[py][rx].lower() != symbol:
                    rx -= 1
                    break
                if board[py][rx].isupper():
                    xupgradeCount += 1
                xcount += 1
                if rx + 1 > r - 1:
                    break
        if dy - 1 >= 0: # ^
            while True:
                dy -= 1
                if board[dy][px].lower() != symbol:
                    dy += 1
                    break
                if board[dy][px].isupper():
                    yupgradeCount += 1
                ycount += 1
                if dy - 1 < 0:
                    break
        if uy + 1 <= c - 1: # ^
            while True:
                uy += 1
                if board[uy][px].lower() != symbol:
                    uy -= 1
                    break
                if board[uy][px].isupper():
                    yupgradeCount += 1
                ycount += 1
                if uy + 1 > c - 1:
                    break

        if xcount >= 3 and ycount >= 3: # L or T shape
            if xupgradeCount + yupgradeCount != 0: # if there's a upgraded symbol
                xtemplist, ytemplist = symbolUpgradeClearlistPrint(px, py, symbol, xupgradeCount + yupgradeCount, board)
                for i in range(len(xtemplist)):
                    xclearlist.append(xtemplist[i])
                    yclearlist.append(ytemplist[i])
            for y in range(dy, uy + 1):
                xclearlist.append(px)
                yclearlist.append(y)
            for x in range(lx, rx + 1):
                xclearlist.append(x)
                yclearlist.append(py)
            upgradedict["A"].append([px, py]) # add super 

        elif xcount >= 3 and xcooldown == 0:
            if xupgradeCount != 0: # if there's a upgraded symbol in the row
                xtemplist, ytemplist = symbolUpgradeClearlistPrint(px, py, symbol, xupgradeCount, board)
                for i in range(len(xtemplist)): # extracting the x/y clearlist
                    xclearlist.append(xtemplist[i])
                    yclearlist.append(ytemplist[i])
            if xcount >= 5:
                for x in range(lx + 3, rx - 1): # for row of 5, 1 super. for row of 6, 2 super ,etc
                    upgradedict["A"].append([x, py])
            elif xcount == 4: # upgrade to upgraded symbol for 4 in a row
                upgradedict[symbol.upper()].append([px, py])
            for x in range(lx, rx + 1): # for all xcount >= 3, clear the symbols
                xclearlist.append(x)
                yclearlist.append(py)
            xcooldown = xcount

        elif ycount >= 3 and ycooldown == 0:
            if yupgradeCount != 0: # if there's a upgraded symbol in the row
                xtemplist, ytemplist = symbolUpgradeClearlistPrint(px, py, symbol, xupgradeCount, board)
                for i in range(len(ytemplist)): # extracting the x/y clearlist
                    xclearlist.append(xtemplist[i])
                    yclearlist.append(ytemplist[i])
            if ycount >= 5:
                for y in range(dy + 3, uy - 1): # for row of 5, 1 super. for row of 6, 2 super ,etc
                    upgradedict["A"].append([x, py])
            elif ycount == 4: # upgrade to upgraded symbol for 4 in a row
                upgradedict[symbol.upper()].append([px, py])
            for y in range(dy, uy + 1): # for all xcount >= 3, clear the symbols
                xclearlist.append(px)
                yclearlist.append(y)
            ycooldown = ycount + 1

        if xcooldown > 0:
            xcooldown -= 1
        if ycooldown > 0 and py != tempy:
            tempy = py
            ycooldown -= 1

    return xclearlist, yclearlist, upgradedict


def symbolUpgradeClearlistPrint(px, py, symbol, upgradeCount, board):
    c, r = len(board), len(board[0])
    rmax = min([r - 1, px + (upgradeCount) + 1]) # the end of the row
    rmin = max([-1, px - (upgradeCount)]) # the start of row
    cmax = min([c - 1, py + (upgradeCount) + 1]) # the end of column
    cmin = max([-1, px - (upgradeCount)]) # the start of column
    xlist = [] # list of x position to be cleared
    ylist = [] # list of y position to be cleared
    symbol = symbol.upper()

    if symbol == "H":
        for y in range(cmin + 1, cmax + 1): # give the height of the row to be cleared
            for x in range(0, r): # whole row clear
                ylist.append(y)
                xlist.append(x)
    elif symbol == "D":
        for y in range(0, c): # whole column clear
            for x in range(rmin + 1, rmax + 1): # give the width of the column to be cleared
                ylist.append(y)
                xlist.append(x)
    elif symbol == "S":
        for y in range(cmin + 1, cmax + 1): # give box height
            for x in range(rmin + 1, rmax + 1): # give box width
                ylist.append(y)
                xlist.append(x) 
    elif symbol == "C":
        for y in range(0, c): # for the whole column
            if py % 2 == y % 2: # find if a certain y position is odd or even like the inputted y position
                xlist.append(px)
                ylist.append(y)
        for x in range(0, r): # for the whole row
            if px % 2 == x % 2: # find if a certain x position is odd or even like the inputted x position
                xlist.append(x)
                ylist.append(py)
    return xlist, ylist # xclearlist, yclearlist
