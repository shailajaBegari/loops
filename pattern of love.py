r=0
while r<=3:
    c=0
    while c<=16:
        if ((r==0)and (c!=1 and c!=2 and c!=4 and c!=5 and c!=6 and c!=8 and c!=9 and c!=10 and c!=12 and c!=13 and c!=15)) or ((r==1)and (c!=2 and c!=4 and c!=5 and c!=7 and c!=9 and c!=10 and c!=13 and c!=15)) or ((r==2)and (c!=1 and c!=4 and c!=6 and c!=8 and c!=10 and c!=12 and c!=15 )) or ((r==3)and (c!=1 and c!=2 and c!=5 and c!=6 and c!=7 and c!=8 and c!=9  and c!=12 and c!=13 and c!=15)):
            print("*",end=" ")
        else:
            print(end="  ")
        c=c+1
    print()
    r=r+1                 