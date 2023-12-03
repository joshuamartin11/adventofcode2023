with open('D3\input.txt') as f:
    lines = f.readlines()

schematic = list()

for line in lines:
    schematic.append(list(line.strip()))

total = 0

for row in range(len(schematic)):
    adjacency = False
    number = []
    for col in range(len(line)):

        if schematic[row][col].isdigit():
            number.append(schematic[row][col])
            for x, y in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
                try:
                    if schematic[row + y][col + x] != '.' and not schematic[row + y][col + x].isdigit():
                        adjacency = True
                except IndexError: #outside board.
                    pass
            if col + 1 == len(line) or not schematic[row][col + 1].isdigit():
                if adjacency:
                    total += int(''.join(number))
                    print(''.join(number))
                adjacency = False
                number = []


print(total)



