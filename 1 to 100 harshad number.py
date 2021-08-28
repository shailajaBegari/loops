num=1
while num<=100:
    j=num
    sum=0
    while j>0:
        d=j%10
        j=j//10
        sum=sum+d
    if num%sum==0:
        print(num)
    num=num+1         
