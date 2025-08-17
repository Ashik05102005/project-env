def fact(x):
    f=1
    for i in range (1,x):
        f=f*i
    return f
a=int(input("enter a number"))
f=fact(a)
print(f)