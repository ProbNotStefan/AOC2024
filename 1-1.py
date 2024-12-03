l1,l2,c = [],[],0
for line in open("1.txt","r+"):(l1.append(int(line.split()[0])),l2.append(int(line.split()[1])))
l1,l2=sorted(l1),sorted(l2)
for i in range(len(l1)):c+=abs(l1[i]-l2[i])
print(c)