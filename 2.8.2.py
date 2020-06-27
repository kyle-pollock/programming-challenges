import sys
import math

numCards = 52
numSuits = 4

values = [ '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A' ]
suits = [ 'C', 'D', 'H', 'S' ]


def blackWins():
    print("Black wins.")

def whiteWins():
    print("White wins.")

def tie():
    print("Tie.")


def rankCard(value, suit):
    for i in range(math.floor(numCards/numSuits)):
        if values[i] == value:
            for j in range(numSuits):
                if suits[j] == suit:
                    return(i*numSuits + j)

def suit(card):
    return suits[card % numSuits]

def value(card):
    return values[math.floor(card / numSuits)]

def number(card):
    return math.floor(card / numSuits)

def highCard(blackHand, whiteHand):
    for i in reversed(range(len(blackHand))):
        if number(blackHand[i]) > number(whiteHand[i]):
            blackWins()
            return
        elif number(whiteHand[i]) > number(blackHand[i]):
            whiteWins()
            return
    tie()


def isTwoPair(hand):
    counter = [ 0 for x in values ]
    for card in hand:
        counter[number(card)] += 1
    pairs = []

    for i in range(len(counter)):
        if counter[i] == 2:
            pairs.append(i)

    return list(reversed(pairs))

def isPair(hand):
    counter = [ 0 for x in values ]
    for card in hand:
        counter[number(card)] += 1
    pairs = []
    if 2 in counter:
        return counter.index(2)
    else:
        return -1


def isStraight(hand):
    return [number(x) for x in hand] == list(range(number(hand[0]), number(hand[4])+1))

def isStraightFlush(hand):
    suits = set()
    for card in hand:
        suits.add(suit(card))
    if len(suits) == 1:
        return isStraight(hand)

def isFourOfAKind(hand):
    counter = [ 0 for x in values ]
    for card in hand:
        counter[number(card)] += 1
    if 4 in counter:
        return counter.index(4)
    if 5 in counter:
        return counter.index(5)
    else:
        return -1

def isThreeOfAKind(hand):
    counter = [ 0 for x in values]
    for card in hand:
        counter[number(card)] += 1
    if 3 in counter:
        return counter.index(3)
    else:
        return -1

def isFullHouse(hand):
    counter = [ 0 for x in values ]
    for card in hand:
        counter[number(card)] += 1
    if 3 in counter and 2 in counter:
        return counter.index(3)
    else:
        return -1

def isFlush(hand):
    suits = set()
    for card in hand:
        suits.add(suit(card))
    return len(suits) == 1



for line in sys.stdin:
    game = [ card for card in line.strip().split() ]

    blackHand = sorted([rankCard(x[0], x[1]) for x in game[:5]])
    whiteHand = sorted([rankCard(x[0], x[1]) for x in game[5:]])

    if isStraightFlush(blackHand):
        if isStraightFlush(whiteHand):
            highCard(blackHand, whiteHand)
        else:
            blackWins()
    elif isStraightFlush(whiteHand):
        whiteWins()

    elif isFourOfAKind(blackHand) > -1:
        if isFourOfAKind(whiteHand) > -1:
            blackHigh = isFourOfAKind(blackHand)
            whiteHigh = isFourOfAKind(whiteHand)
            if blackHigh > whiteHigh:
                blackWins()
            elif whiteHigh > blackHigh:
                whiteWins()
            else:
                tie()
        else:
            blackWins()
    elif isFourOfAKind(whiteHand) > -1:
        whiteWins()

    elif isFullHouse(blackHand) > -1:
        if isFullHouse(whiteHand) > -1:
            blackHigh = isFullHouse(blackHand)
            whiteHigh = isFullHouse(whiteHand)
            if blackHigh > whiteHigh:
                blackWins()
            elif whiteHigh > blackHigh:
                whiteWins()
            else:
                tie()
        else:
            blackWins()
    elif isFullHouse(whiteHand) > -1:
        whiteWins()

    elif isFlush(blackHand):
        if isFlush(whiteHand):
            highCard(blackHand, whiteHand)
        else:
            blackWins()
    elif isFlush(whiteHand):
        whiteWins()

    elif isStraight(blackHand):
        if isStraight(whiteHand):
            highCard(blackHand, whiteHand)
        else:
            blackWins()
    elif isStraight(whiteHand):
        whiteWins()

    elif isThreeOfAKind(blackHand) > -1:
        if isThreeOfAKind(whiteHand) > -1:
            blackHigh = isThreeOfAKind(blackHand)
            whiteHigh = isThreeOfAKind(whiteHand)
            if blackHigh > whiteHigh:
                blackWins()
            elif whiteHigh > blackHigh:
                whiteWins()
            else:
                tie()
        else:
            blackWins()
    elif isThreeOfAKind(whiteHand) > - 1:
        whiteWins()

    elif len(isTwoPair(blackHand)) == 2:
        if len(isTwoPair(whiteHand)) == 2:
            blackPairs = isTwoPair(blackHand)
            whitePairs = isTwoPair(whiteHand)
            winnerFound = False
            for i in range(2):
                if blackPairs[i] > whitePairs[i]:
                    winnerFound = True
                    blackWins()
                    break;
                elif whitePairs[i] > blackPairs[i]:
                    winnerFound = True
                    whiteWins()
                    break;

            if not winnerFound:
                highCard(list(filter(lambda a: values.index(value(a)) not in blackPairs, blackHand)), list(filter(lambda a: values.index(value(a)) not in whitePairs, whiteHand)))

        else:
            blackWins()
    elif len(isTwoPair(whiteHand)) == 2:
        whiteWins()

    elif isPair(blackHand) > -1:
        if isPair(whiteHand) > -1:
            blackHigh = isPair(blackHand)
            whiteHigh = isPair(whiteHand)
            if blackHigh > whiteHigh:
                blackWins()
            elif whiteHigh > blackHigh:
                whiteWins()
            elif blackHigh == whiteHigh:
                highCard(list(filter(lambda a: values.index(value(a)) != blackHigh, blackHand)), list(filter(lambda a: values.index(value(a)) != whiteHigh, whiteHand)))
        else:
            blackWins()

    elif isPair(whiteHand) > -1:
        whiteWins()

    else:
        highCard(blackHand, whiteHand)
