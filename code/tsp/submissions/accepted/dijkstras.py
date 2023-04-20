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

x=0

while time.time()-startTime<1.9:
 x+=1
 order=[]
 order.append(random.randint(0,n-1))
 
 unvisited=[*range(n)]
 unvisited.remove(order[-1])

 for i in range(n-1):
  
  bestNeighbour=unvisited[-1]
  closest=math.inf

  for neighbour in unvisited[:-1]:
   currDist=distance(cities[order[-1]],cities[neighbour])

   if currDist<closest:
    closest=currDist
    bestNeighbour=neighbour
  
  order.append(bestNeighbour)
  unvisited.remove(bestNeighbour)
 


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
