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

'''
This naive greedy search algorithm also has only a one-move horizon 
and considers moving the snake to the position which appears to be
closest to the food. But it will actually find out the shortest path 
using BFS. However, it will not find out the potential shortest path 
to the food because of its one-move horizon. When the agent can not 
find out any obvious path to the food, it will fail. The difference 
can be seen through visualization of the snake moving.
'''
def stillNaiveGreedyAgent(world):
    r = world.row
    c = world.col
    S = world.curState
    V = getValidMove(S, r, c)
    if len(V) == 0:
        return None
    
    food = S[0]
    head = S[1]
    found = False

    # initialize the distance table
    distance = []
    for x in range(c+2):
        distance.append([])
        for y in range(r+2):
            distance[x].append(None)
    found = False
    for x in range(1,c+1):
        for y in range(1,r+1):
            distance[x][y] = float('inf') # all entries left with None value are borders
    distance[food[0]][food[1]] = 0 # food position

    # BFS starts from the food and ends at the snake head
    visited = [] # Graph search
    fringe = [food]
    while len(fringe) != 0:
        cur = fringe[0] # BFS: FIFO fringe
        visited.append(cur)

        up = (cur[0],cur[1]-1)     # successor after action ( 0,-1)
        down = (cur[0],cur[1]+1)   # successor after action ( 0, 1)
        left = (cur[0]-1,cur[1])   # successor after action (-1, 0)
        right = (cur[0]+1,cur[1])  # successor after action ( 1, 0)
        for pos in [up,down,left,right]:
            # 1. not visited 2. not border 3. not have been expanded 4. not part of snake body
            if pos not in visited and distance[pos[0]][pos[1]] != None and pos not in fringe and pos not in S[2:]:
                if pos == head: # reach the head 
                    found = True # path to food is found
                    # stop expanding after reaching the head
                else:
                    fringe.append(pos)
                    distance[pos[0]][pos[1]] = distance[cur[0]][cur[1]] + 1 # update distance
        fringe.pop(0)  # BFS: FIFO fringe
    if not found:
        return None
    else:
        directions = {}
        for v in V:
            directions[v] = distance[v[0]+head[0]][v[1]+head[1]]
        return min(directions, key=directions.get)