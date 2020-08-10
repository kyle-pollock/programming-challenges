import sys
import bisect

fibs=[1, 2];
for i in range(500):
    fibs.append(fibs[-2] + fibs[-1]);

for line in sys.stdin:
    a, b = [int(x) for x in line.split()]
    if a == 0 and b == 0:
        break

    lower = bisect.bisect_left(fibs, a)
    if lower == len(fibs):
        print(0)
        continue
    higher = bisect.bisect(fibs, b) - 1
    if higher < 0:
        print(0)
        continue

    print(higher - lower + 1)
