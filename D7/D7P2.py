vals = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}

with open('D7/input.txt') as f:
    lines = f.readlines()


def fourOfKind(hand):
    for v in hand:
        if hand.count(v) == 4:
            if hand.count(1) == 1 or hand.count(1) == 4:
                return 7
            else:
                return 6
    return 0


def threeOfKind(hand):
    for v in hand:
        if hand.count(v) == 3:
            if(hand.count(1) == 3 or hand.count(1) == 1):
                return 6
            return 4
            
    return 0

def pairs(hand):
    valuesCounted = []
    pairsCount = 0
    for v in hand:
        if hand.count(v) == 2 and v not in valuesCounted:
            valuesCounted.append(v)
            pairsCount += 1
    if pairsCount == 2:
        if hand.count(1) == 1:
            return 5
        if hand.count(1) == 2:
            return 6
        return 3
    if pairsCount == 1:
        if hand.count(1) == 1 or hand.count(1) == 2:
            return 4
        return 2


    return 0

def fullHouse(hand):
    if threeOfKind(hand) > 0 and pairs(hand) > 0:
        if hand.count(1) == 2 or hand.count(1) == 3:
            return 7
        if hand.count(1) == 1:
            return 6
        return 5
    return 0

def betterHand (h1, h2):
    h1 = list(h1)
    h2 = list(h2)

    h1Score = 0
    h2Score = 0

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
    if h1.count(h1[0]) == 5:
        h1Score = 7
    if h2.count(h2[0]) == 5:
        h2Score = 7

    #4 of a kind:
    h1TempScore = fourOfKind(h1)
    h2TempScore = fourOfKind(h2)
    if h1TempScore > h1Score:
        h1Score = h1TempScore
    if h2TempScore > h2Score:
        h2Score = h2TempScore


    #full house:
    h1TempScore = fullHouse(h1)
    h2TempScore = fullHouse(h2)
    if h1TempScore > h1Score:
        h1Score = h1TempScore
    if h2TempScore > h2Score:
        h2Score = h2TempScore

    #3 of a kind:
    h1TempScore = threeOfKind(h1)
    h2TempScore = threeOfKind(h2)
    if h1TempScore > h1Score:
        h1Score = h1TempScore
    if h2TempScore > h2Score:
        h2Score = h2TempScore

    #pairs:
    h1TempScore = pairs(h1)
    h2TempScore = pairs(h2)
    if h1TempScore > h1Score:
        h1Score = h1TempScore
    if h2TempScore > h2Score:
        h2Score = h2TempScore
    
    if h1.count(1) == 1:
        if 2 > h1Score:
            h1Score = 2
    if h2.count(1) == 1:
        if 2 > h2Score:
            h2Score = 2

    if h1Score == h2Score:
        for i in range(len(h1)):
            if h1[i] > h2[i]:
                return 1
            elif h1[i] < h2[i]:
                return 2
    if h1Score > h2Score:
        return 1
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
    total += int(hand[1]) * (i + 1)
print(total)

