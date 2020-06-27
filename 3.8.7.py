import sys
from collections import deque

def getDoublets(target, words):
    result = []
    for i in range(len(target)):
        for k in "abcdefghijklmnopqrstuvwxyz":
            word = target[:i] + k + target[i+1:]
            if word in words:
                result.append(word)

    return result

def bfs(start, end, words):
    visited = {start: None}
    words.remove(start)
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node == end:
            path = deque()
            path.appendleft(node)
            curr = visited[node]
            while curr != None:
                path.appendleft(curr)
                curr = visited[curr]
            return "\n".join(path)

        for doublet in getDoublets(node, words):
            visited[doublet] = node
            words.remove(doublet)
            queue.append(doublet)
    return "No solution."

allwords = set()
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        break
    allwords.add(line)

game = 0
for line in sys.stdin:
    if game > 0:
        print()
    start, end = line.strip().split()
    if len(start) != len(end):
        print("No solution.")
    elif start not in allwords:
        print("No solution.")
    elif end not in allwords:
        print("No solution.")
    else:
        print(bfs(start, end, {x for x in allwords if len(x) == len(end)}))
    game += 1
