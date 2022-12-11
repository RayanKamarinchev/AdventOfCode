#                 [B] [L]     [J]
#             [B] [Q] [R]     [D] [T]
#             [G] [H] [H] [M] [N] [F]
#         [J] [N] [D] [F] [J] [H] [B]
#     [Q] [F] [W] [S] [V] [N] [F] [N]
# [W] [N] [H] [M] [L] [B] [R] [T] [Q]
# [L] [T] [C] [R] [R] [J] [W] [Z] [L]
# [S] [J] [S] [T] [T] [M] [D] [B] [H]
#  1   2   3   4   5   6   7   8   9
sets = [["W", "L", "S"], ["Q", "N", "T", "J"], ["J", "F", "H", "C", "S"], ["B", "G", "N", "W", "M", "R", "T"], ["B", "Q", "H", "D", "S", "L", "R", "T"]
    , ["L", "R", "H", "F", "V", "B", "J", "M"], ["M", "J", "N", "R", "W", "D"], ["J", "D", "N", "H", "F", "T", "Z", "B"], ["T", "F", "B", "N", "Q", "L", "H"]]
[s.reverse() for s in sets]

text = input()
while text!= "":
    text = text.replace("move ", "")
    text = text.replace("from ", "")
    text = text.replace("to ", "")
    n = int(text.split(" ")[0])
    start = int(text.split(" ")[1])-1
    end = int(text.split(" ")[2])-1
    sets[end].extend(sets[start][-n:])
    sets[start] = sets[start][0:len(sets[start])-n]
    text = input()
print(''.join([s[-1] for s in sets]))