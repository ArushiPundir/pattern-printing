n=5
for i in range(n): # for row 
    for j in range(1,i+1): #for the spaces in col
        print(" " ,end="")
    for j in range (n):     # for the pattern in col
        print("*",end="")
    print()