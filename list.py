my_list=[1,2,3,4,-1,0]
#my_list.append(9999)
#my_list.insert(0,999)
#print(len(my_list))
#my_list.pop(2)
#my_list_2=[5,6,7]
#new_list=my_list.copy()
#new_list.pop()
#print(*new_list)
#cnt=my_list.count(2)   append,pop,sort,print gud mrng length of the string
#my_list.sort()
#print(my_list)
#my_list=list(map(int,input().split(",")))
#print(*my_list)
my_list=list(map(int,input().split(" ")))
print("1.append")
print("2.pop")
print("3.sort")
print("4.gud mrng,length of the string is")
choice(int(input())
elif(choice ==3):
if(choice ==1):
    my_list.append(22)
    print(*my_list)
elif(choice ==2):
    my_list.pop(2) 
    print(*my_list)
elif(choice ==3):
     my_list.sort() 
     print(*my_list)
elif(choice ==4):
    n=len(my_list)
    print(f"gud mrng,length is{n}")

