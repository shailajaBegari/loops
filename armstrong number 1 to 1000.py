n=1
while n<=1000:
    m=n
    sum=0
    while m>0:
        rem=m%10
        sum=sum+rem**3
        m=m//10
    if sum==n:
        print(n) 
    n=n+1        
