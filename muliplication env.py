s=int(input("STARTING NUMBER FOR MULTIPLICATION TABLE :"))
e=int(input("ENDING NUMBER FOR MULTIPLICATION TABLE   :"))
e=e+1
for i in range (s,e,1):
    print("\n\t"+str(i)+"-MULTIPLICATION TABLE")
    print("\t______________________")
    int(i)
    for x in range(11):
        if (x != 0):
            m = x * i
            print(str(x) + "*" + str(i) + "=" + str(m))
            int(x)
            int(i)
            int(m)
