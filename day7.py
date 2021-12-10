def fuelCost(pos, crabs):
    cost = 0
    for c in crabs:
        if c > pos:
            cost += (c - pos)
        else:
            cost += (pos - c)
    return cost


def fuelCost2(pos, crabs):
    cost = 0
    buff = 0
    for c in crabs:
        if c > pos:
            buff = c - pos
        else:
            buff = pos - c

        cost += ((buff/2)*(buff+1))
    
    return cost


file = open("input-2021-7.txt")

crabs = file.readline().split(',')

crabs = [int(i) for i in crabs]

least = fuelCost2(0, crabs)
buff = 0
for i in crabs:
    buff = fuelCost2(i, crabs)
    if buff < least:
        least = buff

print(least)
