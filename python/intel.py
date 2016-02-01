def terrain_info(ants):
    terrain = [[0 for row in range(ants.self.rows)] for col in range(ants.self.cols)]
    for row in range(ants.self.rows):
        for col in range(ants.self.cols):
            if ants.passable((row,col)):
                terrain[row][col] = 1
    return terrain
