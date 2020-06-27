import sys

for case in range(int(sys.stdin.readline())):
    original_turtles = []
    sorted_turtles = []
    n = int(sys.stdin.readline())
    for i in range(n):
        original_turtles.append(sys.stdin.readline()[:-1])
    for i in range(n):
        sorted_turtles.append(sys.stdin.readline()[:-1])

    original_turtles = [x for x in reversed(original_turtles)]
    sorted_turtles = [x for x in reversed(sorted_turtles)]

    not_in_place = []
    j = 0
    for i in range(n):
        if j >= n:
            break
        if original_turtles[i] != sorted_turtles[j]:
            not_in_place.append(original_turtles[i])
        else:
            j += 1
    for turtle in sorted_turtles:
        if turtle in not_in_place:
            print(turtle)
    print()
