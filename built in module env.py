import random as r
import math as m
def rectangle():
    #area of rectangle
    l=r.randrange(1,10)
    b=r.randrange(2,7)
    a=l*b
    print("LENGTH ="+str(l))
    print("BREADTH="+str(b))
    print("AREA OF RECTANGLE IS :"+str(a))
def  circle():
    #AREA OF CIRCLE
    p=m.pi
    ra=r.uniform(1,6)
    area=(m.pi)*(m.pow(ra,2))
    print("RANDOM RADIUS="+str(ra))
    print("AREA OF CIRCLE IS :"+str(area))
    area=m.floor(area)
    print("AREA ROUND OF TO FLOOR IS :"+str(area))
con=1
while(con):
    print("IF YOU WANT TO FIND AREA OF \n1.RECTANGLE\n2.CIRCLE ")
    choice=input("ENTER YOUR CHOICE :")
    if (choice=="RECTANGLE") or (choice=="rectangle"):
        print("\t\t\tAREA OF RECTANGLE\n")
        rectangle()
    elif (choice=="CIRCLE") or (choice=="circle"):
        print("\t\t\tAREA OF CIRCLE\n")
        circle()
    else:
        print("INVALID CHOICE")
    con=input("DO YOU WANT TO CONTINUE(0/1) :")

