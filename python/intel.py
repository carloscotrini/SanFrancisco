def terrain_info(ants):
    terrain = {}
    for row in range(ants.self.rows):
        for col in range(ants.self.cols):
            if ants.passable((row,col)):
                terrain[(row,col)] = 1
            else:
                terrain[(row,col)] = 0
    return terrain
