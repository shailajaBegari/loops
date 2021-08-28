n=int(input('enter number'))
sum=0
m=n
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
if m%sum==0:
    print('harshad')
else:
    print('no')
      


