file = open("input-2021-1.txt")

nums = []
tripleSums = []
count = 0
buff = 0

for line in file:
    nums.append(int(line))

for x in range(3):
    buff += nums[x]

tripleSums.append(buff)

for x in range(3,len(nums)):
    buff -= nums[x-3]
    buff += nums[x]
    tripleSums.append(buff)
    
for x in range(1, len(tripleSums)):
    if tripleSums[x] > tripleSums[x-1]:
        count += 1



print(count)
