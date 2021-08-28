i=0
while i<=5:
    j=6-i
    while j>0:
        print(end='')
        j-=1
    k=65
    num=i+1
    while num>0:
        print(chr(k),end='')
        num-=1
        k+=1
    l=65
    n=i+1
    while n>0:
        print(chr(l+i),end='')
        n=n-1
        l=l-1
    print()
    i=i+1