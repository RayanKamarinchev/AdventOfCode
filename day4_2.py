line = input()
sum = 0
while line != "":
    pairs = line.split(",")
    p1n1 = int(pairs[0].split("-")[0])
    p1n2 = int(pairs[0].split("-")[1])
    p2n1 = int(pairs[1].split("-")[0])
    p2n2 = int(pairs[1].split("-")[1])
    if p1n1>=p2n1 and p1n1<= p2n2:
        sum+=1
    elif p1n2>=p2n1 and p1n2<= p2n2:
        sum+=1
    elif p2n2>=p1n1 and p2n2<= p1n2:
        sum+=1
    elif p2n2>=p1n1 and p2n2<= p1n2:
        sum+=1
    line = input()
print(sum)