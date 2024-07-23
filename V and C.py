#print all the vowels followed by consonents
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwwxyz"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
    if(i in vowel ):
        print(i,end=" ")
for i in inp:
    if (i in consonent):
        print(i,end=" ")