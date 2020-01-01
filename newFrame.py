import pygame

import math
import random
import sys
import copy

import numpy as np

class Simplified_World():

    def __init__(self, row=20, col = 20):
        self.row = row
        self.col = col
        self.curState = [None, (self.row // 2 + 1, self.col // 2 + 1)] 
        self.curState[0] = randomPos(self.curState, self.row, self.col)
    '''
    curState : [foodPos, headPos, bodyCube1Pos, bodyCube2Pos, ...]
    '''

def randomPos(curState, row, col):
    if len(curState) == row * col + 1: # + 1 because food is curState[0]
        return False
    while True:
        x = random.randint(1,row)
        y = random.randint(1,col)
        if (x,y) in curState[1:]: #curState[1:] is the snake
            continue
        else:
            break
    return (x,y)
    
def snakeMove(curState, row, col, dirx, diry):
    if (dirx, diry) not in getValidMove(curState, row, col):
        return None
    newHead = (curState[1][0] + dirx, curState[1][1] + diry)
    newState = copy.deepcopy(curState)
    newState.insert(1, newHead)
    if newHead == newState[0]:
        newState[0] = None
    else:
        newState.pop()
    return newState

def getValidMove(curState, row, col):
    # Big enough
    if len(curState) == row*col + 1:
        return []
    validMove = []
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    head = curState[1]
    for d in directions:
        newHead = (head[0]+d[0], head[1]+d[1])
        # Invalid move: Turning around
        if len(curState) > 2 and newHead == curState[2]:
            continue
        # Invalid move: Reaching boundary
        elif newHead[0] == 0 or newHead[0] == col+1 or newHead[1] == 1 or newHead[1] == row+1:
            continue
        # Invalid move: Hitting itself
        elif newHead in curState[1:len(curState)-1]:
            continue
        else:
            validMove.append(d)
    return validMove


