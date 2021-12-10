import time

def breed(fish):
        total = 0
        count = [0]*9
        for i in range(len(fish)): 
                count[int(fish[i])] += 1
        
        done = 0
        for i in range(256):
                done = count[0]
                for j in range(8):
                        count[j] = count[j+1]
                count[8] = done
                count[6] += done
        
        for c in count:
                total += c
        return total

file = open("input-2021-6.txt")

fish = []
fish = file.readline().split(',')

start = time.time()
print(breed(fish))
end = time.time()
print(end - start)
