#!/usr/bin/env python3

n = int(input())
if n == 1:
    print(0)
elif n == 2:
    l = list(map(int, input().split()))
    s = l[:]
    if s[1] < s[0]:
        s[0], s[1] = s[1], s[0]
    ans = 0
    for i in range(2):
        if l[i] != s[i]:
            ans += 1
    print(ans)
else:
    print(0)