# tic tac toe

from random import randint


board = []
game = True

def init():
    print("\n*********************")
    print("***  TIC TAC TOE  ***")
    print("*********************")
    print("   (c) 2020 aki\n")

def winGame(message):
    print()
    print("Congratulations! You have won the game!")
    print(message)
    print()

def looseGame(message):
    print()
    print("Computer wins! Bad luck :(")
    print(message)
    print()

def gameOver():
    global game
    print("GAME OVER!")
    game = False
    return game

def setBoard():
    row1 = []
    row2 = []
    row3 = []

    for position in range(3):
        row1.append(0)

    for position in range(3):
        row2.append(0)

    for position in range(3):
        row3.append(0)

    board.append(row1)
    board.append(row2)
    board.append(row3)
    return board


def playHuman():
    print("Human's turn:")
    humanInputRow = int(input("Input row (0-2): "))
    humanInputCol = int(input("Input col (0-2): "))
    for row in range(3):
        for col in range(3):
            if board[humanInputRow][humanInputCol] == 9:
                print("You can't place your stone onto computer's position!")
                print("Please try again...")
                printBoard()
                playHuman()
                return board
            if board[humanInputRow][humanInputCol] == 1:
                print("You can't place your stone onto your own position!")
                print("Please try again...")
                printBoard()
                playHuman()
                return board
            elif board[humanInputRow][humanInputCol] == 0:
                board[humanInputRow][humanInputCol] = 1
                return board

def playComputer():
    print("\nComputer's turn:")
    computerInputRow = randint(0, 2)
    computerInputCol = randint(0, 2)
    print("Row =", computerInputRow, ", Col =", computerInputCol)
    for row in range(3):
        for col in range(3):
            if board[computerInputRow][computerInputCol] == 9:
                playComputer()
                return board
            elif board[computerInputRow][computerInputCol] == 1:
                playComputer()
                return board
            elif board[computerInputRow][computerInputCol] == 0:
                board[computerInputRow][computerInputCol] = 9
                return board

def printBoard():
    print("\nPlayfield for this turn:\n")
    print("   0 1 2")
    # row 0
    newChar = ""
    for char in board[0]:
        if char == 0:
            newChar += ". "
        if char == 1:
            newChar += "o "
        if char == 9:
            newChar += "x "
    print("0:", newChar)

    # row 1
    newChar = ""
    for char in board[1]:
        if char == 0:
            newChar += ". "
        if char == 1:
            newChar += "o "
        if char == 9:
            newChar += "x "
    print("1:", newChar)

    # row 2
    newChar = ""
    for char in board[2]:
        if char == 0:
            newChar += ". "
        if char == 1:
            newChar += "o "
        if char == 9:
            newChar += "x "
    print("2:", newChar)

    print()

def checkRows():
    # human
    if board[0] == [1,1,1]:
        winGame("You have 111 in a row 0!")
        gameOver()

    if board[1] == [1,1,1]:
        winGame("You have 111 in a row 1!")
        gameOver()

    if board[2] == [1,1,1]:
        winGame("You have 111 in a row 2!")
        gameOver()

    # computer
    if board[0] == [9,9,9]:
        winGame("Computer has 999 in a row 0!")
        gameOver()

    if board[1] == [9,9,9]:
        winGame("Computer has 999 in a row 1!")
        gameOver()

    if board[2] == [9,9,9]:
        winGame("Computer has 999 in a row 2!")
        gameOver()

def checkCols():
    # human
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        winGame("You have 111 in a col | 0!")
        gameOver()

    if board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        winGame("You have 111 in a col | 1!")
        gameOver()

    if board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        winGame("You have 111 in a col | 2!")
        gameOver()

    # computer
    if board[0][0] == 9 and board[1][0] == 9 and board[2][0] == 9:
        looseGame("Computer has 999 in a col | 0!")
        gameOver()

    if board[0][1] == 9 and board[1][1] == 9 and board[2][1] == 9:
        looseGame("Computer has 999 in a col | 1!")
        gameOver()

    if board[0][2] == 9 and board[1][2] == 9 and board[2][2] == 9:
        looseGame("Computer has 999 in a col | 2!")
        gameOver()

def checkDiags():
    # human
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        winGame("You have 111 in a diag \\!")
        gameOver()

    if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        winGame("You have 111 in a diag /!")
        gameOver()

    # computer
    if board[0][2] == 9 and board[1][1] == 9 and board[2][0] == 9:
        looseGame("Computer has 999 in a diag / !")
        gameOver()

    if board[0][0] == 9 and board[1][1] == 9 and board[2][2] == 9:
        looseGame("Computer has 999 in a diag \\ !")
        gameOver()

# main loop
init()
setBoard()
while game == True:
    playHuman()
    playComputer()
    checkRows()
    checkCols()
    checkDiags()
    printBoard()
else:
    print("Bye!\n")
