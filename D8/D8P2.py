import math



with open('D8/input.txt') as f:
    lines = f.readlines()

dirMap = {}
nodes = []
for line in lines[2::]:
    splitLine = line.split(" = ")
    dirMap[splitLine[0]] = splitLine[1].strip("()\n").split(", ")
    if splitLine[0][2] == "A":
        nodes.append(splitLine[0])




stepsCounts = []
for curNode in nodes:
    dirIndex = 0
    stepsCount = 0
    while(curNode[2] != "Z"):
        
        stepsCount += 1

        if lines[0][dirIndex] == "R":
            curNode = dirMap[curNode][1]
        else:
            curNode = dirMap[curNode][0]

        dirIndex += 1
        if dirIndex == len(lines[0])-1:
            dirIndex = 0

    stepsCounts.append(stepsCount)

print(math.lcm(*stepsCounts))
