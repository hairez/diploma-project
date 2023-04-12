#!/usr/bin/env python3

import sys
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))

print(cmdlinearg('tc'))

R = int(cmdlinearg('R'))
C = int(cmdlinearg('C'))
N = int(cmdlinearg('N'))
B = int(cmdlinearg('B'))

mode = cmdlinearg('mode', 'random')

total = []
upper = []
blocked = set()
for i in range(0, R):
    for j in range(0, C):
        if i == 0 or i == R-1 or j == 0 or j == C-1:
            blocked.add((i,j))
        else:
            total.append((i,j))
            if i < R//2:
                upper.append((i,j))

if mode == 'random':
    extra_blocked = random.sample(total, B)
elif mode == 'half':
    extra_blocked = random.sample(upper, B)

blocked |= set(extra_blocked)
starts = []
for i in range(0, R):
    for j in range(0, C):
        if mode == 'half' and i > 1:
            break
        if (i,j) not in blocked:
            starts.append((i,j))
start = starts[random.randrange(0, len(starts))]

print(R,C,N)
for i in range(0, R):
    line = []
    for j in range(0, C):
        if (i,j) == start:
            line.append('O')
        elif (i,j) in blocked:
            line.append('#')
        else:
            line.append('.')
    print("".join(line))




