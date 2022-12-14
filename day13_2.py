from functools import cmp_to_key

pairs = []
text = input()
while text != "end":
    if text != "":
        smth = eval(text)
        pairs.append(smth)
    text = input()


def compare(pair1, pair2):
    for (i, p) in enumerate(pair1):
        if i > len(pair2) - 1:
            return 1
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
            return -1
        elif p > t:
            return 1
    if len(pair1) < len(pair2):
        return -1
    return 0


sum = 0
pairs.extend([[[2]],[[6]]])
pairs.sort(key=cmp_to_key(compare))
print((pairs.index([[2]])+1)*(pairs.index([[6]])+1))