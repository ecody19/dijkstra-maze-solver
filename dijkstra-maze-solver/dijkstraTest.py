import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import copy

start = [1,1]
maze = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

fig, ax = plt.subplots(1, 1)
my_plot = ax.imshow(maze, extent=[0, 1, 0, 1])
plt.savefig('test.png', dpi=250)

def checkDijkstraObstacle (distMap, pos, dir):
    ctc=copy.deepcopy(pos)
    if dir ==1:
        ctc[0] -= 1
    elif dir ==2:
        ctc[1] += 1
    elif dir ==3:
        ctc[0] += 1
    elif dir ==4:
        ctc[1] -= 1

    if distMap[ctc[0],ctc[1]]==-1:
        isValid = True
    else:
        isValid = False
    return (isValid, ctc)

def checkEscape (map, pos):
    a=copy.deepcopy(np.size(maze,0))
    b=copy.deepcopy(np.size(maze,1))
    if pos[0] == 0 or pos[0]==a or pos[1] == 0 or pos[1]==b:
        isDone = True
    else:
        isDone = False
    return (isDone)

def init():
    print ("hi")
    my_plot.set_data(maze)

def dijkstra(j, maze, start):
    print('done with one row')
    distMap = copy.deepcopy(maze)
    distMap[distMap == 0] = -1
    distMap[distMap==1]=0
    distMap[(start[0]),(start[1])]=1

    moveMap = np.zeros([np.size(maze, 0),np.size(maze, 1)], dtype = int)

    checkDist = 1
    isDone = False
    
    while isDone == False:
        [row,column]=np.where(distMap == checkDist)
        for i in range (0,np.size(row)):
            pos = [row[i],column[i]]
            for direction in range (1,5):
                (isValid, ctc) = checkDijkstraObstacle(distMap, pos, direction)
                if isValid == True:
                    distMap[ctc[0],ctc[1]] = (distMap[pos[0],pos[1]])+1
                    moveMap[ctc[0],ctc[1]] = (direction)
                    maze[ctc[0],ctc[1]] = 3
                    my_plot.set_data(maze)
                    plt.savefig('test{}.png'.format(j), dpi=250)
                    yield my_plot
                    isDone = checkEscape(maze, ctc)

            
        checkDist += 1
    print (distMap)
    return my_plot

print("Hello")
animation.FuncAnimation(fig, dijkstra, fargs = (maze, start), init_func=init, frames=200)
plt.show()
print("world")