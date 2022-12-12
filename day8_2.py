matrix = list()
text = input()
mx = 0
while text!= "":
    matrix.append([int(c) for c in text])
    text = input()
for (i, r) in enumerate(matrix[1:-1], start=1):
    for (j, n) in enumerate(r[1:-1], start=1):
        # 30373
        # 25512
        # 65332
        # 33549
        # 35390
        max1 = 0
        for x in [row[j] for row in matrix[:i]]:
            max1+=1
            if x >= n:
                break
        max2 = 0
        for x in [row[j] for row in matrix[i+1:]].__reversed__():
            max2 += 1
            if x >= n:
                break
        max3 = 0
        for x in r[:j].__reversed__():
            max3 += 1
            if x >= n:
                break
        max4 = 0
        for x in (r[j+1:]):
            max4 += 1
            if x >= n:
                break
        # max1 = max(max1, 1)
        # max2 = max(max2, 1)
        # max3 = max(max3, 1)
        # max4 = max(max4, 1)
        score = (max1)*(max2)*(max3)*(max4)
        if score > mx:
            mx=score
print(mx)
