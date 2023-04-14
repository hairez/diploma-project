#!/usr/bin/env python3
import matplotlib.pyplot as plt

labels=["g1/001-random_small.in","g2/002-random_medium.in","g3/003-random_big.in","g4/004-sweden.in","g5/005-united_states.in",
        "g6/006-strictlyIncrease.in","g7/007-circle.in","g8/008-grid.in","g9/009-straight.in","g10/010-strictlyIncrease_small.in"]

for t in labels:

    file=open(f"/home/harry/diploma-project/code/tsp/data/secret/{t}")

    inp = [*file]
    file.close()

    x=[]
    y=[]

    for str in inp[1:]:
        currx,curry=map(int,str.split())
        x.append(currx)
        y.append(curry)

    if t == "g4/004-sweden.in":
        plt.figure(figsize=(4.8,9.6))
    elif t == "g4/004-sweden.in":
        plt.figure(figsize=(6.4*2,4.8*2))
    else:
        plt.figure(figsize=(6.4*2,4.8*2))

    plt.scatter(x, y,s=1)

    plt.xlabel('x - axis')

    plt.ylabel('y - axis')
    

    plt.title(t)
    
    if t=="g10/010-strictlyIncrease_small.in":
        t="g1/010-strictlyIncrease_small.in"
    
    plt.savefig("/home/harry/diploma-project/code/visualizer/testdata/"+t[4:6]+".png")

    plt.clf()