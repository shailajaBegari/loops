n=int(input('enter number'))
i=1
count=0
while count<=n:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1     
    if c==2:
        print(i)
        count=count+1
    i=i+1    