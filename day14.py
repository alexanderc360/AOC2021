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
 #       print(buff)
        polymer.append(template[i])
        for j in key:
            if buff == j[0]:
                polymer.append(j[1])
    #print(polymer)
    p = ""
    for i in polymer:
        p += i

    return p + " "


def insert2(poly, key):
	cur = ''
	newPoly = dict(poly)
	for i in poly:
		for j in key:
			if i == j[0]:
				cur = i[0] + j[1]
		if cur in newPoly.keys():
			newPoly[cur] += poly[i]
		else:
			newPoly[cur] = 1
	return newPoly
	

file = open("input-2021-14.txt")

template = file.readline()
file.readline()
#print(template)

key = []

for line in file:
    key.append([i.strip() for i in line.split(" -> ")])

#for i in key:
 #   print(i)

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

print(polymer)
print(insert2(polymer, key))
from collections import Counter

letterCount = Counter(template.strip())

#print(letterCount.keys())

#print(max(letterCount.values()) - min(letterCount.values()))
