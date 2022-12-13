text = input();
lines = list()
while text!="":
    lines.append(text)
    text=input()
p1 = []
cycles = []
for line in lines:
    cycles.extend([0] if line == "noop" else [0, int(line.split()[1])])
for i in range(20, 221, 40):
    p1.append(i * (sum(cycles[:i-1]) + 1))
crt = [["."] * 40 for _ in range(6)]
print(f"Part 1: {sum(p1)}")
for c in range(len(cycles)):
    x = sum(cycles[:c]) + 1
    if c % 40 in range(x - 1, x + 2):
        crt[c//40][c%40] = "#"
print("Part 2:")
for line in crt:
    print("".join([p if p == "#" else " " for p in line]))