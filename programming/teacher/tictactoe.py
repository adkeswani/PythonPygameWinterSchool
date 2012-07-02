TOP_LEFT = 0
TOP_MIDDLE = 1
TOP_RIGHT = 2
MIDDLE_LEFT = 3
MIDDLE_MIDDLE = 4
MIDDLE_RIGHT = 5
BOTTOM_LEFT = 6
BOTTOM_MIDDLE = 7
BOTTOM_RIGHT = 8

squares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
numFreeSquares = 9
currPlayer = "O"
won = False

def doMove(squares, currPlayer):
    move = int(raw_input())
    if move > 9 or move < 1 or squares[move - 1] == "X" or squares[move - 1] == "O":
        return False
    else:
        squares[move - 1] = currPlayer
        return True

def hasWon(squares, currPlayer):
    #Rows
    if squares[TOP_LEFT] == currPlayer and squares[TOP_MIDDLE] == currPlayer and squares[TOP_RIGHT] == currPlayer:
        return True
    elif squares[MIDDLE_LEFT] == currPlayer and squares[MIDDLE_MIDDLE] == currPlayer and squares[MIDDLE_RIGHT] == currPlayer:
        return True
    elif squares[BOTTOM_LEFT] == currPlayer and squares[BOTTOM_MIDDLE] == currPlayer and squares[BOTTOM_RIGHT] == currPlayer:
        return True
    #Columns
    elif squares[TOP_LEFT] == currPlayer and squares[MIDDLE_LEFT] == currPlayer and squares[BOTTOM_LEFT] == currPlayer:
        return True
    elif squares[TOP_MIDDLE] == currPlayer and squares[MIDDLE_MIDDLE] == currPlayer and squares[BOTTOM_MIDDLE] == currPlayer:
        return True
    elif squares[TOP_RIGHT] == currPlayer and squares[MIDDLE_RIGHT] == currPlayer and squares[BOTTOM_RIGHT] == currPlayer:
        return True
    #Diagonals
    elif squares[TOP_RIGHT] == currPlayer and squares[MIDDLE_MIDDLE] == currPlayer and squares[BOTTOM_LEFT] == currPlayer:
        return True
    elif squares[TOP_LEFT] == currPlayer and squares[MIDDLE_MIDDLE] == currPlayer and squares[BOTTOM_RIGHT] == currPlayer:
        return True
    else:
        return False

def display (squares):
    print squares[TOP_LEFT], squares[TOP_MIDDLE], squares[TOP_RIGHT]
    print squares[MIDDLE_LEFT], squares[MIDDLE_MIDDLE], squares[MIDDLE_RIGHT]
    print squares[BOTTOM_LEFT], squares[BOTTOM_MIDDLE], squares[BOTTOM_RIGHT]

while numFreeSquares > 0 and not won:
    display(squares)

    print "Player", currPlayer, "enter the square number for your move"

    while not doMove(squares, currPlayer):
        print "Invalid move. Please enter the square number for your move"

    numFreeSquares = numFreeSquares - 1

    if hasWon(squares, currPlayer):
        print "Player", currPlayer, "wins!"
        won = True
    else:
        if currPlayer == "O":
            currPlayer = "X"
        else:
            currPlayer = "O"
