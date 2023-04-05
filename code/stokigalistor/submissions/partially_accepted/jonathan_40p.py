#!/usr/bin/env python3

n = int(input())
inp = list(map(int, input().split()))

s = inp[:]
for i in range(n):  # bubble sort
    for j in range(i + 1, n):
        if s[i] > s[j]:
            s[i], s[j] = s[j], s[i]

ans = 0
for i in range(n):
    if s[i] != inp[i]:
        ans += 1
print(ans)