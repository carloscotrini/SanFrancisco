from random import randint

def execute(loc, target, path, ants):
    if len(path) > 0:
        next_step = path[1]
        walk_direction = ants.direction(loc, next_step)
        return walk_direction[0]
    else:
        d_list = ['n', 's', 'w', 'e']
        d = d_list[random.randint(0, 4)]
        return d
