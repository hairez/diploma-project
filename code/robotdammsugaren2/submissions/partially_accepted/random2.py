#!/usr/bin/env python3
import random
random.seed(123)
t = input()
(R, C, N) = map(int, input().split())
chars = "^<>v"
answer = []
prev = 'x'
for _ in range(0, N):
    c = chars[random.randrange(0, 4)]
    while c == prev:
        c = chars[random.randrange(0, 4)]
    answer.append(c)
    prev = c
print("".join(answer))