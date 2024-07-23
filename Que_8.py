#given a space separated integer list find the average of elements present in the even index
list=list(map(int,input().split(" ")))
sum=0
n=len(list)
for i in range(len(list)):
     if (i%2==0):
         sum+=list[i]
         print(sum/n)


