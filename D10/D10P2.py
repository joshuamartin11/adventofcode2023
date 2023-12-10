
with open('D10/inputtest.txt') as f:
    lines = f.readlines()
map = []
start = []
for row, line in enumerate(lines):
    gridLine = []
    for col, c in enumerate(line.strip()):
        gridLine.append(c)
        if c == "S":
            start = [c,row,col,0]
        gridLine.append(".")
    map.append(gridLine)
    map.append(['.']*len(line.strip()) * 2)




def checkDirs(up,down,left,right,row,col):
    global map
    connected = False
    if up:
        try:
            if map[row - 2][col] == '7' or map[row - 2][col] == "|" or map[row - 2][col] == "F":
                map[row-1][col] = "|"
                connected = True
        except IndexError:
            pass
    if down:
        try:
            if map[row + 2][col] == 'L' or map[row + 2][col] == "|" or map[row + 2][col] == "J":
                map[row+1][col] = "|"
                connected = True
        except IndexError:
            pass
    if left:
        try:
            if map[row][col-2] == 'L' or map[row][col-2] == "-" or map[row][col-2] == "F":
                map[row][col-1] = "-"
                connected = True
        except IndexError:
            pass
    if right:
        try:
            if map[row][col+2] == '7' or map[row][col+2] == "-" or map[row][col+2] == "J":
                map[row][col+1] = "-"
                connected = True
        except IndexError:
            pass
    return connected


for row, line in enumerate(map):
    for col, c in enumerate(line):
        connected = False
        if c == "S":
            connected = checkDirs(True,True,True,True,row,col)
        if c == "|":
            connected = checkDirs(True,True,False,False,row,col)
        if c == "-":
            connected = checkDirs(False,False,True,True,row,col)
        if c == "L":
            connected = checkDirs(True,False,False,True,row,col)
        if c == "J":
            connected = checkDirs(True,False,True,False,row,col)
        if c == "7":
            connected = checkDirs(False,True,True,False,row,col)
        if c == "F":
            connected = checkDirs(False,True,False,True,row,col)
        if connected == False:
            map[row][col] = '.'

for col in range(len(line)):
    if map[0][col] == ".":
        queue = [[0,col]]
        while queue:
            curNode = queue.pop()
            for x, y in [(0,1), (1,0), (0,-1),  (-1,0)]:
                try:
                    if map[curNode[0] + y][curNode[1] + x] == ".":
                        queue.append([curNode[0] + y, curNode[1] + x])
                except IndexError: #outside board.
                    pass
            map[curNode[0]][curNode[1]] = "O"
    if map[len(map) - 1][col] == ".":
        queue = [[len(map) - 1,col]]
        while queue:
            curNode = queue.pop()
            for x, y in [(0,1), (1,0), (0,-1),  (-1,0)]:
                try:
                    if map[curNode[0] + y][curNode[1] + x] == ".":
                        queue.append([curNode[0] + y, curNode[1] + x])
                except IndexError: #outside board.
                    pass
            map[curNode[0]][curNode[1]] = "O"

for row in range(len(map)):
    if map[row][0] == ".":
        queue = [[row,0]]
        while queue:
            curNode = queue.pop()
            for x, y in [(0,1), (1,0), (0,-1),  (-1,0)]:
                try:
                    if map[curNode[0] + y][curNode[1] + x] == ".":
                        queue.append([curNode[0] + y, curNode[1] + x])
                except IndexError: #outside board.
                    pass
            map[curNode[0]][curNode[1]] = "O"
    if map[row][len(map[0]) - 1] == ".":
        queue = [[row, len(map[0]) - 1]]
        while queue:
            curNode = queue.pop()
            for x, y in [(0,1), (1,0), (0,-1),  (-1,0)]:
                try:
                    if map[curNode[0] + y][curNode[1] + x] == ".":
                        queue.append([curNode[0] + y, curNode[1] + x])
                except IndexError: #outside board.
                    pass
            map[curNode[0]][curNode[1]] = "O"

# print(map)


count = 0
for row in range(0,len(map),2):
    for col in range(0,len(map[0]),2):
        # print(map[row][col])
        # print(c)
        if map[row][col] == ".":
            map[row][col] = "I"
            count += 1
            # print('yes')


for line in map:
    print(''.join(line))

# for row in range(0,len(map),2):
#     for col in range(0,len(map[0]),2):
#         print(map[row][col], end="")
#     print()
    
print(count)
