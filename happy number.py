n=int(input('enter number'))
sum=0
num=n
while sum!=1 and sum!=4:
    sum=0
    while num>0:
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    num=sum
if sum==1:
    print('happy number')
else:
    print('not a harshad number')            