from itertools import product
from copy import copy

def isdistinct(ls):

    unique=[]
    for elem in ls:
        if elem!=0 and elem in unique:
            return False
        unique.append(elem)
    # del unique
    return True

def isvalid(brd):
    # checking rowise
    for i in range(len(brd)):
        row=[brd[i][0],brd[i][1],brd[i][2]]
        if not isdistinct(row):
            return False
        col=[brd[0][i],brd[1][i],brd[2][i]]
        if not isdistinct(col):
            return False

    return True

def solve(board,empty=9):

    if empty==0:
        return isvalid(board)
    
    for r,c in product(range(3),repeat=2):

        if board[r][c]!=0:
            continue
        board2=copy(board)
        for test in [1,2,3]:
            board2[r][c]=test
            if isdistinct(board2) and solve(board2,empty-1):
                return True

            board[r][c]=0

    return False


board=[[0,0,0],
        [1,0,0],
        [0,3,1]]
for row in board:
    print(row)  

solve(board,6)
print("")
for row in board:
    print(row)  