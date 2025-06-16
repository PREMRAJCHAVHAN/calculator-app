a=float(input("enter number"))
b=input("enter operator")
c=float(input("enter number"))
d==0
if b=="+":
     d=a+c

elif b=="-":
    d=a-c

elif b=="*":
    d=a*c

elif b=="/":
    if c!=0:
        d=a/c
    else:
        print("cannot divided by 0")

else:
    print("invalid syntax")

print(d)