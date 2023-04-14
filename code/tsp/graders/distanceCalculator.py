import math


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
 x,y=map(int,input().split())
 cities.append((x,y))

order=[]

for a in range(n):
 order.append(int(input()))

print(totalDist(order))