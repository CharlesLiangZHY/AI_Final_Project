import math
import random
import pygame
import numpy as np

import sys

class World():

    def __init__(self, row=20):
        self.row = row
        self.snake = Snake((self.row // 2 + 1, self.row // 2 + 1), self.row)
        # self.snake = Snake((1, 2), self.row)
        self.food = self.randomPos()
        # self.food = (-1,-1)
        

    def randomPos(self):
        invalidPos = self.snake.body
        if len(invalidPos) == self.row * self.row:
            return False
        while True:
            x = random.randint(1,self.row)
            y = random.randint(1,self.row)
            if len(list(filter(lambda z:z.pos == (x,y), invalidPos))) > 0:
                continue
            else:
                break
        return (x,y)

    def snakeMove(self, dirx, diry):
        if self.snake.move(dirx, diry):
            snakeHead = self.snake.head.pos
            if snakeHead[0] == self.food[0] and snakeHead[1] == self.food[1]: # Food has been eaten.
                self.snake.addCube()
                temp = self.randomPos()
                if temp == False:
                    self.food = (0,0)
                    return False
                else:
                    self.food = temp
            return True
        else:
            return False
        
        

        
    def draw(self, window, width, background = (255,255,255)):
        if(width < 10*self.row):
            print("The window width is too small.(At least 10*row pixels)")
            return False
        else:
            window.fill(background)

            grid = width // self.row 
            x = 0
            y = 0
            for i in range(self.row):
                x = x + grid 
                y = y + grid
                pygame.draw.line(window, (0,0,0), (x,0), (x,width)) # draw horizontal
                pygame.draw.line(window, (0,0,0), (0,y), (width,y)) # draw vertical

            if self.food != (0,0):
                foodCube = Cube(self.food, 0, 0, (255, 255, 0))
                foodCube.draw(window, grid)


            self.snake.draw(window, grid)


            pygame.display.update()
            return True

class Cube():

    def __init__(self, start, dirx=1, diry=0, color=(105,105,105)):
        self.pos = start # (x , y)
        '''
        left:  dirX = -1 dirY =  0
        right: dirX =  1 dirY =  0
        up:    dirX =  0 dirY = -1
        down:  dirX =  0 dirY =  1
        food:  dirX =  0 dirY =  0
        '''
        self.dirX = dirx 
        self.dirY = diry

        self.color = color # (r, g, b)

    def move(self, dirx, diry):
        self.dirX = dirx 
        self.dirY = diry 
        self.pos =  (self.pos[0] + self.dirX, self.pos[1] + self.dirY)
        

    def draw(self, window, grid, eyes=False):
        x = self.pos[0]-1
        y = self.pos[1]-1
        pygame.draw.rect(window, self.color, (x*grid+1, y*grid+1, grid-2, grid-2))
        


class Snake():
    body = []
    turns = {} # record which direction the cube is goint to turn if it reaches this position
    def __init__(self, headLoc, mapSize):
        self.head = Cube(headLoc, 0, 0, (0,0,0)) 
        self.body.append(self.head)
        self.dirX = self.head.dirX
        self.dirY = self.head.dirY
        self.mapSize = mapSize

        self.boringAgentInit = 0

    def move(self, dirx, diry):

        # Invalid move: Reaching boundary
        head = self.head.pos
        if head[0] + dirx == 0 or head[0] + dirx == self.mapSize + 1:
            return False    
        elif head[1] + diry == 0 or head[1] + diry == self.mapSize + 1:
            return False 
        # Invalid move: Turn around
        elif self.dirX + dirx == 0 and self.dirY + diry == 0 and self.dirY + self.dirX != 0 and len(self.body) != 1:
            return False 
        

        self.dirX = dirx 
        self.dirY = diry 
        self.turns[self.head.pos[:]] = (self.dirX, self.dirY) # must be pos[:]

        

        for index, cube in enumerate(self.body):
            p = cube.pos
            if p in self.turns:
                direction = self.turns[p]
                cube.move(direction[0],direction[1])
                if index == len(self.body)-1: # tail
                    self.turns.pop(p)
            else:
                cube.move(cube.dirX, cube.dirY)

        # Invalid move: Eating itself
        if (self.head.pos[0], self.head.pos[1]) in list(map(lambda z:z.pos, self.body[1:])):
            return False

        return True

    def getValidMove(self):
        if len(self.body) == self.mapSize * self.mapSize:
            return []
        validMove = []
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        head = self.head.pos
        for d in directions:
            dirx = d[0]
            diry = d[1]
            if head[0] + dirx == 0 or head[0] + dirx == self.mapSize + 1:
                continue    
            elif head[1] + diry == 0 or head[1] + diry == self.mapSize + 1:
                continue
            # Invalid move: Turn around
            elif self.dirX + dirx == 0 and self.dirY + diry == 0 and self.dirY + self.dirX != 0:
                continue

            newHead = (head[0]+dirx, head[1]+diry)
            if (newHead[0], newHead[1]) in list(map(lambda z:z.pos, self.body[1:len(self.body)-1])):
                continue

            validMove.append(d)

        return validMove



    def addCube(self):
        oldTail = self.body[-1]
        if oldTail.dirX == 1 and oldTail.dirY == 0:
            self.body.append(Cube((oldTail.pos[0]-1, oldTail.pos[1])))
        elif oldTail.dirX == -1 and oldTail.dirY == 0:
            self.body.append(Cube((oldTail.pos[0]+1, oldTail.pos[1])))
        elif oldTail.dirX == 0 and oldTail.dirY == 1:
            self.body.append(Cube((oldTail.pos[0], oldTail.pos[1]-1)))
        elif oldTail.dirX == 0 and oldTail.dirY == -1:
            self.body.append(Cube((oldTail.pos[0], oldTail.pos[1]+1)))

        self.body[-1].dirX = oldTail.dirX 
        self.body[-1].dirY = oldTail.dirY

    def draw(self, window, grid): 
        for cube in self.body:
            cube.draw(window, grid)




