import sys
for line in sys.stdin:
    stack = [ int(x) for x in line.split() ]
    srtd = sorted(stack)
    answer = []
    print(*stack, sep=' ')
    for i in reversed(range(len(stack))):
        while stack[i] != srtd[i]:
            index_max = stack[:i+1].index(max(stack[:i+1]))
            if index_max != 0:
                stack = list(reversed(stack[:index_max+1])) + stack[index_max+1:]
                answer.append(len(stack) - index_max)
            stack = list(reversed(stack[:i+1])) + stack[i+1:]
            answer.append(len(stack) - i)
    answer.append(0)
    print(*answer, sep=' ')
