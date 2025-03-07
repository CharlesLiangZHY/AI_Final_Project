from snake_frame import *

from boringAgent import *
from searchAgent import *


if __name__ == '__main__':
    # R = int(sys.argv[1])
    for r in range(3,11):
        testTime = 100
        total = 0
        for i in range(testTime):
            w = World(r, r)
            move = 0
            while True:
                # d = boringAgent(w)
                d = Forward_Checking_Agent(w)
                move += 1
                if d != None and move < r**4:
                    w.snakeMove(d[0],d[1])
                else:
                    break
            total += move
            # print("Test",i+1,": Map size is ", r, " x ", r, ". Score is ", len(w.snake.body)-1, ". Used ", move, "moves.")
        print("Map size is", r, "Average move: ", total // testTime)





'''
Boring Agent
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

