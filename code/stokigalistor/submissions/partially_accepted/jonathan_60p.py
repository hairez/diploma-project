#!/usr/bin/env python3

def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i + 1] < l[i]:
            return False
    return True

n = int(input())
inp = list(map(int, input().split()))

r = list(reversed(inp))
s = inp[:]
if is_sorted(r):
    s = r
else:
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]

ans = 0
for i in range(n):
    if s[i] != inp[i]:
        ans += 1
print(ans)