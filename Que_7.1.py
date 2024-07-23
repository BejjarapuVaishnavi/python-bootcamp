## you are given with a comma separated natural numbers 1 to 10 print even numbers
list=list(map(int,input().split(",")))
for i in range(1,len(list),2):
 print(list[i])
    


