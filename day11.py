import math


class Monkey:
    items = list()
    a = 0
    b = 1
    c = 0
    div = 1
    ok = 1,
    no = 1
    inspects = 0

    def __init__(self, items, a, b, c, div, ok, no):
        self.items = items
        self.a = a
        self.b = b
        self.c = c
        self.div = div
        self.ok = ok
        self.no = no

    def increase(self):
        self.inspects += len(self.items)
        for (j, i) in enumerate(self.items):
            if self.c != 0:
                i += self.c
            else:
                i = self.a * i * i + self.b * i + self.c
            i=i%9699690
            self.items[j] = i


monkeys = [Monkey([62, 92, 50, 63, 62, 93, 73, 50], 0, 7, 0, 2, 7, 1),
           Monkey([51, 97, 74, 84, 99], 0, 0, 3, 7, 2, 4),
           Monkey([98, 86, 62, 76, 51, 81, 95], 0, 0, 4, 13, 5, 4),
           Monkey([53, 95, 50, 85, 83, 72], 0, 0, 5, 19, 6, 0),
           Monkey([59, 60, 63, 71], 0, 5, 0, 11, 5, 3),
           Monkey([92, 65], 1, 0, 0, 5, 6, 3),
           Monkey([78], 0, 0, 8, 3, 0, 7),
           Monkey([84, 93, 54], 0, 0, 1, 17, 2, 1)]
# monkeys = [Monkey([79, 98], 0, 19, 0, 23, 2, 3),
#            Monkey([54, 65, 75, 74], 0, 0, 6, 19, 2, 0),
#            Monkey([79, 60, 97], 1, 0, 0, 13, 1, 3),
#            Monkey([74], 0, 0, 3, 17, 0, 1)]
cycles = 10000
for c in range(cycles):
    for m in monkeys:
        m.increase()
        for i in m.items:
            if i % m.div == 0:
                monkeys[m.ok].items.append(i)
            else:
                monkeys[m.no].items.append(i)
        m.items.clear()
vals = [m.inspects for m in monkeys]
vals.sort()
print(vals)
print(vals[-1] * vals[-2])
