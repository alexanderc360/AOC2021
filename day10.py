def corrupt(line):
    stack = []
    for i in line:
        if i == '(' or i == '[' or i == '{' or i == '<':
            stack.append(i)
        if i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 3
        if i == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return 57
        if i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 1197
        if i == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                return 25137
    return 0


def incomplete(line):
    stack = []
    close = []
    for i in line:
        if i == '(' or i == '[' or i == '{' or i == '<':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
        elif i == '>':
            if stack[-1] == '<':
                stack.pop()

    for i in range(len(stack)):
        buff = stack.pop()
        if buff == '(':
            close.append(')')
        elif buff == '[':
            close.append(']')
        elif buff == '{':
            close.append('}')
        elif buff == '<':
            close.append('>')
    
    score = 0
    for i in close:
        score *= 5
        if i == ')':
            score += 1
        elif i == ']':
            score += 2
        elif i == '}':
            score += 3
        elif i == '>':
            score += 4

    return score

file = open("input-2021-10.txt")

lines = []
for f in file:
    lines.append(f)


score = 0

scoreList = []
for i in lines:
    if corrupt(i) == 0:
        scoreList.append(incomplete(i))

scoreList = sorted(scoreList)

print(scoreList[int((len(scoreList) - 1) / 2)])

#for i in lines:
 #   score += corrupt(i)

#print(score)
