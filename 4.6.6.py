import sys

cases = int(sys.stdin.readline())
sys.stdin.readline()
for case in range(cases):
    if case > 0:
        print()
    fares = [int(x) for x in sys.stdin.readline().split()]

    snapshots = []
    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            break
        snapshots.append(line)

    snapshots.sort(key=lambda x: x.split()[1])
    snapshots.sort(key=lambda x: x.split()[0])

    curr_plate = None
    isEnter = False
    isValid = False
    sum = 0
    for snapshot in snapshots:
        plate, stamp, state, km = snapshot.split()
        km = int(km)

        if plate != curr_plate:
            sum += 200
            if isValid and curr_plate:
                print(f'{curr_plate} ${sum / 100:.2f}')
            curr_plate = plate
            sum = 0
            isEnter = False
            isValid = False

        # if state == 'enter' and not isEnter:
        if state == 'enter':
            startStamp = stamp
            startKm = km
            isEnter = True

        if state == 'exit' and isEnter:
            isValid = True
            sum += 100
            endStamp = stamp
            endKm = km
            isEnter = False

            km = abs(startKm - endKm)
            rate = fares[int(startStamp[6:8])]
            sum += km * rate

    if isValid and curr_plate:
        sum += 200
        print(f'{curr_plate} ${sum / 100:.2f}')
