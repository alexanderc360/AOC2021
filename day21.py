def turn(pos, roll):
	buff = 0
	for i in range(3):
		buff += roll
		roll += 1
	for i in range(buff):
		pos += 1
		if pos == 11:
			pos = 1
	return pos


file = open('input-2021-21.txt')

score = (0,0)

pos = [9,6]

roll = 1


one = 0
two  = 0 
for i in range(1000):
	one = turn(pos[0],roll)
	roll += 3
	score = (score[0] + one, score[1])
	if score[0] >= 1000:
		print('score', (roll - 1) * score[1])
		break
	two = turn(pos[1],roll)
	roll += 3
	score = (score[0], score[1] + two)
	if score[1] >= 1000:
		print('score', (roll - 1) * score[0])
		break
	pos[0] = one
	pos[1] = two
	print(score)
