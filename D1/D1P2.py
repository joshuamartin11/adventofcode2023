with open('D1\input.txt') as f:
    lines = f.readlines()
    val = 0

    #list of number strings.
    numWord = ['one','two','three','four','five','six','seven','eight','nine']

    #read through each line of the input
    for line in lines:

        #Index values to test against.
        firstInd = 100
        lastInd = -1

        #iterate through each index of the numWord list.
        for i in range(0,len(numWord)):

            #Get the index of the first instance of the number word.
            ind = line.find(numWord[i])
            #If the first instance is an index closer to the front of the line.
            if ind >= 0 and ind < firstInd:
                #replace the previous instance and set the new index.
                firstInd = ind
                first = str(i + 1)
            
            #Same for digits.
            ind = line.find(str(i + 1))
            if ind >= 0 and ind < firstInd:
                firstInd = ind
                first = str(i + 1)

            #Same for number words reversed.
            ind = line.rfind(numWord[i])
            if ind >= 0 and ind > lastInd:
                lastInd = ind
                last = str(i + 1)
            
            #Same for digits reversed.
            ind = line.rfind(str(i + 1))
            if ind >= 0 and ind > lastInd:
                lastInd = ind
                last = str(i + 1)

        val += int(first + last)
    print(val)