#!/usr/bin/env python3
import matplotlib.pyplot as plt

labels=["g1/001-random_small.in","g2/002-random_medium.in","g3/003-random_big.in","g4/004-sweden.in","g5/005-united_states.in",
        "g6/006-strictlyIncrease.in","g7/007-circle.in","g8/008-grid.in","g9/009-straight.in","g1/001-random_small.in"]

for t in labels:

    file=open(f"/home/harry/diploma-project/code/TSP/data/secret/{t}")

    inp = [*file]
    file.close()

    x=[]
    y=[]

    for str in inp[1:]:
        currx,curry=map(int,str.split())
        x.append(currx)
        y.append(curry)

    plt.scatter(x, y,s=1)

    plt.xlabel('x - axis')

    plt.ylabel('y - axis')
    

    plt.title(t)
    

    plt.savefig("code/visualizer/"+t[4:-3]+".png")

    plt.clf()