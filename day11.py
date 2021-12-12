def nineCount(row, col, grid):
	count = 0
	for i in range(row - 1, row + 2, 1):
		for j in range(col - 1, col + 2, 1):
			if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
				if grid[i][j] > 9:
					count += 1
	return count


def turn(grid):
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])): # adds 1 to every energy level
			grid[i][j] = (grid[i][j][0] + 1, False)	
	#for i in range(len(grid)):
	#	for j in range(len(grid[0])):
	#		if grid[i][j] <= 9:
	#			grid[i][j] += nineCount(i, j, grid)
	
	#for x in range(2):
	#	for i in range(len(grid)):
	#		for j in range(len(grid[0])):
	#			if grid[i][j] > 9:
	#				count += 1
	#				grid[i][j] = 0
	return grid, count





file = open("day11.txt")

grid = []

for line in file:
	row = []
	for i in line:
		if i != '\n':
			pair = (int(i), False) # [0] represents the energy level. [1] represents if has flashed yet this turn
			row.append(pair)
	grid.append(row)



for line in grid:
	print(line)
print('\n')

count = 0
for i in range(3):
	grid, count = turn(grid)
	for line in grid:
		print(line)
	print()
print(count)


print(grid[0][1][1])
