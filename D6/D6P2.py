with open('D6\input.txt') as f:
    lines = f.readlines()

time = int(''.join([str(s) for s in lines[0].split() if s.isdigit()]))
distance = int(''.join([str(s) for s in lines[1].split() if s.isdigit()]))

total = 1

count = 0

firstFound = False
for x in range(0,time):
    if (time - x) * x > distance:
        firstFound = True
        count += 1
total *= count
print(total)
