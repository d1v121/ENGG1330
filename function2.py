
#check validity of player's input
#not debugged
'''a move is valid if:
1. two pieces involved in the swap are within the board boundaries
2. the direction inputted is one of w, a, s, d.
3. after the pieces are swapped, at least one of 
them have adjacent pieces of the same type 
(that can form either a row or column of 3) which
qualifies for elimination.  '''

'''this checking function is carried out after 
the board is generated, checked for any
possible upgrades and elimination. 
This function serve to make sure the player's input 
will result in a new elimination, and is worth continue 
checking for higher upgrades'''

def swap(board, x1, y1, x2, y2):
    board[y1][x1], board[y2][x2] = board[y2][x2], board[y1][x1]
    return board

def doSwap(board, x, y, direction):
    if direction == "w":
        new_x, new_y = x, y + 1
    elif direction == "a":
        new_x, new_y = x - 1, y
    elif direction == "s":
        new_x, new_y = x, y - 1
    elif direction == "d":
        new_x, new_y = x + 1, y
    return swap(board, x, y, new_x, new_y)

#helper function 2
def check_for_matches(board):
    # function to see if the swap meets the minimum requirement (three identical pieces in a row or column)
    for y in range(len(board)):
        for x in range(len(board)):
            piece = board[y][x]
            # Check horizontally for matches
            if x < len(board) - 2 and piece.lower() == (board[y][x + 1].lower()) == (board[y][x + 2].lower()):
                return True  # if a horizontal match is found
            # Check vertically for matches
            if y < len(board) - 2 and piece.lower() == (board[y + 1][x].lower()) == (board[y + 2][x].lower()):
                return True  # if a vertical match is found
    return False

# helper function 3 to check if both pieces involved in the swap are within the board boundaries
def validate_input(board, x1, y1, x2, y2):
    # condition 1 (the position given by the player cannot be negative)
    if x1 < 0 or y1 < 0:
        return False
    # condition 2 (the position given by the player cannot exceed the range of the row and the column of the board)
    if x1 > len(board) - 1 or y1 > len(board) - 1:
        return False
    # apply the same conditions to the other piece
    if x2 < 0 or y2 < 0:
        return False
    if x2 > len(board) - 1 or y2 > len(board) - 1:
        return False

    #if one of the pieces being swapped is a super, then it automatically passes the validity check
    if (board[y1][x1] == "A" or board[y2][x2] == "A"):
        if not (board[y1][x1] == "A" and board[y2][x2] == "A"):
            return True
        else:
            return False

    board = swap(board, x1, y1, x2, y2)
    # Check for matches after the swap
    match_found = check_for_matches(board)
    # Undo the swap
    board = swap(board, x1, y1, x2, y2)
    # if there is match_found is true, it means the move is valid
    return match_found

#main function starts here:
def legal_move(board):
    # ask the player to input in the format: x, y, direction
    while True:
        command = input("Please enter the piece you'd like to swap, and the direction for swapping (x,y,dir): ").split(",")
        x, y, direction = int(command[0]) - 1, int(command[1]) - 1, command[2]
        # find the coordinates of the other piece based on which direction given for the swap
        if direction == "w":
            new_x, new_y = x, y + 1
        elif direction == "a":
            new_x, new_y = x - 1, y
        elif direction == "s":
            new_x, new_y = x, y - 1
        elif direction == "d":
            new_x, new_y = x + 1, y
        else:
            print("This move is invalid! Please try a different move!")
            continue

        if validate_input(board, x, y, new_x, new_y):
            return x, y, direction
        else:
            print("This move is invalid! Please try a different move!")
            continue

