from snake_frame import *
import copy

def Greedy_Agent(world):
    s = world.snake
    head = s.head.pos
    V = s.getValidMove()
    if len(V) == 0:
        return None
    if world.GreedycalculateDistance(world.food):
        directions = {}
        for v in V:
            directions[v] = world.distance[v[1]+head[1]][v[0]+head[0]]
        return min(directions, key=directions.get)


def forwardCheck(virtualWorld):
    virtualSnake = virtualWorld.snake
    if len(virtualSnake.body) == virtualWorld.row * virtualWorld.col - 1:
        return True
    f = virtualWorld.food
    Eaten = False

    while not Eaten:

        V = virtualSnake.getValidMove()
        head = virtualSnake.head.pos
        action = [0,0]
        if virtualWorld.calculateDistance(f):

            directions = {}
            for v in V:
                directions[v] = virtualWorld.distance[v[1]+head[1]][v[0]+head[0]]
            action = min(directions, key=directions.get)
            if (virtualSnake.head.pos[0] + action[0], virtualSnake.head.pos[1] + action[1]) == f:
                Eaten = True
            virtualWorld.snakeMove(action[0],action[1])

    return virtualWorld.calculateDistance(virtualSnake.body[-1].pos)

def forwardCheckTail(virtualWorld, d):
    virtualSnake = virtualWorld.snake
    virtualWorld.snakeMove(d[0],d[1])
    return virtualWorld.calculateDistance(virtualSnake.body[-1].pos)


def Forward_Checking_Agent(world):
    r = world.row
    s = world.snake
    head = s.head.pos
    f = world.food
    V = s.getValidMove()
    if len(V) == 0:
        return None
    if world.calculateDistance(world.food):
        virtualWorld = copy.deepcopy(world)
        virtualWorld.snake.body = copy.deepcopy(world.snake.body)
        virtualWorld.snake.head = virtualWorld.snake.body[0]
        virtualWorld.snake.turns = copy.deepcopy(world.snake.turns)
        
        if forwardCheck(virtualWorld):

            # print("Not cause trouble and go to eat food")

            directions = {}
            for v in V:
                directions[v] = world.distance[v[1]+head[1]][v[0]+head[0]]
            return min(directions, key=directions.get)
        else:

            if world.calculateDistance(s.body[-1].pos):

                # print("Cause trouble, follow tail")

                directions = []
                for v in V:
                    if world.distance[v[1]+head[1]][v[0]+head[0]] != float('inf'):
                        directions.append(v)
                return directions[random.randint(0,len(directions)-1)]
    else:
        virtualWorld = copy.deepcopy(world)
        virtualWorld.snake.body = copy.deepcopy(world.snake.body)
        virtualWorld.snake.head = virtualWorld.snake.body[0]
        virtualWorld.snake.turns = copy.deepcopy(world.snake.turns)

        if world.calculateDistance(s.body[-1].pos):

            # print("At least we can follow tail")

            
            directions = []
            danger = []
            for v in V:
                if world.distance[v[1]+head[1]][v[0]+head[0]] != float('inf'):
                    directions.append(v)
                else:
                    danger.append(v)
            
            if len(danger) == 1:
                if forwardCheckTail(virtualWorld,danger[0]):
                    directions.append(danger[0])

            choice = random.randint(0,len(directions)-1)
            # print(choice)
            return directions[choice]
        else:
            # print("WTF")
            return V[random.randint(0,len(V)-1)]













            