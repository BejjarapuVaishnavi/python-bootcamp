#print tjr elements at a particular index in a cyclic ratation
list=list(map(int,input().split()))
k=int(input())
idx=k%len(list)
print(list[idx-1])

