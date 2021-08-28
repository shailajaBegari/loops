pos=int(input("enter a pos:"))
a=0
b=1
i=0
while pos>=0:
    if pos==i:
        print(a)
        break
    c=a+b
    a=b
    b=c
    i=i+1


