#find the  elements that is present in k+n index 
list=list(map(int,input().split()))
k=int(input())
n=int(in
if len(list) < (k+n):
    print("error")
else:
    for i in range (len(list)):
     print(list[k+n])
     break
          