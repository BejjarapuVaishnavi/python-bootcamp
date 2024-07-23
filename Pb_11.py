#find the maximum elements in a given list 
#test case:0
#12 23 36 44 45 57
#test case:1
#56 76 -8 12 34 -99
my_list=list(map(int,input().split()))
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]

print(max)
