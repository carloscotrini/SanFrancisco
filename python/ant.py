def execute(self, loc, target, path, ants):
    if len(path) > 0:
        next_step = path[0]
        walk_direction = ants.direction(loc, next_step)
        return walk_direction
    else:
        return 'n'
