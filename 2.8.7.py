import sys

cases = int(sys.stdin.readline())
sys.stdin.readline()


def getCorrectList(problems):
    correct = []
    for problemNumber, attempts in problems.items():
        found = False
        if not found:
            for attempt in attempts:
                if attempt[1] == 'C':
                    found = True
                    correct.append(problemNumber)
                    break
    return correct


def getPenaltyTime(problems, correctOnes):
    totalTime = 0
    numIncorrect = 0
    for solved in correctOnes:
        found = False
        if not found:
            for attempt in problems[solved]:
                if attempt[1] == 'I':
                    numIncorrect += 1
                if attempt[1] == 'C':
                    totalTime += attempt[0]
                    found = True
                    break
    return totalTime + (numIncorrect * 20)


for case in range(cases):
    scores = {}
    if case > 0:
        print()

    while True:
        line = sys.stdin.readline().strip()
        if len(line) == 0:
            break
        contestant, problem, time, L = line.split()
        contestant = int(contestant)
        problem = int(problem)
        time = int(time)

        if contestant not in scores:
            scores[contestant] = {}
        if problem not in scores[contestant]:
            scores[contestant][problem] = []
        scores[contestant][problem].append((time, L))

    players = {}
    for contestant, problems in scores.items():
        correctOnes = getCorrectList(problems)
        time = getPenaltyTime(problems, correctOnes)
        players[contestant] = (contestant, len(correctOnes), time,)

    values = list(players.values())

    values.sort(key = lambda c: (c[1] * -1, c[2], c[0]))

    for value in values:
        print(*value, sep=' ')
