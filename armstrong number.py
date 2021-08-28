n=int(input('enter  how many digits'))
m=int(input('enter number'))
sum=0
num=m
while num>0:
    digit=num%10
    sum=sum+digit**n
    num=num//10
if sum==m:
    print('armstrong')
else:
    print('no')        
 