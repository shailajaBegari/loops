r=0
while r<=4:
    c=0
    while c<=5:
        if ((r==0) and (c!=0 and c!=1 and c!=4 and c!=5)) or ((r==1) and (c!=0 and c!=2 and c!=3 and c!=4 and c!=5)) or ((r==2) and (c!=0 and c!=2)) or ((r==3) and (c!=0 and c!=2 and c!=4 )) or ((r==4)and (c!=0 and c!=1 and c!=4)):
            print("*",end="  " )
        else:
            print(end="   ")
        c=c+1
    print()
    r=r+1            