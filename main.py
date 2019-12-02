from snake_frame import *

def Long_Live_Snake():
    print("\
              xxxxxxxxxxxx\n\
            xxx           xxxxxxxx\n\
           xx              xx-----xxxx\n\
          xx         xxx   x xx-------xxxx\n\
         xx         x| x   x   xx--------xx\n\
        xx         x|| x   x    xx---------xx\n\
        xx        x ||x    x      xx--------xx\n\
        xx         xxx    xx       xx---------xx\n\
        xx               xx         xx---------xx\n\
        xx              xx           xx---------xx\n\
        xx             xx            xx---------xx\n\
         xx           xx             xx--------xx\n\
          xx       xxx               xx-------xx\n\
            xxxxxxx---xx             xx-------x\n\
             xx  x------x            xx------x      x\n\
             xx  x-------x           xx-----x      x-\n\
            xx    x------x          xx-----x      x-\n\
           xx      x-----x         xx----xx      x-\n\
          x x       x---x         xx---xx       x-x\n\
         x   x      x--x         xx---xx       x--x\n\
        x     x      xx         xx---xx       x--xx\n\
       x      x      x         xx---xx       x--x x\n\
                    x         xx---xx       x--x  x\n\
                  xx         xx---xx       x--x   x\n\
                 x          xx--xx        x--x   xx\n\
               xx          xx--x        xx--x   x\n\
              xx          xx--xx      xx---x    xx\n\
             xx           x-----xx   xx---x    xx\n\
             xx            xx-----xxxx---x    xx\n\
             xx             xx---------xx    xx\n\
             xx              xx------xx     xx\n\
             xx                xxxxxx      xx\n\
              xx                         xxx\n\
               xxx                     xxx\n\
                 xxxx               xxx\n\
                    xxxxxxxxxxxxxxxx")

def argParse(argv):
    if '-k' in sys.argv or '-key' in sys.argv or '-keyboard' in argv:
        if '-s' in sys.argv or '-step' in sys.argv:
            return "Step" 
        else:
            return "Keyboard"
    elif '-t' in sys.argv or '-test' in sys.argv:
     return "Test"

if __name__ == '__main__':

    if argParse(sys.argv) == "Keyboard" or argParse(sys.argv) == "Step":
        width = 100
        pygame.init()
        window = pygame.display.set_mode((width,width))
        clock = pygame.time.Clock()

        flag = True
        world = World(2)
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
            if receiveCmd:
                if world.snakeMove(dirx, diry):
                    pass
                else:
                    flag = False
            # pygame.time.delay(100)

            flag = flag and world.draw(window, width)
            receiveCmd = False

        print("End.")
        print("Score is ", len(world.snake.body)-1)

    elif argParse(sys.argv) == "Test":
        width = 200
        pygame.init()
        window = pygame.display.set_mode((width, width))
        clock = pygame.time.Clock()


        world = World(4)
        snake = world.snake
        world.draw(window, width)
        pygame.time.delay(1000)

        while True:       
            # event listening (Essential!)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.time.delay(1000)
            clock.tick(5)

            V = snake.getValidMove()
            if len(V) == 0:
                pass
            else: 
              if world.snakeMove(V[0][0], V[0][1]):
                print(V)
              else:
                break
            world.draw(window, width)
            



    else:
        Long_Live_Snake()

