with open('D6\input.txt') as f:
    lines = f.readlines()

times = [int(s) for s in lines[0].split() if s.isdigit()]
distances = [int(s) for s in lines[1].split() if s.isdigit()]
print(times)
print(distances)

total = 1

for i, time in enumerate(times):
    count = 0
    for x in range(0,time):
        if (time - x) * x > distances[i]:
            count += 1
    total *= count
print(total)
