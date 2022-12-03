cal = input()
packs = []
current = 0;
while cal!='e':
    if cal == "":
        packs.append(current)
        current = 0
    else:
        current+=int(cal)
    cal = input()
print(max(packs))
packs.remove(max(packs))
print(max(packs))
packs.remove(max(packs))
print(max(packs))
packs.remove(max(packs))