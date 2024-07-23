#input=hello123world
#output=6
check="0123456789"
ans=0
i="hello123World"
inp=i.lower()
for i in inp:
   if(i in check):
    ans+=int(i)
print(ans)

