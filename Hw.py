#even or odd
'''n=int(input())
if(n%2==0):
    print("even")
else:
    print("odd")
    #greatest of three
n=int(input())'''

#greatest of three
'''n1=int(input())
n2=int(input())
n3=int(input())
if(n1>n2 and n1>n3):
    print("n1 is greater")
elif(n2>n1 and n2>n3):
    print("n2 is greater")
else:
    print("n3 is greater")'''

#sum of all elements in an array
'''arr=[1,2,3]
sum=0
for i in arr:
    sum=sum+i
print(sum)'''

#peak element***********(first peak element)
'''list=list(map(int,input().split()))
count=0
for i in range(1,len(list)-1):
    if(list[i]>list[i-1] and list[i]>list[i+1]):
        count=i
        break
print(list[count])'''
#to print all peak elemnts
'''list=list(map(int,input().split()))
count=0
for i in range(1,len(list)-1):
    if(list[i]>list[i-1] and list[i]>list[i+1]):
        print(list[i],end=" ")'''

#if the last element is a peak element
'''list=list(map(int,input().split()))
count=0
for i in range(1,len(list)-1):
    if(list[i]>list[i-1] and list[i]>list[i+1]):
        count=i
if(list[-1]>list[-2] and list[-1]>count):
    count=len(list)-1
print(list[count]) '''


#check whether given numnber is palindrome are not using while loop
'''n=int(input())
s=n
rev=""
while(n>0):
    rem=n%10
    rev+=str(rem)
    n=n//10
if s==int(rev):
    print("palindrome")
else:
    print("not palindrome") '''






