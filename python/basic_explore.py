from math import sqrt
from astar import *
from random import randint

def is_in_boundary(ants, visibility, cur_x, cur_y):
	if (visibility[cur_x][cur_y] > 0):
		delta = [(1,0),(0,1),(0,-1),(-1,0)]
		for dx,dy in delta:
			if visibility[(cur_x + dx) % ants.rows][(cur_y + dy) % ants.cols] == 0:
				return True
	return False

def issue_exploration_orders(ants, free_ants, visibility, destinations,
        astar_map):
        d_list = ['n', 's', 'w', 'e']
	for ant in free_ants:
		mx = int(sqrt(ants.viewradius2))
                oldest_loc_x = None
                oldest_loc_y = None
                for d_row in range(-mx,mx+1):
                    for d_col in range(-mx,mx+1):
			cur_x = (ant[0] + d_row) % ants.rows
			cur_y = (ant[1] + d_col) % ants.cols
                        if (cur_x, cur_y) in destinations:
                            continue
			if is_in_boundary(ants, visibility, cur_x, cur_y):
				if oldest_loc_x == None or visibility[oldest_loc_x][oldest_loc_y] < visibility[cur_x][cur_y]:
					oldest_loc_x = cur_x
					oldest_loc_y = cur_y
		
                #destinations[(oldest_loc_x, oldest_loc_y)] = True
                path = astar_search(ant, (oldest_loc_x, oldest_loc_y),
                        astar_map)
                if path:
                    if not path[1] in destinations:
                        d = ants.direction(ant, path[1])
                        ants.issue_order((ant, d[randint(0, len(d)-1)])         )
                        destinations[path[1]] = True
                    else:
                        d = d_list[random.randint(0, 4)]
                        ants.issue_order((ant, d))

        return destinations

