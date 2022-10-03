import random

# ● Your challenge will be
# ● Writing the core logic for the tic-tac-toe game.
# ○ No UI work is needed, only the core logic.

# ● Rules of the game
# ○ There are only two players, respectively X & O.
# ○ Any of the players can start the game.
# ○ Players play turns by putting their marks on empty squares.
# ○ The first player to get 3 of its marks in a row wins the game.
# ○ When all 9 squares are full, the game is over.

# TODO: Create a class
#  Create def board that will be played on and print it
#  Create def choose player (with random int)
#  Create option for player to make first call on te board
#  Visualise it on the board
#  Create function with the rules
#  #

# TODO: What I find difficult is the OOP concept


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

running = True

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def choosePlayer(self):
    symbolX = 'X'
    symbolO = 'O'

    chooseSymbol = input('What symbol do you choose?(X or O): ')

    if chooseSymbol == 'X':
        player1 = symbolX
        player2 = symbolO
    else:
        player1 = symbolO
        player2 = symbolX

    r = random.randint(0,1)
    options = [player1, player2]

    for x in options:
        playertomove = options[r]
        print(f'The player that starts first is player: {playertomove}\n')
    print(playertomove)

def input(board):
    print('You can choose between number 1-9. Where number 1-3 = row 1, 4-6 = row 2, 7-9 = row 3')
    choice = int(input('Please select a spot: '))

    if board[choice-1] == '-':
         board[choice - 1] = playertomove
    else:
        print('Spot is already taken')

# Check for win
def checkHorizontal(board):
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def checkVerical(board):
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[3]
        return True

def checkDiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def checkWin(board):
    pass




def switchPlayer(self):
    global playertomove
    if playertomove == "X":
        playertomove = "O"
    else:
        playertomove = "X"


while running:
    printboard(board)
    choosePlayer(board)
    input(board)

