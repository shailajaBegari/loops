
row=1
i=1
while row<=5:
    if row%2==0:
        z=i+row-1
        col=1
        while col<=row:
            print(z,end=" ")
            z-=1
            col=col+1
            i=i+1
        print()
    else:
        odd=1
        k=i
        while odd<=row:
            print(k,end=" ")
            k=k+1
            i=i+1
            odd=odd+1
        print()
    row=row+1