import sys


for line in sys.stdin:
    numStudents, = [int(x) for x in line.split()]

    if numStudents == 0:
        break

    dollars = []
    cents = []
    bills = []
    for i in range(0, numStudents):
        dollar, cent = [int(x) for x in sys.stdin.readline().split('.')]
        bills.append([dollar, cent])
        dollars.append(dollar)
        cents.append(cent)

    totalDollars = sum(dollars)
    totalCents = sum(cents)
    totalDollars += (int(totalCents / 100))
    totalCents = (int(totalCents % 100))

    meanDollars = int(totalDollars / numStudents)
    remainderDollars = totalDollars % numStudents
    totalCents += (remainderDollars * 100)

    meanCents = int(totalCents / numStudents)
    remainderCents = totalCents % numStudents

    bills.sort(reverse=True, key=lambda item: item[0] + (item[1] / 100))

    tally = 0
    for bill in bills:
        if remainderCents > 0:
            item = abs(((bill[0] * 100) + bill[1]) - ((meanDollars * 100) + (meanCents + 1)))
            remainderCents -= 1
        else:
            item = abs(((bill[0] * 100) + bill[1]) - ((meanDollars * 100) + (meanCents)))
        tally += item
    print('${0:.2f}'.format(tally / 2 / 100))
