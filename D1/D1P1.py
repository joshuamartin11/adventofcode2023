with open('D1\input.txt') as f:
    lines = f.readlines()
    val = 0
    #Read through the lines
    for line in lines:
        #read through each character
        for c in line:
            #
            if c.isdigit():
                v1 = c
                break
        for c in reversed(line):
            if c.isdigit():
                v2 = c
                break
        val += int(v1 + v2)
    print(val)