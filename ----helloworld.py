""""
n=input()
n1=""
n2=""
for i in n:
    if(ord(i)==45):
        n1+=i 
    if(ord(i)>=97 and ord(i)<=122):
        n2+=i
print(n1,n2,end="")
 """


inp=input()
count=0
ans=""
for i in inp:
    if(i="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)
 