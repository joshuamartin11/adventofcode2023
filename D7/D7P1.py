vals = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

with open('D7/inputtest.txt') as f:
    lines = f.readlines()


def fourOfKind(hand):
    for v in hand:
        if hand.count(v) == 4:
            return True
    return False

def threeOfKind(hand):
    for v in hand:
        if hand.count(v) == 3:
            return True
    return False

def pairs(hand):
    valuesCounted = []
    pairsCount = 0
    for v in hand:
        if hand.count(v) == 2 and v not in valuesCounted:
            valuesCounted.append(v)
            pairsCount += 1
    return pairsCount



def betterHand (h1, h2):
    h1 = list(h1)
    h2 = list(h2)

    for i in range(len(h1)):
        if h1[i].isalpha():
            h1[i] = vals[h1[i]]
        else:
            h1[i] = int(h1[i])
        if h2[i].isalpha():
            h2[i] = vals[h2[i]]
        else:
            h2[i] = int(h2[i])
    #5 of a kind:
    if h1.count(h1[0]) == 5 and h2.count(h2[0]) == 5:
        for i in range(len(h1)):
            if h1[i] > h2[i]:
                return 1
            elif h1[i] < h2[i]:
                return 2
    if h1.count(h1[0]) == 5:
        return 1
    if h2.count(h2[0]) == 5:
        return 2

    #4 of a kind:
    if fourOfKind(h1) and fourOfKind(h2):
        for i in range(len(h1)):
            if h1[i] > h2[i]:
                return 1
            elif h1[i] < h2[i]:
                return 2
    if fourOfKind(h1):
        return 1
    if fourOfKind(h2):
        return 2

    #full house:
    if (threeOfKind(h1) and pairs(h1) == 1) and (threeOfKind(h2) and pairs(h2) == 1):
        for i in range(len(h1)):
            if h1[i] > h2[i]:
                return 1
            elif h1[i] < h2[i]:
                return 2
    if threeOfKind(h1) and pairs(h1) == 1:
        return 1
    if threeOfKind(h2) and pairs(h2) == 1:
        return 2


    #3 of a kind:
    if threeOfKind(h1) and threeOfKind(h2):
        for i in range(len(h1)):
            if h1[i] > h2[i]:
                return 1
            elif h1[i] < h2[i]:
                return 2
    if threeOfKind(h1):
        return 1
    if threeOfKind(h2):
        return 2

    #2 pairs:
    if pairs(h1) == 2 and pairs(h2) == 2:
        for i in range(len(h1)):
            if h1[i] > h2[i]:
                return 1
            elif h1[i] < h2[i]:
                return 2
    if pairs(h1) == 2:
        return 1
    if pairs(h2) == 2:
        return 2
    
    #1 pairs:
    if pairs(h1) == 1 and pairs(h2) == 1:
        for i in range(len(h1)):
            if h1[i] > h2[i]:
                return 1
            elif h1[i] < h2[i]:
                return 2
    if pairs(h1) == 1:
        return 1
    if pairs(h2) == 1:
        return 2

    for i in range(len(h1)):
        if h1[i] > h2[i]:
            return 1
        elif h1[i] < h2[i]:
            return 2

    
def bubbleSort(arr):
    n = len(arr)
     
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):

            if betterHand(arr[j][0], arr[j+1][0]) == 1:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
hands = []
for line in lines:
    hands.append(line.split(' '))

bubbleSort(hands)
total = 0
for i,hand in enumerate(hands):
    print(hand[0])
    print(hand[1])
    total += int(hand[1]) * (i + 1)
print(total)


