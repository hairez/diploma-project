#!/usr/bin/env python3

n = int(input())

list1 = list(map(int,input().split()))

list2 = sorted(list1)

print(sum(list1[i] != list2[i] for i in range(n)))
