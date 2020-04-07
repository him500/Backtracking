import numpy as np
N=int(input())
# N=4
board=np.zeros((N,N))

print(board)

def check(brd,pos):
    x,y=pos
    # checking left side
    for j in range(y):
        if brd[x][j]==1:
            return False

    
    i=x-1
    j=y-1       # checking up-left diagonal
    while(i>=0 and j>=0):
        if brd[i][j]==1:
            return False
        i-=1
        j-=1

    i=x+1
    j=y-1       # checking down-right diagonal
    while(i<N and j>=0):
        if brd[i][j]==1:
            return False
        i+=1
        j-=1

    return True



def nQueen(board,position):

    x,y=position
    if y>=N:
        return True

    board[x][y]=1
    # print("check")
    # print(board)
    for i in range(N):
        if check(board,position) and nQueen(board,(i,y+1)):
            return True
    board[x][y]=0

    return False

for r in range(N):
    if nQueen(board,(r,0)):
        break;

print(" ")
print(board)