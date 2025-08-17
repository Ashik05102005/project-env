def addition(x,y):
    result = x+y
    print("RESULT OF ADDITION:"+str(result))
def substraction(x,y):
    result = x-y
    print("RESULT OF SUBSTRACTION:" + str(result))
def multiplication(x,y):
    result = x*y
    print("RESULT OF MULTIPLICATION:" + str(result))
def division(x,y):
    result = x/y
    print("RESULT OF DIVISION:" + str(result))
def mod(x,y):
    result = x/y
    print("REMINDER IS:" + str(result))
choice=1
while(choice==1):
    a=int(input("ENTER THE NUMBER     :"))
    op=input("ENTER THE OPERRATION :")
    b=int(input("ENTER THE NUMBER     :"))
    if(op=="+"):
        addition (a,b)
    elif(op=="-"):
        substraction(a,b)
    elif (op == "*"):
        multiplication(a,b)
    elif (op == "/"):
        division(a,b)
    elif (op == "%"):
        division(a,b)
    else:
        print("inavild operation")
    choice=int(input("do you want to continue(0/1)"))






