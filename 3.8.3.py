import sys

for a in sys.stdin:
    a = ''.join(sorted(a.strip()))
    b = ''.join(sorted(sys.stdin.readline().strip()))

    aDict = {}
    bDict = {}

    for i in a:
        if i in aDict:
            aDict[i] += 1
        else:
            aDict[i] = 1

    for i in b:
        if i in bDict:
            bDict[i] += 1
        else:
            bDict[i] = 1

    for key in [x for x in aDict.keys()]:
        if key not in bDict.keys():
            aDict.pop(key, None)
        else:
            aCount = aDict[key]
            bCount = bDict[key]
            if aCount > bCount:
                aDict[key] = bDict[key]
            elif bCount > aCount:
                bDict[key] = aDict[key]

    for key in [x for x in bDict.keys()]:
        if key not in aDict.keys():
            bDict.pop(key, None)

    for key in sorted(aDict.keys()):
        print(key * aDict[key], end='')
    print()
