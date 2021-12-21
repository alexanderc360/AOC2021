def step(xVel,yVel, target):
    x = 0
    y = 0
    
    hits = False
    maxY = 0
    while y > target[1][0] and x < target[0][1]:
        x += xVel
        y += yVel
        if y > maxY:
            maxY = y
        if xVel > 0:
            xVel -= 1
        elif xVel < 0:
            xVel += 1
        yVel -= 1
        if x >= target[0][0] and x <= target[0][1] and y >= target[1][0] and y <= target[1][1]:
            hits = True
    if hits:
        return maxY
    return -1


file = open('input-2021-17.txt')

line = file.readline()

xRange = line[line.index('x') + 2:line.index(',')].split('..')

xRange = [int(i) for i in xRange]

yRange = line[line.index('y') + 2:].split('..')

yRange = [int(i) for i in yRange]

print(xRange, yRange)

target = []
target.append(xRange)
target.append(yRange)

print(target)

l = []
y = 0
for i in range(target[0][1] + 1):
    for j in range(-120, 2000, 1):
        if step(i,j,target) >= 0:
            l.append((i,j))
            y += 1
        #        if step(i, j, target) > y:
 #           y = step(i,j,target)
print(y)
