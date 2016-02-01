def l2_distance(ant, food):
	return (ant[0] - food[0]) ** 2 + (ant[1] - food[1]) ** 2

def pick(food, free_ants):
	closest_ant = None
	for ant in free_ants:
		if closest_ant == None:
			closest_ant = ant
		elif l2_distance(closest_ant, food) > l2_distance(ant, food):
			closest_ant = ant
	
	return closest_ant

