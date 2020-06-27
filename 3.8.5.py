import sys

def isAccepted(submittedLines, correctLines):
    if len(submittedLines) != len(correctLines):
        return False
    for i in range(len(submittedLines)):
        if submittedLines[i] != correctLines[i]:
            return False
    return True


def isPresentationError(submittedLines, correctLines):
    submittedNumerals = []
    correctNumerals = []

    for line in submittedLines:
        for c in line:
            if c.isnumeric():
                submittedNumerals.append(c)

    for line in correctLines:
        for c in line:
            if c.isnumeric():
                correctNumerals.append(c)

    return submittedNumerals == correctNumerals


run_num = 0
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    else:
        isProcessing = True
        run_num += 1

    correctLines = []
    for i in range(n):
        correctLines.append(sys.stdin.readline())

    m = int(sys.stdin.readline())
    submittedLines = []
    for i in range(m):
        submittedLines.append(sys.stdin.readline())

    result = "Wrong Answer"
    if isAccepted(submittedLines, correctLines):
        result = "Accepted"
    elif isPresentationError(submittedLines, correctLines):
        result = "Presentation Error"

    print(f"Run #{run_num}: {result}")
