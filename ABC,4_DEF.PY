#input=ABC,4
#output=DEF
inp=input()
n=inp.upper()
for i in inp:
    print(chr(ord(i)+4),end="")