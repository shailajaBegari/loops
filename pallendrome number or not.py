n=int(input('enter number'))
m=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if m==rev:
    print('palindrome')
else:
    print('no')   