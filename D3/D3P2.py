with open('D3\input.txt') as f:
    lines = f.readlines()

schematic = list()

for line in lines:
    schematic.append(list(line.strip()))

total = 0

for row in range(len(schematic)):
    for col in range(len(line)):
        numbers = list()
        if schematic[row][col] == "*":
            for x, y in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
                try:
                    if schematic[row + y][col + x].isdigit():
                        number = [schematic[row + y][col + x]]
                        if schematic[row + y][col + x + 1].isdigit():
                            number.append(schematic[row + y][col + x + 1])
                            if schematic[row + y][col + x + 2].isdigit():
                                number.append(schematic[row + y][col + x + 2])
                        if schematic[row + y][col + x - 1].isdigit():
                            number.insert(0,schematic[row + y][col + x - 1])
                            if schematic[row + y][col + x - 2].isdigit():
                                number.insert(0,schematic[row + y][col + x - 2])
                        if int(''.join(number)) not in numbers:
                            numbers.append(int(''.join(number)))   
                except IndexError: #outside board.
                    pass
            if len(numbers) == 2:
                print(numbers)
                total += numbers[0] * numbers[1]
                numbers = []


print(total)