#DICTIONARY FOR CONTACT  DETAILS
contact=["Nix","Vex","Juno","Cyra","Dex"]
x=1
for i in contact:
    print(str(x)+"."+i)
    int(x)
    x=x+1
#DICTIONARIES CREATION
nix={"name":"nix","place":"kozhikode","phone":"0123456789"}
vex={"name":"vex","place":"kannur","phone":"1234567890"}
juno={"name":"juno","place":"malapuram","phone":"2345678901"}
cyra={"name":"cyra","place":"vayanad","phone":"3456789012"}
dex={"name":"dex","place":"kollam","phone":"4567890123"}
a=1
while(a==1):
    n=int(input("select whose contact you need : "))
    if(n==1):
        print(nix)
    elif(n==2):
        print(vex)
    elif(n==3):
        print(juno)
    elif(n==4):
        print(cyra)
    elif(n==5):
        print(dex)
    else:
        print("invalid option")
    a=int(input("do you want to continue(0/1)"))