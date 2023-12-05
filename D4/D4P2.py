
def countCards(cardCount, index):
    cardCount += 1
    winnerCount = 0
    for number in cardStack[index][1]:
        if number in cardStack[index][0]:
            winnerCount += 1
            if index + winnerCount < len(cardStack):
                cardCount = countCards(cardCount, index + winnerCount)
    return cardCount
            
with open('D4\input.txt') as f:
    lines = f.readlines()

cardStack = []

for line in lines:

    card = line.split(':')[1].strip()
    cardSplit = card.split('|')

    winners = cardSplit[0].strip().split(' ')
    while "" in winners:
        winners.remove("")

    numbers = cardSplit[1].strip().split(' ')
    cardStack.append((winners,numbers))
total = 0
for i in range(0,len(cardStack)):
    total = countCards(total, i)
print(total)


