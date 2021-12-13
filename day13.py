def fold(axis, val):
    if axis == 'x':
        print('hotdog ', val)
    else:
        print('hamburger ', val)


file = open("input-2021-13.txt")


x = 0
y = 0
points = []
for line in file:
    if line == '\n':
        break
    else:
        buff = line.split(',')
        buff = [int(i) for i in buff]
        if buff[0] > x:
            x = buff[0]
        if buff[1] > y:
            y = buff[1]
        points.append(buff)

paper = []
x += 1
y += 1
for i in range(y):
    buff = []
    for j in range(x):
        buff.append('.')
    paper.append(buff)

for p in points:
    for i in range(y):
        for j in range(x):
            if j == p[0] and i == p[1]:
                paper[i][j] = '#'

for line in file:
    axis = line[line.index('=') - 1:line.index('=')]
    val = int(line[line.index('=') + 1:])
    fold(axis,val)

for p in paper:
    print(p)
