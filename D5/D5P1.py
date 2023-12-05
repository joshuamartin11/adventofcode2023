with open('D5\input.txt') as f:
    lines = f.readlines()

almanac = []


category = []
for line in lines:
    if line != '\n':
        if [int(s) for s in line.split() if s.isdigit()]:
            category.append([int(s) for s in line.split() if s.isdigit()])
        else:
            almanac.append(category)
            category = []
almanac.append(category)

locations = []

for seed in almanac[0][0]:
    curNum = seed
    for category in almanac[1::]:
        for range in category:
            

            if curNum >= range[1] and curNum < range[1] + range[2]:
 
                curNum = curNum - (range[1] - range[0])
                break

                

    locations.append(curNum)

print(min(locations))