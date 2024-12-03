c,l = 0,"".join(open("3.txt","r+"));from contextlib import suppress;exec("def mul(x,y): return x*y")
for i in range(len(l)):
    for j in range(5):
        with suppress(SyntaxError,NameError,TypeError): c += eval(l[i:i+8+j])*int(l[i:i+4] == "mul(");break
print(c)