#members list
myfile=open('content.txt')
print(myfile.read())
n=1
while(n):
    myfile=open('content.txt','a')
    myfile.write("\n->"+input("ENTER YOUR NAME  :"))
    n=int(input("do you add more names(o/1)"))
myfile=open('content.txt','r')
print(myfile.read())
