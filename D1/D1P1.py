with open('D1\input.txt') as f:
    lines = f.readlines()
    
val = 0
#Read through the lines
for line in lines:
    #read through each character
    for c in line:
        #Check if the character is a number
        if c.isdigit():
            #If it is a number set v1 to that character
            v1 = c
            break
    #read through each character in the string backwards
    for c in reversed(line):
        if c.isdigit():
            v2 = c
            break
    #Concatenate the strings together, make it an int and add it to the total.
    val += int(v1 + v2)
#print the final value.
print(val)