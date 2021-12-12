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

grid = [[0]*size]*size

print(grid)
