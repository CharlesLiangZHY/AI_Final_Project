from newFrame import *

def greedyAgent(world, fakeSearch = True):
    r = world.row
    c = world.col
    S = world.curState
    V = getValidMove(S, r, c)
    if len(V) == 0:
            return None

    food = S[0]
    head = S[1]

    if fakeSearch:
        distance = []
        for x in range(c+2):
            distance.append([])
            for y in range(r+2):
                distance[x].append(None)

        found = False
        for x in range(1,c+1):
            for y in range(1,r+1):
                distance[x][y] = float('inf')
        distance[food[0]][food[1]] = 0
        
        visited = []
        fringe = [food]
        while len(fringe) != 0:
            loc = fringe[0] # BFS: FIFO fringe
            visited.append(loc) # graph search
            up = (loc[0],loc[1]-1)
            down = (loc[0],loc[1]+1)
            left = (loc[0]-1,loc[1])
            right = (loc[0]+1,loc[1])
            for pos in [up,down,left,right]:
                if pos not in visited and distance[pos[0]][pos[1]] != None and pos not in fringe:
                    if pos == head:
                        found = True
                    else:
                        fringe.append(pos)
                        distance[pos[0]][pos[1]] = distance[loc[0]][loc[1]] + 1  
            fringe.pop(0) # BFS: FIFO fringe
        
        directions = {}
        for v in V:
            directions[v] = distance[v[0]+head[0]][v[1]+head[1]]
        return min(directions, key=directions.get)
        
