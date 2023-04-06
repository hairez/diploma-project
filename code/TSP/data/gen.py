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
max_ai = int(cmdlinearg('max_ai', 10**9))
n = int(cmdlinearg('n', 10**6))
rev = int(cmdlinearg('reversed', 0))

print(n)

a = [random.randint(0, max_ai) for i in range(n)]
if rev:
    a = reversed(sorted(a))
print(' '.join(map(str, a)))