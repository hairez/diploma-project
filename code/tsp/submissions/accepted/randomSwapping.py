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
bestOrder=[1]
shortestPath=math.inf



while time.time()-startTime<1.9:
    order=[*range(n)]
    random.shuffle(order)

    t=currT=0
    while time.time()-startTime<1.9:
        
        t+=1
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

            currT=t
            order[x],order[y]=order[y],order[x]

        elif t-currT>4000:
            break
    
    
    temp=totalDist(order)

    if shortestPath>temp:
        shortestPath=temp
        bestOrder=order[::]




for node in bestOrder:
 print(node)

"""
print(time.time()-startTime)
print(t)
"""