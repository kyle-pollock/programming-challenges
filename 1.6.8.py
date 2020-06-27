import sys

cases = int(sys.stdin.readline())

sys.stdin.readline()

def getWinners(candidates, ballots):
    scoreboard = [ 0 for x in candidates ]

    for ballot in ballots:
        scoreboard[ballot[0]] += 1

    # single winner?
    for i in range(1, len(scoreboard)):
        if (scoreboard[i] / (len(ballots))) > .5:
            return [ candidates[i] ]
    # tie?
    pops = set()
    for i in range(1, len(scoreboard)):
        if (scoreboard[i] > 0):
            pops.add(scoreboard[i])

    if len(pops) == 1:
        tied = []
        for i in range(1, len(scoreboard)):
            if (scoreboard[i] > 0):
                tied.append(candidates[i])
        return tied

    return []


def getLosers(candidates, ballots, prevLosers):
    scoreboard = [ 0 for x in candidates ]

    for ballot in ballots:
        scoreboard[ballot[0]] += 1

    min = 999999
    for i in range(1, len(scoreboard)):
        if scoreboard[i] < min and i not in prevLosers:
            min = scoreboard[i]

    losers = []
    for i in range(1, len(scoreboard)):
        if scoreboard[i] == min and i not in prevLosers:
            losers.append(i)

    return losers



def elect(candidates, ballots):

    losers = []
    while True:
        winners = getWinners(candidates, ballots)

        if len(winners) > 0:
            print(*winners, sep='\n')
            break

        newLosers = getLosers(candidates, ballots, losers)

        for ballot in ballots:
            for l in newLosers:
                ballot.remove(l)

        losers.extend(newLosers)


for case in range(cases):
    candidates = ['blank']
    ballots = []

    numCandidates = int(sys.stdin.readline())

    for i in range(numCandidates):
        candidates.append(sys.stdin.readline().strip())

    for ballot in sys.stdin:
        ballot = ballot.strip()
        if len(ballot) == 0:
            if case > 0:
                print()
            elect(candidates, ballots)
            break;

        ballot = [ int(vote) for vote in ballot.split()]
        ballots.append(ballot)

if case > 0:
    print()
elect(candidates, ballots)
