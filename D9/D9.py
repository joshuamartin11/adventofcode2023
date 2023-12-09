with open('D9/input.txt') as f:
    lines = f.readlines()
total = 0
totalP2 = 0
for line in lines:

    diffs = [[int(s) for s in line.split()]]
    while (True):

        diff = []
        for i in range(len(diffs[-1]) - 1):
            diff.append(diffs[-1][i+1] - diffs[-1][i])
        diffs.append(diff)

        if diff[-1] == 0:
            break
    diffs[-1].append(0)
    
    for i in range(1, len(diffs)):
        diffs[-i - 1].append(diffs[-i - 1][-1] + diffs[-i][-1])
        #The whole of P2:
        diffs[-i - 1].insert(0,diffs[-i - 1][0] - diffs[-i][0])

    total += diffs[0][-1]
    totalP2 += diffs[0][0]

print(total)
print(totalP2)



