#print(ord('A'))#123 to 127.....91 to 96
#check how many vowels are there in string
""""
n=(input())
vow=['a','e','i','o','u']
count=0
for i in n:
    if i in vow:
        count+=1
print(count)
"""""



n=(input())
vow=['a','e','i','o','u']
count=0
for i in n:
    if i not in vow:
        count+=1
print(count)
