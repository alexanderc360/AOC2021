import math
file = open("input-2021-24.txt")




def alu(file, inp):
	inp = str(inp)
	i = -1
	j = -1
	vals = [0,0,0,0]
	for line in file:
		snd = False

		if line[4] == 'w':
			i = 0
		elif line[4] == 'x':
			i = 1
		elif line[4] == 'y':
			i = 2
		elif line[4] == 'z':
			i = 3
		if line[:3] != 'inp' and ord(line[6]) > 57:
			snd = True
			if line[5:].strip() == 'w':
                		j = 0
			elif line[5:].strip() == 'x':
				j = 1
			elif line[5:].strip() == 'y':
				j = 2
			elif line[5:].strip() == 'z':
                        	j = 3

		if line[:3] == 'add':
			if snd:
				vals[i] += vals[j]
			else:
				vals[i] += int(line[5:].strip())
		#print('+')
		elif line[:3] == 'mul':
			if snd:
				vals[i] *= vals[j]
			else:
				vals[i] *= int(line[5:].strip())
		#print('*')
		elif line[:3] == 'div':
			if snd:
				vals[i] = math.floor(vals[i] / vals[j])
			else:	
				vals[i] = math.floor(vals[i] / int(line[5:].strip()))
		#print('/')
		elif line[:3] == 'mod':
			
			if snd:
				vals[i] %= vals[j]
			else:
				vals[i] %= int(line[5:].strip())
	#	print('%')
		elif line[:3] == 'eql':
			if vals[i] == vals[j]:
				vals[i] = 1
			else:
				vals[i] = 0
	#	print('=')
		elif line[:3] == 'inp':
			vals[i] = int(inp[0])
			inp = inp[1:]
		print(vals)
	return vals
	#print()

start = 99999999999999
vals = [0]*4
print(alu(file, 23079246999999))
#while vals[3] != 0:
#	vals = alu(file, start)
#	start -= 1
#print(vals, start)
