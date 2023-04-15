#!/usr/bin/env python3
import matplotlib.pyplot as plt

labels=["g1/001-random_small.in","g2/002-random_medium.in","g3/003-random_big.in","g4/004-sweden.in","g5/005-united_states.in",
        "g6/006-strictlyIncrease.in","g7/007-circle.in","g8/008-grid.in","g9/009-straight.in","g10/010-strictlyIncrease_small.in"]

for t in labels:

    inputFile=open(f"/home/harry/diploma-project/code/tsp/data/secret/{t}")

    inp=[*inputFile]
        
    inputFile.close()

    n=int(inp[0])
    
    cityX=[]
    cityY=[]
    
    for string in inp[1]:
        x,y=map(int,string.split())
        cityX.append(x)
        cityY.append(y)
    
    #ta in input från /output/001.......
    #specifiera vilken ordning det ska vara i.
    #plotta
    
