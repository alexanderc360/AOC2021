def draw(start, end, grid):
	#print(start, end)
	if start[0] == end[0]:  # verticle
		if start[1] > end[1]: 
			for i in range(end[1], start[1] + 1, 1):
				grid[i][start[0]] += 1
		else:
			for i in range(start[1], end[1] + 1, 1):
				grid[i][end[0]] += 1
	elif start[1] == end[1]:  # horizontal 
		if start[0] > end[0]:
			for i in range(end[0], start[0] + 1, 1):
				grid[start[1]][i] += 1
		else:
			for i in range(start[0], end[0] + 1, 1):
				grid[end[1]][i] += 1
				# diagnol
	else:	
		if start[0] > end[0]:
			if start[1] > end[1]:
				for i in range(start[0] - end[0] + 1):
					grid[start[1] - i][start[0] - i] += 1
			if start[1] < end[1]:
				for i in range(start[0] - end[0] + 1):
					grid[start[1] + i][start[0] - i] += 1
		elif start[0] < end[0]:
                	if start[1] > end[1]:
                        	for i in range(end[0] - start[0] + 1):
                                	grid[start[1] - i][start[0] + i] += 1
                	if start[1] < end[1]:
                        	for i in range(end[0] - start[0] + 1):
                                	grid[start[1] + i][start[0] + i] += 1

	return grid


file = open("input-2021-5.txt")


def demention(a, b):
    m = 0
    for i in a:
        if i[0] > m:
            m = i[0]
        if i[1] > m:
            m = i[1]
    for i in b:
        if i[0] > m:
            m = i[0]
        if i[1] > m:
            m = i[1]
    return m

startPoints = []
endPoints = []

for line in file:
    startPoints.append(line[0:line.find('->') - 1].split(','))
    endPoints.append(line[line.find('->') + 3:len(line) - 1].split(','))

for i in range(len(startPoints)):
    startPoints[i] = [int(j) for j in startPoints[i]]
    endPoints[i] = [int(k) for k in endPoints[i]]

#print(startPoints)
size = demention(startPoints, endPoints)

grid = []
for i in range(size + 1):
	buff = []
	for j in range(size + 1):
		buff.append(0)
		#buff.append((i, j))
	grid.append(buff)

#print(startPoints)

for i in range(len(startPoints)):
	grid = draw(startPoints[i], endPoints[i], grid)

#for i in grid:
#	print(i)

count = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] > 1:
			count += 1

print(count)
