pairs = [[]]
text = input()
while text != "end":
    if text == "":
        pairs.append([])
    else:
        smth = eval(text)
        pairs[-1].append(smth)
    text = input()


def compare(pair1, pair2):
    for (i, p) in enumerate(pair1):
        if i > len(pair2) - 1:
            return -1
        t = pair2[i]
        if type(p)==list or type(t)==list:
            if not type(p)==list:
                p = [p]
            if not type(t)==list:
                t = [t]
            res = compare(p, t)
            if res != 0:
                return res
        elif p < t:
            return 1
        elif p > t:
            return -1
    if len(pair1) < len(pair2):
        return 1
    return 0


sum = 0
for (i, pair) in enumerate(pairs):
    if compare(pair[0], pair[1]) > -1:
        sum += i+1
print(sum)