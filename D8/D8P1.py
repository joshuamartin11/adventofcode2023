with open('D8/input.txt') as f:
    lines = f.readlines()

dirMap = {}
for line in lines[2::]:
    splitLine = line.split(" = ")
    dirMap[splitLine[0]] = splitLine[1].strip("()\n").split(", ")


curNode = "AAA"

dirIndex = 0
stepsCount = 0

while(curNode != "ZZZ"):
    
    stepsCount += 1

    if lines[0][dirIndex] == "R":
        curNode = dirMap[curNode][1]
    else:
        curNode = dirMap[curNode][0]

    dirIndex += 1
    if dirIndex == len(lines[0])-1:
        dirIndex = 0

print(stepsCount)