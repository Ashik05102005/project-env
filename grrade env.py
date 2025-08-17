marks=int(input("ENTER YOUR MARKS :"))
if(marks<=100):
    if(marks>=90):
        print("GRADE A")
    elif(marks>=80):
        print("GRADE B")
    elif(marks>=70):
        print("GRADE C")
    elif(marks>=60):
        print("GRADE D")
    else:
        print("FAILED")
else:
    print("invalid")
