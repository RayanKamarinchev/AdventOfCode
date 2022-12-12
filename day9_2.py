positions = [[0,0]]
rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
text = input()
while text!="":
    dir = text[0]
    steps = int(text.split(" ")[1])
    if dir == 'R':
        rope[0][1]+=steps
    elif dir == 'L':
        rope[0][1]-=steps
    elif dir == 'U':
        rope[0][0]+=steps
    else:
        rope[0][0]-=steps
    for (i, t) in enumerate(rope[1:], start=1):
        x = t[1] - rope[i-1][1]
        y = t[0] - rope[i-1][0]
        minN = min(abs(x), abs(y))
        maxN = max(abs(x), abs(y))
        if minN > 1 or maxN > 1:
            for j in range(1, minN+1):
                t[0] += int(-y / abs(y))
                t[1] += int(-x / abs(x))

                x = t[1] - rope[i - 1][1]
                y = t[0] - rope[i - 1][0]
                minN = min(abs(x), abs(y))
                maxN = max(abs(x), abs(y))

                if minN<=1 and maxN<=1:
                    break
                if i == 9:
                    help = [t[0], t[1]]
                    positions.append(help) if help not in positions else positions
        for i in range(1, maxN - minN):
            if maxN == abs(y):
                t[0] += int(-y / abs(y))
            else:
                t[1] += int(-x / abs(x))
            if i == 9:
                help = [t[0], t[1]]
                positions.append(help) if help not in positions else positions

    text=input()
print(len(positions))