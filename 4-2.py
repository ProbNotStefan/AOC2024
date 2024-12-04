c = 0
l = [line.strip() for line in open("4.txt", "r+")]
for i in range(1, len(l) - 1):
    for j in range(1, len(l[0]) - 1): c += int(l[i][j] == "A" and (((l[i-1][j-1] == "M" and l[i+1][j+1] == "S") or (l[i-1][j-1] == "S" and l[i+1][j+1] == "M")) and ((l[i+1][j-1] == "M" and l[i-1][j+1] == "S") or (l[i+1][j-1] == "S" and l[i-1][j+1] == "M"))))
print(c)