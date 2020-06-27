import sys

cases = int(sys.stdin.readline())
sys.stdin.readline()
for case in range(cases):
    if case > 0:
        print()

    frags = set()
    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            break
        frags.add(line)

    candidates = set()
    while len(frags) != 0:
        minFrags = [ x for x in frags if len(x) == len(min(frags, key=len)) ]
        maxFrags = [ x for x in frags if len(x) == len(max(frags, key=len)) ]

        newCandidates = set()
        for smaller in minFrags:
            for bigger in maxFrags:
                newCandidates.add(smaller + bigger)
                newCandidates.add(bigger + smaller)

        if len(candidates) == 0:
            candidates = newCandidates
        else:
            candidates &= newCandidates

        if len(candidates) == 1:
            break
        frags = [ x for x in frags if x not in minFrags + maxFrags ]
    print(list(candidates)[0])
