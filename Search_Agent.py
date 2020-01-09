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
Tips: Remember to uncomment the line: 
    "# pass # will hold on the termination" in visualize() function.
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

'''
Here I am going to implement a real BFS and Astar agent,which will 
be really resource-consuming. Without forward checking, both 
agents will fall into dead end very easily. To maintain consistency
of code, although it can return a sequence of moves leading the snake
to eat the food, I still let it return the next move.
'''
def bfsAgent(world):
    r = world.row
    c = world.col
    if r > 6 or c > 6:
        print("The map size should be smaller.")
        return None
    S = world.curState
    V = getValidMove(S, r, c)
    if len(V) == 0:
        return None

    length = len(S) # goal test is that length of state grows
    fringe = []
    expanded = set()

    fringe.append((tuple(S),[])) # start state
    while not len(fringe) == 0:
        cur, moves = fringe.pop(0) # BFS: FIFO fringe

        if len(cur) == length + 1: # eaten food, body grew
            return moves[0]
        
        expanded.add(cur)
        V = getValidMove(cur, r, c)
        for v in V:
            newState = tuple(snakeMove(list(cur), r, c, v[0], v[1]))
            if newState in expanded:
                continue
            else:
                fringe.append((newState, moves + [v]))

    # uncomment two lines below, the snake will stop if it can not find a path to food
    V = getValidMove(S, r, c)
    return V[random.randint(0,len(V)-1)] # find no path, return a random valid move
'''
My heuristic function is the Manhattan Distance between snake head 
and food. Combined with the cumulative cost, we have the successor
choice function.
'''
def astarAgent(world):
    r = world.row
    c = world.col
    if r > 6 or c > 6:
        print("The map size should be smaller.")
        return None
    S = world.curState
    V = getValidMove(S, r, c)
    if len(V) == 0:
        return None

    length = len(S) # goal test is that length of state grows
    fringe = priorityQueue() # use priority queue for Astar successor function
    expanded = set()

    fringe.push((tuple(S),[], 0), ManhattanDistance(S[0], S[1])) # start state, additional store the cumulative cost
    while not fringe.isEmpty():
        cur, moves, cost = fringe.pop()

        if len(cur) == length + 1: # eaten food, body grew
            return moves[0]
        
        expanded.add(cur)
        V = getValidMove(cur, r, c)
        for v in V:
            newState = tuple(snakeMove(list(cur), r, c, v[0], v[1]))
            g = cost + 1
            h = 0 if len(newState) == length+1 else ManhattanDistance(newState[0], newState[1])
            f = g + h
            if newState in expanded:
                continue
            else:
                fringe.push((newState, moves + [v], g), f)

    # uncomment two lines below, the snake will stop if it can not find a path to food
    V = getValidMove(S, r, c)
    return V[random.randint(0,len(V)-1)] # find no path, return a random valid move

'''
Here I am going to implement an Astar with forward checking. The main idea
of forward checking has been mentioned in LongLive_Agent. The forward checking
is n-step, it will do a n-step BFS to check whether all successores in n-step 
are possible dead ends. Here we consider the situation that the snake can not 
move following its tail as the dead end. If it cannot find a safe path(maybe 
because of the forward step is too small), the agent will let the snake move
to a random valid position
'''
def calculateDistance(distance, r, c, target, state): # copy from LongLive_Agent.py
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

def forwardCheck(state, r, c, forwardStep):
    # initialize the distance table
    V = getValidMove(state, r, c)
    if len(V) == 0:
        return False

    distance = []
    for x in range(c+2):
        distance.append([])
        for y in range(r+2):
            distance[x].append(None)

    fringe = []
    expanded = set()
    fringe.append((state, 0)) # stores the node level of the search tree
    while not len(fringe) == 0:
        cur, level = fringe.pop(0) # BFS: FIFO fringe
        tail = cur[-1]
        if calculateDistance(distance, r, c, tail, cur):
            return True # safe
        expanded.add(cur)
        if level < forwardStep: # limit expansion depth
            V = getValidMove(cur, r, c)
            for v in V:
                newState = tuple(snakeMove(list(cur), r, c, v[0], v[1]))
                if newState in expanded:
                    continue
                else:
                    fringe.append((newState, level+1))
    return False

def astarForwardCheckingAgent(world, forwardStep = 2):
    r = world.row
    c = world.col
    if r > 7 or c > 7:
        print("The map size should be smaller. The recommended map size for this agent is 6x6.")
        return None
    S = world.curState
    length = len(S) # goal test is that length of state grows
    V = getValidMove(S, r, c)
    if len(V) == 0:
        return None
    if length == r*c: # final step
        return V[0]

    fringe = priorityQueue() # use priority queue for Astar successor function
    expanded = set()

    fringe.push((tuple(S),[], 0), ManhattanDistance(S[0], S[1])) # start state, additional store the cumulative cost
    while not fringe.isEmpty():
        cur, moves, cost = fringe.pop()

        safe = forwardCheck(cur, r, c, forwardStep)
        if len(cur) == length + 1 and safe: # eaten food, body grew
            return moves[0]
        expanded.add(cur) # graph search
        if len(cur) == length + 1 and not safe:
            pass # Discard this branch
        else:
            V = getValidMove(cur, r, c)
            for v in V:
                newState = tuple(snakeMove(list(cur), r, c, v[0], v[1]))
                g = cost + 1
                h = 0 if len(newState) == length+1 else ManhattanDistance(newState[0], newState[1])
                f = g + h
                if newState in expanded:
                    continue
                else:
                    fringe.push((newState, moves + [v], g), f)

    # uncomment two lines below, the snake will stop if it can not find a path to food
    V = getValidMove(S, r, c)
    return V[random.randint(0,len(V)-1)] # find no path, return a random valid move

