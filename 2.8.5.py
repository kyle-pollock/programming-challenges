import sys
import math

NUM_CARDS = 52
values = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace' ]
suits = [ 'Clubs', 'Diamonds', 'Hearts', 'Spades' ]

def applyShuffle(deck, shuffle):
    newDeck = [ 0 for x in range(NUM_CARDS + 1)]
    for j in range(1, NUM_CARDS + 1):
        i = shuffle[j]
        newDeck[j] = deck[i]
    return newDeck

def getValue(card):
    return values[(card-1) % len(values)]

def getSuit(card):
    return suits[math.floor((card-1) / len(values))]

def printDeck(deck):
    for i in range(1, NUM_CARDS+1):
        card = deck[i]
        print("{0} of {1}".format(getValue(card), getSuit(card)))


cases = int(sys.stdin.readline().strip())
sys.stdin.readline()

for case in range(cases):
    deck = [ x for x in range(0, NUM_CARDS + 1)]
    shuffles = int(sys.stdin.readline().strip())
    shuffleDict = {}

    numTokens = shuffles * NUM_CARDS
    count = 0
    allTokens = []
    while count < numTokens:
        shuffleLine = [int(x) for x in sys.stdin.readline().strip().split()]
        count += len(shuffleLine)
        allTokens.extend(shuffleLine)

    for shuffle in range(1, shuffles+1):
        shuffleDict[shuffle] = [0] + allTokens[((shuffle-1) * NUM_CARDS):NUM_CARDS*shuffle]

    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            break
        currentShuffle = int(line)
        deck = applyShuffle(deck, shuffleDict[currentShuffle])
    if case > 0:
        print()
    printDeck(deck)
