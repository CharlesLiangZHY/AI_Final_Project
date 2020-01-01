from newFrame import *
import ASIIC_Art
import Boring_Agent
import Search_Agent

def argParse(argv):
    if '-s' in argv:
        return "Debug"
    elif '-pacman' in sys.argv:
        return "Pacman"
    elif '-ll' in sys.argv:
        return "LongLiveSnake"
    elif '-b' in sys.argv:
        return "Boring"
    elif '-g' in sys.argv:
        return "Greedy"
    

if __name__ == '__main__':
    row = 10 # default
    col = 10 # default
    grid = 40 # default
    # parsing #row, #col and grid side length 
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-w':
            col = int(sys.argv[i+1])
            continue
        elif sys.argv[i] == '-h':
            row = int(sys.argv[i+1])
            continue
        elif sys.argv[i] == '-grid':
            grid = int(sys.argv[i+1])
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

        elif argParse(sys.argv) == "Boring":
            width = col * grid
            height = row * grid
            pygame.init()
            window = pygame.display.set_mode((width,height))
            clock = pygame.time.Clock()

            world = Simplified_World(row,col)
            world.draw(window, width, height)

            move = 0
            while True:
                pygame.time.delay(25)
                clock.tick(50) # frame
                # event listening (Essential!)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                
                d = Boring_Agent.boringAgent(world)
                move += 1
                if d != None:
                    if world.moveSnake(d[0],d[1]):
                        pass
                    else:
                        break
                        # pass
                else:
                    break
                world.draw(window, width, height)
                pygame.time.delay(25)

            print("End.")
            print("Score is ", len(world.curState)-2, ". Used ", move-1, "moves.")
        elif argParse(sys.argv) == "Greedy":
            width = col * grid
            height = row * grid
            pygame.init()
            window = pygame.display.set_mode((width,height))
            clock = pygame.time.Clock()

            world = Simplified_World(row,col)
            world.draw(window, width, height)

            move = 0
            while True:
                pygame.time.delay(25)
                clock.tick(50) # frame
                # event listening (Essential!)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                
                d = Search_Agent.greedyAgent(world)
                move += 1
                if d != None:
                    if world.moveSnake(d[0],d[1]):
                        pass
                    else:
                        break
                        # pass
                else:
                    break
                world.draw(window, width, height)
                pygame.time.delay(25)

            print("End.")
            print("Score is ", len(world.curState)-2, ". Used ", move-1, "moves.")

















