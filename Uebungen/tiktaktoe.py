#   | 1 | 2 | 3 |
#   -------------
#   | 4 | 5 | 6 |
#   -------------
#   | 7 | 8 | 9 |

board = []
currentPlayer = ""
winner = ""

def boardIntial():
    global currentPlayer
    board.clear()
    for i in range(10):
        board.append("-")
    currentPlayer = "X"

def printBoard():
    print(f"\n  | {board[1]} | {board[2]} | {board[3]} |")
    print("  -------------")
    print(f"  | {board[4]} | {board[5]} | {board[6]} |")
    print("  -------------")
    print(f"  | {board[7]} | {board[8]} | {board[9]} |")

def checkVerti():
    global winner
    for col in [(1,4,7), (2,5,8), (3,6,9)]:
        if board[col[0]] == board[col[1]] == board[col[2]] != "-":
            winner = board[col[0]]
            return True
    return False

def checkHori():
    global winner
    for row in [(1,2,3), (4,5,6), (7,8,9)]:
        if board[row[0]] == board[row[1]] == board[row[2]] != "-":
            winner = board[row[0]]
            return True
    return False

def checkDiag():
    global winner
    for diag in [(1,5,9), (3,5,7)]:
        if board[diag[0]] == board[diag[1]] == board[diag[2]] != "-":
            winner = board[diag[0]]
            return True
    return False

def changePlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def checkWin():
    if checkVerti() or checkHori() or checkDiag():
        return True

def checkTie():
    for i in range(1, 10):
        if board[i] == "-":
            return False
    return True


boardIntial()

while True:
    printBoard()
    zug = int(input(f"Spieler {currentPlayer}, wähle ein Feld (1-9): "))

    if board[zug] != "-":
        print("Feld bereits belegt! Nochmal.")
        continue

    board[zug] = currentPlayer

    if checkWin():
        printBoard()
        print(f"Spieler {winner} hat gewonnen!")
        break

    if checkTie():
        printBoard()
        print("Unentschieden!")
        break

    changePlayer()