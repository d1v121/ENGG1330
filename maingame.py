import time           
import random

import animations
import function1
import function2
import function3
import function4
import validboardfunction


def main():
    animations.welcomeanimation()
    while True: 
        try:
            size, board, moves_remaining = function1.f1main()
        except UnboundLocalError:
            print("Please enter a valid difficulty! (easy, medium, hard)")
            continue
        else:
            break

    xclearlist, yclearlist, noUse = function3.checkBoardClearUpgrade(board) #initial board clear
    while len(xclearlist) != 0:
        board = function4.clearAction(xclearlist, yclearlist, board)
        board = function4.fillClear(board)
        xclearlist, yclearlist, nouse = function3.checkBoardClearUpgrade(board)
        
    score = 0 #initialise score 
    noCleared = 0 # initialise No. of moves cleared
 
    while moves_remaining >0: # main game loop 
        score = function4.score(score, noCleared) # start player cycle
        noCleared = 0
        
        function1.printBoardwScore(board, moves_remaining, score)
        while True:
            try:
                px, py, direction = function2.legal_move(board) # get player move and check valid
            except Exception:
                print("Please enter a valid move! (x,y,direction)")
                continue
            break
            
        
        function1.printBoard(function2.doSwap(board, px, py, direction))
        xclearlist, yclearlist, upgradelist = function3.checkPlayerMoveUpgrade(px, py, direction, board)
        con = True

        while con: # clear board after player move and do upgrade
            noCleared += len(xclearlist) # for calculating score
            board = function4.clearAction(xclearlist, yclearlist, board) # clearing part
            board = function4.upgradeAction(upgradelist, board) # upgrade part
            function1.printBoard(board)
            board = function4.fillClear(board) # fill in cleared space
            xclearlist, yclearlist, upgradelist = function3.checkBoardClearUpgrade(board)
            if len(xclearlist) == 0:
                con = False

        if not validboardfunction.validboardcheckerhorizontal(board) and not validboardfunction.validboardcheckervertical(board): #check if there's valid move in board
            moves_remaining = -1 
            break # loses
        moves_remaining -= 1
    score = function4.score(score, noCleared)
    function1.printBoard(board)
    if moves_remaining == -1:
        print("No move valid moves! Your score is " + str(score))
    else:
        print("You ran out of moves! Your score is " + str(score))
    
main()




