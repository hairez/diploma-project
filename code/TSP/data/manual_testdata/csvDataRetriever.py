#!/usr/bin/env python3


file=open("/home/harry/diploma-project/code/TSP/data/manual_testdata/svenska-stader.csv")

inp=[*file]
file.close()

out=open("/home/harry/diploma-project/code/TSP/data/manual_testdata/sweden.in","w")

coordinates=[]

for string in inp[1:]:
    d=string.split(",")
    x=int(float(d[-2])*10000)
    y=int(float(d[-1])*10000)
    coordinates.append((y,x))
    if x>1000000:print(x)
    if y>1000000:print(y)

out.write(str(len(coordinates))+"\n")
for x,y in coordinates:
    out.write(f"{x} {y}\n")

out.close()






file=open("/home/harry/diploma-project/code/TSP/data/manual_testdata/uscities.csv")

inp=[*file]
file.close()

out=open("/home/harry/diploma-project/code/TSP/data/manual_testdata/united_states.in","w")

coordinates=[]

for string in inp[1:10001]:
    d=string.split("\",\"")
    x=int(float(d[6])*1000)
    y=int(float(d[7])*1000)
    coordinates.append((y,x))
    if x>1000000:print(x)
    if y>1000000:print(y)

out.write(str(len(coordinates))+"\n")
for x,y in coordinates:
    out.write(f"{x} {y}\n")

out.close()
