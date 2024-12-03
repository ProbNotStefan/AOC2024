l1,l2,c = [],[],0
for line in open("1.txt","r+"):t=(l1.append(int(line.split()[0])),l2.append(int(line.split()[1])))
l1,l2 = sorted(l1),sorted(l2)
for i in range(len(l1)):c+=sum(l2[j]for j in range(len(l2))if l2[j]==l1[i])
print(c)