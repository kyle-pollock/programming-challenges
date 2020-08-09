import sys
from collections import deque

def hasSameColorNeigbhor(color, neighbors, colors):
    for neighbor in neighbors:
        if color == colors[neighbor]:
            return True
    return False


def colorNeighborsOppositeColor(color, neighbors, colors):
    for neighbor in neighbors:
        if colors[node] == 'R':
            colors[neighbor] = 'B'
        else:
            colors[neighbor] = 'R'


for n in sys.stdin:
    n = int(n)
    if n == 0:
        break

    num_edges = int(sys.stdin.readline())
    g = [[] for x in range(n)]
    colors = ['' for x in range(n)]
    discovered = [False for x in range(n)]

    for i in range(num_edges):
        v, e = [int(x) for x in sys.stdin.readline().split()]
        g[v].append(e)

    queue = deque()
    queue.append(0)

    isBicolorable = True
    colors[0] = 'R'
    discovered[0] = True
    while queue:
        node = queue.popleft()

        if hasSameColorNeigbhor(colors[node], g[node], colors):
            isBicolorable = False
            break

        colorNeighborsOppositeColor(colors[node], g[node], colors)

        for neighbor in g[node]:
            if not discovered[neighbor]:
                discovered[neighbor] = True
                queue.append(neighbor)

    if isBicolorable:
        print('BICOLORABLE.')
    else:
        print('NOT BICOLORABLE.')
