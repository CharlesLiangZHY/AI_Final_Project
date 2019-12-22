from snake_frame import *

def Greedy_Agent(world):
    s = world.snake
    head = s.head.pos
    V = s.getValidMove()
    if len(V) == 0:
        return None
    world.calculateDistance()
    directions = {}
    for v in V:
        directions[v] = world.distance[v[1]+head[1]][v[0]+head[0]]
    return min(directions, key=directions.get)


def Wander_Agent(world):
    r = world.row
    s = world.snake
    head = s.head.pos
    f = world.food
    V = s.getValidMove()
    if len(V) == 0:
        return None

    