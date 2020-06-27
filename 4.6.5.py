import sys

class Job():
    def __init__(self, pos, days, cost):
        self.pos = pos
        self.days = int(days)
        self.cost = int(cost)

    def get_cost(self):
        return self.cost
    def get_pos(self):
        return self.pos

    def __lt__(self, other):
        return self.days * other.cost < other.days * self.cost

    def __repr__(self):
        return f'{self.days} {self.cost}'

cases = int(sys.stdin.readline())
for case in range(cases):
    sys.stdin.readline()
    if case > 0:
        print()

    num_jobs = int(sys.stdin.readline())
    jobs = []
    for i in range(num_jobs):
        jobs.append(Job(i+1, *sys.stdin.readline().split()))
    print(*[ x.get_pos() for x in sorted(jobs) ], sep=' ')
