c = 0
for line in open("2.txt","r+"):
    line=list(map(int,line.split()));d,b = line[0]-line[1] < 0, True
    c += int(False not in [not (abs(line[i]-line[i+1]) > 3 or abs(line[i]-line[i+1]) == 0 or (d == True and line[i]-line[i+1] > 0) or (d == False and line[i]-line[i+1] < 0)) for i in range(len(line)-1)])
print(c)