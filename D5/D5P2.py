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
# print(almanac)
# print(almanac[0][0][0])

location = 100000
for i in range(0, len(almanac[0][0]), 2):
    print(i)
    for seed in range(almanac[0][0][i], almanac[0][0][i] + almanac[0][0][i+1]):
        curNum = seed
        for category in almanac[1::]:
            for r in category:
                
                if curNum >= r[1] and curNum < r[1] + r[2]:
    
                    curNum = curNum - (r[1] - r[0])
                    break

                
        if curNum < location:
            location = curNum
# print(locations)

print(print(location))