def is_in_boundary(ants, visibility, cur_x, cur_y):
	if (visibility[cur_x][cur_y] > 0):
		delta = [(1,0),(0,1),(0,-1),(-1,0)]
		for dx,dy in delta:
			if visibility[(cur_x + dx) % ants.rows][(cur_y + dy) % ants.cols] == 0:
				return True
	return False

def issue_exploration_orders(ants, free_ants, visibility):
	for ant in free_ants:
		mx = int(sqrt(ants.viewradius2))
                for d_row in range(-mx,mx+1):
                    for d_col in range(-mx,mx+1):
			cur_x = ant[0] + d_row % ants.rows
			cur_y = ant[1] + d_col % ants.cols
			if is_in_boundary(ants, visibility, cur_x, cur_y):
				if visibility[oldest_loc_x][oldest_loc_y] < visibility[cur_x][cur_y]:
					oldest_loc_x = cur_x
					oldest_loc_y = cur_y
		ants.issue_order((ant, ants.direction(ant, (oldest_loc_x, oldest_loc_y))))
