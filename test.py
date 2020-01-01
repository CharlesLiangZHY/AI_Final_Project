from newFrame import *



if __name__ == '__main__':
    row = 5
    col = 6
    w = Simplified_World(row,col)
    w.curState = [(1,1), (2,3), (2,4), (2,5), (3,5)]

    width = col*40
    height = row*40
    pygame.init()
    window = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    
    w.draw(window, width, height)
    pygame.time.delay(200)
    while True: 
              
        # event listening (Essential!)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.time.delay(25)
        clock.tick(50)
        w.draw(window, width, height)