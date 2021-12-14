def genNewGrid(axis, val, grid):
    newGrid = []
    x = len(grid[0])
    y = len(grid)

    if axis == 'x':
        for i in range(y):
            buff = []
            for j in range(val):
                if grid[i][j] == '#':
                    buff.append('#')
                else:
                    buff.append('.')
            newGrid.append(buff)
    else:
        for i in range(val):
            buff = []
            for j in range(x):
                if grid[i][j] == '#':
                    buff.append('#')
                else:
                    buff.append('.')
            newGrid.append(buff)

    return newGrid


def fold(axis, val, grid):
	newGrid = genNewGrid(axis, val, grid)
	if axis == 'x':
		for i in range(len(grid)):
                        for j in range(val + 1, len(grid[0]), 1):
                                if grid[i][j] == '#' and grid[i][2 * val -j] != '#':
                                        newGrid[i][2 * val -j] = '#'
	else:
		for i in range(val + 1, len(grid), 1):
			for j in range(len(grid[0])):
				if grid[i][j] == '#' and grid[2 * val - i][j] != '#':
					newGrid[2 * val - i][j] = '#'

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
	paper[p[1]][p[0]] = '#'

for line in file:
	axis = line[line.index('=') - 1:line.index('=')]
	val = int(line[line.index('=') + 1:])
	paper = fold(axis,val, paper)
	count = 0
	for i in paper:
		for j in i:
	        	if j == '#':
	               		count += 1
	print(count)

for p in paper:
    print(p)

