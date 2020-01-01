import pygame

import math
import random
import sys
import copy

import numpy as np

class Simplified_World():

    def __init__(self, row=10, col = 10):
        self.row = row
        self.col = col
        self.curState = [None, (self.col // 2 + 1, self.row // 2 + 1)] 
        self.curState[0] = randomPos(self.curState, self.row, self.col)

        self.boringAgentInit = 0 # for Boring_Agent
    '''
    curState : [foodPos, headPos, bodyCube1Pos, bodyCube2Pos, ...]
    '''
    
    def moveSnake(self, dirx, diry):
        newState = snakeMove(self.curState, self.row, self.col, dirx, diry)
        if newState == None:
            return False
        self.curState = newState
        if self.curState[0] == None: # food was eaten
            self.curState[0] = randomPos(self.curState, self.row, self.col)
        return True


    def draw(self, window, width, height, markTail = False, background = (255,255,255)):
        if width < 10*self.row and height < 10*self.col:
            print("The window is too small.")
            return False
        if width // self.col != height // self.row:
            print("Please check gird side length.")
            return False
        else:
            window.fill(background)
            grid = width // self.col
            y = 0
            for i in range(self.row):
                y = y + grid
                pygame.draw.line(window, (0,0,0), (0,y), (width,y)) # draw vertical lines
            x = 0
            for i in range(self.col):
                x = x + grid 
                pygame.draw.line(window, (0,0,0), (x,0), (x,height)) # draw horizontal lines
            
            # draw food
            if self.curState[0] != None:
                foodX = self.curState[0][0] - 1
                foodY = self.curState[0][1] - 1
                pygame.draw.rect(window, (255,255,0), (foodX*grid+1, foodY*grid+1, grid-2, grid-2)) # (255,255,0):Yellow

            # draw head
            headX = self.curState[1][0] - 1
            headY = self.curState[1][1] - 1
            pygame.draw.rect(window, (0,0,0), (headX*grid+1, headY*grid+1, grid-2, grid-2)) # (0,0,0):Black

            # draw body
            if not markTail:
                for cube in self.curState[2:]:
                    cubeX = cube[0] - 1
                    cubeY = cube[1] - 1
                    pygame.draw.rect(window, (105,105,105), (cubeX*grid+1, cubeY*grid+1, grid-2, grid-2)) # (105,105,105):Grey
            else:
                for cube in self.curState[2:len(self.curState)-1]:
                    cubeX = cube[0] - 1
                    cubeY = cube[1] - 1
                    pygame.draw.rect(window, (105,105,105), (cubeX*grid+1, cubeY*grid+1, grid-2, grid-2)) # (105,105,105):Grey
                if len(self.curState) > 2:
                    tailX = self.curState[len(self.curState)-1][0] - 1
                    tailY = self.curState[len(self.curState)-1][1] - 1
                    pygame.draw.rect(window, (255,0,0), (tailX*grid+1, tailY*grid+1, grid-2, grid-2)) # (255,0,0):Red

            pygame.display.update()

def randomPos(curState, row, col):
    if len(curState) == row * col + 1: # + 1 because food is curState[0]
        return None
    while True:
        x = random.randint(1,col)
        y = random.randint(1,row)
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
    # Having filled the world
    if len(curState) == row*col + 1:
        return []
    validMove = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    '''
        left:  dirX = -1 dirY =  0
        right: dirX =  1 dirY =  0
        up:    dirX =  0 dirY = -1
        down:  dirX =  0 dirY =  1
    '''
    head = curState[1]
    
    for d in directions:
        newHead = (head[0]+d[0], head[1]+d[1])
        # print(d,newHead)
        # Invalid move: Turning around
        if len(curState) > 2 and newHead == curState[2]:
            continue
        # Invalid move: Reaching boundary
        elif newHead[0] == 0 or newHead[0] == col+1 or newHead[1] == 0 or newHead[1] == row+1:
            continue
        # Invalid move: Hitting itself
        elif newHead in curState[1:len(curState)-1]:
            continue
        else:
            validMove.append(d)
    return validMove



