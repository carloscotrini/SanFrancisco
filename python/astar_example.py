from astar import *

# ================= EXAMPLE USAGE ================
ants_map = [[LAND for col in range(8)] for row in range(8)]
ants_map[2][5] = 'A'
ants_map[3][5] = 'A'
ants_map[4][5] = 'A'
ants_map[5][5] = 'A'

# Update Map
astar_map = make_map(ants_map)

# Call A star search
path = astar_search(tuple([1, 1]), tuple([5, 7]), astar_map)

# print results
if path is None:
    print "No path found"
else:
    print "Path found:", path


