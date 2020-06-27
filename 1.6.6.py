import sys
import math

cases = int(sys.stdin.readline())

null = sys.stdin.readline()

for case in range(cases):
    if case > 0:
        print()

    registers = [0 for x in range(10)]
    ram = [0 for x in range(1000)]

    i = 0
    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            break
        ram[i] = int(line)
        i += 1

    i = 0
    halt = False
    executions = 0
    while not halt:
        executions += 1

        instruction = math.floor(ram[i] / 100)

        d = math.floor(ram[i] % 100 / 10)
        n = ram[i] % 10

        if instruction == 1:
            halt = True

        elif instruction == 2:
            registers[d] = n

        elif instruction == 3:
            registers[d] = (registers[d] + n) % 1000

        elif instruction == 4:
            registers[d] = (registers[d] * n) % 1000

        elif instruction == 5:
            registers[d] = registers[n]

        elif instruction == 6:
            registers[d] = (registers[d] + registers[n]) % 1000

        elif instruction == 7:
            registers[d] = (registers[d] * registers[n]) % 1000

        elif instruction == 8:
            registers[d] = ram[registers[n]]

        elif instruction == 9:
            ram[registers[n]] = registers[d]

        elif instruction == 0 and registers[n] != 0:
            i = registers[d]
            continue

        i += 1

    print(executions)
