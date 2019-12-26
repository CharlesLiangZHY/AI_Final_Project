import pygame

import math
import random
import sys

import numpy as np

class World():

    def __init__(self, row=20, col = 20):
        
        self.row = row
        self.col = col
        self.snake = Snake((self.row // 2 + 1, self.col // 2 + 1), [self.row, self.col])
        
        self.food = self.randomPos()
        self.distance = []
        
        for y in range(self.col+2):
            self.distance.append([])
            for x in range(self.row+2):
                self.distance[y].append(0)
        
        
        

    def randomPos(self):
        
        invalidPos = self.snake.body
        # print(invalidPos)
        if len(invalidPos) == self.row * self.col:
            return False
        while True:
            x = random.randint(1,self.row)
            y = random.randint(1,self.col)
            if len(list(filter(lambda z:z.pos == (x,y), invalidPos))) > 0:
                # print("OK2")
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
        
    def calculateDistance(self, target):
        found = False
        for x in range(1,1+self.row):
            for y in range(1,1+self.col):
                self.distance[y][x] = float('inf')
        self.distance[target[1]][target[0]] = 1
        head = self.snake.head.pos
        visited = []
        fringe = [target]
        while len(fringe) != 0:
            loc = fringe[0]
            visited.append(loc)
            up = (loc[0],loc[1]-1)
            down = (loc[0],loc[1]+1)
            left = (loc[0]-1,loc[1])
            right = (loc[0]+1,loc[1])

            for cube in [up,down,left,right]:
                if cube not in visited and self.distance[cube[1]][cube[0]] != 0 and cube not in fringe and cube not in list(map(lambda z:z.pos, self.snake.body[1:])):
                    # print(list(map(lambda z:z.pos, self.snake.body[:])))
                    # print(head)
                    if cube == head:
                        # print(cube)
                        found = True
                    else:
                        fringe.append(cube)
                        self.distance[cube[1]][cube[0]] = self.distance[loc[1]][loc[0]] + 1
                    
            fringe.pop(0)
        # print(found)
        return found

    def GreedycalculateDistance(self, target):
        found = False
        for x in range(1,1+self.row):
            for y in range(1,1+self.col):
                self.distance[y][x] = float('inf')
        self.distance[target[1]][target[0]] = 1
        head = self.snake.head.pos
        visited = []
        fringe = [target]
        while len(fringe) != 0:
            loc = fringe[0]
            visited.append(loc)
            up = (loc[0],loc[1]-1)
            down = (loc[0],loc[1]+1)
            left = (loc[0]-1,loc[1])
            right = (loc[0]+1,loc[1])

            for cube in [up,down,left,right]:
                if cube not in visited and self.distance[cube[1]][cube[0]] != 0 and cube not in fringe:
                    # print(list(map(lambda z:z.pos, self.snake.body[:])))
                    # print(head)
                    if cube == head:
                        # print(cube)
                        found = True
                    else:
                        fringe.append(cube)
                        self.distance[cube[1]][cube[0]] = self.distance[loc[1]][loc[0]] + 1
                    
            fringe.pop(0)
        # print(found)
        return found

        
    def draw(self, window, width, height, background = (255,255,255)):
        if width < 10*self.row and height < 10*self.col:
            print("The window is too small.")
            return False
        if width // self.row != height // self.col:
            print("Please check gird side length.")
            return False
        else:
            window.fill(background)

            grid = width // self.row 
            x = 0
            y = 0
            for i in range(self.row):
                y = y + grid 
                pygame.draw.line(window, (0,0,0), (y,0), (y,height)) # draw horizontal
                
            for i in range(self.col):
                x = x + grid
                pygame.draw.line(window, (0,0,0), (0,x), (width,x)) # draw vertical
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
        

    def draw(self, window, grid, debug=False):
        x = self.pos[0]-1
        y = self.pos[1]-1
        if debug == False:
            pygame.draw.rect(window, self.color, (x*grid+1, y*grid+1, grid-2, grid-2))
        else:
            pygame.draw.rect(window, (255,0,0), (x*grid+1, y*grid+1, grid-2, grid-2))



class Snake():
    def __init__(self, headLoc, mapSize):
        self.body = []
        self.turns = {} # record which direction the cube is goint to turn if it reaches this position
        self.head = Cube(headLoc, 0, 0, (0,0,0)) 
        self.body.append(self.head)
        self.dirX = self.head.dirX
        self.dirY = self.head.dirY
        self.mapSize = mapSize
        self.boringAgentInit = 0

    def move(self, dirx, diry):

        # Invalid move: Reaching boundary
        head = self.head.pos
        if head[0] + dirx == 0 or head[0] + dirx == self.mapSize[0] + 1:
            return False    
        elif head[1] + diry == 0 or head[1] + diry == self.mapSize[1] + 1:
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
        if len(self.body) == self.mapSize[0] * self.mapSize[1]:
            return []
        validMove = []
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        head = self.head.pos
        for d in directions:
            dirx = d[0]
            diry = d[1]
            if head[0] + dirx == 0 or head[0] + dirx == self.mapSize[0] + 1:
                continue    
            elif head[1] + diry == 0 or head[1] + diry == self.mapSize[1] + 1:
                continue
            # Invalid move: Turn around
            elif self.dirX + dirx == 0 and self.dirY + diry == 0 and self.dirY + self.dirX != 0 and len(self.body) > 1:
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
            if cube == self.body[-1] and len(self.body) > 1:
                cube.draw(window, grid, True)
            else:
                cube.draw(window, grid)

            # cube.draw(window, grid)
            




