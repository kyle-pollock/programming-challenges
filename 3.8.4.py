import sys

plaintext = "the quick brown fox jumps over the lazy dog"

def checkSpaces(line):
    for i in range(len(plaintext)):
        if plaintext[i] == ' ' and line[i] != ' ':
            return False
    return True

def checkLetter(line, letter, freq):
    mapping = ''
    for i in range(len(plaintext)):
        if plaintext[i] == letter:
            if mapping == '':
                mapping = line[i]
            elif mapping != line[i]:
                return False
    return freq == line.count(mapping)

def createMapping(line):
    mapping = {}
    for i in range(len(line)):
        if line[i] == ' ':
            continue
        mapping[line[i]] = plaintext[i]
    return mapping

def decrypt(mapping, lines):
    for line in lines:
        for c in line:
            if c.isalpha():
                print(mapping[c], end='')
            else:
                print(c, end='')
        print()


cases = int(sys.stdin.readline())
sys.stdin.readline()
for case in range(cases):
    if case > 0:
        print()

    lines = []
    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            break
        lines.append(line)

    found = False
    for line in lines:
        if len(line) != len(plaintext):
            continue
        if not checkSpaces(line):
            continue
        if not checkLetter(line, 'o', 4):
            continue
        if not checkLetter(line, 'e', 3):
            continue
        if not checkLetter(line, 'h', 2):
            continue
        if not checkLetter(line, 'r', 2):
            continue
        if not checkLetter(line, 't', 2):
            continue
        if not checkLetter(line, 'u', 2):
            continue

        mapping = createMapping(line)
        if len(mapping) != 26:
            continue
        found = True
        decrypt(mapping, lines)
        break

    if not found:
        print("No solution.")
