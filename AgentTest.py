from newFrame import *

import Boring_Agent
import Search_Agent
import LongLive_Agent

def run(agent, col, row):
    world = Simplified_World(row,col)

    move = 0
    score = 0
    while True and move < (row*col)**2 and score < 2*row*col // 3: # to avoid endless loops
        d = agent(world)
        move += 1
        if d != None:
            if world.moveSnake(d[0],d[1]):
                pass
            else:
                break
        else:
            break
        score = len(world.curState)-2
    return [score, move]

if __name__ == '__main__':
    # agent = Boring_Agent.boringAgent
    agent = LongLive_Agent.longLiveAgent
    for r in range(3,11):

        testTime = 100

        total = 0
        for i in range(testTime):
            score, move = run(agent, r, r)
            total += move
            
        print("Map size is", r, "Average move: ", total // testTime)






'''
Until now, I didn't find any code can beat this.
Boring Agent(to fill the map) 
Map size is 3 Average move:  37
Map size is 4 Average move:  72
Map size is 5 Average move:  223
Map size is 6 Average move:  334
Map size is 7 Average move:  757
Map size is 8 Average move:  1036
Map size is 9 Average move:  1924
Map size is 10 Average move:  2491
Map size is 11 Average move:  4145
Map size is 12 Average move:  5237
Map size is 13 Average move:  7866
Map size is 14 Average move:  9680
Map size is 15 Average move:  13681
Map size is 16 Average move:  16488
Map size is 17 Average move:  22253
Map size is 18 Average move:  26380
Map size is 19 Average move:  34354
Map size is 20 Average move:  40063
'''


'''
Boring Agent(to fill 2/3 map)
Map size is 3 Average move:  22
Map size is 4 Average move:  61
Map size is 5 Average move:  152
Map size is 6 Average move:  298
Map size is 7 Average move:  562
Map size is 8 Average move:  929
Map size is 9 Average move:  1511
Map size is 10 Average move:  2212
'''

'''
LongLive Agent(to fill 2/3 map)
Map size is 3 Average move:  13
Map size is 4 Average move:  35
Map size is 5 Average move:  78
Map size is 6 Average move:  154
Map size is 7 Average move:  246
Map size is 8 Average move:  412
Map size is 9 Average move:  626
Map size is 10 Average move:  893
'''

