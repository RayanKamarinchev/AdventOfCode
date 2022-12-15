text = input()
cd = {}
path = []
workable = []
while text != "":
    if text.split()[0] == '$':
        if text.split()[1] == "cd":
            if text.split()[2] == "/":
                path = []
            elif text.split()[2] == "..":
                path.pop()
            else:
                path.append(text.split()[2])
        else:
            workable = cd
            for p in path:
                workable = workable[p]
    else:
        if text.split()[0] == "dir":
            workable[text.split()[1]] = {}
        else:
            workable[text.split()[1]] = int(text.split()[0])

    text = input()

sums = []


def calcSize(dir):
    sum = 0
    for key, d in dir.items():
        if type(d) == dict:
            sum += calcSize(d)
        else:
            sum += d
    sums.append(sum)
    return sum


max = calcSize(cd)
print("Part1: ")
print(sum([s for s in sums if s <= 100000]))
print("Part2:")
print(min([s for s in sums if s >= max-40000000]))
