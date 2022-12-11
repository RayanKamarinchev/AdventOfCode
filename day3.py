
text = input()
sum = 0
while text!="":
    text1 = text[0:int(len(text)/2)]
    text2 = text[int(len(text)/2): int(len(text))]
    match = []
    for c in text1:
        if c in text2:
            match.append(c)
    match = match[0]
    if match.isupper():
       sum+=ord(match) - 38
    else:
        sum+=ord(match)-96
    text = input()
print(sum)