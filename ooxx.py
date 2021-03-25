board=[[str(i+1+k*3) for i in range(3)] for k in range(3)]
playerInput="A"



def drawBoard(grid):
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
                print("|   ",grid[array][i],"   ",sep="",end="")
            print("|")
            array+=1

        count+=1


def playerMove(grid):
    inputChecker=False

    while not inputChecker:
        choose=str(input("Make a move :"))

        for i in range(3):
            for k in range(3):
                if(grid[i][k]==choose):
                    grid[i][k]="O"
                    inputChecker=True
    return grid

def computerMove(grid):
    blockValue=[[0 for i in range(3)] for k in range(3)]
    
    for i in range(3):
        for k in range(3):
            if(grid[i][k]!="O"):
                if(k==0 and grid[i][k+1]==grid[i][k+2]):
                    if(grid[i][k+2]=="X"):
                        blockValue[i][k]+=1000
                    else:
                        blockValue[i][k]+=900

                if(k==1 and grid[i][k-1]==grid[i][k+1]):
                    if(grid[i][k+1]=="X"):
                        blockValue[i][k]+=1000
                    else:
                        blockValue[i][k]+=900

                if(k==2 and grid[i][k-1]==grid[i][k-2]):
                    if(grid[i][k-1]=="X"):
                        blockValue[i][k]+=1000
                    else:
                        blockValue[i][k]+=900

                if(i==0 and grid[i+1][k]==grid[i+2][k]):
                    if(grid[i+1][k]=="X"):
                        blockValue[i][k]+=1000
                    else:
                        blockValue[i][k]+=900

                if(i==1 and grid[i-1][k]==grid[i+1][k]):
                    if(grid[i+1][k]=="X"):
                        blockValue[i][k]+=1000
                    else:
                        blockValue[i][k]+=900

                if(i==2 and grid[i-1][k]==grid[i-2][k]):
                    if(grid[i-1][k]=="X"):
                        blockValue[i][k]+=1000
                    else:
                        blockValue[i][k]+=900

    


