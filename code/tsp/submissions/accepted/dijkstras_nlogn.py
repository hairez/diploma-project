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

startTime=time.time()

bestOrder=[]
shortestPath=math.inf


logValue=math.ceil(math.log2(n))
x=0

while time.time()-startTime<1.9:
 x+=1
 order=[]
 
 
 unvisited=[*range(n)]
 random.shuffle(unvisited)

 order.append(unvisited.pop())

 for i in range(n-1):
  
  bestNeighbour=unvisited[-1]
  closest=math.inf


  focus=[]

  temp=min(len(unvisited),logValue)
  for j in range(temp):
   focus.append(unvisited.pop())
  
  for neighbour in focus:
   currDist=distance(cities[order[-1]],cities[neighbour])

   if currDist<closest:
    closest=currDist
    bestNeighbour=neighbour
  
  order.append(bestNeighbour)
 
  temp=len(focus)
  for j in range(temp):
   x=focus.pop()
   if x==bestNeighbour:
    continue
   else:
    unvisited.append(x)
 
 temp=totalDist(order)

 if shortestPath>temp:
    shortestPath=temp
    bestOrder=order[::]


for node in bestOrder:
 print(node)

"""
print(time.time()-startTime)
print(x)
"""
