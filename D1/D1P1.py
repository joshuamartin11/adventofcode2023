with open('D1\input.txt') as f:
    lines = f.readlines()
    val = 0
    for line in lines:
        for c in line:
            if c.isnumeric():
                v1 = c
                break
        for c in reversed(line):
            if c.isnumeric():
                v2 = c
                break
        val += int(v1 + v2)
    print(val)