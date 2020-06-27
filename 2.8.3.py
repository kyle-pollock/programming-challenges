import sys

saturday = 7
cases = int(sys.stdin.readline().strip())

def markFridays(days):
    for i in range(6, len(days), 7):
        days[i] = '@'

def markDays(days, average, symbol):
    for i in range(average, len(days), average):
        if days[i] != '@':
            days[i] = symbol

for case in range(cases):
    parameterCache = {}
    numDays = int(sys.stdin.readline().strip())
    days = [ 0 for x in range(numDays+1)]
    days[0] = '@'
    markFridays(days)
    markDays(days, saturday, '@')
    numParties = int(sys.stdin.readline().strip())

    for i in range(numParties):
        param = int(sys.stdin.readline().strip())
        if param in parameterCache:
            continue
        else:
            parameterCache[param] = True
            markDays(days, param, 1)
    print(days.count(1))
