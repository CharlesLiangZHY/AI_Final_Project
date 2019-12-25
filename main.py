from snake_frame import *

from boringAgent import *
from searchAgent import *


def Long_Live_Snake():
    print("\
              xxxxxxxxxxxx\n\
            xxx           xxxxxxxx\n\
           xx              xx-----xxxx\n\
          xx         xxx   x xx-------xxxx\n\
         xx         x| x   x   xx--------xx\n\
        xx         x|| x   x    xx---------xx\n\
        xx        x ||x    x      xx--------xx\n\
        xx         xxx    xx        x---------xx\n\
        xx               xx          x---------xx\n\
        xx              xx            x---------xx\n\
        xx             xx              x---------xx\n\
         xx           xx               x--------xx\n\
          xx       xxx                 x-------xx\n\
            xxxxxxx---xx               x-------x\n\
             xx  x------x             x------x      x\n\
             xx  x-------x           xx-----x      x-\n\
            xx    x------x          xx-----x      x-x\n\
           xx      x-----x         xx----xx      x-x\n\
          x x       x---x         xx---xx       x-x\n\
         x   x      x--x         xx---xx       x-x\n\
        x     x      xx         xx---xx       x-x\n\
       x      x      x         xx---xx       x--x\n\
                    x         xx---xx       x--xx\n\
                  xx         xx---xx       x--x x\n\
                 x          xx--xx        x--x  x\n\
               xx          xx--x        xx--x   x\n\
              xx          xx--xx      xx---x    x\n\
             x           xx-----xx   xx---x     x\n\
            x            xx------xxxx---xx     x\n\
            x             xx-----------x      x\n\
            x               xx-------xx      x\n\
             x                xxxxxxx       x\n\
              x                           xx\n\
               xx                       xx\n\
                 xx                   xx\n\
                   xxx             xxx\n\
                      xxxxxxxxxxxxx")


def whosBOSS():
  print("\
                                        ,==.\n\
                                        \\ o ',\n\
                        .--.             \\    \\.''..''..''.\n\
 _       _       _     '-._ \\            /    ;'..''..''..'\n\
|_|     |_|     |_|    .-'  /           /   .'         .''.    .''..''..''..''.\n\
                        '--'            \"==\"           '..'    '..''..''..''..'\n\
                                                       .''..''..''.\n\
                                                       '..''..''..'")

def argParse(argv):
    if '-k' in sys.argv or '-key' in sys.argv or '-keyboard' in argv:
        if '-s' in sys.argv or '-step' in sys.argv:
            return "Step" 
        else:
            return "Keyboard"
    elif '-random' in sys.argv:
     return "Random"
    elif '-pacman' in sys.argv:
        return "Pacman"
    elif '-ll' in sys.argv:
        return "LongLiveSnake"
    elif '-boring' in sys.argv:
        return "Boring"
    elif '-g' in sys.argv:
        return "Greedy"
    elif '-f' in sys.argv:
        return "Forward"

if __name__ == '__main__':
    row = 8
    col = 8
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-w':
            row = int(sys.argv[i+1])
            continue
        elif sys.argv[i] == '-h':
            col = int(sys.argv[i+1])
            continue
    if row < 2 or col < 2:
        print("The map is too small!")
    else:
        if argParse(sys.argv) == "Keyboard" or argParse(sys.argv) == "Step":
            mode = 0
            if argParse(sys.argv) == "Step":
                mode = 1
            width = row*40
            height = col*40
            pygame.init()
            window = pygame.display.set_mode((width,height))
            clock = pygame.time.Clock()

            flag = True
            world = World(row,col)
            receiveCmd = False
            dirx = 0
            diry = 0
            while flag:       
                pygame.time.delay(100)
                clock.tick(5) # frame
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
                if mode == 1: # Step mode
                    if receiveCmd:
                        if world.snakeMove(dirx, diry):
                            print(world.snake.getValidMove())
                            print(world.snake.body[-1].pos)
                            world.calculateDistance(world.snake.body[-1].pos)
                            print(world.distance)
                            pass
                        else:
                            flag = False
                else:
                    if world.snakeMove(dirx, diry):
                        pass
                    else:
                        flag = False

                flag = flag and world.draw(window, width, height)
                receiveCmd = False

            print("End.")
            print("Score is ", len(world.snake.body)-1)

        elif argParse(sys.argv) == "Random":
            width = row*40
            height = col*40
            pygame.init()
            window = pygame.display.set_mode((width,height))
            clock = pygame.time.Clock()


            world = World(row,col)
            snake = world.snake
            world.draw(window, width, height)
            pygame.time.delay(200)

            while True:       
                # event listening (Essential!)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                pygame.time.delay(50)
                clock.tick(10)

                V = snake.getValidMove()
                if len(V) == 0:
                    pass
                else: 
                    v = V[random.randint(0,len(V)-1)]
                if world.snakeMove(v[0], v[1]):
                    pass
                else:
                    break
                world.draw(window, width, height)
            print("End.")
            print("Score is ", len(world.snake.body)-1)

        elif argParse(sys.argv) == "Boring":
            width = row*40
            height = col*40
            pygame.init()
            window = pygame.display.set_mode((width, height))
            clock = pygame.time.Clock()


            world = World(row,col)
            snake = world.snake
            world.draw(window, width, height)
            pygame.time.delay(200)

            while True:       
                # event listening (Essential!)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                pygame.time.delay(50)
                clock.tick(10)

                d = boringAgent(world)
                
                if d != None:
                    world.snakeMove(d[0],d[1])
                    
                else:
                    break
                    # pass
                world.draw(window, width, height)

            print("End.")
            print("Score is ", len(world.snake.body)-1)
            
        elif argParse(sys.argv) == "Greedy":
            width = row*40
            height = col*40
            pygame.init()
            window = pygame.display.set_mode((width, height))
            clock = pygame.time.Clock()


            world = World(row,col)
            snake = world.snake
            world.draw(window, width, height)
            pygame.time.delay(200)

            

            while True:       
                # event listening (Essential!)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                pygame.time.delay(50)
                clock.tick(10)

                d = Greedy_Agent(world)
                if d != None:
                    world.snakeMove(d[0],d[1])
                else:
                    # break
                    pass
                world.draw(window, width, height)

            print("End.")
            print("Score is ", len(world.snake.body)-1)

        elif argParse(sys.argv) == "Forward":
            width = row*40
            height = col*40
            pygame.init()
            window = pygame.display.set_mode((width, height))
            clock = pygame.time.Clock()


            world = World(row,col)
            snake = world.snake
            world.draw(window, width, height)
            pygame.time.delay(200)

            # d = Forward_Checking_Agent(world)
            # print(d)
            
            # if d != None:
            #     # print("OK")
            #     world.snakeMove(d[0],d[1])
            # else:
            #     # break
            #     pass
            # # print(world.snake.head.pos)
            # world.draw(window, width, height)
            
            while True:       
                # event listening (Essential!)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                pygame.time.delay(50)
                clock.tick(10)
                
                d = Forward_Checking_Agent(world)
                if d != None:
                    # print("OK")
                    world.snakeMove(d[0],d[1])
                else:
                    break
                    # pass
                world.draw(window, width, height)

            print("End.")
            print("Score is ", len(world.snake.body)-1)

    if argParse(sys.argv) == "Pacman":
        whosBOSS()
    elif argParse(sys.argv) == "LongLiveSnake":
        Long_Live_Snake()

