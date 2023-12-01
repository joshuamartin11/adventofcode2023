with open('D1\input.txt') as f:
    lines = f.readlines()
    val = 0
    numWord = ['one','two','three','four','five','six','seven','eight','nine']
    for line in lines:
        firstInd = 100
        lastInd = -1
        for i in range(0,len(numWord)):
            ind = line.find(numWord[i])
            if ind >= 0 and ind < firstInd:
                firstInd = ind
                first = str(i + 1)
            
            ind = line.find(str(i + 1))
            if ind >= 0 and ind < firstInd:
                firstInd = ind
                first = str(i + 1)

            ind = line.rfind(numWord[i])
            if ind >= 0 and ind > lastInd:
                lastInd = ind
                last = str(i + 1)
            
            ind = line.rfind(str(i + 1))
            if ind >= 0 and ind > lastInd:
                lastInd = ind
                last = str(i + 1)

        print(first + last)

        

        val += int(first + last)
    print(val)