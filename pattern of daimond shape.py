r=0
while r<=4:
    c=0
    while c<=4:
        if ((c==0 or c==4) and (r!=0 and r!=1 and r!=3 and r!=4)) or ((c==1 or c==3)and (r!=0 and r!=4)) or ((c==2)):
            print("*",end='  ')
        else:
            print(end='   ')
        c=c+1
    print()
    r=r+1            