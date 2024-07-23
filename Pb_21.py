# x is trying to create a new password for his instagram account these are the required conditions for creating a nrw password
#condition 1. minimum length is 8 maximum length is 15
#conditoin 2.only@,/ allowed in a password
#condition 3. no spaces are allowed
#condition 4.only alpha numbers are allowed
# you are supposed to print weak if length is exact
# you are supposed to print medium if length between 8 to 12
# you are supposed to print strong if length between 12 to 15
password=input()
n=len(password)
count=0
new="@/"
if n<8 or n>15:
    print("Please follow the conditions")
else:
    for i in password:
        if (i in new[0] or new[1]) and " " not in password:
            count+=1
            break
    if count==0:
        print("follow the conditions")
    else:
        if n==8:
            print("Weak")
        elif n>8 or n<12:
            print("Medium")
        else:
            print("Strong")        
