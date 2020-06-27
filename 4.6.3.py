import sys

cases = int(sys.stdin.readline())
for case in range(cases):
    sys.stdin.readline()
    if case > 0:
        print()

    n = int(sys.stdin.readline())

    people = []
    for i in range(n):
        people.append(int(sys.stdin.readline()))
    people.sort()

    sum = 0
    answer = []
    while people:
        if len(people) == 1:
            answer.append(f"{people[0]}")
            sum += people.pop()
            break
        if len(people) == 2:
            answer.append(f"{people[0]} {people[1]}")
            sum += people.pop()
            people.pop()
            break

        if len(people) == 3:
            answer.append(f"{people[0]} {people[2]}")
            sum += people[2]
            answer.append(f"{people[0]}")
            sum += people[0]
            answer.append(f"{people[0]} {people[1]}")
            sum += people[1]
            people.pop()
            people.pop()
            people.pop()
            break

        fastest = people[0]
        fast = people[1]
        slow = people[-2]
        slowest = people[-1]

        fastFirstTime = fast + fastest + slowest + fast
        shuttleTime = slowest + fastest + slow + fastest

        if fastFirstTime <= shuttleTime:
        # if fast <= (.5 * slow):
            # fast first
            answer.append(f"{fastest} {fast}")
            sum += fast
            answer.append(f"{fastest}")
            sum += fastest
            answer.append(f"{slow} {slowest}")
            sum += slowest
            answer.append(f"{fast}")
            sum += fast
            people.pop()
            people.pop()
        else :
            # shuttle
            answer.append(f"{fastest} {slowest}")
            sum += slowest
            answer.append(f"{fastest}")
            sum += fastest
            answer.append(f"{fastest} {slow}")
            sum += slow
            answer.append(f"{fastest}")
            sum += fastest
            people.pop()
            people.pop()

    print(sum)
    print(*answer, sep='\n')
