c, l = 0, [line.strip() for line in open("4.txt", "r+")]
for p in range(len(l)): c += sum([int(l[p][i:i+4] in ["XMAS", "SAMX"]) for i in range(len(l[0])-3)])
for p in range(len(l) - 3): c += sum([int("".join(l[p+k][i] for k in range(4)) in ["XMAS", "SAMX"]) for i in range(len(l[0]))])
for p in range(len(l) - 3): c += sum([int("".join(l[p+k][i+k] for k in range(4)) in ["XMAS", "SAMX"]) for i in range(len(l[0])-3)]+[int("".join(l[p+k][i-k] for k in range(4)) in ["XMAS", "SAMX"]) for i in range(3, len(l[0]))])
print(c)