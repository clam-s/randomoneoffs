
import copy


board = [["-" for i in range(3)]for i in range(3)]
validChars = ["a","b","c"]
def pboard(oboard): #using oboard so that can show other than main board if needed
   print(f"""
   a   b   c
1  {oboard[0][0]}   {oboard[0][1]}   {oboard[0][2]}
       
2  {oboard[1][0]}   {oboard[1][1]}   {oboard[1][2]}
       
3  {oboard[2][0]}   {oboard[2][1]}   {oboard[2][2]}
""")
def wincheck(oboard):#True if won False if no player has won uses oboard because also used in eval
    for i in range(3):
        if oboard[0][i] == oboard[1][i] == oboard[2][i] !="-":
            return True
        if oboard[i][0] == oboard[i][1] == oboard[i][2] !="-":
            return True
    if oboard[0][0] == oboard[1][1] == oboard[2][2] != "-":
        return True
    if oboard[2][0] == oboard[1][1] == oboard[0][2] != "-":
        return True
    return False
def playerTurn(turn):#note if you want to evaluate the board as a player you can do it with eval 1
    if turn%2 == 0:
        player = "X"
    else:
        player = "O"
    print(f"player {player} turn make your move")
    validmove = False
    while not validmove:
        pboard(board)
        move = input("enter your move \n").split()
        if len(move) !=2:
            print("you made a mistake while entering move please put it in the format (letter coordinate) (number coordinate)")
            continue
        if move[0] == "evaluate" or move[0] == "eval":
            pboard(evaluate(board,turn)[0])
            continue
        try:
            move[1] = int(move[1])
        except ValueError:
            print("you made a mistake while entering move please put it in the format (letter coordinate) (number coordinate)")
            continue
        if move[1]<1 or move[1]>3:
            print("you made a mistake while entering move please put it in the format (letter coordinate) (number coordinate)")
            continue
        invalidChars = True
        for i in range(3):
            if move[0] == validChars[i]:
                move[0] = i
                invalidChars = False
        if invalidChars:
            print("you made a mistake while entering move please put it in the format (letter coordinate) (number coordinate)")
            continue
        move[1] -= 1
        if board[move[1]][move[0]] != "-":
            print("this spot has been taken please enter another move")
        else:
            board[move[1]][move[0]] = player
            validmove = True
def evaluate(pos,turn) :#returns list and float
   #print(turn)
   #pboard(pos)


    if turn == 8:#auto return if draw, returns eval board, board avg
        return pos,0
    if turn >=4: #win only possible after 5 moves. is 4 because turns start at 0
        if wincheck(pos):
            if (turn-1)%2 == 0:
                return pos,1
            else:
                return pos,-1
    evalBoard = copy.deepcopy(pos)#makes a copy of the board to put evals(use deep copy because python when using .copy() on an array copies the outside but keeps ref on the inside)
   #pboard(eval)
   #both vars used for calc avg later
    count = 0
    rtotal = 0
    for i in range(3):
        for j in range(3):
            if pos[i][j] == "-":
                count += 1
                if turn%2 == 0:
                    pos[i][j] = "X"
                else:
                    pos[i][j] = "O"
                temp = evaluate(pos,turn+1)[1] # finds the average value of the next board
                pos[i][j] = "-"
                evalBoard[i][j] = temp
                rtotal+= temp
               #pboard(eval)
    temp = round((rtotal/count),3) # the average value of the board
    return evalBoard ,temp
         
#main game loop
print("-----------------------Aydin's Tic Tac Toe-----------------------")
validIn = False
while not validIn:
    print("""
enter 1 to play against a friend
enter 2 to play against bot""")
    try:
        option = int(input())
    except:
        print("enter a number")
    if option<=2 or option>=1:
       validIn = True
print("enter your moves in the following format: \n[letter coordinate][space][number coordinate] \npress enter to continue")
input()




if option == 1:
    turn = -1 #turns start on -1
    won = False
    while turn<8 and not won:
        turn +=1
        playerTurn(turn)
        won = wincheck(board)








if option ==2:
    start = "A"
    while start not in ["x","o"]:
        start = input("would you like to start as x or o \n").lower()
    turn = -1
    won = False
    if start == "x":
        while turn<8 and not won:
            turn += 1
            if turn%2 == 0:
                playerTurn(turn)
                pboard(board)
            else:
               
                small = [0,0,2] #index index current smallest found
                if turn == 7: #handles special case on the 7th move where eval doesn't work(dont know why)
                    for i in range(3):
                        for j in range(3):
                            evals,null = evaluate(board,turn-1)
                            if isinstance(evals[i][j], (int,float)):
                                if -evals[i][j] == -1:
                                    small= [i,j]
                else:
                    evals,null = evaluate(board,turn)
                    for i in range(3):# searches for the most advantageous move for O according to evaluation
                        for j in range(3):
                            if board[i][j] == "-":
                                if isinstance(evals[i][j], (int,float)):
                                    if evals[i][j] < small[2]:
                                        small = [i,j,evals[i][j]]
                board[small[0]][small[1]] = "O"
                print("bot move")
                #print(small)
                pboard(board)
            won = wincheck(board)
    else:
        while turn<8 and not won:
            turn += 1
            if turn%2 != 0:
                playerTurn(turn)
                pboard(board)
            else:
                evals,_ = evaluate(board,turn)#
                small = [0,0,-2] #index index current smallest found
                if turn == 8: #handles special case that happens on move 8(again no idea why it happens)
                    for i in range(3):
                        for j in range(3):
                            if board[i][j] == "-":
                                small = [i,j,-3]
                else:
                    for i in range(3):
                         for j in range(3):
                            if board[i][j] == "-":
                                if isinstance(evals[i][j], (int,float)):
                                    if evals[i][j] > small[2]:
                                        small = [i,j,evals[i][j]]
                board[small[0]][small[1]] = "X"
                print("bot move")
                pboard(board)
             
                won = wincheck(board)












#stuff to conclude the game
pboard(board)
if won:
   if turn%2 == 0:
       print("X has won")
   else:
       print("O has won")
else:
   print("Draw")
