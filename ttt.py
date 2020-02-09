# tic tac toe

from random import random, randint


board = []
game = True

print()

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
    humanInputRow = int(input("Row (0-2): "))
    humanInputCol = int(input("Col (0-2): "))
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
    computerInputRow = randint(0, 2)
    computerInputCol = randint(0, 2)
    print("Computer played: Row =", computerInputRow, "Col =", computerInputCol)
    for row in range(3):
        for col in range(3):
            if board[computerInputRow][computerInputCol] == 9:
                print("computer hit its own position and plays again")
                playComputer()
                return board
            elif board[computerInputRow][computerInputCol] == 1:
                print("computer hit human's position and plays again")
                playComputer()
                return board
            elif board[computerInputRow][computerInputCol] == 0:
                board[computerInputRow][computerInputCol] = 9
                return board

def printBoard():
    print("\nPlayfield for this turn:\n")

    # row 0
    newChar = ""
    for char in board[0]:
        if char == 0:
            newChar += ". "
        if char == 1:
            newChar += "o "
        if char == 9:
            newChar += "x "
    print("  ", newChar)

    # row 1
    newChar = ""
    for char in board[1]:
        if char == 0:
            newChar += ". "
        if char == 1:
            newChar += "o "
        if char == 9:
            newChar += "x "
    print("  ", newChar)

    # row 2
    newChar = ""
    for char in board[2]:
        if char == 0:
            newChar += ". "
        if char == 1:
            newChar += "o "
        if char == 9:
            newChar += "x "
    print("  ", newChar)

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

setBoard()
while game == True:
    playHuman()
    playComputer()
    checkRows()
    checkCols()
    checkDiags()
    printBoard()
    # print("game: ", game)
else:
    print("Bye!\n")
