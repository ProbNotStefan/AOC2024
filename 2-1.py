c,b,d = 0, True, False
for line in open("2.txt","r+"):
    line=list(map(int,line.split()));d,b = line[0]-line[1] < 0, True
    for i in range(len(line)-1):
        if abs(line[i]-line[i+1]) > 3 or abs(line[i]-line[i+1]) == 0 or (d == True and line[i]-line[i+1] > 0) or (d == False and line[i]-line[i+1] < 0): b = False
    if b == True: c += 1
print(c)