names= []
n=int(input("ENTER THE NUMBERS OF STUDENTS :"))
n=n+1
#to read n numbers to list
for i in range(1, n):
    names.append(input("ENTER NAME"))
x=1
#to print list onee by one
for i in names:
    print(str(x)+"."+i)
    int(x)
    x=x+1
choice=input("if you want to addd more(y/n)")
flag=0
while choice=="y" or choice=="Y" :
    names.append(input("ENTER NAME"))
    choice = input("if you want to enter more(y/n)")
    flag=1
x=1
if flag==1:
    for i in names:
        print(str(x) + "." + i)
        int(x)
        x = x + 1