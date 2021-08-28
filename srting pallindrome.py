n=input("enter the string:")
m=""
i=-1
while i>=-len(n): 
    m=m+n[i]
    i=i-1
if n==m:
    print("palindrome")
else:
    print("not palindrome")       