from newFrame import *

import Boring_Agent
import Search_Agent
import LongLive_Agent
import QL_Agent 

import pandas as pd 
import pickle

def run(agent, col, row, ql=None):
    world = Simplified_World(row,col)

    move = 0
    score = 0
    while True and move < (row*col)**2: #to avoid endless loops
        d = None
        if ql == None:
            d = agent(world)
        else:
            d = agent(world, ql)
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

'''
Export moves and scores as .CSV format
'''
def exportData(agent, col, row, filename, ql=None):
    world = Simplified_World(row,col)

    result = []
    m = 0
    s = 0
    while True and m < (row*col)**2: #to avoid endless loops
        if ql == None:
            d = agent(world)
        else:
            d = agent(world, ql)
        m += 1
        if d != None:
            if world.moveSnake(d[0],d[1]):
                pass
            else:
                break
        else:
            break
        s = len(world.curState)-2
        result.append([m,s])
    columns = ["Move", "Score"]
    data = pd.DataFrame(result, columns=columns)
    data.to_csv(filename, index=0)
    
    return [s, m]
if __name__ == '__main__':
    # agent = Boring_Agent.boringAgent
    # agent = Search_Agent.veryNaiveGreedyAgent
    # agent = Search_Agent.bfsAgent
    # agent = Search_Agent.astarAgent
    # agent = LongLive_Agent.longLiveAgent
    # agent = Search_Agent.astarForwardCheckingAgent
    agent = QL_Agent.qlAgent

    # for r in range(3,11):
    #     testTime = 100
    #     total = 0
    #     for i in range(testTime):
    #         score, move = run(agent, r, r)
    #         total += move
    #     print("Map size is", r, "Average move: ", total // testTime)

    # r = 6
    # testTime = 100
    # success = 0
    # for i in range(testTime):
    #     score, move = run(agent, r, r)
    #     if score == r*r - 1:
    #         success += 1
    # print("Success rate is", success / testTime)

    # for i in range(10):
    #     filename = "Export/Boring_test" + str(i+1) + ".csv"
    #     exportData(agent, 6, 6, filename)

    # for i in range(10,20):
    #     filename = "Export/Boring_test" + str(i+1) + ".csv"
    #     exportData(agent, 20, 20, filename)

    # for i in range(20,30):
    #     filename = "Export/Boring_test" + str(i+1) + ".csv"
    #     exportData(agent, 10, 10, filename)

    # for i in range(10):
    #     filename = "Export/Greedy_test" + str(i+1) + ".csv"
    #     exportData(agent, 6, 6, filename)

    # for i in range(10,20):
    #     filename = "Export/Greedy_test" + str(i+1) + ".csv"
    #     exportData(agent, 20, 20, filename)

    # for i in range(20,30):
    #     filename = "Export/Greedy_test" + str(i+1) + ".csv"
    #     exportData(agent, 40, 40, filename)

    # for i in range(10):
    #     filename = "Export/BFS_test" + str(i+1) + ".csv"
    #     exportData(agent, 6, 6, filename)

    # for i in range(10,50):
    #     filename = "Export/BFS_test" + str(i+1) + ".csv"
    #     exportData(agent, 6, 6, filename)
    
    # for i in range(10):
    #     filename = "Export/Astar_test" + str(i+1) + ".csv"
    #     exportData(agent, 6, 6, filename)
    
    # for i in range(10,50):
    #     filename = "Export/Astar_test" + str(i+1) + ".csv"
    #     exportData(agent, 6, 6, filename)

    # for i in range(10):
    #     filename = "Export/AstarWithForwardChecking_test" + str(i+1) + ".csv"
    #     exportData(agent, 6, 6, filename)


    # for i in range(10):
    #     filename = "Export/LongLive_test" + str(i+1) + ".csv"
    #     exportData(agent, 10, 10, filename)





    for i in range(10):
        filename = "Export/QL_test" + str(i+1) + ".csv"

        with open("Trained/T2.pkl", 'rb') as file:
            QL = pickle.loads(file.read())
        exportData(agent, 40, 40, filename, QL)









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

'''
AstarForwardChecking Agent with 2-step forward checking 
Success rate for 6x6 map: 0.88
'''

'''
LongLive Agent
Success rate for 6x6 map: 0.85
'''