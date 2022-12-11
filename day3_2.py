textA = input()
textB = input()
textC = input()

sum = 0
while textA!="":
    match = []
    for c in textA:
        if c in textB and c in textC:
            match.append(c)
    match = match[0]
    if match.isupper():
       sum+=ord(match) - 38
    else:
        sum+=ord(match)-96
    textA = input()
    textB = input()
    textC = input()
print(sum)