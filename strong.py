n=int(input('enter number'))
sum=0
m=n
while n>0:
    i=1
    fact=1
    r=n%10
    while (i<=r):
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if (sum==m):
    print('strong')
else:
    print('not')            