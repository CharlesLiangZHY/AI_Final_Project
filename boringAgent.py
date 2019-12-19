from snake_frame import *






def boringAgent(world):
	r = world.row
	if r%2 != 0:
		print("The length of side must be even number.")
		return None

	s = world.snake
	loc = s.head.pos
	d = (s.dirX, s.dirY)
	f = world.food
	V = s.getValidMove()
	if len(V) == 0:
		return None

	if len(s.body) == 1 and (0,-1) in V and s.boringAgentInit != 1:
		if loc[0] == f[0] and loc[1] + 1 == f[1]:
			for v in V:
				if v != (0,-1):
					return v
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
