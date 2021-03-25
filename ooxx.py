board=str([[i+1+k*3 for i in range(3)] for k in range(3)])

print(board)


def drawBoard(board):
    count = 0
    array = 0
    while count < 13:
        if(count%4==0):
            for i in range(3):
                print("+-------",end="")
            print("+")

        elif(count%4==1 or count%4==3):
            for i in range(3):
                print("|       ",end="")
            print("|")

        else:
            for i in range(3):
                print("|   ",board[array][i],"   ",sep="",end="")
            print("|")
            array+=1

        count+=1

drawBoard(board)

