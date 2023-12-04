with open('D4\input.txt') as f:
    lines = f.readlines()

total = 0
for line in lines:
    card = line.split(':')[1].strip()
    cardSplit = card.split('|')

    winners = cardSplit[0].strip().split(' ')
    while "" in winners:
        winners.remove("")
    numbers = cardSplit[1].strip().split(' ')
    points = 0
    for number in numbers:
        if number in winners:
            if points == 0:
                points = 1
            else:
                points *= 2
    total += points
print(total)