from collections import Counter
import time

def insert(template, key):
    polymer = []
    count = 0
    for i in range(len(template) - 1):
        buff = template[i] + template[i + 1]
        for j in key:
            if buff == j[0]:
                count += 1
        
    for i in range(len(template) - 1):
        buff = template[i] + template[i + 1]
        polymer.append(template[i])
        for j in key:
            if buff == j[0]:
                polymer.append(j[1])
    p = ""
    for i in polymer:
        p += i

    return p + " "


def insert2(poly, key):
    newPoly = {}
    for i in poly:
        fst = ''
        snd = ''
        for j in key:
            if i == j[0]:
                fst = i[0] + j[1]
                snd = j[1] + i[1]
        if i == 'B\n':
            newPoly['B\n'] = 1
        if fst != '' and snd != '':
            if fst in newPoly.keys():
                newPoly[fst] += poly[i]
            else:
                newPoly[fst] = poly[i]
            if snd in newPoly.keys():
                newPoly[snd] += poly[i]
            else:
                newPoly[snd] = poly[i]
    return newPoly
	

file = open("input-2021-14.txt")

template = file.readline()
file.readline()

key = []
for line in file:
    key.append([i.strip() for i in line.split(" -> ")])


#print(template)
#for i in range(10):
	#print(i)
	#template = insert(template, key)
#    print(template)


polymer = {}

for i in range(len(template) - 1):
	cur = template[i] + template[i + 1]
	if cur in polymer.keys():
		polymer[cur] += 1
	else:
            polymer[cur] = 1

for i in range(40):
    polymer = insert2(polymer, key)

letters = {}
for i, j in polymer.items():
    if i[0] in letters.keys():
        letters[i[0]] += (1 * j)
    else:
        letters[i[0]] = (1 * j)

print(max(letters.values()) - min(letters.values()))
