matrix = list()
text = input()
times = 0
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
        max1 = max([row[j] for row in matrix[:i]])
        max2 = max([row[j] for row in matrix[i:]])
        max3 = max(r[:j])
        max4 = max(r[j+1:])
        if max([row[j] for row in matrix[:i]]) >= n and max([row[j] for row in matrix[i+1:]]) >= n and max(r[:j]) >= n and max(r[j+1:]) >= n:
            times+=1
print(sum([len(row) for row in matrix])-times)
