from newFrame import *
import ASIIC_Art
import Boring_Agent
import Search_Agent
import LongLive_Agent

def argParse(argv):
    if '-s' in argv:
        return "Debug"
    elif '-pacman' in sys.argv:
        return "Pacman"
    elif '-Snake' in sys.argv:
        return "LongLiveSnake"
    elif '-random' in sys.argv:
        return "Random"
    elif '-b' in sys.argv:
        return "Boring"
    elif '-g' in sys.argv:
        return "Greedy"
    elif '-ll' in sys.argv:
        return "LongLive"
    elif '-bfs' in sys.argv:
        return "BFS"
    elif '-astar' in sys.argv:
        return "Astar"
    
    

def visualize(agent, col, row, grid, timeDelay):
    width = col * grid
    height = row * grid
    pygame.init()
    window = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()

    world = Simplified_World(row,col)
    world.draw(window, width, height)

    move = 0
    while True:
        pygame.time.delay(5)
        clock.tick(50) # frame
        # event listening (Essential!)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        d = agent(world)
        move += 1
        if d != None:
            if world.moveSnake(d[0],d[1]):
                pass
            else:
                break
        else:
            break
            # pass # It will hold on the termination.
        world.draw(window, width, height)
        pygame.time.delay(timeDelay)

    score = len(world.curState)-2
    print("The map size is", row, "x", col, "; Score is", score, "; Used", move-1, "moves.")  
    if score == row*col - 1:
        print("Success!")

def run(agent, col, row):
    world = Simplified_World(row,col)

    move = 0
    while True and move < (row*col)**2: # to avoid endless loops
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
    print("The map size is", row, "x", col, "; Score is", score, "; Used", move-1, "moves.")  
    if score == row*col - 1:
        print("Success!")

def randomAgent(world):
    r = world.row
    c = world.col
    S = world.curState
    V = getValidMove(S, r, c)
    if len(V) == 0:
        return None
    return V[random.randint(0, len(V)-1)]

if __name__ == '__main__':
    row = 10 # default
    col = 10 # default
    grid = 40 # default
    visualization = True
    # parsing arguments
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-w':
            col = int(sys.argv[i+1])
            continue
        elif sys.argv[i] == '-h':
            row = int(sys.argv[i+1])
            continue
        elif sys.argv[i] == '-wh':
            row = int(sys.argv[i+1])
            col = int(sys.argv[i+1])
            continue
        elif sys.argv[i] == '-grid':
            grid = int(sys.argv[i+1])
            continue
        elif sys.argv[i] == '-nv': # not to visualize
            visualization = False
            continue
    if row < 2 or col < 2:
        print("The map is too small!")
    else:
        if argParse(sys.argv) == "Pacman":
            ASIIC_Art.whosBOSS()
        elif argParse(sys.argv) == "LongLiveSnake":
            ASIIC_Art.Long_Live_Snake()
        
        elif argParse(sys.argv) == "Debug":
            width = col * grid
            height = row * grid
            pygame.init()
            window = pygame.display.set_mode((width,height))
            clock = pygame.time.Clock()

            world = Simplified_World(row,col)
            world.draw(window, width, height)

            receiveCmd = False
            dirx = 0
            diry = 0

            while True:
                # print(world.curState[1])
                pygame.time.delay(25)
                clock.tick(50) # frame
                # event listening (Essential!)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        dirx = -1
                        diry = 0
                        receiveCmd = True
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        dirx = 1
                        diry = 0
                        receiveCmd = True
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                        dirx = 0
                        diry = -1
                        receiveCmd = True
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                        dirx = 0
                        diry = 1
                        receiveCmd = True

                if receiveCmd: # print debug information here
                    if world.moveSnake(dirx, diry):
                        pass
                    else:
                        break
                
                world.draw(window, width, height)
                receiveCmd = False
                pygame.time.delay(25)

        elif argParse(sys.argv) == "Random":
            if visualization:
                timeDelay = 10
                visualize(randomAgent, col, row, grid, timeDelay)
            else:
                run(randomAgent, col, row)

        elif argParse(sys.argv) == "Boring":
            if visualization:
                timeDelay = 10
                visualize(Boring_Agent.boringAgent, col, row, grid, timeDelay)
            else:
                run(Boring_Agent.boringAgent, col, row)

        elif argParse(sys.argv) == "Greedy":

            greedyAgent = Search_Agent.veryNaiveGreedyAgent
            # greedyAgent = Search_Agent.stillNaiveGreedyAgent

            if visualization:
                timeDelay = 25
                visualize(greedyAgent, col, row, grid, timeDelay)
            else:
                run(greedyAgent, col, row)

        elif argParse(sys.argv) == "LongLive":
            if visualization:
                timeDelay = 25
                visualize(LongLive_Agent.longLiveAgent, col, row, grid, timeDelay)
            else:
                run(LongLive_Agent.longLiveAgent, col, row)

        elif argParse(sys.argv) == "BFS":
            if visualization:
                timeDelay = 25
                visualize(Search_Agent.bfsAgent, col, row, grid, timeDelay)
            else:
                run(Search_Agent.bfsAgent, col, row)

        elif argParse(sys.argv) == "Astar":
            if visualization:
                timeDelay = 25
                visualize(Search_Agent.astarAgent, col, row, grid, timeDelay)
            else:
                run(Search_Agent.astarAgent, col, row)


        





    
















