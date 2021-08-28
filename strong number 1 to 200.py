n=1
while n<=200:
    m=n
    sum=0
    while m>0:
        i=1
        fact=1
        r=m%10
        while i<=r:
            fact=fact*i
            i=i+1
        sum=sum+fact
        m=m//10
    if sum==n:
        print(n)
    n=n+1     