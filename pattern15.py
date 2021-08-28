
ascii = 65
i=1
while i<=5:
    j=1
    while j<=5:
        character = chr(ascii)
        print(character, end=' ')
        j=j+1
        ascii+=1
    print()
    i=i+1