text = input()
target = 2000000
res = []
while text!="":
    x1 = int(text.split(" ")[0])
    y1 = int(text.split(" ")[1])
    x2 = int(text.split(" ")[2])
    y2 = int(text.split(" ")[3])
    distance = abs(x1-x2) + abs(y1-y2)
    for d in range(distance):
        range1 = x1 + d*2+1
        range2 = x1 - d*2+1
        replacor = [r for r in res if (r[0] >= range1 and r[0] <= range2) or (r[1] >= range1 and r[1] <= range2)]
        if replacor != []:
            replacor[0][0] = min(replacor[0][0], range1)
            replacor[0][1] = max(replacor[0][1], range2)
        else:
            res.append([range1, range2])
    text=input()

for e in res:
    replacor = [r for r in res if (r[0] >= e[0] and r[0] <= e[1]) or (r[1] >= e[0] and r[1] <= e[1])]
    if len(replacor)>1:
        replacor[1][0] = min(replacor[1][0], e[0])
        replacor[1][1] = max(replacor[1][1], e[1])
        res.remove(e)
for e in res:
    replacor = [r for r in res if (r[0] >= e[0] and r[0] <= e[1]) or (r[1] >= e[0] and r[1] <= e[1])]
    if len(replacor)>1:
        replacor[1][0] = min(replacor[1][0], e[0])
        replacor[1][1] = max(replacor[1][1], e[1])
        res.remove(e)
for e in res:
    replacor = [r for r in res if (r[0] >= e[0] and r[0] <= e[1]) or (r[1] >= e[0] and r[1] <= e[1])]
    if len(replacor)>1:
        replacor[1][0] = min(replacor[1][0], e[0])
        replacor[1][1] = max(replacor[1][1], e[1])
        res.remove(e)
print(sum([abs(r[0]-r[1]) for r in res]))