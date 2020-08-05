import sys


def isCorrect(answers, sums, used):
    # for each remainding answer
    for i in range(3, len(answers)):

        # for each unused sum
        isDone = False
        for j, isUsed in enumerate(used):
            if isDone:
                break
            if isUsed:
                continue

            # temporarily use the sum
            used[j] = True
            # temporarily set new answer = sums[j] - answer[0]
            newAnswer = sums[j] - answers[0]
            answers[i] = newAnswer

            # for each answer 1 - i
            inner_used = list(used)
            for k in range(1, i):
                # confirm that x3 + answer[k] is in sums
                temp = newAnswer + answers[k]
                if temp not in sums:
                    used[j] = False
                    answers[i] = '@'
                    break

                #make sure it is not used
                indices = [i for i, x in enumerate(sums) if x == temp]
                all_good = False
                for q in indices:
                    if inner_used[q] == False:
                        all_good = True
                        inner_used[q] = True
                        break

                if not all_good:
                    used[j] = False
                    answers[i] = '@'
                    break
            isDone = used[j]


for line in sys.stdin:
    line = [int(x) for x in line.split()]
    n = line[0]
    sums = sorted(line[1:])
    answers = ['@' for x in range(n)]
    init_used = [False for x in sums]
    init_used[0] = True
    init_used[1] = True

    isFound = False
    for i in range(2, len(sums)):
        # make a brand new used list
        used = list(init_used)

        # check to see if it combo will work
        total = (sums[0] + sums[1] + sums[i])
        if total % 2 == 1:
            continue
        total = int(total / 2)

        answers[0] = total - (sums[i])
        answers[1] = total - (sums[1])
        answers[2] = total - (sums[0])
        used[i] = True

        isCorrect(answers, sums, used)
        if '@' not in answers:
            isFound = True
            print(*answers, sep=' ')
            break

    if not isFound:
        print("Impossible")
