from newFrame import *

'''
This naive greedy search algorithm has a one-move horizon and
only considers moving the snake to the position which appears to
be closest to the food (even never considering whether its body 
blocked the way to the food). I use Manhattan distance to define
how close the snake head is to the food.
'''
def ManhattanDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def veryNaiveGreedyAgent(world):
    r = world.row
    c = world.col
    S = world.curState
    V = getValidMove(S, r, c)
    if len(V) == 0:
        return None

    food = S[0]
    head = S[1]
    directions = {}
    for v in V:
        pos = (head[0]+v[0], head[1]+v[1])
        directions[v] = ManhattanDistance(food, pos)
    
    return min(directions, key=directions.get)