from snake_frame import *



def argParse(argv):
    if '-k' in sys.argv or '-key' in sys.argv or '-keyboard' in argv:
        return "Keyboard"
    elif '-t' in sys.argv or '-test' in sys.argv:
     return "Test"

if __name__ == '__main__':

    if argParse(sys.argv) == "Keyboard":
        width = 400
        pygame.init()
        window = pygame.display.set_mode((width,width))
        clock = pygame.time.Clock()

        flag = True
        world = World(10)

        receiveCmd = False
        dirx = 0
        diry = 0
        while flag:
            # event listening (Essential!)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.time.delay(100)
            clock.tick(5) # frame

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    dirx = -1
                    diry = 0
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    dirx = 1
                    diry = 0
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    dirx = 0
                    diry = -1
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    dirx = 0
                    diry = 1
            
            if world.snakeMove(dirx, diry):
                pass
            else:
                flag = False
            # pygame.time.delay(100)

            flag = flag and world.draw(window,width)

        print("End.")
        print("Score is ", len(world.snake.body)-1)

    elif argParse(sys.argv) == "Test":
        world = World(10)
        snake = world.snake
        
        print(snake.head.pos)

        world.snakeMove(-1,0)

        print(snake.head.pos)

        snake.move(-1,0)

        print(snake.head)

    else:
     print("\
             xxxxxxxxxxxxx\n\
           xx            xxxxxxxxxxx\n\
          xx                xx------xxxx\n\
         xx           xxx    xx--------xxxx\n\
        xx           x  x     xxxx--------xx\n\
       xx           x  x      x   xx---------xx\n\
       xx           xxx       x    xx--------xx\n\
       xx                     x     xx---------xx\n\
       xx                     x      x----------xx\n\
       xx                   xx       x----------xx\n\
       xx                 xx          x---------xx\n\
        xx             xxx            x--------xx\n\
         xx          xx               x-------xx\n\
           xxxxxxxxxx--x              x------xx\n\
             x  x------x             x------xx\n\
             x x x-------x           x------x\n\
            x x   x------x           x-----x         xxxx\n\
           x x     x-----x          x----x         xx--x\n\
          x x       x---x          x---xx        xx--xx\n\
         x   x      x--x          x---x        xx--xx\n\
        x     x      xx          x---x        x--xx\n\
       x       x    xx          x---x        x--xx\n\
                   xx          x---x        x--x x\n\
                 xx           x---x        x--x  x\n\
                xx           x--xx        x--x  x\n\
               xx           x--x         x--x   x\n\
             xx           x---x       xx--x   x\n\
             xx           x-----x    xx---x   x\n\
             xx            xx-----xxxx---x    x\n\
             xx             xx----------x    x\n\
             xx              xx------xx     x\n\
             xx                xxxxxx      x\n\
              xx                         xx\n\
               xx                      xxx\n\
                xx                  xxx\n\
                  xxxxxxxxxxxxxxxxxx")