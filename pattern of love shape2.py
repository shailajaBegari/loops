# r=0
# while r<=5:
#     c=0
#     while c<=6:
#         if ((r==0 and c%3!=0) or (r==1 and c%3==0) or (r-c==2) or (r+c==8)):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#         c=c+1
#     print()
#     r=+1




r=0
while r<=5:
    c=0
    while c<=6:
        if ((c==0 or c==6) and (r!=0 and r!=3 and r!=4 and r!=5)) or ((c==1 or c==5) and(r!=1 and r!=2 and r!=4 and r!=5)) or ((c==2 or c==4)and (r!=1 and r!=2 and r!=3 and r!=5)) or ((c==3) and (r!=0 and r!=2 and r!=3 and r!=4)):
            print("*",end=  "  ")
        else:
            print(end='  ')
        c=c+1    
    print()
    r=r+1









