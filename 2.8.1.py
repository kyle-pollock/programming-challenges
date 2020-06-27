import sys

for line in sys.stdin:
    tokens = [ int(i) for i in line.strip().split() ]
    n = tokens.pop(0)
    if n == 1:
        print("Jolly")
        continue
    s = [ 0 for i in tokens ]
    isJolly = True
    for i in range(1, len(tokens)):
        value = abs(tokens[i] - tokens[i - 1])
        if value == 0 or value >= n or s[value] == 1:
            isJolly = False
            break
        s[value] = 1
    tokens.pop(0)
    if not isJolly or (0 in tokens):
        print("Not jolly")
    else:
        print("Jolly")
