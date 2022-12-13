text = input();
lines = list()
while text!="":
    lines.append(text)
    text=input()
input = [line for line in lines]
i = 1
c = 1
sum = 1
res = 0
image=""

for comand in input:
    if comand.split()[0]=="noop":
        i+=1
        if c >= sum and c <= sum + 2:
            image += "#"
        else:
            image += "."
    else:
        num = int(comand.split()[1])
        
        i+=1
        if c>=sum and c <= sum + 2:
            image += "#"
        else:
            image += "."
        if i%40==20:
            res+=i*sum
        i+=1
        if c >= sum and c <= sum + 2:
            image += "#"
        else:
            image += "."
        c=i%40
        sum+=num
    if i % 40 == 20:
        res += i * sum
print(f"Part 1 : {res}")
[print(i) for i in [image[i:i+40] for i in range(0, len(image), 40)]]

