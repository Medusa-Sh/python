#take input
print("half pyramid pattern of (*):")
n=int (input("Enter the number of rows:"))
#outer loop to handle number of rows
for i in range(0,n):
    #inner loop to handle number of columns
    for j in range(0,i+1):
        print("*",end=" ")
    print()