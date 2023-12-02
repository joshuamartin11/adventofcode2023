with open('D2\input.txt') as f:
    lines = f.readlines()

    count = 0

    for i,line in enumerate(lines):
        #Set the max value of each colour to 0 to start, this will change each time a new, higher value is found.
        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        subsets = line.split(':')[1].split(';')
        for subset in subsets:
            pull = subset.split(',')
            for round in pull:
                splitRound = round.split(' ')
                #Test if each colour's count is higher than the previous maxium, if it is replace it.
                if splitRound[2].strip() == "red" and int(splitRound[1]) >  maxRed:
                    maxRed = int(splitRound[1])
                if splitRound[2].strip() == "green" and int(splitRound[1]) >  maxGreen:
                    maxGreen = int(splitRound[1])
                if splitRound[2].strip() == "blue" and int(splitRound[1]) >  maxBlue:
                    maxBlue = int(splitRound[1])

        #Add the product of the maximums to the counts.
        count += maxRed * maxGreen * maxBlue
    #Print the final count.
    print(count)