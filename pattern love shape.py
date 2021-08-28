r=0
while r<=5:
    c=0
    while c<=6:
        if ((r==0 and c%3!=0) or (r==1 and c%3==0) or (r-c==2) or (r+c==8)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
        c=c+1
    print()
    r=r+1 












