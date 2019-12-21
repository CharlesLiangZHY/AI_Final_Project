from snake_frame import *






def boringAgent(world):
    r = world.row
    c = world.col
    s = world.snake
    x = s.head.pos[0]
    y = s.head.pos[1]
    f = world.food
    V = s.getValidMove()

    if len(V) == 0:
        return None

    if r%2 == 0:
        if len(s.body) == 1 and (0,-1) in V and s.boringAgentInit == 0:
            if x == f[0] and y-1 == f[1]:
                return (-1,0) # left
            else:
                
                return (0,-1) # up
        else:

            if y == 1:
                s.boringAgentInit = 1
                if (-1,0) in V:
                    return (-1,0) # left
                else:
                    if (0,1) in V:
                        print("OK")
                        return (0,1) # down
            else:
                if x == 1:
                    if (0,1) in V:
                        return (0,1) # down
                    else:
                        if (1,0) in V:
                            return (1,0) # right
                elif x == r:
                    if (0,-1) in V:
                        return (0,-1) # up
                    else:
                        if (-1,0) in V:
                            return (-1,0) # left
                elif y == c and x%2 == 1:
                    return (1,0) # right
                elif y == 2 and x%2 == 0:
                    return (1,0) # right
                elif y == c and x%2 == 0:
                    return (0,-1) # up
                elif y == 2 and x%2 == 1:
                    return (0,1) # down
                else:
                    if x%2 == 1:
                        return (0,1) # down
                    else:
                        return (0,-1) # up
                    
    elif c%2 == 0:
        
        if len(s.body) == 1 and (-1,0) in V and s.boringAgentInit == 0:
            
            if x-1 == f[0] and y == f[1]:
                return (0,-1) # up
            else:
                return (-1,0) # left
        else:

            if x == 1:
                s.boringAgentInit = 1
                if (0,1) in V:
                    return (0,1) # down
                else:
                    if (1,0) in V:
                        return (1,0) # right
            else:
                if y == c:
                    if (1,0) in V:
                        return (1,0) # right
                    else:
                        if (0,-1) in V:
                            return (0,-1) # up
                elif y == 1:
                    if (-1,0) in V:
                        return (-1,0) # left
                    else:
                        if (0,1) in V:
                            return (0,1) # down
                elif x == r and y%2 == 1:
                    return (-1,0) # left
                elif x == 2 and y%2 == 0:
                    return (1,0) # right
                elif x == r and y%2 == 0:
                    return (0,-1) # up
                elif x == 2 and y%2 == 1:
                    return (0,-1) # up
                else:
                    if y%2 == 1:
                        return (-1,0) # left
                    else:
                        return (1,0) # right   

    else: # odd side length

        if len(s.body) == 1 and s.boringAgentInit == 0:
            if x == f[0] and y - 1 == f[1]:
                return (-1,0) # left
            else:
                if (0,-1) in V:
                    return (0,-1) # up
                else:
                    s.boringAgentInit = 2
                    return (-1, 0) # left
        else:
            if y == 1:
                if (-1,0) in V:
                    return (-1,0) # left
                else:
                    return (0,1) # down
            else:
                if x < r and x%2 == 1:
                    if (0,1) in V:
                        return (0,1) # down
                    else:
                        return (1,0) # right
                elif x < r-1 and x%2 == 0:
                    if (0,-1) in V and y != 2:
                        return (0,-1) # up
                    else:
                        if y == 2:
                            return (1,0) # right
                elif x == r-1:
                    if y == c:
                        if s.boringAgentInit == 2:
                            s.boringAgentInit = 1
                            return (0,-1) # up

                        else:
                            s.boringAgentInit = 2
                            return (1,0) # right
                    elif y%2 == 0:
                        return (1,0) # right
                    elif y%2 == 1 and y > 1:
                        return (0,-1) # up  
                elif x == r:
                    if y == c:
                        return (0,-1) # up
                    else:
                        if y%2 == 0:
                            return (0,-1) # up
                        else:
                            return (-1,0) #left
