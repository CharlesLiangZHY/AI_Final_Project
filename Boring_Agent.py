from newFrame import *

def boringAgent(world):
    r = world.row
    c = world.col
    S = world.curState
    V = getValidMove(S, r, c)
    if len(V) == 0:
            return None

    f = S[0] # food
    x = S[1][0] # head x
    y = S[1][1] # head y

    if c%2 == 0:
        if len(S) == 2 and (0,-1) in V and world.boringAgentInit == 0:
            if x == f[0] and y-1 == f[1]:
                return (-1,0) # left
            else:
                
                return (0,-1) # up
        else:

            if y == 1:
                world.boringAgentInit = 1
                if (-1,0) in V:
                    return (-1,0) # left
                else:
                    if (0,1) in V:
                        return (0,1) # down
            else:
                if x == 1:
                    if (0,1) in V:
                        return (0,1) # down
                    else:
                        if (1,0) in V:
                            return (1,0) # right
                elif x == c:
                    if (0,-1) in V:
                        return (0,-1) # up
                    else:
                        if (-1,0) in V:
                            return (-1,0) # left
                elif y == r and x%2 == 1:
                    return (1,0) # right
                elif y == 2 and x%2 == 0:
                    return (1,0) # right
                elif y == r and x%2 == 0:
                    return (0,-1) # up
                elif y == 2 and x%2 == 1:
                    return (0,1) # down
                else:
                    if x%2 == 1:
                        return (0,1) # down
                    else:
                        return (0,-1) # up
                    
    elif r%2 == 0:
        
        if len(S) == 2 and (-1,0) in V and world.boringAgentInit == 0:
            
            if x-1 == f[0] and y == f[1]:
                return (0,-1) # up
            else:
                return (-1,0) # left
        else:

            if x == 1:
                world.boringAgentInit = 1
                if (0,1) in V:
                    return (0,1) # down
                else:
                    if (1,0) in V:
                        
                        return (1,0) # right
            else:
                if y == r:
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
                elif x == c and y%2 == 1:
                    return (-1,0) # left
                elif x == 2 and y%2 == 0:
                    return (1,0) # right
                elif x == c and y%2 == 0:
                    return (0,-1) # up
                elif x == 2 and y%2 == 1:
                    return (0,-1) # up
                else:
                    if y%2 == 1:
                        return (-1,0) # left
                    else:
                        return (1,0) # right   

    else: # odd side length

        if len(S) == 2 and world.boringAgentInit == 0:
            if x == f[0] and y - 1 == f[1]:
                return (-1,0) # left
            else:
                if (0,-1) in V:
                    return (0,-1) # up
                else:
                    world.boringAgentInit = 2
                    return (-1, 0) # left
        else:
            if y == 1:
                if (-1,0) in V:
                    return (-1,0) # left
                else:
                    return (0,1) # down
            else:
                if x < c and x%2 == 1:
                    if (0,1) in V:
                        return (0,1) # down
                    else:
                        return (1,0) # right
                elif x < c-1 and x%2 == 0:
                    if (0,-1) in V and y != 2:
                        return (0,-1) # up
                    else:
                        if y == 2:
                            return (1,0) # right
                elif x == c-1:
                    if y == r:
                        if world.boringAgentInit == 2:
                            world.boringAgentInit = 1
                            return (0,-1) # up

                        else:
                            world.boringAgentInit = 2
                            return (1,0) # right
                    elif y%2 == 0:
                        return (1,0) # right
                    elif y%2 == 1 and y > 1:
                        return (0,-1) # up  
                elif x == c:
                    if y == r:
                        return (0,-1) # up
                    else:
                        if y%2 == 0:
                            return (0,-1) # up
                        else:
                            return (-1,0) #left

