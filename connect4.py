import re
from time import sleep as wait

RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"  
CLEAR = "\033c"

board = [['-' for _ in range(7)]for _ in range(6)]

def pboard():
    print("1  2  3  4  5  6  7")
    for i in range(6):
        for j in range(7):
            match board[i][j]:
                case "B":
                    print(f"{BLUE}O {RESET}", end = " ")
                case "R":
                    print(f"{RED}O {RESET}", end = " ")
                case _:
                    print(f"{RESET}- {RESET}", end = " ")
        print()

def gravityAnim(col):
    wait(0.1)
    j = 0
    print(CLEAR)
    pboard()
    for j in range(5):
        if board[j+1][col] == '-':
            board[j][col], board[j+1][col] = board[j+1][col],board[j][col]
            wait(0.1)
            print(CLEAR)
            pboard()
        else:
            break
    return j+1

def isful(col):
    if board[0][col] != '-':
        return True
    return False

def winCheck(x,y,board): #expand from last entry approach
    left = 5
    right = -1
    for _ in range(5):
        left -= 1
        right+= 1
        if x-left < 0:
            continue
        if x + right >7:
            continue
        coords = range(x-left,x+right+2)
        if board[y][coords[0]] == board[y][coords[1]] == board[y][coords[2]] == board[y][coords[3]] != '-': 
            return True
    up = 5
    down = -1

    for _ in range(5):
        up -= 1
        down+= 1
        if y-up< 0:
            continue
        if y + down>6:
            continue
        coords = range(y-up,y+down+2)
        if board[coords[0]][x] == board[coords[1]][x] == board[coords[2]][x] == board[coords[3]][x] != '-': 
            return True
    y -=1 
    for delta in range(-3,1):
        if y +delta >= 0 and y+delta +3 <=5:
            if x + delta  >=0 and x + delta + 3 <= 6:
                if board[y+delta][x+delta] == board[y+delta+1][x+delta+1] == board[y+delta+2][x+delta+2] == board[y+delta+3][x+delta+3] != '-':
                    return True
            if x - delta  <=6 and x - delta - 3 >= 0:
                if board[y+delta][x-delta] == board[y+delta+1][x-delta-1] == board[y+delta+2][x-delta-2] == board[y+delta+3][x-delta-3] != '-':
                    return True
                
    return False


def playerturn(color):
    validIn = False
    while not validIn:
        In = 0
        In = input(f"{color} to play enter a coloumn number")
        if len(In) != 1:
            print("Please only type 1 digit")
            continue
        try:
            In = int(In) -1
        except ValueError:
            print("please enter a number")
            continue
        if In not in range(0,7):
            print("please enter a valid coloumn")
            continue
        if isful(In):
            print("please enter a coloumn with avalible rows")
        validIn = True
    return int(In)

def game():
    colour = 'R'
    pboard()
    for _ in range(7*6):
        if colour == 'R':
            colour = 'B'
        else:
            colour = "R"
        Inp = playerturn(colour)
        board[0][Inp] = colour
        y =gravityAnim(Inp)
        won = winCheck(Inp,y,board)
        if won:
            break

    if won:
        print(f"{colour} won")
    else:
        print("draw")


game()
