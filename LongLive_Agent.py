from newFrame import *

'''
This strategy is to add a very conservative forward-checking to 
the best first search algorithm. This strategy can ensure that 
the snake will never die, but it may never fill the whole map.
Because it 
'''
def longLiveAgent(world):
    r = world.row
    c = world.col
    S = world.curState
    V = getValidMove(S, r, c)
    if len(V) == 0:
        return None