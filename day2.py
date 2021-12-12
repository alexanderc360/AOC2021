file = open("input-2021-2.txt")

y = 0
x = 0
buff = []


#for line in file:
#    buff = line.split()
#    if buff[0] == 'forward':
#        x += int(buff[1])
#    elif buff[0] == 'down':
#        y += int(buff[1])
#    elif buff[0] == 'up':
#        y -= int(buff[1])
#print(x*y)

aim = 0

for line in file:
    buff = line.split()
    if buff[0] == 'down':
        aim += int(buff[1])
    elif buff[0] == 'up':
        aim -= int(buff[1])
    elif buff[0] == 'forward':
        x += int(buff[1])
        y += (aim * int(buff[1]))

print(x*y)

