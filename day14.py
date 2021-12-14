def insert(template, key, step):
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
for i in range(10):
    template = insert(template, key, i)
#    print(template)

from collections import Counter

letterCount = Counter(template.strip())


print(max(letterCount.values()) - min(letterCount.values()))
