from math import sqrt
from itertools import product
from ants import *

class AStar(object):
    def __init__(self, graph):
        self.graph = graph
        
    def heuristic(self, node, start, end):
        raise NotImplementedError
        
    def search(self, start, end):
        openset = set()
        closedset = set()
        current = start
        openset.add(current)
        while openset:
            current = min(openset, key=lambda o:o.g + o.h)
            if current == end:
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                return path[::-1]
            openset.remove(current)
            closedset.add(current)
            for node in self.graph[current]:
                if node in closedset:
                    continue
                if node in openset:
                    new_g = current.g + current.move_cost(node)
                    if node.g > new_g:
                        node.g = new_g
                        node.parent = current
                else:
                    node.g = current.g + current.move_cost(node)
                    node.h = self.heuristic(node, start, end)
                    node.parent = current
                    openset.add(node)
        return None

class AStarNode(object):
    def __init__(self):
        self.g = 0
        self.h = 0
        self.parent = None
        
    def move_cost(self, other):
        raise NotImplementedError

class AStarGrid(AStar):
    def heuristic(self, node, start, end):
        # NOTE: this is traditionally sqrt((end.x - node.x)**2 + (end.y - node.y)**2)
        # However, if you are not interested in the *actual* cost, but only relative cost,
        # then the math can be simplified.
        return abs(end.x - node.x) + abs(end.y - node.y)
        #return sqrt((end.x - node.x)**2 + (end.y - node.y)**2)

class AStarGridNode(AStarNode):
    def __init__(self, x, y):
        self.x, self.y = x, y
        super(AStarGridNode, self).__init__()

    def move_cost(self, other):
        diagonal = abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
        return 14 if diagonal else 10

    def __repr__(self):
        return '(%d %d)' % (self.x, self.y)

def make_map(ants_map):
    rows = len(ants_map)
    cols = len(ants_map[0])

    nodes = [[AStarGridNode(r, c) for c in range(cols)] for r in range(rows)]
    graph = {}
    for x, y in product(range(rows), range(cols)):
        node = nodes[x][y]
        graph[node] = []
        for i, j in product([-1, 0, 1], [-1, 0, 1]):
            if not (0 <= x + i < rows): continue
            if not (0 <= y + j < cols): continue
            v = ants_map[x+i][y+j]
            # if not land, food, or dead ants
            if v != LAND and v != FOOD and v != DEAD: continue
            graph[nodes[x][y]].append(nodes[x+i][y+j])
    return graph, nodes

def astar_search(start_loc, dest_loc, astar_map):
    paths = AStarGrid(astar_map[0])
    nodes = astar_map[1]
    start = nodes[start_loc[0]][start_loc[1]]
    end = nodes[dest_loc[0]][dest_loc[1]]
    path = paths.search(start, end)
    if path:
        path = [tuple([p.x, p.y]) for p in path]
    return path

