def execute(loc, target, path, ants):
    if len(path) > 0:
        next_step = path[0]
        walk_direction = ants.direction(loc, next_step)
        return walk_direction[0]
    else:
        return 'n'
