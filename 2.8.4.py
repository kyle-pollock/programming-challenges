import sys

n = int(sys.stdin.readline().strip())
dictionary = []

def checkWord(dictionary, words, mapping):
    if not words:
        return True, mapping

    subwords = [w for w in dictionary if len(w) == len(words[0])]

    for w in subwords:
        if checkMapping(w, words[0], mapping):

            newMapping = {**createMap(w, words[0]), **mapping}
            values = list(newMapping.values())
            if len(values) != len(set(values)):
                continue

            isSolution, correctMapping = checkWord(dictionary, words[1:], newMapping)
            if isSolution:
                return True, correctMapping

    return False, {}

def createMap(word, target):
    mapping = {}
    for i in range(len(target)):
        currentTargetLetter = target[i]
        currentLetter = word[i]
        mapping[currentTargetLetter] = currentLetter
    return mapping

def checkMapping(word, target, mapping):
    newOnes = {}
    otherOnes = {}
    for i in range(len(target)):
        currentTargetLetter = target[i]
        currentLetter = word[i]
        if currentTargetLetter in newOnes and currentLetter != newOnes[currentTargetLetter]:
            return False
        if currentLetter in otherOnes and currentTargetLetter != otherOnes[currentLetter]:
            return False
        else:
            newOnes[currentTargetLetter] = currentLetter
            otherOnes[currentLetter] = currentTargetLetter


    for i in range(len(target)):
        currentTargetLetter = target[i]
        currentLetter = word[i]
        if currentTargetLetter in mapping:
            if mapping[currentTargetLetter] != currentLetter:
                return False
        # check to see if value is already used
    return True

for i in range(n):
    word = sys.stdin.readline().strip().lower()
    dictionary.append(word)

for line in sys.stdin:
    words = line.strip().split()
    isSolution, mapping = checkWord(dictionary, sorted(words, key = lambda s: len(s), reverse=True), {})

    if isSolution:
        for c in line:
            if c in mapping:
                print(mapping[c], end='')
            else:
                print(c, end='')

    else:
        for c in line:
            if c.islower():
                print('*', end='')
            else:
                print(c, end='')
