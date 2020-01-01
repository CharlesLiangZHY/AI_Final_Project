from newFrame import *

'''
This strategy is to add a very conservative forward-checking to 
the best first search algorithm. This strategy can ensure that 
the snake will never die, but it may never fill the whole map.
When there is no obvious path to the food or if it follows
the found path, it seems like to get it into danger, in both cases,
the snake will take the most conservative action i.e. following its
tail. The danger I mentioned before is that there is no obvious path
to follow its tail after eaten the food.
This agent is improved from stillNaiveGreedyAgent(). The snake will never
die but it may fall into random walk or kind of loop.
'''
def calculateDistance(distance, r, c, target, state):
    head = state[1] # snake head
    found = False
    # initialize distance table
    for x in range(1,c+1):
        for y in range(1,r+1):
            distance[x][y] = float('inf')
    distance[target[0]][target[1]] = 0

    # BFS starts from the target position and ends at the snake head
    visited = [] # Graph search
    fringe = [target]
    while len(fringe) != 0:
        cur = fringe[0] # BFS: FIFO fringe
        visited.append(cur)

        up = (cur[0],cur[1]-1)     # successor after action ( 0,-1)
        down = (cur[0],cur[1]+1)   # successor after action ( 0, 1)
        left = (cur[0]-1,cur[1])   # successor after action (-1, 0)
        right = (cur[0]+1,cur[1])  # successor after action ( 1, 0)
        for pos in [up,down,left,right]:
            # 1. not visited 2. not border 3. not have been expanded 4. not part of snake body
            if pos not in visited and distance[pos[0]][pos[1]] != None and pos not in fringe and pos not in state[2:]:
                if pos == head: # reach the head 
                    found = True # path to target is found
                    # stop expanding after reaching the head
                else:
                    fringe.append(pos)
                    distance[pos[0]][pos[1]] = distance[cur[0]][cur[1]] + 1 # update distance
        fringe.pop(0)  # BFS: FIFO fringe
    return found # if found == False, there is no obvious path from head to target

def naiveForwardCheckDanger(state, r, c):
    if len(state) == r*c - 2:
        return True

    # initialize the distance table
    distance = []
    for x in range(c+2):
        distance.append([])
        for y in range(r+2):
            distance[x].append(None)
    
    food = state[0]
    eaten = False

    while not eaten:
        V = getValidMove(state, r, c)
        head = state[1]
        action = None
        if calculateDistance(distance, r, c, food, state):
            directions = {}
            for v in V:
                directions[v] = distance[head[0]+v[0]][head[1]+v[1]]
            action = min(directions, key=directions.get)
            if (head[0]+action[0], head[1]+action[1]) == food:
                eaten = True
            state = snakeMove(state, r, c, action[0], action[1])

    tail = state[-1]
    return calculateDistance(distance, r, c, tail, state)

# def naiveForwardCheckTail(state, r, c, d):
#     # initialize the distance table
#     tempDistance = []
#     for x in range(c+2):
#         distance.append([])
#         for y in range(r+2):
#             distance[x].append(None)

#     tempState = snakeMove(state, r, c, d[0], d[1])
#     tail = tempState[-1] # the last entry
#     return calculateDistance(tempDistance, tail, tempState)

def longLiveAgent(world):
    r = world.row
    c = world.col
    S = world.curState
    V = getValidMove(S, r, c)
    if len(V) == 0:
        return None
    
    food = S[0]
    head = S[1]
    tail = S[-1]

    # initialize the distance table
    distance = []
    for x in range(c+2):
        distance.append([])
        for y in range(r+2):
            distance[x].append(None)

    if calculateDistance(distance,r,c,food,S):
        if naiveForwardCheckDanger(S,r,c):
            # print("Not cause trouble and go to eat food.")
            directions = {}
            for v in V:
                directions[v] = distance[head[0]+v[0]][head[1]+v[1]]
            return min(directions, key=directions.get)
        else:
            if calculateDistance(distance,r,c,tail,S):
                # print("Cause trouble, so follow the tail.")
                directions = []
                for v in V:
                    if distance[head[0]+v[0]][head[1]+v[1]] != float('inf'):
                        directions.append(v)
                return directions[random.randint(0,len(directions)-1)] # randomly select direction
            else:
                print("Can find path to food, but can not find path to tail.")
                # This case will never happen, because the strategy always keep the snake able to follow its tail.

    else:
        if calculateDistance(distance,r,c,tail,S):
            # print("At least it can follow the tail.")
            directions = []
            danger = []
            for v in V:
                if distance[head[0]+v[0]][head[1]+v[1]] != float('inf'):
                    directions.append(v)
                else:
                    danger.append(v)
            
            if len(danger) == 1:
                tempState = snakeMove(S, r, c, danger[0][0], danger[0][1])
                newTail = tempState[-1] # the last entry
                if calculateDistance(distance, r, c, newTail, tempState):
                    directions.append(danger[0])

            choice = random.randint(0,len(directions)-1)
            return directions[choice]
        
        else:
            print("Can not find path to food as well as path to tail.")
            # This case will never happen, because the strategy always keep the snake able to follow its tail.
