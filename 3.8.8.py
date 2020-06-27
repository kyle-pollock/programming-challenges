import sys
import re

limit = 72

chunks = []
chunk = ''
inChunk = False
for line in sys.stdin:
    if len(line.strip()) == 0:
        if inChunk:
            chunks.append(chunk)
            inChunk = False
        chunks.append('\n')
    else:
        if not inChunk:
            inChunk = True
            chunk = ''
        chunk = chunk + line
if len(chunk) > 0:
    chunks.append(chunk)

for chunk in chunks:
    if chunk == '\n':
        print()
        continue

    words = chunk.split()
    spaces = re.split('\S+', chunk)

    answer = []
    count = 0
    for i in range(len(spaces)):

        if '\n' in spaces[i]:
            spaces[i] = spaces[i].replace('\n', ' ')
        if (count + len(spaces[i])) > limit:
            answer.append('\n')
            # print()
            count = 0
        else:
            answer.append(spaces[i])
            # print(spaces[i], end='')
            count += len(spaces[i])
        # else:
            # if '\n ' not in spaces[i]:
            #     spaces[i] = spaces[i].replace('\n', ' ')
            # print(spaces[i], end='')
            # count += len(spaces[i])

        if i < len(words):
            if i == 0 and len(words[i]) > limit:
                answer.append(words[i])
                # print(words[i], end='')
                count = len(words[i])
                continue

            if (i == len(words)-1) and len(words[i]) > limit:
                answer.append('\n')
                answer.append(words[i])
                # print()
                # print(words[i], end='')
                count = len(words[i])
                break

            if (count + len(words[i])) > limit:
                answer.append('\n')
                # print()
                count = 0
            # print(words[i], end='')
            answer.append(words[i])
            count += len(words[i])
    # print()
    answer.append('\n')

    fulltext = ''
    for a in answer:
        fulltext += a
        # print(a, end='')
        # if len(a) > 0 and a.endswith(' \n'):
        #     print(a.rstrip())
        # else:
        #     print(a, end='')
    for line in fulltext.split('\n'):
        if len(line) > 0:
            print(line.rstrip())
