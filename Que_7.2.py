#how many even numbers are there in above question
list=list(map(int,input().split(",")))
count=0
for i in range(1,len(list),2):
        count+=1
print(count)        
