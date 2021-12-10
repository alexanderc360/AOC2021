def correctNums(cipher):
    letters = [0]*7
    buff = cipher[0]

    for i in cipher[1]:
        if i not in buff: # top bar
            letters[0] = i

    for i in buff:
        for j in cipher:
            if len(j) == 6:
                if i not in j: # determines which right bar is 2 
                    letters[2] = i
    
    if letters[2] == buff[0]: # whichever bar is not 2, add to space 5
        letters[5] = buff[1]
    else:
        letters[5] = buff[0]


    buff = cipher[2] # set buff to the code for four

    for i in buff:
        for j in cipher:
            if len(j) == 6:
                if letters[5] in j and letters[2] in j:
                    if i not in j: # uses zero to determine letter in space 3
                        letters[3] = i
    
    for i in buff:
        if i not in letters: # other letter goes in space 1
            letters[1] = i
    
    buff = cipher[9] # set buff to eight

    
    for i in buff:
        for j in cipher:
            if len(j) == 6:
                if letters[3] in j:
                    if letters[2] in j: # ensures that j is nine
                        if i not in j: # the missing bar goes in 4
                            letters[4] = i
    for i in buff:
        if i not in letters: # sets last letter to space 6
            letters[6] = i

    return letters


def decipher(letters, output):
    nums = [[letters[0], letters[1], letters[2], letters[4], letters[5], letters[6]],
            [letters[2], letters[5]],
            [letters[0], letters[2], letters[3], letters[4], letters[6]],
            [letters[0], letters[2], letters[3], letters[5], letters[6]], 
            [letters[1], letters[2], letters[3], letters[5]],
            [letters[0], letters[1], letters[3], letters[5], letters[6]],
            [letters[0], letters[1], letters[3], letters[4], letters[5], letters[6]],
            [letters[0], letters[2], letters[5]], 
            [letters[0], letters[1], letters[2], letters[3], letters[4], letters[5], letters[6]], 
            [letters[0], letters[1], letters[2], letters[3], letters[5], letters[6]]]
    
    for i in range(len(nums)):
        nums[i] = sorted(nums[i])
    
    buff = 0
    tenPow = 1000

    for i in output:
        buff += (nums.index(i)*tenPow)
        tenPow /= 10
    
    return buff



file = open("input-2021-8.txt")

code = []
output = []
total = 0
buff = ""

for line in file:
    buff = line[0:line.find('|')-1].split()
    for i in range(len(buff)):
        buff[i] = sorted(buff[i])
    code.append(sorted(buff, key= len))
    
    buff = line[line.find('|') + 1:].split()
    for i in range(len(buff)):
        buff[i] = sorted(buff[i])
    output.append(buff)

for i in range(len(code)):
    total += decipher(correctNums(code[i]), output[i])

print(total)
