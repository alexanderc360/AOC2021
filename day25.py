file = open("input-2021-25.txt")

grid = []

for i in file:
    buff = []
    for j in i:
        if j != '\n':
            buff.append(j)
    grid.append(buff)

# print(grid)


# for row in grid:
#     for c in row:
#         if c == '>':
#             print('>')
x = len(grid[0]) - 1
y = len(grid) - 1

print(grid)
buffGrid = grid[0]

i = 0
while i < len(buffGrid):
    if buffGrid[i] == '>':
        if i < x and buffGrid[i + 1] == '.':
            buffGrid[i] = '.'
            buffGrid[i + 1] = '>'
            i = i + 1
        elif i == x and buffGrid[0] == '.':
            buffGrid[i] = '.'
            buffGrid[0] = '>'
    i = i + 1


k = 0

# for i in grid:
#     print(k)
#     k += 1
print(buffGrid)
