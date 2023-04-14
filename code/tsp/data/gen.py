#!/usr/bin/env python3

import sys
import random
import math


def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default


random.seed(int(cmdlinearg('seed', sys.argv[-1])))

n = int(cmdlinearg('n', 10**5))

increase = int(cmdlinearg('increase', 0))

circle = int(cmdlinearg('circle', 0))

grid = int(cmdlinearg('grid', 0))

straight = int(cmdlinearg('straight', 0))

print(n)

coordinates=[]

if increase:

    tempX=set()
    tempY=set()

    while len(tempX)<n:
        tempX.add(random.randint(-10**6,10**6))
    while len(tempY)<n:
        tempY.add(random.randint(-10**6,10**6))
    
    allX=[*tempX]
    allY=[*tempY]
    
    allX.sort()
    allY.sort()

    for a in range(n):
        coordinates.append((allX[a],allY[a]))
    


elif circle:

    tempCoordinates=set()
    while len(tempCoordinates)<n:
        theta=random.uniform(0,2*math.pi)

        tempCoordinates.add((int(10**6*math.cos(theta)),int(10**6*math.sin(theta))))
    
    for a in tempCoordinates:
        coordinates.append(a)
    


elif grid:

    
    for x in range(int(math.sqrt(n))):
        for y in range(int(math.sqrt(n))):
            coordinates.append((x,y))
    
    

    
elif straight:
    tempCoordinates=set()
    while len(tempCoordinates)<n:
        tempCoordinates.add((random.randint(-10**6,10**6),0))
    
    for a in tempCoordinates:
        coordinates.append(a)

else:
    tempCoordinates=set()
    while len(tempCoordinates)<n:
        tempCoordinates.add((random.randint(-10**6,10**6),random.randint(-10**6,10**6)))
    
    for a in tempCoordinates:
        coordinates.append(a)





random.shuffle(coordinates)

allCoordinates=set()
for a in coordinates:
    allCoordinates.add(a)
if len(allCoordinates)!=n:
    print("error, not enough unique coordinates")
    exit()


for x,y in coordinates:
    print(x,y)