from snake_frame import *
import pickle

class QLearning():
    def __init__(self, stateFormat = None, actionList = None):
        self.stateFormat = stateFormat
        self.actionList = actionList
        self.Episode = 0
        self.Epsilon = 1.0 # Exploit states, after 100 episode will decrease to 0
        self.QValueTable = None

    def save(self, filename):

'''
I think it is difficult to train on the full world state, since
the state size is too large. I simplify the state.

RL_state : [obstacle left, obstacle right, obstacle up, obstacle down, Direction of food to head, ]
Direction of food to head includes:
    Up-left   : (-1, -1)
    Up        : (-1,  0)
    Up-right  : (-1, -1)
    Left      : (-1,  0)
    Right     : ( 1,  0)
    Down-left : (-1,  1)
    Down      : ( 0,  1)
    Down-right: ( 1,  1)
'''

# Simplified state
def transfer_to_RL_state(state, r, c):
    food = state[0]
    head = state[1]
    left = (head[0]-1, head[1])
    right = (head[0]+1, head[1])
    up = (head[0], head[1]-1)
    down = (head[0], head[1]+1)
    if left[0] == 0 or right[0] == c+1 or 





# Reward
def reward(oldState, newState):
    pass











# Advanced policy
def follow_the_longest_path_to_path(state, r, c):
    pass

def follow_the_shortest_path_to_path(state, r, c):
    pass

def follow_the_longest_path_to_food(state, r, c):
    pass

def follow_the_shortest_path_to_path(state, r, c):
    pass

