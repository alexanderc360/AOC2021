def genNewGrid(axis, val, grid):
    newGrid = []
    x = len(grid[0])
    y = len(grid)

    if axis == 'x':
        print(val)
        for i in range(y):
            buff = []
            for j in range(val):
                if grid[i][j] == '#':
                    buff.append('#')
                else:
                    buff.append('.')
            newGrid.append(buff)
    else:
        print(val)
        for i in range(val):
            buff = []
            for j in range(x):
                if grid[i][j] == '#':
                    buff.append('#')
                else:
                    buff.append('.')
            newGrid.append(buff)

    #for i in newGrid:
     #   print(i)
    return newGrid


def fold(axis, val, grid):
    newGrid = genNewGrid(axis, val, grid)

    return newGrid


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
    print(line)
    axis = line[line.index('=') - 1:line.index('=')]
    val = int(line[line.index('=') + 1:])
    paper = fold(axis,val, paper)
    #paper = genNewGrid(axis,val,paper)

print()
for p in paper:
    print(p)
