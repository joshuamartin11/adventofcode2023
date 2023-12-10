with open('D10/input.txt') as f:
    lines = f.readlines()
map = []
start = []
for row, line in enumerate(lines):
    gridLine = []
    for col, c in enumerate(line):
        gridLine.append(c)
        if c == "S":
            start = [c,row,col,0]
    map.append(gridLine)

steps = [start]


def checkDirs(up,down,left,right,pos):
    newDirs = []
    if up:
        try:
            if map[pos[1] - 1][pos[2]] == '7' or map[pos[1] - 1][pos[2]] == "|" or map[pos[1] - 1][pos[2]] == "F":
                newDirs.append([map[pos[1] - 1][pos[2]], pos[1] - 1, pos[2], pos[3] + 1])
        except IndexError:
            pass
    if down:
        try:
            if map[pos[1] + 1][pos[2]] == 'L' or map[pos[1] + 1][pos[2]] == "|" or map[pos[1] + 1][pos[2]] == "J":
                newDirs.append([map[pos[1] + 1][pos[2]], pos[1] + 1, pos[2], pos[3] + 1])
        except IndexError:
            pass
    if left:
        try:
            if map[pos[1]][pos[2] - 1] == 'L' or map[pos[1]][pos[2] - 1] == "F" or map[pos[1]][pos[2] - 1] == "-":
                newDirs.append([map[pos[1]][pos[2] - 1], pos[1], pos[2] - 1, pos[3] + 1])
        except IndexError:
            pass
    if right:
        try:
            if map[pos[1]][pos[2] + 1] == '7' or map[pos[1]][pos[2] + 1] == "J" or map[pos[1]][pos[2] + 1] == "-":
                newDirs.append([map[pos[1]][pos[2] + 1], pos[1], pos[2] + 1, pos[3] + 1])
        except IndexError:
            pass
    return newDirs

while(steps):
    curPos = steps.pop(0)
    if curPos[0] == "S":
        for dir in checkDirs(True,True,True,True,curPos):
            steps.append(dir)
    if curPos[0] == "|":
        for dir in checkDirs(True,True,False,False,curPos):
            steps.append(dir)
    if curPos[0] == "-":
        for dir in checkDirs(False,False,True,True,curPos):
            steps.append(dir)
    if curPos[0] == "L":
        for dir in checkDirs(True,False,False,True,curPos):
            steps.append(dir)
    if curPos[0] == "J":
        for dir in checkDirs(True,False,True,False,curPos):
            steps.append(dir)
    if curPos[0] == "7":
        for dir in checkDirs(False,True,True,False,curPos):
            steps.append(dir)
    if curPos[0] == "F":
        for dir in checkDirs(False,True,False,True,curPos):
            steps.append(dir)
    map[curPos[1]][curPos[2]] = curPos[3]

# print(stepCount)
maxSteps = 0
for line in map:
    for c in line:
        if isinstance(c, int) and c > maxSteps:
            maxSteps = c
print(maxSteps)
    
    
    
    
