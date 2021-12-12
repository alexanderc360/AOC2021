def lowPoint(row, col, grid):
    low = True
    buff = grid[row][col]

    if row == 0:
        if col == 0:
            if buff >= grid[row + 1][col] or buff >= grid[row][col + 1]:
                low = False
        elif col == len(grid[0]) - 1:
            if buff >= grid[row + 1][col] or buff >= grid[row][col - 1]:
                low = False
        else:
            if buff >= grid[row + 1][col] or buff >= grid[row][col + 1] or buff >= grid[row][col - 1]:
                low = False
    elif row == len(grid) - 1:
        if col == 0:
            if buff >= grid[row - 1][col] or buff >= grid[row][col + 1]:
                low = False
        elif col == len(grid[0]) - 1:
            if buff >= grid[row - 1][col] or buff >= grid[row][col - 1]:
                low = False
        else:
            if buff >= grid[row - 1][col] or buff >= grid[row][col + 1] or buff >= grid[row][col - 1]:
                low = False
    else:
        if col == 0:
            if buff >= grid[row - 1][col] or buff >= grid[row + 1][col] or buff >= grid[row][col + 1]:
                low = False
        elif col == len(grid[0]) - 1:
            if buff >= grid[row - 1][col] or buff >= grid[row + 1][col] or buff >= grid[row][col - 1]:
                low = False
        else:
            if buff >= grid[row - 1][col] or buff >= grid[row + 1][col]\
                    or buff >= grid[row][col - 1] or buff >= grid[row][col + 1]:
                low = False

    #if low:
        #return buff + 1
    #else:
        #return -1
    return low


def basin(row, col, grid, size):

    print(size)
    #print(row, " ", col)
    #print(grid[row][col])
    if row == 0:
        if grid[row + 1][col] != 9:
            grid[row + 1][col] = 9
            basin(row + 1, col, grid, size + 1)
        
    elif row == len(grid) - 1:
        if grid[row -1][col] != 9:
            grid[row + 1][col] = 9
            basin(row - 1, col, grid, size + 1)
    else:
        if grid[row + 1][col] != 9:
            grid[row + 1][col] = 9
            basin(row + 1, col, grid, size + 1)
        if grid[row - 1][col] != 9:
            grid[row + 1][col] = 9
            basin(row - 1, col, grid, size + 1)

    return size

file = open("input-2021-9.txt")

grid = []
buff =[]

while(1):
    c = file.read(1)
    if not c:
        break
    elif c == '\n':
        buff = [int(i) for i in buff]
        grid.append(buff)
        buff = []
    else:
        buff.append(c)

count = 0
spots = []
#for i in range(len(grid)):
 #   for j in range(len(grid[0])):
       # buff = lowPoint(i,j,grid)
        #if buff > -1:
  #       if lowPoint(i,j,grid):
print(basin(2,2,grid,1))
            #count += buff

#print(count)
