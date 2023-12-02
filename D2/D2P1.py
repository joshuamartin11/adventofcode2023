with open('D2\input.txt') as f:
    lines = f.readlines()


#Max number of cubes of each colour that can be used.
redCount = 12
greenCount = 13
blueCount = 14

count = 0
#Run through each game in the input storing the index as i.
for i,line in enumerate(lines):
    #Set the default validity to True, if any of the rounds is not possible this is set to false.
    valid = True
    #Get rid of the leading found number and split the games into the subsets separated by a semicolon.
    subsets = line.split(':')[1].split(';')
    #Run through each subset.
    for subset in subsets:
        #Separate each subset into how many times each colour was pulled.
        pull = subset.split(',')
        #Iterate through each one.
        for round in pull:
            splitRound = round.split(' ')
            #Run through each colour to test if it is valid if it isn't set valid to False.
            if splitRound[2].strip() == "red" and int(splitRound[1]) >  redCount:
                valid = False
            if splitRound[2].strip() == "green" and int(splitRound[1]) >  greenCount:
                valid = False
            if splitRound[2].strip() == "blue" and int(splitRound[1]) >  blueCount:
                valid = False
    #Add the game id to the count if after each test the game is still valid.
    if valid == True:
        count += i + 1
#Print the final count
print(count)