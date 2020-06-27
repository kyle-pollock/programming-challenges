import sys
import math

startOfDay = '10:00'
endOfDay = '18:00'

class TimeRange:
    def __init__(self, start, end):
        self.startHour = int(start[:2])
        self.startMin = int(start[3:])
        self.endHour = int(end[:2])
        self.endMin = int(end[3:])

    def rank(self):
        return self.startHour * 60 + self.startMin

    def length(self):
        return (self.endHour * 60 + self.endMin) - (self.startHour * 60 + self.startMin)

    def lapse(self):
        total = self.length()
        if total / 60 >= 1:
            return f'{math.floor(total / 60)} hours and {total % 60}'
        return f'{total}'

    def getStart(self):
        return f'{self.startHour}:{self.startMin:02}'

    def getEnd(self):
        return f'{self.endHour}:{self.endMin:02}'

    def __lt__(self, other):
        return self.rank() < other.rank()

    def __str__(self):
        return f'starts at {self.startHour}:{self.startMin:02} and will last for {self.lapse()} minutes.'

day = 1
for line in sys.stdin:
    appointments = []
    for i in range (int(line)):
        appointments.append(TimeRange(*sys.stdin.readline().split()[:2]))
    appointments.sort()

    max = -1
    curr = startOfDay
    for appointment in appointments:
        slot = TimeRange(curr, appointment.getStart())
        if slot.length() > max:
            max = slot.length()
            answer = slot
        curr = appointment.getEnd()

    slot = TimeRange(curr, endOfDay)
    if slot.length() > max:
        max = slot.length()
        answer = slot

    print(f'Day #{day}: the longest nap {answer}')
    day += 1
