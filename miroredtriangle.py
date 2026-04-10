rows=int(input("Enter the number of rows:"))
if rows<=0:
    print("Please enter a positive number")
else:
    for i in range(0,rows):
        for j in range(0,rows-i-1):
            print(" ",end=" ")
        for k in range(0,i+1):
            print("@",end=" ")
        print()