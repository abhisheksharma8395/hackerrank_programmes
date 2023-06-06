a=int(input(""))
b=a%2
if (b!=0):
    print("Weird")
if (b==0):
    if a in range(2,6,1):
        print("Not Weird")
    if a in range(6,21,1):
        print("Weird")
    if a in range(21,101,1):
        print ("Not Weird")