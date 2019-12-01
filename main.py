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
        while flag:
            # event listening (Essential!)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.time.delay(20)
            clock.tick(5) # frame

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    dirx = -1
                    diry = 0
                    if world.snakeMove(dirx, diry):
                        pass
                    else:
                        flag = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    dirx = 1
                    diry = 0
                    if world.snakeMove(dirx, diry):
                        pass
                    else:
                        flag = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    dirx = 0
                    diry = -1
                    if world.snakeMove(dirx, diry):
                        pass
                    else:
                        flag = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    dirx = 0
                    diry = 1
                    if world.snakeMove(dirx, diry):
                        pass
                    else:
                        flag = False

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

        print(snake.head.pos)