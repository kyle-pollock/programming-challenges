import sys

categories = [ 1, 2, 3, 4, 5, 6, 'chance', '3kind', '4kind', '5kind', 'short', 'long', 'full']

def isKind(roll, digit):
    freq = [ 0 for x in range(7) ]
    for die in roll:
        freq[die] += 1
        if freq[die] == digit:
            return True
    return False


def isShort(roll):
    if 1 in roll and 2 in roll and 3 in roll and 4 in roll:
        return True
    if 2 in roll and 3 in roll and 4 in roll and 5 in roll:
        return True
    if 3 in roll and 4 in roll and 5 in roll and 6 in roll:
        return True
    return False


def isLong(roll):
    if 1 in roll and 2 in roll and 3 in roll and 4 in roll and 5 in roll:
        return True
    if 2 in roll and 3 in roll and 4 in roll and 5 in roll and 6 in roll:
        return True
    return False


def isFull(roll):
    freq = [ 0 for x in range(7) ]
    for die in roll:
        freq[die] += 1
    return 2 in freq and 3 in freq


def calcPoints(roll, category):
    points = 0
    if category in [1,2,3,4,5,6]:
        points = (roll.count(category) * category)
    elif category == 'chance':
        points = sum(roll)
    elif category == '3kind':
        if isKind(roll, 3):
            points = sum(roll)
    elif category == '4kind':
        if isKind(roll, 4):
            points = sum(roll)
    elif category == '5kind':
        if isKind(roll, 5):
            points = 50
    elif category == 'short':
        if isShort(roll):
            points = 25
    elif category == 'long':
        if isLong(roll):
            points = 35
    elif category == 'full':
        if isFull(roll):
            points = 40
    return points

def newSolution():
    return [0 for x in range(len(categories)+2)]

def createBitMask(num):
    result = 0
    for i in range(num):
        result += 2**i
    return result

def clearBit(value, bit):
    return value & ~(1<<bit)

def setBit(value, bit):
    return value | (1<<bit)

def getSetBits(value):
    bits = []
    for i in range(13):
        if value & 2**i:
            bits.append(i)
    return bits

def getZeroBit(value):
    for i in range(13):
        if value & 2**i == 0:
            return i

def getStart(numBits):
    result = 0
    for i in range(numBits):
        result = setBit(result, i)
    return result

def getEnd(numBits):
    result = (2**13) - 1
    for i in reversed(range(13 - numBits)):
        result = clearBit(result, i)
    return result

def isBonus(prev, new):
    return (sum(prev[:5]) + new) >= 63

def solve(rolls, num_cats, roll_mask, memo):
    if (num_cats, roll_mask) in memo:
        return memo[num_cats, roll_mask]

    if num_cats == 1:
        roll = rolls[getSetBits(roll_mask)[0]]
        points = calcPoints(roll, categories[0])
        solution = newSolution()
        solution[0] = points
        solution[14] = points
        memo[(num_cats, roll_mask)] = solution
        return solution

    pointsCache = []
    for i in range(13):
        pointsCache.append(calcPoints(rolls[i], categories[num_cats-1]))

    start = getStart(num_cats)
    end = getEnd(num_cats)
    for mask in range(start, end+1):
        setBits = getSetBits(mask)
        if len(getSetBits(mask)) == num_cats:
            max = -1
            for x in setBits:
                prevMask = clearBit(mask, x)
                prevPoints = solve(rolls, num_cats-1, prevMask, memo)
                newPoints = pointsCache[x]

                bonus = 0
                if num_cats == 6 and isBonus(prevPoints, newPoints):
                    bonus = 35

                total = prevPoints[14] + newPoints + bonus
                if total > max:
                    max = total
                    sol = list(prevPoints)
                    sol[num_cats-1] = newPoints
                    if bonus > 0:
                        sol[13] = bonus
                    sol[14] = total

            memo[num_cats, mask] = sol
    return memo[num_cats, roll_mask]

round = 0
for line in sys.stdin:
    if round == 0:
        round = 1
        rolls = []
    rolls.append([int(x) for x in line.split()])
    if round == 13:
        print(*solve(rolls, 13, createBitMask(13), {}), sep=' ')
        round = 0
    else:
        round += 1
