positions = [[0,0]]
t = [0, 0]
h = [0,0]
text = input()
while text!="":
    dir = text[0]
    steps = int(text.split(" ")[1])
    if dir == 'R':
        h[1]+=steps
    elif dir == 'L':
        h[1]-=steps
    elif dir == 'U':
        h[0]+=steps
    else:
        h[0]-=steps
    x = t[1]-h[1]
    y = t[0]-h[0]
    minN = min(abs(x),abs(y))
    maxN = max(abs(x),abs(y))
    if minN>1 or maxN>1:
        for i in range(1, minN + 1):
            t[0] += int(-y / abs(y))
            t[1] += int(-x / abs(x))
            help = [t[0], t[1]]
            positions.append(help) if help not in positions else positions
    for i in range(1,maxN-minN):
        if maxN==abs(y):
            t[0]+=int(-y/abs(y))
        else:
            t[1]+=int(-x/abs(x))
        help = [t[0], t[1]]
        positions.append(help) if help not in positions else positions
    text=input()
print(len(positions))