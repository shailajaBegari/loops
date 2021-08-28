n=int(input('enter number'))
i=1
fact=1
count=0
while i<=n:
    if n%i==0:
        print(i)
        count=count+1
    i=i+1
print(count,'count')        