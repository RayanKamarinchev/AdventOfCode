matrix = []
for i in range(170):
    matrix.append(['.'] * 1000)
matrix.append(['#']*1000)
text = input()
while text != "":
    lines = text.split(" -> ")
    for i in range(0, len(lines)-1):
        x1 = int(lines[i].split(",")[0])
        y1 = int(lines[i].split(",")[1])
        x2 = int(lines[i+1].split(",")[0])
        y2 = int(lines[i+1].split(",")[1])
        if x1 != x2:
            for c in range(abs(x1-x2)+1):
                matrix[y1][c+min(x1, x2)] = '#'
        else:
            for c in range(abs(y1-y2)+1):
                matrix[c+min(y1, y2)][x1] = '#'
    text = input()

def generate_sand():
    sx = 0
    sy = 500
    while True:
        try:
            if matrix[sx + 1][sy] != '#':
                sx += 1
            elif sy == 0:
                return -1
            elif matrix[sx + 1][sy - 1] != '#':
                sx += 1
                sy -= 1
            elif matrix[sx + 1][sy + 1] != '#':
                sx += 1
                sy += 1
            else:
                matrix[sx][sy] = '#'
                return 1
        except:
            return -1

def generate_sand2():
    sx = 0
    sy = 500
    if matrix[sx][sy]=='#':
        return -1
    while True:
        if matrix[sx + 1][sy] != '#':
            sx += 1
        elif matrix[sx + 1][sy - 1] != '#':
            sx += 1
            sy -= 1
        elif matrix[sx + 1][sy + 1] != '#':
            sx += 1
            sy += 1
        else:
            matrix[sx][sy] = '#'
            return 1

[print(row) for row in matrix]
#Part 1
# res = 1
# pas = generate_sand()
# while True:
#     pas = generate_sand()
#     if pas == -1:
#         break
#     res += pas

#Part 2
res = 1
pas = generate_sand2()
while True:
    pas = generate_sand2()
    if pas == -1:
        break
    res += pas


print(res)
