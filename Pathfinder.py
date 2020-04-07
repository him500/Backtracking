from itertools import product

def findpath(maze,position):
    if position==(N-1,N-1):
        return [(N-1,N-1)]
    
    i,j=position

    if i+1<N and maze[i][j]==1:
        path=findpath(maze,(i+1,j))
        if path:
            return [(i,j)]+path

    if j+1<N and maze[i][j]==1:
        path=findpath(maze,(i,j+1))
        if path:
            return [(i,j)]+path

    return None


maze = [[ 1 , 0 , 1, 0 , 0],
        [ 1 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 0 , 0],
        [ 1 , 1 , 1, 1 , 1]]
N=len(maze)
for row in maze:
    for col in row:
        print(col,end=" ")
    print("") 

path=findpath(maze,(0,0))

for position in path:
    x,y=position
    maze[x][y]="x"
print("")


for row in maze:
    for col in row:
        print(col,end=" ")
    print("")
