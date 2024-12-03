c = 0
def check(line): return int(False not in [not (abs(line[i]-line[i+1]) > 3 or abs(line[i]-line[i+1]) == 0 or (line[0]-line[1] < 0 and line[i]-line[i+1] > 0) or (line[0]-line[1] > 0 and line[i]-line[i+1] < 0)) for i in range(len(line)-1)])
for line in open("2.txt","r+"):
    line=list(map(int,line.split()));c += int((1 in [check([line[j] for j in range(len(line)) if j != i]) for i in range(len(line))]) or check(line)==1)
print(c)