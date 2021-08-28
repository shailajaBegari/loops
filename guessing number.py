n=int(input('enter number'))
i=1
while i<=5:
    m=int(input('enter number'))
    i=i+1
    if n>m:
        print('u r gessing number is greater')
    elif n<m:
        print('u r gessing number is lesserthan')
    elif n==m: 
        print('equal')
        print("your guess is correct")
        break    
    elif i==5:
        print("you are chance over")
print('thank you')