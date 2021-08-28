rows = 15
print("g" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("s" * i, end="")
        print("_" * j, end="")
        print("s" * i, end="\n")
        i = i -1
        j = j + 2














