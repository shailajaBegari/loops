n=int(input('enter number'))
sum=0
while n>0:
    a=n%10
    n=n//10
    sum=sum+a
print(sum)
