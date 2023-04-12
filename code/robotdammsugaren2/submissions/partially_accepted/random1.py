#!/usr/bin/env python3
import random
random.seed(123)
t = input()
(R, C, N) = map(int, input().split())
chars = "^<>v"
answer = []
for _ in range(0, N):
    answer.append(chars[random.randrange(0, 4)])
print("".join(answer))