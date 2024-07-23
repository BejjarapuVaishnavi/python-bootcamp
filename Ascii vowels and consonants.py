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


#consonants
"""""
n=(input())
vow=['a','e','i','o','u']
count=0
for i in n:
    if i not in vow:
        count+=1
print(count) 
""""" 
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwwxyz"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
    if(i in vowel ):
        count+=1
for i in inp:
    if (i in consonent):
         c+=1
print(count)
print(c)