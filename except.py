c = 1
while c==1:
    try:
        a=int(input("ENTER TWO NUMBERS :"))
        b=int(input())
        result=a/b
        print(result)
    except  ZeroDivisionError :
         print("cant divide")
    except  ValueError :
         print("check the data type")
    c=int(input("DO YOU WANT TO CONTINUE(0/1):"))