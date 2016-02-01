def terrain_info(ants):
    terrain = [[0 for row in range(ants.rows)] for col in range(ants.cols)]
    for row in range(ants.rows):
        for col in range(ants.cols):
            if ants.passable((row,col)):
                terrain[row][col] = 1
    return terrain
