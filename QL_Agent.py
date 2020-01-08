from newFrame import *
from Search_Agent import ManhattanDistance

import pickle

class QLearning():
    def __init__(self, name, QValueTable = None, stateFormat = None, actionList = None):
        self.stateFormat = stateFormat
        self.actionList = actionList
        self.Episode = 0
        self.Epsilon = 1.0 # Exploit states, after 100 episode will decrease to 0
        self.QValueTable = QValueTable
        self.name = name

    def save(self): # save as .pkl format
        f = open(self.name+".pkl", 'wb')
        f.write(pickle.dumps(self))
        f.close()
    # Code to read saved data:
    # with open(filename, 'rb') as file:
    # T = pickle.loads(file.read())
'''
I think it is difficult to train on the full world state, since
the state size is too large. I simplify the state.

Naive RL state : 
[obstacle left, obstacle right, obstacle up, obstacle down, Direction of food to head]

Direction of food to head includes:
    Up-left   : (-1, -1)
    Up        : ( 0, -1)
    Up-right  : ( 1, -1)
    Left      : (-1,  0)
    Right     : ( 1,  0)
    Down-left : (-1,  1)
    Down      : ( 0,  1)
    Down-right: ( 1,  1)
'''
def generate_QValueTable_of_NaiveRLstate():
    QValueTable = {} # State size: 8 * 2^4 = 128 ; Action size: 4
    action = [(-1,0), (1,0), (0,-1), (0,1)]
    foodDirections = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
    for a in action:
        for d in foodDirections: 
            for oL in range(2):  
                for oR in range(2):
                    for oU in range(2):
                        for oD in range(2):
                            QValueTable[((oL, oR, oU, oD, d), a)] = 0
    return QValueTable


'''
stateTransformFunction format : function(origin world state, r, c)
rewardFunction format : function(old world state, new world state)
'''
# Transfer full world state to Naive_RL_state
def transform_to_NaiveRLstate(state, r, c):
    RL_state = [None, None, None, None, None]

    food = state[0]
    head = state[1]
    left = (head[0]-1, head[1])
    right = (head[0]+1, head[1])
    up = (head[0], head[1]-1)
    down = (head[0], head[1]+1)
    if left[0] == 0 or left in state[1:]:
        RL_state[0] = 1
    else:
        RL_state[0] = 0
    if right[0] == c+1 or right in state[1:]: 
        RL_state[1] = 1
    else:
        RL_state[1] = 0
    if up[1] == 0 or up in state[1:]: 
        RL_state[2] = 1
    else:
        RL_state[2] = 0
    if down[1] == r+1 or down in state[1:]: 
        RL_state[3] = 1
    else:
        RL_state[3] = 0
    
    dirx = 0
    diry = 0
    if food[1] < head[1]:
        diry = -1
        if food[0] < head[0]:
            dirx = -1   # Up-left   : (-1, -1)
        elif food[0] == head[0]:
            dirx = 0    # Up        : ( 0, -1)
        else:
            dirx = 1    # Up-right  : ( 1, -1)
    elif food[1] == head[1]:
        diry = 0
        if food[0] < head[0]:
            dirx = -1   # Left      : (-1,  0)
        elif food[0] > head[0]:
            dirx = 1    # Right     : ( 1,  0)
    else:
        diry = 1
        if food[0] < head[0]:
            dirx = -1   # Down-left : (-1,  1)
        elif food[0] == head[0]:
            dirx = 0    # Down      : ( 0,  1)
        else:
            dirx = 1    # Down-right: ( 1,  1)
    RL_state[4] = (dirx, diry)
    
    return tuple(RL_state) 


# Reward according to full world state
def naive_reward(oldState, newState):
    eatFoodReward = 20
    deathReward = -50
    getCloserReward = 1
    getFurtherReward = -1

    oldDistance = ManhattanDistance(oldState(0), oldState(1))
    newDistance = ManhattanDistance(newState(0), newState(1))

    if newState == None:
        return deathReward
    elif newState[0] != oldState[0]:
        return eatFoodReward
    elif oldDistance > newDistance:
        return getCloserReward
    elif oldDistance < newDistance:
        return getFurtherReward
    else:
        return 0


def tossCoin(p):
    if random.uniform(0,1) < p:
        return 1
    else:
        return 0


def QValueUpdate(QValueTable, actions, R, QState, newRLState, learningRate, discounting):
    sample = R + discounting * max(map(lambda a: QValueTable[(newRLState, a)], actions)) # 帅
    QValueTable[QState] = (1 - learningRate) * QValueTable[QState] + learningRate * sample

def naive_train(qLearning, mapsize, learningRate, discounting):
    r, c = mapsize
    world = Simplified_World(row,col)
    oldState = world.curState
    oldRLState = transform_to_NaiveRLstate(oldState, r, c)

    e = qLearning.Epsilon
    actions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while True:
        forcing_exploration = tossCoin(e) # 1 act randomly and 0 act according to QValue 
        if forcing_exploration == 1:
            a = actions[random.randint(0, len(actions)-1)]
        else:
            pass
        
        newState = world.moveSnake(a[0], a[1])
        newRLState = transform_to_NaiveRLstate(newState, r, c)
        R = naive_reward(oldState, newState)
        QState = (oldRLState, a)
        QValueUpdate(qLearning.QValueTable, actions, R, QState, newRLState, learningRate, discounting)
        

    qLearning.Episode += 1
    if qLearning.Epsilon > 0:
        qLearning.Epsilon -= 0.01 # lower epsilon over time
    qLearning.save()



























# Advanced policy
def follow_the_longest_path_to_path(state, r, c):
    pass

def follow_the_shortest_path_to_path(state, r, c):
    pass

def follow_the_longest_path_to_food(state, r, c):
    pass

def follow_the_shortest_path_to_path(state, r, c):
    pass

