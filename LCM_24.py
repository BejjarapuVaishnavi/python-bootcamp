a=int(input())
b=int(input())
mul=a*b
while b!=0:
    a,b=b,a%b
print(mul//a)