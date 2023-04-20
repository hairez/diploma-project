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

def segmentDist(path):
 dist=0

 for i in range(1,len(path)):
  dist+=distance(cities[path[i]],cities[path[i-1]])
 
 return dist


def getLeft(i,order):

 if i==0:
  return order[-1]
 return order[i-1]

def getRight(i,order):

 if i==len(order)-1:
  return order[0]
 return order[i+1]
 

startTime=time.time()

bestOrder=[1]
shortestPath=math.inf


t=currT=0

while time.time()-startTime<1.9:

    order=[*range(n)]

    random.shuffle(order)

    while time.time()-startTime<1.9:
        t+=1
        x=random.randint(0,n-2)
        y=random.randint(x+1,n-1)

        if x==y:continue

        xLeft=getLeft(x,order)
        yRight=getRight(y,order)

        if xLeft==order[y]:continue
        if xLeft==yRight:continue

        distBefore=segmentDist([order[x],xLeft]) + segmentDist([order[y],yRight])

        distAfter=segmentDist([order[x],yRight]) + segmentDist([order[y],xLeft])

        if distAfter<distBefore:
            currT=t
            order=order[:x]+order[x:y+1][::-1]+order[y+1:]
            #print(totalDist(order))
        elif t-currT>5000:
            break

    temp=totalDist(order)

    if shortestPath>temp:
        shortestPath=temp
        bestOrder=order[::]


for node in order:
 print(node)

"""
print(time.time()-startTime)
print(t)
"""