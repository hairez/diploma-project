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

def segmentDist(path):
 dist=0

 for i in range(1,len(path)):
  dist+=distance(cities[path[i]],cities[path[i-1]])
 
 return dist

def getSegment(i,order):
 segment=[]

 if i==0:
  segment.append(order[-1])
 else:
  segment.append(order[i-1])
 

 segment.append(order[i])


 if i==len(order)-1:
  segment.append(order[0])
 else:
  segment.append(order[i+1])
 
 return segment

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
 startTime=time.time()

 bestOrder=[]
 shortestPath=math.inf


 for a in range(1):

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

 
 while time.time()-startTime<1.9:
  x,y=random.randint(0,n-1),random.randint(0,n-1)

  if x==y:continue

  seg1=getSegment(x,order)
  seg2=getSegment(y,order)

  distBefore=segmentDist(seg1) + segmentDist(seg2)

  seg1[1],seg2[1]=seg2[1],seg1[1]

  if seg1[1]==seg1[2]:
   seg1[2],seg2[0]=seg2[0],seg1[2]
  elif seg1[1]==seg1[0]:
   seg1[0],seg2[2]=seg2[2],seg1[0]

  distAfter=segmentDist(seg1) + segmentDist(seg2)

  if distAfter<distBefore:
   order[x],order[y]=order[y],order[x]

 for node in order:
  print(node)