n=1
while n<=100:
    m=n
    rev=0
    while rev<=m:
        r=m%10
        rev=(rev*10)+r
        m=m//10
    if rev==n:
        print(n)
    n=n+1      