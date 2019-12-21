from snake_frame import *

import numpy as np

def BFS_Agent(world):
    r = world.row
    s = world.snake
    head = s.head.pos
    f = world.food
    V = s.getValidMove()
    if len(V) == 0:
        return None

    distance = np.zeros((r+2,r+2))
    
    for x in range(1,1+r):
        for y in range(1,1+r):
            if (x,y) not in s.body:
                distance[y][x] = float('inf')
    distance[f[1]][f[0]] = 1

    visited = []
    fringe = [f]
    while len(fringe) != 0:
        loc = fringe[0]
        visited.append(loc)
        up = (loc[0],loc[1]-1)
        down = (loc[0],loc[1]+1)
        left = (loc[0]-1,loc[1])
        right = (loc[0]+1,loc[1])

        for d in [up,down,left,right]:
            if d not in visited and distance[d[1]][d[0]] != 0:
                fringe.append(d)
                distance[d[1]][d[0]] = distance[loc[1]][loc[0]] + 1
        fringe.pop(0)
    directions = {}
    for v in V:
        directions[v] = distance[v[1]+head[1]][v[0]+head[0]]
    return min(directions, key=directions.get)


def BFS_Wander_Agent(world):
    r = world.row
    s = world.snake
    head = s.head.pos
    f = world.food
    V = s.getValidMove()
    if len(V) == 0:
        return None

    