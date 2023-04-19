import math
import time
import random

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

startTime = time.time()


order=[*range(n)]
bestDist=math.inf
bestOrder=[]

while time.time()-startTime<1.9:
 temp = totalDist(order)

 if bestDist>temp:
    bestDist=temp
    bestOrder=order[::]

 random.shuffle(order)

for a in bestOrder:
 print(a)
