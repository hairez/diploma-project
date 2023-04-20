import math
import time
import random
from itertools import permutations

def totalDist(path):
 dist=0

 dist+=distance(cities[path[0]],cities[path[-1]])

 for i in range(1,len(path)):
  dist+=distance(cities[path[i]],cities[path[i-1]])

 return dist


def distance(p1,p2=(0,0)):
 x1,y1=p1
 x2,y2=p2

 return math.sqrt((y2-y1)**2+(x2-x1)**2)


n=int(input())

cities=[]

for a in range(n):
 x,y=map(eval,input().split())
 cities.append((x,y))

#^^^^^ same for every solution

startTime=time.time()

if n<=10: #only works for n<11. 
 allPossiblePerms=[]
 order=[*range(n-1)]
 allPossiblePerms=permutations(order)

 shortestPath=math.inf
 bestOrder=order

 for currOrder in list(allPossiblePerms):
    currOrder=list(currOrder)
    temp=totalDist(currOrder+[n-1])

    if shortestPath>temp:
        shortestPath=temp
        bestOrder=currOrder[::]+[n-1]
 
 for node in bestOrder:
   print(node)
 #print(time.time()-startTime)

else:
 #do some other heuristic
 exit()