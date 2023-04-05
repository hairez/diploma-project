#!/usr/bin/env python3

n=int(input())

list1=list(map(int,input().split()))

list2=list1
#Notera att python skapar en referens till list1 från list2 om man gör på det här viset.
#Om list2 sorteras här kommer även list1 att sorteras.

list2.sort()

output=0

for i in range(n):
    if list1[i]!=list2[i]:
        output+=1

print(output)