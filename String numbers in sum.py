sum=0
i=1
while i<=2:
    user=input('enter the numbers in the form of words::')
    a=user.split()
    j=0
    b=''
    while j<len(a):
        if a[j]=='zero':
            b+=str(0)
        elif a[j]=='one':
            b+=str(1)
        elif a[j]=='two':
            b+=str(2)
        elif a[j]=='three':
            b+=str(3)
        if a[j]=='four':
            b+=str(4)
        elif a[j]=='five':
            b+=str(5)
        if a[j]=='six':
            b+=str(6)
        elif a[j]=='seven':
            b+=str(7)
        if a[j]=='eight':
            b+=str(8)
        elif a[j]=='nine':
            b+=str(9)
        j=j+1
    sum=sum+int(b)
    i=i+1
print(sum)



