def winCheck(board):
    row = [0]*5
    col = [0]*5
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'x':
                row[i] += 1
                col[j] += 1
    for i in range(5):
        if row[i] == 5:
            return True
        elif col[i] == 5:
            return True
    
def sim(nums, game):
    for n in nums:  # running through the called numbers
        for i in game:  # running through the boards
            for j in range(5):
                for k in range(5):
                    if i[j][k] == n:
                        i[j][k] = 'x'
        for i in game:
            if winCheck(i):
                return i, n

def simLast(nums, game):
    winBoards = [0]*len(game)
    #lastWon = -1
    for n in nums:  # running through the called numbers
        winCount = 0
        for i in range(len(game)):  # running through the boards
            for j in range(5):
                for k in range(5):
                    if game[i][j][k] == n:
                        game[i][j][k] = 'x'
            if winCheck(game[i]):
                winBoards[i] = 1
                lastWon = i
        for x in winBoards:
            winCount += x
        if winCount == len(winBoards):
            print(lastWon)
            return n, game[lastWon-1]



file = open("input-2021-4.txt")

nums = file.readline().split(',')

nums = [int(i) for i in nums]

file.readline()

board = []
game = []

for line in file:
    if line != '\n':
        board.append(line.split())
    if line == '\n':
        for i in range(5):
            board[i] = [int(j) for j in board[i]]

        game.append(board)
        board = []

for i in range(5):
    board[i] = [int(j) for j in board[i]]
game.append(board)
    

score = 0
winning, n = sim(nums, game)



x, last = simLast(nums, game)

for i in range(5):
    for j in range(5):
        if last[i][j] != 'x':
            score += last[i][j]

#for i in range(5):
 #   for j in range(5):
  #      if winning[i][j] != 'x':
   #         score += winning[i][j]

#print(len(game))
print(score*x)

