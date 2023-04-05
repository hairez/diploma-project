#!/usr/bin/env python3

n = int(input())

list1 = list(map(int,input().split()))

list2 = sorted(list1)

output = 0

for i in range(n):
  if list1[i] != list2[i]:
    output += 1
    
print(output)
