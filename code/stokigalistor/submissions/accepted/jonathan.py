#!/usr/bin/env python3

n = int(input())
inp = list(map(int, input().split()))
print(sum(a != b for a, b in zip(inp, sorted(inp))))