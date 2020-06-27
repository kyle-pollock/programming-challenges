import sys

cases = int(sys.stdin.readline().strip())
sentinel = 999999999
answers = {}
hashtable = {}

for case in range(cases):
    hashtable = {}
    answers = {}
    p, n = [int(x) for x in sys.stdin.readline().strip().split()]
    lines = []
    for i in range(p):
        lines.append(["{0}.".format(x.strip()) for x in sys.stdin.readline().strip().split(".:")[0].split(".,")])
    names = []
    for i in range(n):
        names.append(sys.stdin.readline().strip())

    for line in lines:
        for author in line:
            answers[author] = sentinel
            hashtable[author] = set()

    for line in lines:
        for author in line:
            hashtable[author] = hashtable[author].union(set(line)).difference(set([author]))

    if 'Erdos, P.' not in hashtable:
        for name in names:
            print("{0} infinity".format(name))
        continue

    answers['Erdos, P.'] = 1
    stack = [(hashtable['Erdos, P.'], 1)]
    while stack:
        authors, number = stack.pop()
        for author in authors:
            if answers[author] > number:
                answers[author] = number
                stack.append((hashtable[author], number + 1))

    print("Scenario {0}".format(case + 1))
    for name in names:
        if name not in answers or answers[name] == sentinel:
            print("{0} infinity".format(name))
        else:
            print("{0} {1}".format(name, answers[name]))
