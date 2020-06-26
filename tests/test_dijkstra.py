from dijkstraMazeSolver.dijkstraTest import checkDijkstraObstacle as cdo
import numpy as np


def test_dijkstra():
    test1 = np.array ([[0,0,0],[0,1,0],[0,0,0]])
    test2 = np.array ([[0,-1,0],[-1,1,-1],[0,-1,0]])
    test3 = np.array ([[0,-1,0],[0,1,-1],[0,0,0]])
    pos = [1,1]

    ans1 = np.array ([[0,0,0],[0,1,0],[0,0,0]])
    ans2 = np.array ([[0,2,0],[2,1,2],[0,2,0]])
    ans3 = np.array ([[0,2,0],[0,1,2],[0,0,0]])

    for direction in range (1,5):
        (isValid, ctc) = cdo(test1, pos, direction)
        if isValid == True:
            test1[ctc[0],ctc[1]] = (test1[pos[0],pos[1]])+1
    assert test1 == ans1

    for direction in range (1,5):
        (isValid, ctc) = cdo(test2, pos, direction)
        if isValid == True:
            test2[ctc[0],ctc[1]] = (test2[pos[0],pos[1]])+1
    assert test2 == ans2

    for direction in range (1,5):
        (isValid, ctc) = cdo(test3, pos, direction)
        if isValid == True:
            test3[ctc[0],ctc[1]] = (test3[pos[0],pos[1]])+1
    assert test3 == ans3