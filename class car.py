class car:
    company="toyota"
    #insert values to object
    def __init__(self,model,price,colour):
        self.c_model=model
        self.c_price=price
        self.colour=colour
    #display function/method
    def displayDetails(self,i):
        print("CAR NO :"+str(i))
        print("MODEL: TOYOTA "+self.c_model)
        print("PRICE:"+self.c_price)
        print("COLOUR:"+self.colour)
# 3  functions to read model,prince & colour
def model(x):
    model=input("\n CAR NO :"+str(x)+"\nENTER THE MODEL OF THE CAR   :")
    return model
def price():
    price= input("ENTER THE PRICE OF THE CAR  :")
    return price
def colour():
    colour=input("ENTER THE COLOUR OF THE CAR :")
    return colour
print("ENTER MAXIMUM 10 CARS DETAILS ")
n=int(input("ENTER THE NUMBERS OF CARS :"))
i=1
#to create objects
while(i<=n):
    if i==1:
        car1=car(model(i),price(),colour())
        i=i+1
    elif i==2:
        car2=car(model(i),price(),colour())
        i = i + 1
    elif i==3:
        car3=car(model(i),price(),colour())
        i = i + 1
    elif i==4:
        car4=car(model(i),price(),colour())
        i = i + 1
    elif i==5:
        car5=car(model(i), price(), colour())
        i = i + 1
    elif i==6:
        car6=car(model(i), price(), colour())
        i = i + 1
    elif i==7:
        car7=car(model(i), price(), colour())
        i = i + 1
    elif i==8:
        car8=car(model(i), price(), colour())
        i = i + 1
    elif i==9:
        car9=car(model(i), price(), colour())
        i = i + 1
    elif i==10:
        car10=car(model(i), price(), colour())
        i = i + 1
i=1
#to call display-objects method
while(i<=n):
    if i==1:
        car1.displayDetails(i)
        i=i+1
    elif i==2:
        car2.displayDetails(i)
        i = i + 1
    elif i==3:
        car3.displayDetails(i)
        i = i + 1
    elif i==4:
        car4.displayDetails(i)
        i = i + 1
    elif i==5:
        car5.displayDetails(i)
        i = i + 1
    elif i==6:
        car6.displayDetails(i)
        i = i + 1
    elif i==7:
        car7.displayDetails(i)
        i = i + 1
    elif i==8:
        car8.displayDetails(i)
        i = i + 1
    elif i==9:
        car9.displayDetails(i)
        i = i + 1
    elif i==10:
        car10.displayDetails(i)
        i = i + 1











