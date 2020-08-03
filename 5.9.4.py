import sys

for a_str in sys.stdin:
    a_str = a_str.strip()
    a = int(a_str)
    buf = '1' * len(a_str)
    while True:
        if int(buf) % a == 0:
            print(len(str(buf)))
            break
        buf += '1'
