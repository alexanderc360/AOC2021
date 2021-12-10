file = open("input-2021-3.txt")


def biToDec(num):
    twoPow = 1
    decNum = 0
    for i in reversed(num):
        decNum += i * twoPow
        twoPow *= 2
    return decNum


oneCount = [0]*12
tenPow = 1
gamma = []
epsilon = []
for line in file:
    for x in range(12):
        if line[x] == '1':
            oneCount[x] += 1

for x in oneCount:
    if x > 500:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)



#print(biToDec(epsilon)*biToDec(gamma))

def filter(nums, i, j):
    buff = []
    for x in nums:
        if x[i] == j:
            buff.append(x)
    return buff

file = open("input-2021-3.txt")
nums = []
for line in file:
    nums.append(line)

x = 0
while(len(nums)>1):
    count = 0
    for i in nums:
        if i[x] == '1':
            count += 1

    if count >= (len(nums)/2):
        nums = filter(nums, x,'1')
    else:
        nums = filter(nums, x, '0')
    x+=1
print(nums)
