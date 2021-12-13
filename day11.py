count = 0

def flash(row, col, grid):
        global count
        count += 1

        for i in range(row - 1, row + 2, 1):
                for j in range(col - 1, col + 2, 1):
                        if i  >= 0 and j  >= 0 and i < len(grid) and j < len(grid[0]):
                                if not grid[i][j][1]:
                                        grid[i][j] = (grid[i][j][0] + 1, grid[i][j][1])
        grid[row][col] = (0,True)
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                        if grid[i][j][0] > 9:
                                grid = flash(i,j,grid)
        return grid


def turn(grid):
        count = 0
        for i in range(len(grid)):
                for j in range(len(grid[0])): # adds 1 to every energy level
                        grid[i][j] = (grid[i][j][0] + 1, False)
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                        if grid[i][j][0] > 9:
                                grid = flash(i,j,grid)

        return grid





file = open("input-2021-11.txt")

grid = []

for line in file:
        row = []
        for i in line:
                if i != '\n':
                        pair = (int(i), False) # [0] represents the energy level. [1] represents if has flashed yet this turn
                        row.append(pair)
        grid.append(row)

allFlash = False
x = 0

while not allFlash:
        allFlash = True
        grid = turn(grid)
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                        if grid[i][j][1] == False:
                                allFlash = False
        x += 1

print(x)
