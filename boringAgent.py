from snake_frame import *






def boringAgent(world):
    r = world.row
    
        

    s = world.snake
    loc = s.head.pos
    d = (s.dirX, s.dirY)
    f = world.food
    V = s.getValidMove()
    if len(V) == 0:
        return None

    if r%2 == 0:
        if len(s.body) == 1 and (0,-1) in V and s.boringAgentInit != 1:
            if loc[0] == f[0] and loc[1] - 1 == f[1]:
                return (-1,0)
            else:
                return (0,-1)
        else:

            if loc[1] == 1:
                s.boringAgentInit = 1
                if (-1,0) in V:
                    return (-1,0)
                else:
                    if (0,1) in V:
                        return (0,1)

            else:
                if loc[1] == r:
                    if (0,-1) in V:
                        return (0,-1)
                    else:
                        return (1,0)
                elif loc[1] == 2 and loc[0] != r:

                    if (0,1) in V:
                        return (0,1) # down
                    else:

                        return (1,0) # right
                elif loc[1] == 2 and loc[0] == r:
                    return (0,-1)
                else:
                    if (0,1) in V:
                        return (0,1)
                    else:
                        return (0,-1)
    else: # odd side length
        x = loc[0]
        y = loc[1]

        if len(s.body) == 1 and s.boringAgentInit == 0:
            if loc[0] == f[0] and loc[1] - 1 == f[1]:
                return (-1,0)
            else:
                if (0,-1) in V:
                    return (0,-1)
                else:
                    s.boringAgentInit = 2
                    return (-1, 0)



        if x < r-3 and x%2 == 1 and x+y <= r and y != 1:
            return (0,1) # down
        elif x <= r-3 and x%2 == 0 and x+y <= r+2 and y > 2:
            return (0,-1) # up
        elif x < r-3 and x%2 == 1 and x+y == r+1:
            return (1,0) # right
        elif x <= r-3 and x%2 == 0 and y == 2:
            return (1,0) # right
        elif x == r-2 and y == 2:
            return (0,1) # down
        elif x == r-2 and y == 3:
            return (1,0) # right
        elif x == r-1 and y >= 3 and y < r and y%2 == 1:
            return (0,1) # down
        elif x < r and x+y >= r+3 and y%2 == 0:
            return (-1,0) # left
        elif x < r and y%2 == 0 and x+y == r+2:
            return (0,1) # down
        elif x < r-1 and x+y >= r+3 and y%2 == 1:
            return (1,0) # right
        elif x == r-1 and y == r:
            return (1,0) # right
        elif x == r and y > 2:
            return (0,-1) # up
        elif x == r and y == 2 and s.boringAgentInit == 2:
            s.boringAgentInit = 1
            return (-1,0) # left
        elif x == r and y == 2 and s.boringAgentInit == 1:
            s.boringAgentInit = 2
            return (0,-1) # up
        elif x == r-1 and y == 2:
            return (0,-1) # up
        elif y == 1 and x <= r and x > 1 :
            return (-1,0) # left
        elif y == 1 and x == 1:
            return (0,1) # down