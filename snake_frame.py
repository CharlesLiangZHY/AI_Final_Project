import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox



class World():
    def __init__(self, row=20):
        self.row = row
        self.snake = Snake((random.randint(1,self.row), random.randint(1,self.row)))
        self.food = self.randomPos()


    def randomPos(self):
        invalidPos = self.snake.body

        while True:
            x = random.randint(1,self.row)
            y = random.randint(1,self.row)
            if len(list(filter(lambda z:z.pos == (x,y), invalidPos))) > 0:
                continue
            else:
                break
        return (x,y)
        

        
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


            foodCube = Cube(self.food, 0, 0, (245, 222, 179))
            foodCube.draw(window, grid)
            # print("Food: ", foodCube.pos)
            self.snake.draw(window, grid)
            # print("Head: ", self.snake.head.pos)



            pygame.display.update()
            return True

class Cube():

    def __init__(self, start, dirx=1, diry=0, color=(105,105,105)):
        self.pos = start # (x , y)
        '''
        left:  dirX =  1 dirY =  0
        right: dirX = -1 dirY =  0
        up:    dirX =  0 dirY =  1
        down:  dirX =  0 dirY = -1
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
    turns = {}
    def __init__(self, headLoc):
        self.head = Cube(headLoc, 1, 0, (0,0,0))
        self.body.append(self.head)
        self.dirX = self.head.dirX
        self.dirY = self.head.dirY

    def move(self):
        pass

    def addCube(self):
        pass

    def draw(self, window, grid): 
        for cube in self.body:
            cube.draw(window, grid)









if __name__ == '__main__':

    width = 500
    pygame.init()
    window = pygame.display.set_mode((width,width))
    clock = pygame.time.Clock()

    flag = True

    world = World()
    while flag:
        # event listening (Essential!)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.time.delay(50)
        clock.tick(10)
        flag = world.draw(window,width)