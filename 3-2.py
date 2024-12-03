c,l,b = 0,"".join(open("3.txt","r+")).replace("don't","dont"),True;from contextlib import suppress;exec("def mul(x,y): return x*y");exec("def do():global b; b = True");exec("def dont():global b; b = False")
for i in range(len(l)):
    for j in range(4):
        with suppress(SyntaxError,NameError,TypeError): c += eval(l[i:i+8+j])*int(l[i:i+4] == "mul(")*int(b)
print(c)