import random
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentplayer = 'X'
winner = None
gamerunning = True

def printboard(board):
    print(board[0] + ' | ' + board[1] +' | '+ board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] +' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] +' | ' + board[8])

def playerinput(board):
    inp = int(input('Enter a number through 1 to 9: '))
    if inp >= 1 and inp <= 9 and board[inp-1]=='-':
        board[inp-1] = currentplayer
    else:
        print('There is a cross or knot already at the spot or your input was incorrect')

def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

def checktie(board):
    global gamerunning
    if '-' not in board:
        printboard(board)
        print('Game was a tie')
        gamerunning = False

def switchplayer():
    global currentplayer
    if currentplayer == 'X':
        currentplayer = 'O'
    else:
        currentplayer = 'X'

def checkwin():
    global gamerunning
    if checkdiagonal(board) or checkhorizontal(board) or checkrow(board):
        print(f'The winner is {winner}')
        gamerunning = False

def computer(board):
    while currentplayer == 'O':
        position = random.randint(0,8)
        if board[position] == '-':
            board[position] = 'O'
            switchplayer()


while gamerunning:
    printboard(board)
    playerinput(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)

